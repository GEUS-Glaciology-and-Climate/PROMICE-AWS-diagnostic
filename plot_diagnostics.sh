#!/usr/bin/env bash

source /home/aws/miniconda3/etc/profile.d/conda.sh

if [ -d "/mnt/data/aws/pypromice_aws/aws-l0" ]
then
    echo "Running glacio01 version"
    server="glacio01"
    root_dir="/mnt/data/aws/pypromice_aws"
elif [ -d "/data/pypromice_aws/aws-l0" ]
then
    echo "Running Azure version"
    server="azure"
    root_dir="/data/pypromice_aws"
else
    echo "Cannot find aws-l0 folder"
fi

cd $root_dir

conda activate py38
echo "Running l3_processor at `date -u`"

echo 'Checking for updates on aws-l0...'
cd aws-l0
git checkout main
if [ "$server" = "glacio01" ]
then
    echo "reset hard to aws-l0"
    # glacio01 is not allowed to modify l0 so any local modification is discarded
    git reset --hard HEAD # Ignore any locally modified files, and get up-to-date with remote
fi
git pull

echo "Checking for updates on aws-l3"
cd ../aws-l3
git checkout main
git pull

echo "Checking for updates on PROMICE-AWS-data-issues"
cd ../PROMICE-AWS-data-issues
git checkout master
git pull

#--------------------

echo '======================================='
echo "Running AWS TX >> L0 >> L3 processing"

echo "Fetching new L0 TX messages..."
cd ../aws-l0
getL0tx -a ../credentials/accounts.ini -p ../credentials/credentials.ini -c tx/config -u ../credentials/last_aws_uid.ini -o tx

echo "Finding recently fetched files..."
IMEIs=$(find ./tx -maxdepth 1 -type f -mmin -60 | cut -d"/" -f3)
imei_list=""
for i in $(echo $IMEIs | tr ' ' '\n'); do
    imei_list=$(echo $imei_list; grep -l $i ${root_dir}/aws-l0/tx/config/*.toml)	
done	
echo ${imei_list}

cd ../pypromice/src/pypromice
if [[ -n "$imei_list" ]]
then
    echo "Processing L3..."
    parallel --will-cite --bar "getL3 -c {} -i ../../../aws-l0/tx -o ../../../aws-l3/tx" ::: $(ls $imei_list)
else 
    echo "No new TX updates found"
fi

echo "Finished AWS L0 raw >> L3 processing"

#--------------------

echo '======================================='
echo "Running BUFR file export for DMI/WMO..."

echo 'Removing all bufr files from BUFR_out'
cd ../../
rm src/pypromice/postprocess/BUFR_out/*.bufr

echo 'Running getBUFR...'
getBUFR --positions --positions-filepath ../aws-l3/AWS_latest_locations.csv

cd ../aws-operational-processing
if [ "$server" = "azure" ]
then
   echo 'Running bufr_wrapper.sh...'
   ./bufr_wrapper.sh
   echo "DONE WITH BUFR at `date -u`"
else
   echo "skipping BUFR processing"
fi
#------------------

echo '======================================='
echo "Running AWS L0 raw >> L3 processing"

echo "Finding new flag and fix files..."
cd ../PROMICE-AWS-data-issues
flagged=$(find . -maxdepth 2 -type f -name "*.csv" -mmin -120 | cut -d"/" -f3 | cut -d"." -f1 | sort | uniq)

echo "Finding recently added files..."
cd ../aws-l0/raw/config
station_configs=$(find . -maxdepth 1 -type f | cut -d"/" -f2)

for I in $flagged
do
    station_configs=${station_configs:+$station_configs }$I
done
echo $station_configs

imei_list=""
for i in $(echo $station_configs); do
    imei_list=$(echo $imei_list; grep -l ${i%.*} ${root_dir}/aws-l0/raw/config/*.toml)	
done

cd ../../../pypromice/src/pypromice
if [[ -n "$imei_list" ]]
then
    echo "Processing L3..."
    parallel --will-cite --bar "getL3 -c {} -i ../../../aws-l0/raw -o ../../../aws-l3/raw" ::: $(ls $imei_list) 
else 
    echo "No new raw updates found"
fi
echo "Finished AWS L0 raw >> L3 processing"

#------------------

echo '======================================='
echo "Running AWS L3 RAW and TX joiner"
cd ../../../aws-l3

echo "Finding all unique AWS data by name..."
names=$(find . -maxdepth 3 -type f -name "*.csv" -mmin -120 | cut -d"/" -f3 | sort | uniq)
echo $names

echo "Joining L3 data..."
parallel --will-cite --bar --xapply ' ' "joinL3 -s ./raw/{}/{}_10min.csv -t ./tx/{}/{}_hour.csv -o level_3 -d raw" ::: $names

#--------------

echo '======================================='
if [ "$server" = "azure" ]
then
    echo "Pushing new L0 data to aws-l0..."
    cd ../aws-l0
    git add *
    git commit -m "L0 update `date -u`"
    git push
else
    echo "skipping l0 update"
fi

echo "Pushing new L3 products to aws-l3..."
cd ../aws-l3
git add *
git commit -m "L3 update `date -u`"
git push

#--------------

# If running on Azure, then sync and restructure to the mounted Azure fileshare
if [ "$server" = "azure" ]
then
    echo "l3 sync and restructure"
    cd ../aws-operational-processing
    sudo ./sync_l3.sh
    sudo ./restructure_l3.sh
else
    echo "skipping l3 sync and restructure"
fi

echo "Finished at `date -u`"

