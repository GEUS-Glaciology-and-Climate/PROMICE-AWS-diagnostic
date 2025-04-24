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
import matplotlib.pyplot as plt
import xarray as xr
logging.getLogger('matplotlib.font_manager').disabled = True
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

path_to_l0 = '../aws-l0/'
path_to_l0 = 'C:/Users/bav/GitHub/PROMICE data/aws-l0/'
path_l3 = 'C:/Users/bav/GitHub/PROMICE data/thredds-data/metadata/'

path_l2 = 'L2_test/'

df_metadata = pd.read_csv(path_l3+'AWS_stations_metadata.csv')


for station in ['WEG_B']:
# for station in np.unique(np.array(df_metadata.station_id)):
    print(station)
    # Loading the L1 data:
    config_file_tx = path_to_l0 + '/tx/config/{}.toml'.format(station)
    config_file_raw = path_to_l0 + '/raw/config/{}.toml'.format(station)
    output_path = 'L2_test'

    print("\n ======== test get_l2 ========= \n")
    if os.path.isfile(config_file_tx):
        inpath = path_to_l0 + '/tx/'
        pAWS_tx = get_l2(config_file_tx,
                         inpath,
                         output_path+'/tx/',
                         variables=None, metadata=None,
                         data_issues_path='../PROMICE-AWS-data-issues')

    else:
        pAWS_tx = None

    if os.path.isfile(config_file_raw):
        inpath = path_to_l0 + '/raw/'+station+'/'
        pAWS_raw = get_l2(config_file_raw,
                          inpath,
                          output_path+'/raw/',
                         variables=None, metadata=None,
                         data_issues_path='../PROMICE-AWS-data-issues')
    else:
        pAWS_raw = None

    print("\n ======== test join_l2 ========= \n")
    inpath_raw = path_l2 + '/raw/'+station+'/'+station+'_hour.nc'
    inpath_tx = path_l2 + '/tx/'+station+'/'+station+'_hour.nc'
    outpath = 'L2_test/level_2/'

    print(station)
    l2_merged = join_l2(inpath_raw, inpath_tx, outpath,None,None)

    l2_merged.to_dataframe()[[v for v in l2_merged.data_vars if v.endswith('_i')]].plot(marker='o')

#%% test l2tol3
import pandas as pd
import logging, os
from pypromice.process.get_l2tol3 import get_l2tol3
import matplotlib.pyplot as plt
path_l2 = 'L2_test/level_2/'
config_folder = '../aws-l0/metadata/station_configurations/'
outpath = 'L3_test/stations/'
print("\n ======== test l2tol3 ========= \n")

for station in  ['WEG_B']:
# for station in df_metadata.stid:
    inpath = path_l2 + '/'+station+'/'+station+'_hour.nc'

    print(station)
    l3 = get_l2tol3(config_folder, inpath, outpath, None, None, None)

# % plotting L3 lat, lon alt
    try:
        var_list = ['lat','lon','alt']
        fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(13,13))
        if len(var_list)==1:
            ax_list = [ax_list]

        for var, ax in zip(var_list, ax_list):
            if 'gps_'+var in l3.data_vars:
                l3['gps_'+var].plot(ax=ax,
                              marker='.',markeredgecolor='None', linestyle='None',
                        color='tab:green', label='gps_'+var)
            l3[var].plot(ax=ax, marker='.',markeredgecolor='None', linestyle='None',
                            color='tab:orange',label=var)
            ax.set_ylabel(var.replace('gps_',''))
            ax.grid()
            ax.legend()
    except:
        pass

    try:
        plt.figure()
        for v in ['z_surf_1','z_surf_2','z_surf_combined']:
            l3[v].plot(label=v)
        plt.title(station)
        plt.legend()
    except:
        pass
    try:
        l3.to_dataframe()[[v for v in l3.keys() if 'd_t_' in v]].plot()
        plt.gca().invert_yaxis()
        l3.to_dataframe()[[v for v in l3.keys() if 'd_t_' in v]].plot()
        plt.gca().invert_yaxis()
    except:
        pass
    try:
        plt.figure()
        for v in [ 'usr', 'dsr',]:
            l3[v].plot(label=v, marker='x')
        for v in ['usr_cor', 'dsr_cor',]:
            l3[v].plot(label=v, marker='o')
        plt.title(station)
        plt.legend()
    except:
        pass

# %% test join_l3
from pypromice.process.join_l3 import join_l3
import pandas as pd
import matplotlib.pyplot as plt

path_l3_stations = 'L3_test/stations/'
df_metadata = pd.read_csv('../aws-l3-dev/AWS_sites_metadata.csv')
config_folder = '../aws-l0/metadata/station_configurations/'
outpath = 'L3_test/sites/'
folder_gcnet = 'C:/Users/bav/OneDrive - GEUS/Code/PROMICE/GC-Net-Level-1-data-processing/L1/hourly'
folder_glaciobasis = '../GlacioBasis_ESSD/'
print("\n ======== test join_l3 ========= \n")

for site in ['WEG_B']:
# for station in df_metadata.stid:
    inpath = path_l3_stations + '/'+site+'/'+site+'_hour.nc'

    print(site)
    l3_merged, sorted_list_station_data = join_l3(config_folder, site, path_l3_stations,
                        folder_gcnet, # folder_glaciobasis,
                        outpath, None, None)

    plt.figure()
    l3_merged.z_surf_combined.plot()
    l3_merged.z_ice_surf.plot()
    l3_merged.z_boom_u.plot(marker='.')
    plt.title(site)

    plt.figure()
    l3_merged.rh_u_wrt_ice_or_water.plot()
    plt.title(site)

    plt.figure()
    for tmp in sorted_list_station_data[::-1]:
        tmp[0].z_surf_combined.plot(label=tmp[1]['stid'])
        tmp[0].z_ice_surf.plot(label=tmp[1]['stid'])

    plt.legend()

# %%
var_list = [ 'p_u', 't_u', 'rh_u', 'wspd_u',  'wdir_u', 'dsr', 'usr', 'dlr', 'ulr',  'z_boom_u',
            #'t_i_1', 't_i_2', 't_i_3', 't_i_4', 't_i_5', 't_i_6', 't_i_7', 't_i_8',
            'tilt_y', 'tilt_x', 'rot',  'precip_u', 'gps_lat', 'gps_lon', 'gps_alt',  'p_i', 't_i', 'rh_i', 'wspd_i', 'wdir_i']

import matplotlib.pyplot as plt
import math

n_vars = len(var_list)
ncols = 2
nrows = math.ceil(n_vars / ncols)

fig, axs = plt.subplots(nrows, ncols, figsize=(14, 4 * nrows), sharex=True)
axs = axs.flatten()

for i, var in enumerate(var_list):
    for tmp in sorted_list_station_data[::-1]:
        tmp[0][var].plot(ax=axs[i], marker='.', label=tmp[1]['stid'])
    axs[i].set_title(var)
    axs[i].set_ylabel('')
    if i < len(var_list) - 2:
        axs[i].set_xticklabels([])
        axs[i].set_xlabel('')

# Hide any unused subplots
for j in range(i + 1, len(axs)):
    axs[j].set_visible(False)

axs[0].legend(loc='upper right')
axs[0].set_xlim(pd.to_datetime(['2022-01-01', '2025-04-03']))
plt.tight_layout()
