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
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
logging.getLogger('numba').setLevel(logging.WARNING)


# %%

def process_l2_l3(station):

    print(station)
    # Loading the L1 data:
    path_to_l0 = '../aws-l0/'
    config_folder = '../aws-l0/metadata/station_configurations/'
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
    return pAWS_tx, pAWS_raw, l2_merged, l3


# %% test join_l3


def get_join_l3(site):

    print(" ======== test join_l3 ========= \n")
    path_l3_stations = 'L3_test/stations/'
    config_folder = '../aws-l0/metadata/station_configurations/'
    folder_gcnet = '../GC-Net-Level-1-data-processing/L1/hourly'
    folder_glaciobasis = '../historical-zac-data/'

    print(site)
    for f in [f'L3_test/sites/{site}/{site}_hour.nc',
              f'L3_test/sites/{site}/{site}_day.nc',
              f'L3_test/sites/{site}/{site}_month.nc']:
        if os.path.exists(f):
            os.remove(f)

    l3_merged, sorted_list_station_data = join_l3(config_folder, site, path_l3_stations,
                        folder_gcnet, folder_glaciobasis,
                        'L3_test/sites/', None, None)
    return l3_merged, sorted_list_station_data


if __name__ == '__main__':
    df_metadata = pd.read_csv('../thredds-data/metadata/AWS_stations_metadata.csv')
    for station in ['ZAC_Lv3','ZAC_Uv3',]:
    # for station in np.unique(np.array(df_metadata.station_id)):
        pAWS_tx, pAWS_raw, l2_merged, l3 = process_l2_l3(station)

    df_metadata = pd.read_csv('../thredds-data/metadata/AWS_sites_metadata.csv')
    for site in ['ZAC_L','ZAC_U']:
    # for site in df_metadata.site_id:
        l3_merged, sorted_list_station_data = get_join_l3(site)
