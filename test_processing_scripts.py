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
import xarray as xr
import sys, importlib
# purge cached package + submodules
# only useful in debugging mode
for name in list(sys.modules):
    if name == "pypromice" or name.startswith("pypromice."):
        del sys.modules[name]
importlib.invalidate_caches()
from pypromice.pipeline.get_l2 import get_l2
from pypromice.pipeline.join_l2 import join_l2
from pypromice.pipeline.get_l2tol3 import get_l2tol3
from pypromice.pipeline.join_l3 import join_l3
import time


logging.getLogger('matplotlib.font_manager').disabled = True
logging.getLogger("pypromice").setLevel(logging.INFO)
logging.getLogger("pypromice.pipeline").setLevel(logging.INFO)
logging.getLogger("pypromice.pipeline.get_l2").setLevel(logging.INFO)
logging.getLogger('numba').setLevel(logging.WARNING)

config_folder = '../aws-l0/metadata/station_configurations/'
# %%
def process_l2(station):

    print(station)
    # Loading the L1 data:
    path_to_l0 = '../aws-l0/'

    config_file_tx = path_to_l0 + '/tx/config/{}.toml'.format(station)
    config_file_raw = path_to_l0 + '/raw/config/{}.toml'.format(station)
    output_path = 'data/L2_test'

    if os.path.isfile(config_file_tx):
        inpath = path_to_l0 + '/tx/'
        pAWS_tx = get_l2(config_file_tx,
                        inpath,
                         output_path+'/tx/',
                        variables=None, metadata=None,
                        data_issues_path='../PROMICE-AWS-data-issues',
                        declination_path=f"{path_to_l0}/magnetic_declination_coefs/magnetic_declination_igrf_coefs.toml",
                        write_60min=True)

    else:
        pAWS_tx = None

    if os.path.isfile(config_file_raw):
        inpath = path_to_l0 + '/raw/'+station+'/'
        pAWS_raw = get_l2(config_file_raw,
                    inpath,
                    output_path+'/raw/',
                    variables=None,
                    metadata=None,
                    data_issues_path='../PROMICE-AWS-data-issues',
                    declination_path=f"{path_to_l0}/magnetic_declination_coefs/magnetic_declination_igrf_coefs.toml",
                    write_60min=True)

    else:
        pAWS_raw = None
    return pAWS_tx, pAWS_raw


def get_join_l3(site):

    path_l3_stations = 'data/L3_test/stations/'
    folder_gcnet = '../GC-Net-level-1-data-processing/L1/hourly'
    folder_glaciobasis = '../historical-zac-data/'

    for f in [f'data/L3_test/sites/{site}/{site}_hour.nc',
              f'data/L3_test/sites/{site}/{site}_day.nc',
              f'data/L3_test/sites/{site}/{site}_month.nc']:
        if os.path.exists(f):
            os.remove(f)

    l3_merged, sorted_list_station_data = join_l3(config_folder, site, path_l3_stations,
                        folder_gcnet, folder_glaciobasis, 'data/L3_test/sites/', None, None)
    return l3_merged, sorted_list_station_data


if __name__ == '__main__':

    station_metadata = pd.read_csv('../thredds-data/metadata/AWS_stations_metadata.csv')
    site_metadata = pd.read_csv('../thredds-data/metadata/AWS_sites_metadata.csv')
    for site in site_metadata.site_id:
    # for site in ['SWC']:
        t0 = time.perf_counter()
        for station in site_metadata.loc[site_metadata.site_id == site, 'stations'].values[0].split(' '):
        # for station in ['SUM']:
            if station in station_metadata.station_id.values:
                print("\n ======== test get_l2 ========= \n")
                pAWS_tx, pAWS_raw = process_l2(station)

                print("\n ======== test join_l2 ========= \n")
                l2_merged = join_l2('data/L2_test/raw/'+station+'/'+station+'_mixed.nc',
                                    'data/L2_test/tx/'+station+'/'+station+'_mixed.nc',
                                    'data/L2_test/level_2/',None,None)

                print("\n ======== test l2tol3 ========= \n")
                l3 = get_l2tol3(config_folder,
                                'data/L2_test/level_2/'+station+'/'+station+'_mixed.nc',
                                'data/L3_test/stations/', None, None, None)
            else:
                print(f"==== skipping {station} ====")

        print(" ======== test join_l3 ========= \n")
        l3_merged, sorted_list_station_data = get_join_l3(site)

    dt = time.perf_counter() - t0
    # print(f"Elapsed time: {dt:.3f} s")
    # new Elapsed time: 45.259 s
    # v1.11.0 Elapsed time: 138.733 s
    # v1.10.2 Elapsed time: 187.174 s
# %%
# l3_merged, sorted_list_station_data = get_join_l3(site)
# import matplotlib.pyplot as plt
# plt.figure()
# for (ds, attrs) in sorted_list_station_data:
#     ds.t_u.plot(label=attrs['stid'])
#     # l3_merged.t_u.plot()
#     plt.legend()
#     # data_version = 'L2_test/tx/'
#     data_version = 'L3_test/sites/'

#     res = 'hour'
#     res_org = res if res!='mixed' else 'hour'

#     # site = 'CEN2'
#     site_org = site.replace('v3','')

#     var = 'dsr'

#     ds_new = xr.open_dataset(f'data/{data_version}/{site}/{site}_{res}.nc',
#                              decode_times=True)
#     df_new = ds_new.to_dataframe()
#     df_new.index = df_new.index.astype('datetime64[ns]')



#     plt.figure()
#     plt.plot(df_new.index, df_new[var], marker='o', label='new')
#     plt.plot(df_new.index, df_new['z_ice_surf'], label='z_ice_surf')
#     # df_new.loc[:,'snow_height'].plot(label='snow_height')
#     plt.title(data_version + ' ' + site)
#     plt.ylabel(var)

#     station_list = ds_new.attrs['stations'].split(' ')
#     for station in station_list:
#         df_l2 = xr.open_dataset(f'data/L3_test/stations/{station}/{station}_mixed.nc',
#                                 decode_times=True).to_dataframe()
#         df_l2.index = df_l2.index.astype('datetime64[ns]')

#         plt.plot(df_l2.index, df_l2['z_surf_combined'], marker='^',
#                                       label=f'{station} z_surf_combined')


    # df_org = pd.read_csv(f'../thredds-data/level_3_sites/csv/{res_org}/{site_org}_{res_org}.csv')
    # df_org.time = pd.to_datetime(df_org.time)
    # df_org = df_org.set_index('time')
    # df_org.loc[:,var].plot(marker='^',zorder=0, c='k', label='thredds')
    # df_org.loc[:,var].plot(marker='^',zorder=0, c='k', label='thredds')
    # pAWS_tx.L1A.tilt_x.plot(marker='d',label='L1 tilt_x')
    # pAWS_tx.L2.t_rad.plot(marker='d',label='L1 t_rad')
    # plt.legend()
