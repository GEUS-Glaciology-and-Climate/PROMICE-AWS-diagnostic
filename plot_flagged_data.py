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

import xarray as xr
import os
# import matplotlib
# matplotlib.use('Agg')
import tocgen


path_to_l0 = '../aws-l0/'
path_to_l0 = 'C:/Users/bav/GitHub/PROMICE data/aws-l0/'
path_to_l1 = 'C:/Users/bav/GitHub/PROMICE data/aws-l1/'
path_l3 = '../aws-l3/level_3/'
path_l3 = 'C:/Users/bav/GitHub/PROMICE data/aws-l3-dev/level_3/'
path_tx = '../aws-l3/tx/'

from datetime import date
today = date.today().strftime("%Y%m%d")
filename = './plot_compilations/flags_'+today+'.md'
figure_folder='figures/flags_'+today
try:
    os.mkdir(figure_folder)
except:
    pass

df_meta = pd.read_csv(path_l3+'../AWS_latest_locations.csv')
df_metadata = pd.read_csv(path_l3+'../AWS_metadata.csv')

f = open(filename, "w")
def Msg(txt):
    f = open(filename, "a")
    print(txt)
    f.write(txt + "\n")
    
# plt.close('all')

path_to_qc_files = '../PROMICE-AWS-data-issues/'
all_dirs = os.listdir(path_to_qc_files+'adjustments')+os.listdir(path_to_qc_files+'flags')

vari = 'C:/Users/bav/OneDrive - GEUS/Code/PROMICE/pypromice/src/pypromice/process/variables.csv'
if not os.path.isfile(vari):
    vari = 'C:/Users/bav/OneDrive - Geological survey of Denmark and Greenland/Code/PROMICE/pypromice/src/pypromice/process/variables.csv'

zoom_to_good = False

