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

df_latest_loc = pd.read_csv(path_l3+'../AWS_latest_locations.csv')
df_metadata = pd.read_csv(path_l3+'../AWS_metadata.csv')

for station in ['KPC_U']:
# for station in np.unique(np.array(all_dirs)): 
        
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

path_l2 = 'L2_test/level_2/'
df_latest_loc = pd.read_csv('C:/Users/bav/GitHub/PROMICE data/aws-l3-dev/AWS_latest_locations.csv')
df_metadata = pd.read_csv('C:/Users/bav/GitHub/PROMICE data/aws-l3-dev/AWS_metadata.csv')
    
outpath = 'L3_test/stations/'
print("\n ======== test l2tol3 ========= \n")
for station in ['KPC_U']:
# for station in df_metadata.stid:
    inpath = path_l2 + '/'+station+'/'+station+'_hour.nc'
    
    print(station)
    l3 = get_l2tol3(inpath, outpath, None, None)
    
# %% test join_l3
from pypromice.process.join_l3 import join_l3
import pandas as pd

path_l3_stations = 'L3_test/stations/'
df_latest_loc = pd.read_csv('../aws-l3-dev/AWS_latest_locations.csv')
df_metadata = pd.read_csv('../aws-l3-dev/AWS_metadata.csv')
config_folder = '../aws-l0/metadata/station_configurations/'
outpath = 'L3_test/sites/'
folder_gcnet = 'C:/Users/bav/OneDrive - GEUS/Code/PROMICE/GC-Net-Level-1-data-processing/L1/hourly'
print("\n ======== test join_l3 ========= \n")

for site in ['KPC_U']:
# for station in df_metadata.stid:
    inpath = path_l3_stations + '/'+site+'/'+site+'_hour.nc'
    
    print(site)
    l3_merged = join_l3(config_folder, site, path_l3_stations, 
                        folder_gcnet, outpath, None, None)