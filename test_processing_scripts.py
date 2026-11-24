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
def process_l2(station, keep_flagged_data=False):

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
                        write_60min=True,
                        keep_flagged_data=keep_flagged_data)

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
                    write_60min=True,
                    keep_flagged_data=keep_flagged_data)

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
    # for site in site_metadata.site_id:
    for site in ['NUK_K']:
        t0 = time.perf_counter()
        station_list = site_metadata.loc[site_metadata.site_id == site, 'stations'].values[0].split(' ')
        # station_list = ['SUM']

        for station in station_list:
        # for station in ['KPC_L','TUN','NAE','NAU']:
            if station in station_metadata.station_id.values:
                print("\n ======== test get_l2 ========= \n")
                pAWS_tx, pAWS_raw = process_l2(station,
                                               # keep_flagged_data = True
                                               )

                # for k, v in pAWS_raw.L2.attrs.items():
                #     if isinstance(v, (bool, np.bool_)):
                #         pAWS_raw.L2.attrs[k] = int(v)
                # pAWS_raw.L2.to_netcdf(f'data/{station}_L2_raw_with_flags.nc')
                # if pAWS_tx is not None:
                #     for k, v in pAWS_tx.L2.attrs.items():
                #         if isinstance(v, (bool, np.bool_)):
                #             pAWS_tx.L2.attrs[k] = int(v)
                #     if "msg_i" in pAWS_tx.L2:
                #         pAWS_tx.L2["msg_i"] = pAWS_tx.L2["msg_i"].fillna("").astype(str)
                #     pAWS_tx.L2.to_netcdf(f'data/{station}_L2_tx_with_flags.nc')

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


# %%
# l3_merged, sorted_list_station_data = get_join_l3(site)

import matplotlib.pyplot as plt
plt.figure()
for (ds, attrs) in sorted_list_station_data:
    # data_version = 'L2_test/tx/'
    data_version = 'L3_test/stations/'

    res = 'mixed'
    res_org = res if res!='mixed' else 'hour'

    # site = 'CEN2'
    site_org = site.replace('v3','')

    var = 'snow_height'

    ds_new = xr.open_dataset(f'data/{data_version}/{site}/{site}_{res}.nc',
                              decode_times=True)
    df_new = ds_new.to_dataframe()
    df_new.index = df_new.index.astype('datetime64[ns]')



    plt.figure()
    plt.plot(df_new.index, df_new[var], marker='o', label='new')
    plt.title(data_version + ' ' + site)
    plt.ylabel(var)

    if 'stations' in ds_new.attrs.keys():
        station_list = ds_new.attrs['stations'].split(' ')
    else:
        station_list = [site]
    for station in station_list:
        df_l2 = xr.open_dataset(f'data/L2_test/level_2/{station}/{station}_mixed.nc',
                                decode_times=True).to_dataframe()
        df_l2.index = df_l2.index.astype('datetime64[ns]')

    df_org = pd.read_csv(f'../thredds-data/level_3_sites/csv/{res_org}/{site_org}_{res_org}.csv')
    df_org.time = pd.to_datetime(df_org.time)
    df_org = df_org.set_index('time')
    df_org.loc[:,var].plot(marker='^',zorder=0, c='k', label='thredds')
    if var in df_l2.columns:
        df_l2.loc[:,var].plot(marker='^',zorder=0, c='k', label='thredds')

    plt.legend()
