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
from pypromice.process import AWS, resampleL3
from pypromice.process.L3toL4 import toL4
from pypromice.process import getVars, getMeta, addMeta, getColNames, \
    roundValues,  writeCSV, writeNC
import xarray as xr
import os

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

# for station in ['EGP']:
for station in df_metadata.stid[10:]:
    station = station.replace('.csv','')
    infile = 'L3_test/'+station+'/'+station+'_hour.nc'
    print(station)

    if not os.path.isfile(infile):
        makeL3(station)
    # makeL3(station)
    ds1, n1 = loadArr(infile)
    # %%
    # ds1 = toL4(ds1)
    
    from statsmodels.nonparametric.smoothers_lowess import lowess
    for v in ['lat', 'lon', 'alt']:
        ds1=ds1.drop_vars(v)
    for var in ['gps_lat', 'gps_lon', 'gps_alt']:
        if var not in ds1.data_vars: 
            print('no',var,'at',station)
            continue
        if ds1[var].isnull().all(): 
            print('no',var,'at',station)
            continue
        print(var)
        var_out = var
        
        # finding station relocation (above GPS accuracy)
        # diff = ds1[var].to_series().interpolate(method='linear', limit_area='inside', limit_direction='forward').diff()
        # diff = (ds1[var].to_series().resample('12H').asfreq().ffill() - \
        #         ds1[var].to_series().resample('12H').asfreq().bfill())
        diff = ds1[var].to_series().resample('D').median().interpolate(method='linear', limit_area='inside', limit_direction='forward').diff()        
        if var == 'gps_alt':
            thresh = diff.std()*8
        else:
            thresh = diff.std()*6
        list_diff = diff.loc[diff.abs()>thresh].reset_index()
        list_diff['year']=list_diff.time.dt.year
        list_diff=list_diff.groupby('year').max()
        breaks = [None]+list_diff.time.to_list()+[None]

        df_all = pd.Series() # dataframe gathering all the smoothed pieces
        for i in range(len(breaks)-1):
            df = ds1[var].to_series().loc[slice(breaks[i], breaks[i+1])].copy()
            
            y_sm = lowess(df,
                          pd.to_numeric(df.index),
                          is_sorted=True, frac=1/3, it=0,
                          )
            df.loc[df.notnull()] = y_sm[:,1]
            df = df.interpolate(method='linear', limit_area='inside')
            
            last_valid_6_months = slice(df.last_valid_index()-pd.to_timedelta('180D'),None)
            df.loc[last_valid_6_months] = (df.loc[last_valid_6_months].interpolate( axis=0,
                method='spline',order=1, limit_direction='forward', fill_value="extrapolate")).values
            
            first_valid_6_months = slice(None, df.first_valid_index()+pd.to_timedelta('180D'))
            df.loc[first_valid_6_months] = (df.loc[first_valid_6_months].interpolate( axis=0,
                method='spline',order=1, limit_direction='backward', fill_value="extrapolate")).values
            df_all=pd.concat((df_all, df))
            
        print(var_out.replace('gps_','').replace('alt','elev'))
        df_all = df_all[~df_all.index.duplicated(keep='first')]
        ds1[var_out.replace('gps_','').replace('alt','elev')] = ('time', df_all.values)
    
    # %% plotting thresholding of diff
    # fig, ax = plt.subplots(3,1,sharex=True,figsize=(8,12))
    # for i, v in enumerate(['gps_lat', 'gps_lon', 'gps_alt']):
    #     diff = ds1[v].to_series().resample('D').median().interpolate(method='linear', limit_area='inside', limit_direction='forward').diff()
    #     diff.plot(ax=ax[i])
    #     ax[i].axhline(diff.std()*4, c='k')
    #     ax[i].axhline(-diff.std()*4, c='k')

#%%
    plt.close('all')
    fig, ax = plt.subplots(3,1,sharex=True,figsize=(8,12))
    for i, v in enumerate(['gps_lat', 'gps_lon', 'gps_alt']):
        ds1[v].plot(label='observed', marker='.', ax=ax[i])
        
        # diff = (ds1[v].to_series().resample('12H').asfreq().ffill() - \
        #         ds1[v].to_series().resample('12H').asfreq().bfill())
        diff = ds1[v].to_series().resample('D').median().interpolate(method='linear', limit_area='inside', limit_direction='forward').diff()
        if v == 'gps_alt':
            thresh = diff.std()*8
        else:
            thresh = diff.std()*6

        list_diff = diff.loc[diff.abs()>thresh].reset_index()
        list_diff['year']=list_diff.time.dt.year
        list_diff=list_diff.groupby('year').max()
        breaks = [None]+list_diff.time.to_list()+[None]
        
        v=v.replace('gps_','').replace('alt','elev')
        if v not in ds1.data_vars: 
            print('no',v,'at',station)
            continue
        if ds1[v].isnull().all(): 
            print('no',v,'at',station)
            continue
        ds1[v].plot(label='smoothed and interpolated', alpha=0.8, ax=ax[i])
        for time in list_diff.time:
            ax[i].axvline(time,ls='--',c='k')
        ax[i].axvline(np.nan,ls='--',label='detected maintenance',c='k')
        ax[i].set_ylabel(v)
        ax[i].legend()
        ax[i].grid()

    ax[0].set_title(station)
    fig.savefig('figures/GPS_postproc/'+station+'.png',dpi=300)
