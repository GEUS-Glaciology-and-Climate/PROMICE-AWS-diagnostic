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
import logging, toml, os
from pypromice.process.L2toL3 import process_surface_height
from pypromice.process.get_l2 import get_l2
from pypromice.process.join_l2 import join_l2
from pypromice.process.join_l2 import loadArr
from pathlib import Path
# import matplotlib
# matplotlib.use('Agg')

logging.getLogger('matplotlib.font_manager').disabled = True
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

path_to_l0 = 'C:/Users/bav/GitHub/PROMICE data/aws-l0/'
config_folder = '../aws-l0/metadata/station_configurations/'
df_metadata = pd.read_csv('C:/Users/bav/GitHub/PROMICE data/aws-l3-dev/AWS_stations_metadata.csv')

path_l2 = 'L2_test/'
    
# plt.close('all')

for station in ['TAS_L']:
# for station in df_metadata.station_id:
        
    config_file_tx = path_to_l0 + '/tx/config/{}.toml'.format(station)
    config_file_raw = path_to_l0 + '/raw/config/{}.toml'.format(station)
    
    print("\n ======== Processing L2 ========= \n")
    if os.path.isfile(config_file_tx):
        inpath = path_to_l0 + '/tx/'
        pAWS_tx = get_l2(config_file_tx, inpath, path_l2+'/tx/',None,None,
                         data_issues_path='../PROMICE-AWS-data-issues')

    else:
        pAWS_tx = None
        
    if os.path.isfile(config_file_raw):
        inpath = path_to_l0 + '/raw/'+station+'/'
        pAWS_raw = get_l2(config_file_raw, inpath,  path_l2+'/raw/',None,None,
                         data_issues_path='../PROMICE-AWS-data-issues')
    else:
        pAWS_raw = None
        
    print("\n ======== Joining L2 ========= \n")
    inpath_raw = path_l2 + '/raw/'+station+'/'+station+'_hour.nc'
    inpath_tx = path_l2 + '/tx/'+station+'/'+station+'_hour.nc'
    

    print(station)
    l2_merged = join_l2(inpath_raw, inpath_tx, path_l2+'/level_2/', None, None)

    print("\n ======== Processing L3 surface heights ========= \n")

    inpath = path_l2+'/level_2/'+station+'/'+station+'_hour.nc'
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
    
    # %% Perform Level 3 processing
    l3 = process_surface_height(l2, Path('../PROMICE-AWS-data-issues')/'adjustments', station_config).to_dataframe()

    # %%
    fig, ax = plt.subplots(3,1, sharex=True, figsize=(10,10))
    var_list = [v for v in ['z_boom_u','z_boom_l','z_stake','z_pt_cor'] if v in l3.columns]
    l3[var_list].plot(ax=ax[0],marker='.')
    ax[0].set_title(station)
    ax[0].set_ylabel('Height (m)')
    ax[0].grid()

    var_list = [v for v in ['z_surf_1','z_surf_2','z_ice_surf', 'z_surf_1_adj','z_surf_2_adj',
                            'z_surf_combined',] if v in l3.columns]
    l3[var_list].plot(ax=ax[1],marker='.',alpha=0.6)
    ax[1].set_ylabel('Height (m)')
    ax[1].grid()

    var_list = [v for v in ['snow_height'] if v in l3.columns]
    l3[var_list].plot(ax=ax[2],marker='.',alpha=0.6)
    ax[2].set_ylabel('Height (m)')
    ax[2].grid()
    

    fig.savefig('figures/surface_height_assessment/'+station+'.png', dpi=300)