for station in ['SDM']:
# for station in np.unique(np.array(all_dirs)): 
    station = station.replace('.csv','')
    # loading flags
    try:
        flags = pd.read_csv(path_to_qc_files+'flags/'+station+'.csv', comment='#', skipinitialspace=True)
        flags['what was done'] = 'flag'
    except:
        flags = pd.DataFrame()
    
    try:
        adj = pd.read_csv(path_to_qc_files+'adjustments/'+station+'.csv', comment='#', skipinitialspace=True)
        adj['what was done'] = adj['adjust_function'] + ' ' + adj['adjust_value'].astype(str)
    except:
        adj = pd.DataFrame()
        
    try:
        df_flags = pd.concat((flags,adj))[['t0', 't1', 'variable', 'what was done', 'comment', 'URL_graphic']].reset_index(drop=True)
    except:
        df_flags = pd.concat((flags,adj))
        
    # Loading the L1 data:
    config_file = path_to_l0 + '/tx/config/{}.toml'.format(station)
    if os.path.isfile(config_file):
        inpath = path_to_l0 + '/tx/'
        pAWS_tx = AWS(config_file, inpath, var_file=vari)
        # pAWS_tx.getL1()
        pAWS_tx.process()
        try:
            config_file = path_to_l0 + '/raw/config/{}.toml'.format(station)
            inpath = path_to_l0 + '/raw/'+station+'/'
            pAWS_raw = AWS(config_file, inpath)
            # pAWS_raw.getL1()
            pAWS_raw.process()
            ds = pAWS_raw.L1A.combine_first(pAWS_tx.L1A).copy(deep=True)
            ds_l3 = pAWS_raw.L3.combine_first(pAWS_tx.L3).copy(deep=True)
        except:
            print('No raw logger file for',station)
            ds = pAWS_tx.L1A.copy(deep=True)
            ds_l3 = pAWS_tx.L3.copy(deep=True)
    else:
        print('No transmission toml file for',station)
        config_file = path_to_l0 + '/raw/config/{}.toml'.format(station)
        inpath = path_to_l0 + '/raw/'+station+'/'
        pAWS_raw = AWS(config_file, inpath)
        # pAWS_raw.getL1()
        pAWS_raw.process()
        ds = pAWS_raw.L1A.copy(deep=True)
        
        ds.attrs['bedrock'] = str(ds.attrs['bedrock'])
        
        ds_l3 = pAWS_raw.L3

    ds_save = ds.copy(deep=True)
    
    ds = adjustTime(ds, adj_dir=path_to_qc_files+'adjustments')
    ds1 = flagNAN(ds,  flag_dir=path_to_qc_files+'flags')
    ds2 = adjustData(ds1, adj_dir=path_to_qc_files+'adjustments')
    # temp_var = ['t_i_'+str(i) for i in range(12)]
    # %%

    # persistence QC
    ds3 = persistence_qc(ds2)
    
    # percentile QC
    # ds3b = ds3.copy()
    # outlier_detector = ThresholdBasedOutlierDetector.default()
    # ds3b = outlier_detector.filter_data(ds3) 
    
    ds4 = ds3.copy()
    baseline_elevation = (ds3.gps_alt.to_series().resample('M').median()
                          .reindex(ds3.time.to_series().index, method='nearest')
                          .ffill().bfill())
    mask = (np.abs(ds3.gps_alt - baseline_elevation) < 100) & ds3.gps_alt.notnull()
    ds4[['gps_alt','gps_lon', 'gps_lat']] = ds4[['gps_alt','gps_lon', 'gps_lat']].where(mask)

    # smoothing tilt
    ds4['tilt_x'] = smoothTilt(ds4['tilt_x'])
    ds4['tilt_y'] = smoothTilt(ds4['tilt_y'])
    ds4['rot'] = smoothRot(ds4['rot'])
    
    df_L1 = ds.to_dataframe().copy()
    
    if len(df_flags)>0:
        for ind, var_list in zip(df_flags.index, df_flags.variable):
            if var_list == '*':
                df_flags.loc[ind,'variable'] = ' '.join(df_L1.columns)
            elif '*' in var_list:
                df_flags.loc[ind,'variable'] = ' '.join(df_L1.filter(regex=var_list).columns)

        var_list = np.unique(' '.join(df_flags.variable.to_list()).split(' '))
        for v in var_list:
            if v not in ds_save.data_vars:
                Msg(v+' not in variables')
                var_list = var_list[~np.isin(var_list, v)]
                continue
                
            if ds_save[v].isnull().all():
                var_list = var_list[~np.isin(var_list, v)]
    Msg('# '+station)
    var_list = list(ds4.keys())


    var_list_list = [np.array(var_list[i:(i+6)]) for i in range(0,len(var_list),6)]
    # var_list_list = [np.array(['gps_lat','gps_lon','gps_alt'])]
    # var_list_list = [np.array(['t_u','rh_u','wspd_u','z_boom_u','dlr','ulr','dsr','usr'])]
    var_list_list = [
                      np.array(['usr','usr_cor','dsr','dsr_cor', 'tilt_x','tilt_y','rot']),
                      # np.array(['p_u','p_l','p_i']),
                      # np.array(['rh_u','rh_l','rh_i']),
                      # np.array(['wspd_u','wspd_l','wspd_i']),
                     ]  #,'t_u','t_l','t_i', 'rh_u','rh_i','rh_l'])]
    # var_list_list = [np.array(['t_u']+['t_i_'+str(i+1) for i in range(12)])]
    for i, var_list in enumerate(var_list_list):
        if len(var_list) == 0: continue
        if len(var_list[~np.isin(var_list, df_L1.columns)]) >0:
            print(var_list[~np.isin(var_list, df_L1.columns)], 'not in L1 data')
        var_list = var_list[np.isin(var_list, df_L1.columns)]
        fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(12,len(var_list)*2.3))
        fig.subplots_adjust(top=0.83)
        if len(var_list) == 1: fig.subplots_adjust(top=0.7)
            
        if len(var_list)==1: ax_list = [ax_list]
        for var, ax in zip(var_list, ax_list):
            
            ax.plot(ds.time, 
                    ds[var].values,
                    marker='.',color='tab:red', linestyle='None', 
                    label='removed by flag')
            ax.plot(ds1.time, 
                    ds1[var].values,
                    marker='.',color='tab:orange', linestyle='None',
                    label='removed or changed by adjustment')
            ax.plot(ds2.time, 
                    ds2[var].values,
                    marker='.',color='tab:green', linestyle='None',
                    label='filtered with persistence')
            ax.plot(ds3.time, 
                    ds3[var].values,
                    marker='.',color='tab:pink', linestyle='None',
                    label='removed by custom filter (gps_alt, tilt or rot)')
            # if ('gps' in var) | (var in ['tilt_x','tilt_y','rot']):
            #     ax.plot(ds3b.time, 
            #             ds3b[var].values,
            #             marker='.',color='tab:pink', linestyle='None',
            #             label='removed by custom filter (gps_alt, tilt or rot)')
            ax.plot(ds4.time, 
                    ds4[var].values,
                    marker='.',color='tab:blue', linestyle='None',
                    label='final')
            if var == 'gps_alt':
                ax.plot(ds3.time,
                        baseline_elevation,
                        ls='--', c='k')
            if 'cor' in var:
                ax.plot(ds_l3.time,
                         ds_l3[var],       
                         marker='.',color='tab:blue', linestyle='None')

        for var, ax in zip(var_list, ax_list):

            if zoom_to_good:
                ax.set_ylim(ds4[var].min(), ds4[var].max())

            # ax.set_xlim(df_L1.index[[0,-1]])
            # ax.set_ylim(ds3[var].min(),ds2[var].max())
            ax.set_ylabel(var)
            ax.grid()
        title = station+'_%i/%i'%(i+1,len(var_list_list))
        ax_list[0].legend(loc='lower left', title = title, bbox_to_anchor=(0,1.1), ncol=3)
        fig.savefig('%s/%s_%i.png'%(figure_folder, station,i), dpi=120,bbox_inches='tight')
        Msg('![](../%s/%s_%i.png)'%(figure_folder, station,i))
    Msg(' ')
tocgen.processFile(filename, filename[:-3]+"_toc.md")
