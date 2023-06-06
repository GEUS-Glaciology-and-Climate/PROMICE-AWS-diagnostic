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
from pypromice.process import AWS
import os

path_to_l0 = '../aws-l0/'
path_l3 = '../aws-l3/level_3/'
path_tx = '../aws-l3/tx/'
path_gcn= '../GC-Net-Level-1-data-processing/L1/'
path_to_qc_files = '../PROMICE-AWS-data-issues/'
vari = '../pypromice/src/pypromice/process/variables.csv'
df_meta = pd.read_csv(path_l3+'../AWS_station_locations.csv')

filename="./plot_compilations/flags.md"
f = open(filename, "w")
def Msg(txt):
    f = open(filename, "a")
    print(txt)
    f.write(txt + "\n")
    
plt.close('all')


for station in os.listdir(path_to_qc_files+'flags'):
    station = station.replace('.csv','')
    # loading flags
    try:
        df_flags = pd.read_csv(path_to_qc_files+'flags/'+station+'.csv', skipinitialspace=True)
    except:
        print('no flag file')
        continue
    
    # Loading the L1 data:
    config_file = path_to_l0 + '/raw/config/{}.toml'.format(station)
    inpath = path_to_l0 + '/raw/{}/'.format(station)
    try:
        pAWS_gc = AWS(config_file, inpath, var_file=vari)
        pAWS_gc.getL1()
    except:
        print('no raw for',station)
        
    config_file = path_to_l0 + '/tx/config/{}.toml'.format(station)
    inpath = path_to_l0 + '/tx/'
    pAWS_tx = AWS(config_file, inpath, var_file=vari)
    pAWS_tx.getL1()

    pAWS_all = pAWS_tx
    df_L1 = pAWS_all.L1A.combine_first(pAWS_gc.L1A).to_dataframe()
    df_L1.index = pd.to_datetime(df_L1.index, utc=True)
    var_list = np.unique(' '.join(df_flags.variable.to_list()).split(' '))
    
    fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(12,10))
    if len(var_list)==1:
        ax_list = [ax_list]
    Msg(df_flags.to_markdown())
    for var, ax in zip(var_list, ax_list):
        ax.plot(df_L1[var].index, 
                df_L1[var].values,
                marker='.',color='tab:blue', linestyle='None', label='L1')
        for t0, t1, variable in zip(df_flags.t0, df_flags.t1, df_flags.variable):
            if var in variable:
                if not isinstance(t0, str):
                    t0 = pd.to_datetime(df_L1.index[0], utc=True)
                if not isinstance(t1, str):
                    t1 = pd.to_datetime(df_L1.index[-1], utc=True)
                ax.plot(df_L1.loc[t0:t1, var].index,
                        df_L1.loc[t0:t1, var].values,
                        marker='.',color='tab:red', 
                        linestyle='None', label='removed')
        ax.set_ylabel(var)
        # ax.legend()

    plt.suptitle(station)
    plt.suptitle(station)
    fig.savefig('figures/flags/%s.png'%station)
    Msg('1[%s](../figures/flags/%s.png'%(station, station))
