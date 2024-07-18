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
import xarray as xr
import logging, toml
from pypromice.process.L2toL3 import process_surface_height

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

# import matplotlib
# matplotlib.use('Agg')

# path_to_l0 = '../aws-l0/'
path_to_l0 = 'C:/Users/bav/GitHub/PROMICE data/aws-l0/'
path_to_l1 = 'C:/Users/bav/GitHub/PROMICE data/aws-l1/'
# path_l3 = '../aws-l3/level_3/'
path_l2 = 'C:/Users/bav/GitHub/PROMICE data/aws-l2-dev/level_2/'
path_l3 = 'C:/Users/bav/GitHub/PROMICE data/aws-l3-dev/level_3/'
config_folder = '../aws-l0/metadata/station_configurations/'


df_metadata = pd.read_csv(path_l3+'../AWS_stations_metadata.csv')
    
plt.close('all')

for station in ['KAN_Lv3']:
# for station in df_metadata.stid: 
    station = station.replace('.csv','')
    inpath = path_l2+'/'+station+'/'+station+'_hour.nc'
    print(station)
  
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
    
    # importing station_config (dict) from config_folder (str path)
    config_file = config_folder+l2.attrs['station_id']+'.toml'
    with open(config_file) as fp:
        station_config = toml.load(fp)
    # Perform Level 3 processing
    l3 = process_surface_height(l2, station_config).to_dataframe()

    # %%
    plt.figure()
    l3[['z_surf_1','z_surf_2','z_surf_combined','z_ice_surf','snow_height','z_pt_cor']].plot()
    plt.title(station)


