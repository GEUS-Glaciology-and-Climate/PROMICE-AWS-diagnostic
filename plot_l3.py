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
from statsmodels.nonparametric.smoothers_lowess import lowess

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
from pypromice.process import AWS
from pypromice.process.resample import resample_dataset
from pypromice.process.write import getColNames, writeCSV, writeNC, prepare_and_write
from pypromice.process.join_levels import join_levels
from pypromice.process.load import getVars, getMeta
from pypromice.process.utilities import roundValues, addVars, addMeta
from pypromice.process.L2toL3 import toL3
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


filename = 'plot_compilations/L4_overview.md'
f = open(filename, "w")
def Msg(txt):
    f = open(filename, "a")
    print(txt)
    f.write(txt + "\n")
    
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

def makeL2_merged(station):
    config_file = path_to_l0 + '/tx/config/{}.toml'.format(station)
    if os.path.isfile(config_file):
        inpath = path_to_l0 + '/tx/'
        pAWS_all = AWS(config_file, inpath, var_file=vari)
        pAWS_all.getL1()
        pAWS_all.getL2()
        try:
            config_file = path_to_l0 + '/raw/config/{}.toml'.format(station)
            inpath = path_to_l0 + '/raw/'+station+'/'
            pAWS_raw = AWS(config_file, inpath)
            pAWS_raw.getL1()
            pAWS_raw.getL2()
            all_ds = pAWS_raw.L2.combine_first(pAWS_all.L2)
        except:
            print('No raw logger file for',station)
            all_ds = pAWS_all.L2
    else:
        print('No transmission toml file for',station)
        config_file = path_to_l0 + '/raw/config/{}.toml'.format(station)
        inpath = path_to_l0 + '/raw/'+station+'/'
        pAWS_raw = AWS(config_file, inpath)
        pAWS_raw.getL1()
        pAWS_raw.getL2()
        all_ds = pAWS_raw.L2

    # Get hourly, daily and monthly datasets
    print('Resampling L2 data to hourly and printing to file')
    # Define variables and metadata (either from file or pypromice package defaults)
    v = getVars()
    m = getMeta()

    # Write Level 2 dataset to file if output directory given

    prepare_and_write(all_ds, 'L2_test', v, m, '60min', resample = True)
        
    

# %%
for station in ['CEN1']:
# for station in df_metadata.stid:
    plt.close('all')

    station = station.replace('.csv','')
    infile = 'L2_test/'+station+'/'+station+'_hour.nc'
    print(station)

    # if not os.path.isfile(infile):
    makeL2_merged(station)

    l2 = xr.open_dataset(infile)
    l2.attrs['bedrock'] = l2.attrs['bedrock'] == 'True'
    l2.attrs['number_of_booms'] = int(l2.attrs['number_of_booms'] )

    l3 = toL3(l2)
    l2.close()
    print('Resampling L3 data to hourly and printing to file')

    # Write Level 2 dataset to file if output directory given
    prepare_and_write(l3, 'L3_test', getVars(), getMeta(), '60min')
    # %% 
    debug_args=['-s=L3_test/'+station+'/'+station+'_hour.nc',
        # '-g=C:/Users/bav/OneDrive - GEUS/Code/PROMICE/GC-Net-Level-1-data-processing/L1/hourly/',
        # '-p=L3_test/',
        '-o=L4_test/']
    join_l4(debug_args)
    
    # %%
    ds_l4, _ = loadArr('L4_test/'+station.replace('v3','').replace('CEN2','CEN')+'/'+station.replace('v3','').replace('CEN2','CEN')+'_hour.nc')
    
    Msg('## '+station)
    list_del = list(ds_l4.attrs.keys())
    for a in list_del:
        del ds_l4.attrs[a]
    df_l4 = ds_l4.to_dataframe()
    
    var_list = []
    for v in df_l4.columns:
        if 'd_t_i_' in v:
            continue
        if 't_i_' in v:
            continue

        if '_std' in v:
            continue
        if '_q' in v:
            continue
        if 'gps' in v:
            continue
        if v in ['rec','min_y','lat','lon','alt','lat_avg','lon_avg','alt_avg',
                 'rh_i_cor', 'msg_lat','msg_lon','msg_i', 'batt_v_ss', 'fan_dc_u', 
                 'fan_dc_l']:
            continue
        if df_l4[v].isnull().all():
            print(v, 'full of NaN')
            continue
        var_list.append(v)
        
    # var_list = var_list + ['gps_lat', 'gps_lon','gps_alt','t_i_all', 'd_t_i_all']
    # var_list_list = [var_list[i:i+7] for i in range(0, len(var_list), 7)]
    var_list_list = [np.array(['gps_lat', 'gps_lon','gps_alt','t_i_all', 'd_t_i_all']),
                 np.array([v for v in var_list if 'z_' in v]+['snow_height'])]
    for k, var_list in enumerate(var_list_list):
        fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(13,13))
        if len(var_list)==1:
            ax_list = [ax_list]
        
        for var, ax in zip(var_list, ax_list):
            if 'all' in var:
                var_name = '_'.join(var.split('_')[:-1])+'_'
                var = [var_name+str(i) for i in range(1,12) if var_name+str(i) in df_l4.columns]
            if 'gps_' in var:
                var_name = var.split('_')[-1]
                var = ['gps_'+var_name, var_name, var_name+'_avg']
            if isinstance(var, list):
                for v in var:
                    if '_avg' in v:
                        ax.plot(df_l4[v].index, df_l4[v].values, 
                                c='k', ls='--',
                                label=v,alpha=0.7)
                    else:
                        ax.plot(df_l4[v].index, df_l4[v].values, 
                                marker='.',markeredgecolor='None', ls='None',
                                label=v,alpha=0.7)                
                try:
                    ax.set_ylabel(ds_l4[var[0]].units)
                except:
                    print(var[0], 'does not have unit')
                ax.legend(ncol=3)
            else:
                ax.plot(df_l4[var].index, df_l4[var].values, 
                        label=var,
                        marker='.', color='tab:orange')            
                try:
                    ax.set_ylabel(ds_l4[var].units)
                except:
                    print(var, 'does not have unit')
                ax.legend()
            ax.grid()

        plt.suptitle('%s %i/%i'%(station, k+1, len(var_list_list)))
        fig.savefig('figures/plot_l4/%s_%i.png'%(station,k), dpi=300)
        Msg('![%s](../figures/plot_l4/%s_%i.png)'%(station, station,k))
    Msg(' ')
f.close()
