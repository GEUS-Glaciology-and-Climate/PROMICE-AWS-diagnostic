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
path_new = '../aws-l3-dev/stations/'
filename = 'plot_compilations/GPS_data.md'
df_meta = pd.read_csv(path_new+'../AWS_latest_locations.csv')
df_meta2 = pd.read_csv(path_new+'../AWS_metadata.csv')

f = open(filename, "w")
def Msg(txt):
    f = open(filename, "a")
    print(txt)
    f.write(txt + "\n")
station_list = np.unique(pd.concat((df_meta.stid,df_meta2.stid)))
for station in station_list[18:]:
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
        fig.savefig('figures/GPS/%s_%i.png'%(station,k))
        Msg('![%s](../figures/GPS/%s_%i.png)'%(station, station,k))
    df_m = pd.read_csv(path_new+station+'/'+station+'_month.csv')
    df_m.time = pd.to_datetime(df_m.time, utc=True)
    df_m = df_m.set_index('time')
    df_m[[v for v in ['lat','lon','alt'] if v in df_m.columns]].to_csv('figures/GPS/coordinates/%s.csv'%station)
    Msg(' ')
tocgen.processFile(filename, filename[:-3]+"_toc.md")
f.close()

# %% reprocessing
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import os
import tocgen
import xarray as xr
from pypromice.process.L2toL3 import toL3

path_l2 = '../aws-l2-dev/level_2/'
path_l3 = '../aws-l3-dev/'
df_meta = pd.read_csv(path_l3+'/AWS_latest_locations.csv')
df_meta2 = pd.read_csv(path_l3+'/AWS_metadata.csv')
plt.close('all')
station_list = np.unique(pd.concat((df_meta.stid,df_meta2.stid)))
for station in station_list:
# for station in [ 'KPC_L']:
    print(station)
    inpath = path_l2 + station+'/'+station+ '_hour.nc'
    # Define Level 2 dataset from file
    with xr.open_dataset(inpath) as l2:
        l2.load()
    
    # Remove encoding attributes from NetCDF
    for varname in l2.variables:
       if l2[varname].encoding!={}:
           l2[varname].encoding = {}  
            
    if 'bedrock' in l2.attrs.keys():
        l2.attrs['bedrock'] = l2.attrs['bedrock'] == 'True'
    if 'number_of_booms' in l2.attrs.keys():
        l2.attrs['number_of_booms'] = int(l2.attrs['number_of_booms'])

    l3 = toL3(l2).to_dataframe()

    var_list_list = [['gps_lat','gps_lon','gps_alt']]
    for k, var_list in enumerate(var_list_list):
        fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(13,13))
        if len(var_list)==1:
            ax_list = [ax_list]
        
        for var, ax in zip(var_list, ax_list):
            if var in l3.columns:
                if not l3[var].isnull().all():                
                    ax.plot(l3.index, l3[var].values, 
                            marker='o',markeredgecolor='None', linestyle='None', 
                            color='tab:orange',label=var)  
            if var.replace('gps_','') in l3.columns:
                ax.plot(l3.index, l3[var.replace('gps_','')].values, 
                        color='tab:green', label=var.replace('gps_',''))  

            ax.set_ylabel(var.replace('gps_',''))       
            ax.grid()
            ax.legend()
        fig.savefig('figures/GPS_postproc/'+station+'.png',dpi=300)
