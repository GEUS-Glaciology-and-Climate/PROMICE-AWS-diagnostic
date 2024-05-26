# -*- coding: utf-8 -*-
"""
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# from sklearn.linear_model import LinearRegression
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
from pypromice.qc.persistence import persistence_qc
from pypromice.process import AWS, resampleL3
from pypromice.process.L1toL2 import adjustTime, adjustData, flagNAN, smoothTilt, smoothRot
from pypromice.qc.percentiles.outlier_detector import ThresholdBasedOutlierDetector
from pypromice.process.L3toL4 import toL4
from pypromice.process import getVars, getMeta, addMeta, getColNames, \
    roundValues, resampleL3, writeCSV, writeNC
import xarray as xr
import os
# import matplotlib
# matplotlib.use('Agg')


path_to_l0 = '../aws-l0/'
path_to_l0 = 'C:/Users/bav/GitHub/PROMICE data/aws-l0/'
path_to_l1 = 'C:/Users/bav/GitHub/PROMICE data/aws-l1/'
path_l3 = '../aws-l3/level_3/'
path_l3 = 'C:/Users/bav/GitHub/PROMICE data/aws-l3-dev/level_3/'
path_tx = '../aws-l3/tx/'

from datetime import date
today = date.today().strftime("%Y%m%d")
figure_folder='figures/flags_'+today
try:
    os.mkdir(figure_folder)
except:
    pass

df_meta = pd.read_csv(path_l3+'../AWS_latest_locations.csv')
df_metadata = pd.read_csv(path_l3+'../AWS_metadata.csv')

plt.close('all')

vari = 'C:/Users/bav/OneDrive - GEUS/Code/PROMICE/pypromice/src/pypromice/process/variables.csv'
if not os.path.isfile(vari):
    vari = 'C:/Users/bav/OneDrive - Geological survey of Denmark and Greenland/Code/PROMICE/pypromice/src/pypromice/process/variables.csv'

def loadArr(infile):
    if infile.split('.')[-1].lower() in 'csv':
        df = pd.read_csv(infile)
        df['time'] = pd.to_datetime(df['time']).dt.tz_localize(None)
        df = df.set_index('time')
        ds = xr.Dataset.from_dataframe(df)

    elif infile.split('.')[-1].lower() in 'nc':
        with xr.open_dataset(infile) as ds:
            ds = ds.load()
    
    try:
        name = ds.attrs['station_name'] 
    except:
        name = infile.split('/')[-1].split('.')[0].split('_hour')[0].split('_10min')[0]
        
    print(f'{name} array loaded from {infile}')
    return ds, name

def makeL3(station):
    config_file = path_to_l0 + '/tx/config/{}.toml'.format(station)
    if os.path.isfile(config_file):
        inpath = path_to_l0 + '/tx/'
        pAWS_all = AWS(config_file, inpath, var_file=vari)
        pAWS_all.process()
        try:
            config_file = path_to_l0 + '/raw/config/{}.toml'.format(station)
            inpath = path_to_l0 + '/raw/'+station+'/'
            pAWS_raw = AWS(config_file, inpath)
            pAWS_raw.process()
            all_ds = pAWS_raw.L3.combine_first(pAWS_all.L3)
        except:
            print('No raw logger file for',station)
            all_ds = pAWS_all.L3
    else:
        print('No transmission toml file for',station)
        config_file = path_to_l0 + '/raw/config/{}.toml'.format(station)
        inpath = path_to_l0 + '/raw/'+station+'/'
        pAWS_raw = AWS(config_file, inpath)
        # pAWS_raw.getL1()
        pAWS_raw.process()
        ds = pAWS_raw.L1A.copy(deep=True)
        
        ds.attrs['bedrock'] = str(ds.attrs['bedrock'])
        
        all_ds = pAWS_raw.L3

    # Get hourly, daily and monthly datasets
    print('Resampling L3 data to hourly, daily and monthly resolutions...')
    l3_h = resampleL3(all_ds, '60min')
    # l3_d = resampleL3(all_ds, '1D')
    # l3_m = resampleL3(all_ds, 'M')
    
    print(f'Adding variable information...')
    # Load variables look-up table
    var = getVars()
        	
    # Round all values to specified decimals places
    l3_h = roundValues(l3_h, var)
    # l3_d = roundValues(l3_d, var)
    # l3_m = roundValues(l3_m, var)
        
    # Get columns to keep
    if hasattr(all_ds, 'p_l'):
        col_names = getColNames(var, 2, 'raw')  
    else:
        col_names = getColNames(var, 1, 'raw')    

    # Assign station id
    l3_h.attrs['station_id'] = station
    
    # Assign metadata
    print(f'Adding metadata...')
    m = getMeta()
    l3_h = addMeta(l3_h, m)
    # l3_d = addMeta(l3_d, m)
    # l3_m = addMeta(l3_m, m)
      
    # Set up output path
    outpath = os.path.join('L3_test', station)
    
    # Write to files
    if not os.path.isdir(outpath):
        os.mkdir(outpath)
    outfile_h = os.path.join(outpath, station + '_hour')

    writeCSV(outfile_h+'.csv', l3_h, csv_order=None)
    writeNC(outfile_h+'.nc', l3_h)
    

for station in ['EGP']:
# for station in df_metadata.stid: 
    station = station.replace('.csv','')
    infile = 'L3_test/'+station+'/'+station+'_hour.nc'

    makeL3(station)
    ds1, n1 = loadArr(infile)
    ds1 = toL4(ds1)
    
    print(station)
    var_list_list = [np.array(['z_boom_u','z_boom_l','z_stake','z_pt_cor','z_surf_combined'])]
    # %%
    plt.close('all')
    fig, ax = plt.subplots(2,1,sharex=True,figsize=(8,8))
    for v in ['z_surf_1', 'z_surf_2', 'z_pt_cor']:
        if v in ds1.data_vars:
            ds1[v].plot(label=v, ax=ax[0])
    
    ax[0].legend()
    ax[0].set_ylabel('height (m)')
    ax[0].grid()
    ax[0].set_title(station)
    
    
    for v in ['snow_height', 'z_ice_surf', 'z_surf_combined']:
        ds1[v].plot(label=v, ax=ax[1])
    
    ax[1].legend()
    ax[1].set_ylabel('height (m)')
    ax[1].set_title('')
    ax[1].grid()
    fig.savefig('figures/surface_heights/'+station+'.png',dpi=300)
