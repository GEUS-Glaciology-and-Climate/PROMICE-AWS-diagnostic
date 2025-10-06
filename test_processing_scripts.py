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
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr
import sys, importlib
for name in list(sys.modules):
    if name == "pypromice" or name.startswith("pypromice."):
        del sys.modules[name]
importlib.invalidate_caches()
from pypromice.pipeline.get_l2 import get_l2
from pypromice.pipeline.join_l2 import join_l2
from pypromice.pipeline.join_l2 import loadArr
from pypromice.pipeline.get_l2tol3 import get_l2tol3
logging.getLogger('matplotlib.font_manager').disabled = True
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
logging.getLogger('numba').setLevel(logging.WARNING)

path_to_l0 = '../aws-l0/'
config_folder = '../aws-l0/metadata/station_configurations/'
df_metadata = pd.read_csv('../thredds-data/metadata/AWS_stations_metadata.csv')

for station in ['UPE_L']:
# for station in np.unique(np.array(df_metadata.station_id)):
# def process_l2_l3(station):
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
    l2_merged = join_l2('L2_test/raw/'+station+'/'+station+'_hour.nc',
                        'L2_test/tx/'+station+'/'+station+'_hour.nc',
                        'L2_test/level_2/',None,None)

    print("\n ======== test l2tol3 ========= \n")
    l3 = get_l2tol3(config_folder,
                    'L2_test/level_2/'+station+'/'+station+'_hour.nc',
                    'L3_test/stations/', None, None, None)

    if False:
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
import sys, importlib

# purge cached package + submodules
for name in list(sys.modules):
    if name == "pypromice" or name.startswith("pypromice."):
        del sys.modules[name]
importlib.invalidate_caches()

from pypromice.pipeline.join_l3 import join_l3
import pandas as pd
import matplotlib.pyplot as plt

path_l3_stations = 'L3_test/stations/'
df_metadata = pd.read_csv('../thredds-data/metadata/AWS_sites_metadata.csv')
config_folder = '../aws-l0/metadata/station_configurations/'
folder_gcnet = '../GC-Net-Level-1-data-processing/L1/hourly'
folder_glaciobasis = '../GlacioBasis_ESSD/'
print(" ======== test join_l3 ========= \n")
import os


for site in ['UPE_L']:
# for site in df_metadata.site_id:
# def get_join_l3(site):
    print(site)
    for f in [f'L3_test/sites/{site}/{site}_hour.nc',
              f'L3_test/sites/{site}/{site}_day.nc',
              f'L3_test/sites/{site}/{site}_month.nc']:
        if os.path.exists(f):
            os.remove(f)

    l3_merged, sorted_list_station_data = join_l3(config_folder, site, path_l3_stations,
                        folder_gcnet, # folder_glaciobasis,
                        'L3_test/sites/', None, None)

def fresh_load(path):
    ds = xr.open_dataset(path, lock=False, cache=False)
    ds.load()
    ds.close()
    return ds

ds_h = fresh_load(f'L3_test/sites/{site}/{site}_hour.nc')
ds_d = fresh_load(f'L3_test/sites/{site}/{site}_day.nc')
ds_m = fresh_load(f'L3_test/sites/{site}/{site}_month.nc')

var = 'z_boom_u'

plt.figure()
ds_h[var].plot(ax=plt.gca(), marker='o', label='hour')
ds_d[var].plot(ax=plt.gca(), marker='o', label='day')
ds_m[var].plot(ax=plt.gca(), marker='o', label='month')

    # %%
if False:
    # %% Test precipitation

    # %%
    plt.figure()
    (ds_h.rainfall_cor_u*24).plot(ax=plt.gca(), marker='o')
    ds_d.rainfall_cor_u.plot(ax=plt.gca(), marker='o')
    (ds_m.rainfall_cor_u/30).plot(ax=plt.gca(), marker='o')

    plt.figure()
    l2_merged.precip_u.plot(ax=plt.gca(), marker='o')
    ds_h.rainfall_cor_u.cumsum().plot(ax=plt.gca(), marker='o')
    ds_d.rainfall_cor_u.cumsum().plot(ax=plt.gca(), marker='o')
    ds_m.rainfall_cor_u.cumsum().plot(ax=plt.gca(), marker='o')



    # %%

    import matplotlib.pyplot as plt
    import math


    vars_list = ['t_u'] #[v for v in ds_h.data_vars if ds_h[v].notnull().any()]
    nvars = len(vars_list)
    ncols = 1
    nrows = math.ceil(nvars / 6)  # groups of 6 plots per figure

    for g in range(nrows):
        fig, axes = plt.subplots(1, 1, figsize=(10, 12), sharex=True)
        axes = np.atleast_1d(axes)

        for i in range(6):
            idx = g * 6 + i
            if idx >= nvars:
                axes[i].set_visible(False)
                continue
            var = vars_list[idx]
            # ds_l2_10min[var].plot(ax=axes[i], marker=".", ls="None", label="L2 10min w/o completeness")
            # ds_l2_h[var].plot(ax=axes[i], marker=".", ls="None", label="L2 hourly w/o completeness")
            # ds_d[var].plot(ax=axes[i], marker="o", ls="None", label="L3 daily w/o completeness")
            ds_d_f[var].plot(ax=axes[i], marker="o", ls="None", label="__nolegend__")
            ds_d_f[var].plot(ax=axes[i], marker="o", ls="None", label="__nolegend__")
            ds_d_f[var].plot(ax=axes[i], marker="o", ls="None", label="L3 daily filtered")
            axes[i].set_title(var)
            axes[i].legend()

        plt.tight_layout()
        plt.show()
        break



# %%
# var_list = [ 'p_u', 't_u', 'rh_u', 'wspd_u',  'wdir_u', 'dsr', 'usr', 'dlr', 'ulr',  'z_boom_u',
#             #'t_i_1', 't_i_2', 't_i_3', 't_i_4', 't_i_5', 't_i_6', 't_i_7', 't_i_8',
#             'tilt_y', 'tilt_x', 'rot',  'precip_u', 'gps_lat', 'gps_lon', 'gps_alt',  'p_i', 't_i', 'rh_i', 'wspd_i', 'wdir_i']

# import matplotlib.pyplot as plt
# import math

# n_vars = len(var_list)
# ncols = 2
# nrows = math.ceil(n_vars / ncols)

# fig, axs = plt.subplots(nrows, ncols, figsize=(14, 4 * nrows), sharex=True)
# axs = axs.flatten()

# for i, var in enumerate(var_list):
#     for tmp in sorted_list_station_data[::-1]:
#         tmp[0][var].plot(ax=axs[i], marker='.', label=tmp[1]['stid'])
#     axs[i].set_title(var)
#     axs[i].set_ylabel('')
#     if i < len(var_list) - 2:
#         axs[i].set_xticklabels([])
#         axs[i].set_xlabel('')

# # Hide any unused subplots
# for j in range(i + 1, len(axs)):
#     axs[j].set_visible(False)

# axs[0].legend(loc='upper right')
# axs[0].set_xlim(pd.to_datetime(['2022-01-01', '2025-04-03']))
# plt.tight_layout()
