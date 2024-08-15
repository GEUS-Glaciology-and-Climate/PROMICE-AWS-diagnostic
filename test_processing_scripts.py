# -*- coding: utf-8 -*-
"""
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""
import pandas as pd
import numpy as np
import os, logging
from pypromice.process.get_l2 import get_l2
from pypromice.process.join_l2 import join_l2
from pypromice.process.join_l2 import loadArr

path_to_l0 = '../aws-l0/'
path_to_l0 = 'C:/Users/bav/GitHub/PROMICE data/aws-l0/'
path_l3 = '../aws-l3/level_3/'
path_l3 = 'C:/Users/bav/GitHub/PROMICE data/aws-l3-dev/level_3/'

path_l2 = 'L2_test/'

df_metadata = pd.read_csv(path_l3+'../AWS_stations_metadata.csv')

for station in ['CEN2']:
# for station in np.unique(np.array(df_metadata.station_id)): 
        
    # Loading the L1 data:
    config_file_tx = path_to_l0 + '/tx/config/{}.toml'.format(station)
    config_file_raw = path_to_l0 + '/raw/config/{}.toml'.format(station)
    output_path = 'L2_test'
    
    print("\n ======== test get_l2 ========= \n")
    if os.path.isfile(config_file_tx):
        inpath = path_to_l0 + '/tx/'
        pAWS_tx = get_l2(config_file_tx, inpath, output_path+'/tx/',None,None)

    else:
        pAWS_tx = None
        
    if os.path.isfile(config_file_raw):
        inpath = path_to_l0 + '/raw/'+station+'/'
        pAWS_raw = get_l2(config_file_raw, inpath,  output_path+'/raw/',None,None)
    else:
        pAWS_raw = None
        
    print("\n ======== test join_l2 ========= \n")
    inpath_raw = path_l2 + '/raw/'+station+'/'+station+'_hour.nc'
    inpath_tx = path_l2 + '/tx/'+station+'/'+station+'_hour.nc'
    outpath = 'L2_test/level_2/'

    print(station)
    l2_merged = join_l2(inpath_raw,inpath_tx,outpath,None,None)

#%% test l2tol3
import pandas as pd
import logging, os
from pypromice.process.get_l2tol3 import get_l2tol3
import matplotlib.pyplot as plt
path_l2 = 'L2_test/level_2/'
df_metadata = pd.read_csv('C:/Users/bav/GitHub/PROMICE data/aws-l3-dev/AWS_stations_metadata.csv')
    
config_folder = '../aws-l0/metadata/station_configurations/'
outpath = 'L3_test/stations/'
print("\n ======== test l2tol3 ========= \n")
for station in ['CEN2']:
# for station in df_metadata.stid:
    inpath = path_l2 + '/'+station+'/'+station+'_hour.nc'
    
    print(station)
    l3 = get_l2tol3(config_folder, inpath, outpath, None, None)
    
# % plotting L3 lat, lon alt
    var_list = ['lat','lon','alt']
    fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(13,13))
    if len(var_list)==1:
        ax_list = [ax_list]
    
    for var, ax in zip(var_list, ax_list):
        if 'gps_'+var in l3.data_vars:
            l3['gps_'+var].plot(ax=ax,
                         marker='.',markeredgecolor='None', linestyle='None', 
                    color='tab:green', label=var.replace('gps_',''))
        l3[var].plot(ax=ax, marker='.',markeredgecolor='None', linestyle='None', 
                        color='tab:orange',label=var)  
        ax.set_ylabel(var.replace('gps_',''))       
        ax.grid()
        ax.legend()
        
# %% plotting L3 surface heighta
    plt.figure()
    l3['z_surf_1'].plot()
    l3['z_surf_2'].plot()
    l3['z_surf_combined'].plot()
    plt.title(station)
    
    # plt.figure()
    # l3.to_dataframe()[[v for v in l3.keys() if 'd_t_' in v]].plot()    
    # plt.gca().invert_yaxis()
# %% test join_l3
from pypromice.process.join_l3 import join_l3
import pandas as pd

path_l3_stations = 'L3_test/stations/'
df_metadata = pd.read_csv('../aws-l3-dev/AWS_sites_metadata.csv')
config_folder = '../aws-l0/metadata/station_configurations/'
outpath = 'L3_test/sites/'
folder_gcnet = 'C:/Users/bav/OneDrive - GEUS/Code/PROMICE/GC-Net-Level-1-data-processing/L1/hourly'
print("\n ======== test join_l3 ========= \n")

for site in ['CEN']:
# for station in df_metadata.stid:
    inpath = path_l3_stations + '/'+site+'/'+site+'_hour.nc'
    
    print(site)
    l3_merged, sorted_list_station_data = join_l3(config_folder, site, path_l3_stations, 
                        folder_gcnet, outpath, None, None)
    
