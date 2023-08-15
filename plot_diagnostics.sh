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

echo "Checking for updates on PROMICE-AWS-diagnostics"
cd ../PROMICE-AWS-diagnostics
git checkout master
git pull

#--------------------

python flag-diagnostics.py


echo "Pushing new L3 products to aws-l3..."
git add *
git commit -m "diagnostic update `date -u`"
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

