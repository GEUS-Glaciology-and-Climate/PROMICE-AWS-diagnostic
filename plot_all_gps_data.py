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
import matplotlib
matplotlib.use('Agg')
import tocgen

# def main(
data_type = 'sites'
path_new = '../tmp/aws-l3-dev/'+data_type+'/'
filename = 'plot_compilations/GPS_'+data_type+'.md'
df_meta = pd.read_csv(path_new+'../AWS_'+data_type+'_metadata.csv')
df_meta = df_meta.set_index(data_type[:-1]+'_id')
f = open(filename, "w")
def Msg(txt):
    f = open(filename, "a")
    print(txt)
    f.write(txt + "\n")

for station in df_meta.index:
    Msg('## '+station)
    df_new = pd.read_csv(path_new+station+'/'+station+'_hour.csv')
    df_new.time = pd.to_datetime(df_new.time, utc=True)
    df_new = df_new.set_index('time')
    
    var_list_list = [['gps_lat','gps_lon','gps_alt']]
    for k, var_list in enumerate(var_list_list):
        fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(13,13))
        if len(var_list)==1:
            ax_list = [ax_list]
        
        for var, ax in zip(var_list, ax_list):
            if var in df_new.columns:
                if not df_new[var].isnull().all():                
                    ax.plot(df_new.index, df_new[var].values, 
                            marker='.',markeredgecolor='None', linestyle='None', 
                            color='tab:orange',label=var)  
            if var.replace('gps_','') in df_new.columns:
                ax.plot(df_new.index, df_new[var.replace('gps_','')].values, 
                        marker='.',markeredgecolor='None', linestyle='None', 
                        color='tab:green', label=var.replace('gps_',''))  
            ax.set_ylabel(var.replace('gps_',''))       
            ax.grid()
            ax.legend()
        
        no_save = 1
        for ax in ax_list:
            if ax.lines: no_save=0
            if ax.collections: no_save=0
        if no_save == 1:
            continue
        plt.suptitle('%s %i/%i'%(station, k+1, len(var_list_list)))
        fig.savefig('figures/GPS/%s/%s_%i.png'%(data_type, station,k))
        Msg('![%s](../figures/GPS/%s/%s_%i.png)'%(station,data_type, station,k))
    # df_m = pd.read_csv(path_new+station+'/'+station+'_month.csv')
    # df_m.time = pd.to_datetime(df_m.time, utc=True)
    # df_m = df_m.set_index('time')
    # df_m[[v for v in ['lat','lon','alt'] if v in df_m.columns]].to_csv('figures/GPS/coordinates/%s.csv'%station)
    Msg(' ')
tocgen.processFile(filename, filename[:-3]+"_toc.md")
f.close()
