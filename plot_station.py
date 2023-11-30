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
from sklearn.linear_model import LinearRegression
import nead

path_l3 = 'C:/Users/bav/GitHub/PROMICE data/aws-l3-dev/level_3/'
path_tx = 'C:/Users/bav/GitHub/PROMICE data/aws-l3-dev/tx/'
path_gcn= 'C:/Users/bav/GitHub/PROMICE data/GC-Net-Level-1-data-processing/L1/'

df_meta = pd.read_csv(path_l3+'../AWS_latest_locations.csv')

var_list = ['z_boom','z_stake']

station_list = ['ZAK_U']  #df_meta.stid  # if you want them all

plt.close('all')

for station in station_list:
    df_l3 = pd.read_csv(path_l3+station+'/'+station+'_hour.csv')
    df_l3.time = pd.to_datetime(df_l3.time, utc=True)
    df_l3 = df_l3.set_index('time')
    if station not in ['NUK_N', 'QAS_A','TAS_U', 'ZAK_L']:
        df_tx = pd.read_csv(path_tx+station+'/'+station+'_hour.csv')
        df_tx.time = pd.to_datetime(df_tx.time, utc=True)
        df_tx = df_tx.set_index('time')
    else:
        df_tx = pd.DataFrame()
    
    var_list_list = [var_list[i:i+5] for i in range(0, len(var_list), 5)]
    for k, var_list in enumerate(var_list_list):
        fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(13,13))
        if len(var_list)==1:
            ax_list = [ax_list]
    
        for var, ax in zip(var_list, ax_list):
            if (var not in df_l3.columns) & (var not in df_tx.columns):
                print(var, 'not in L3 or tx data at', station)
                if len(var_list) == 1:
                    plt.close(fig)
                continue
            print(var)
            ax.set_ylabel(var)
            if var == 't_i_all':
                var = ['t_i_%i'%i for i in range(1,12) if 't_i_%i'%i in df_l3.columns]
    
                ax.plot(df_l3[var].index, df_l3[var].values, 
                        marker='.',markeredgecolor='None', 
                        linestyle='None', label=var,alpha=0.7)
            else:
                try:
                    ax.plot(df_tx[var].index, df_tx[var].values, marker='.',linestyle='None', label='transmission')
                except:
                    print(var,'not in transmission')
        
                try:
                    ax.plot(df_l3[var].index, df_l3[var].values, marker='.',markeredgecolor='None', linestyle='None', label='l3',alpha=0.5)
                except:
                    print(var,'not in L3 files')
            ax.legend()
            ax.grid()
            
        plt.suptitle('%s %i/%i'%(station, k+1, len(var_list_list)))
