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
                         # outpath = None,
                         variables=None, metadata=None,
                         data_issues_path='../PROMICE-AWS-data-issues')

    else:
        pAWS_tx = None

    if os.path.isfile(config_file_raw):
        inpath = path_to_l0 + '/raw/'+station+'/'
        pAWS_raw = get_l2(config_file_raw,
                    inpath,
                    output_path+'/raw/',
                    # outpath = None,
                    variables=None,
                    metadata=None,
                    data_issues_path='../PROMICE-AWS-data-issues')

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
    df_metadata = pd.read_csv('../thredds-data/metadata/AWS_stations_metadata.csv')
    # for station in np.unique(np.array(df_metadata.station_id)):
    for station in ['TAS_L']:
        print("\n ======== test get_l2 ========= \n")
        pAWS_tx, pAWS_raw = process_l2(station)

        print("\n ======== test join_l2 ========= \n")
        l2_merged = join_l2('data/L2_test/raw/'+station+'/'+station+'_10min.nc',
                            'data/L2_test/tx/'+station+'/'+station+'_hour.nc',
                            'data/L2_test/level_2/',None,None)

        print("\n ======== test l2tol3 ========= \n")
        l3 = get_l2tol3(config_folder,
                        'data/L2_test/level_2/'+station+'/'+station+'_10min.nc',
                        'data/L3_test/stations/', None, None, None)

    df_metadata = pd.read_csv('../thredds-data/metadata/AWS_sites_metadata.csv')
    # for site in df_metadata.site_id:
    for site in ['TAS_L']:
        print(" ======== test join_l3 ========= \n")
        l3_merged, sorted_list_station_data = get_join_l3(site)

        # %%
        import matplotlib.pyplot as plt
        # df_day_org = pd.read_csv('data\L3_test\sites\LYN_L\LYN_L_day_org.csv')
        # df_day_org.time = pd.to_datetime(df_day_org.time)
        # df_day_org = df_day_org.set_index('time')
        # plt.figure()
        # df_day_org.loc['2026':,'z_surf_combined'].plot(marker='o')
        # df_day_org.loc['2026':,'t_u'].plot(marker='o')

        df_day = pd.read_csv(f'data\L3_test\sites\{site}\{site}_hour.csv')
        df_day.time = pd.to_datetime(df_day.time)
        df_day = df_day.set_index('time')
        plt.figure()
        df_day.loc['2025-03-27':,'tilt_x'].plot(marker='o')
        df_day.loc['2025-03-27':,'tilt_y'].plot(marker='o')
        plt.figure()
        df_day.loc['2025-03-27':,'cc'].plot(marker='o')
        plt.figure()
        df_day.loc['2025-03-27':,'t_surf'].plot(marker='o')

        # df_hour = pd.read_csv('data\L3_test\sites\LYN_L\LYN_L_hour.csv')
        # df_hour.time = pd.to_datetime(df_hour.time)
        # df_hour = df_hour.set_index('time')
        # plt.figure()
        # df_hour.loc['2026':,'z_surf_combined'].plot(marker='o')
        # df_hour.loc['2026':,'t_u'].plot(marker='o')

        # # %%
        # import matplotlib.pyplot as plt
        # df_day_org = pd.read_csv('data\L3_test\sites\LYN_L\LYN_L_day_org.csv')
        # df_day_org.time = pd.to_datetime(df_day_org.time)
        # df_day_org = df_day_org.set_index('time')
        # df_day = pd.read_csv('data\L3_test\sites\LYN_L\LYN_L_day.csv')
        # df_day.time = pd.to_datetime(df_day.time)
        # df_day = df_day.set_index('time')

        # plt.figure()
        # df_day_org.loc['2026':,'z_surf_combined'].plot(marker='o')
        # df_day.loc['2026':,'z_surf_combined'].plot(marker='o')

        # df_hour = pd.read_csv('data\L3_test\sites\LYN_L\LYN_L_hour.csv')
        # df_hour.time = pd.to_datetime(df_hour.time)
        # df_hour = df_hour.set_index('time')
        # plt.figure()
        # df_hour.loc['2026':,'z_surf_combined'].plot(marker='o')
        # df_hour.loc['2026':,'t_u'].plot(marker='o')
