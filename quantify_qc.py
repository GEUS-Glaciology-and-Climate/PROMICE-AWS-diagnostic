# -*- coding: utf-8 -*-
"""
Created on %(date)s
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
logging.getLogger("pypromice").setLevel(logging.DEBUG)
logging.getLogger("pypromice.pipeline").setLevel(logging.DEBUG)
logging.getLogger("pypromice.pipeline.get_l2").setLevel(logging.DEBUG)
logging.getLogger('numba').setLevel(logging.WARNING)


def process_l2_no_qc(station,
                     output_path = 'L2_no_qc',
                     data_issues_path='../PROMICE-AWS-data-issues_no'):

    print(station)
    # Loading the L1 data:
    path_to_l0 = '../aws-l0/'
    config_folder = '../aws-l0/metadata/station_configurations/'
    config_file_tx = path_to_l0 + '/tx/config/{}.toml'.format(station)
    config_file_raw = path_to_l0 + '/raw/config/{}.toml'.format(station)



    print("\n ======== test get_l2 ========= \n")
    if os.path.isfile(config_file_tx):
        inpath = path_to_l0 + '/tx/'
        pAWS_tx = get_l2(config_file_tx,
                         inpath,
                         output_path+'/tx/',
                         variables=None, metadata=None,
                         data_issues_path=data_issues_path)

    else:
        pAWS_tx = None

    if os.path.isfile(config_file_raw):
        inpath = f'{path_to_l0}/raw/{station}/'
        pAWS_raw = get_l2(config_file_raw,
                          inpath,
                          output_path+'/raw/',
                         variables=None, metadata=None,
                         data_issues_path=data_issues_path)
    else:
        pAWS_raw = None

    print("\n ======== test join_l2 ========= \n")
    l2_merged = join_l2(f'{output_path}/raw/{station}/{station}_hour.nc',
                        f'{output_path}/tx/{station}/{station}_hour.nc',
                        f'{output_path}/level_2/',None,None)

if __name__ == '__main__':
    df_metadata = pd.read_csv('../thredds-data/metadata/AWS_stations_metadata.csv')
    # for station in ['CEN1']:
    for station in df_metadata.station_id[1:]:
        # process_l2_no_qc(station,
        #                      output_path = 'L2_no_qc',
        #                      data_issues_path='../PROMICE-AWS-data-issues_no')
        process_l2_no_qc(station,
                             output_path = 'L2_test',
                             data_issues_path='../PROMICE-AWS-data-issues')

# %%
