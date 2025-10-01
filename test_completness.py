# -*- coding: utf-8 -*-
"""
Created on %(date)s
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# from sklearn.linear_model import LinearRegression
import os, logging, glob
import matplotlib
# matplotlib.use('Agg')

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

matplotlib.set_loglevel("warning")
logging.getLogger('numba').setLevel(logging.WARNING)
from lib import ( load_flags_and_adjustments, load_L1)

path_to_l0 = 'C:/Users/bav/GitHub/PROMICE data/aws-l0/'
path_to_l1 = 'C:/Users/bav/GitHub/PROMICE data/aws-l1/'
path_tx = '../aws-l3/tx/'

from datetime import date
today = date.today().strftime("%Y%m%d")
filename = './plot_compilations/flags.md'
figure_folder='figures/flags'
try:
    os.mkdir(figure_folder)
except:
    pass

df_metadata = pd.read_csv('../thredds-data/metadata/AWS_stations_metadata.csv')


path_to_qc_files = '../PROMICE-AWS-data-issues/'
all_dirs = os.listdir(path_to_qc_files+'adjustments' )+os.listdir(path_to_qc_files+'flags')

for station in ['NUK_L']: #['KAN_Lv3','QAS_Lv3','QAS_Mv3','SCO_Lv3','SCO_Uv3']:
# for station in np.unique(np.array(all_dirs)):
    station = station.replace('.csv','')

    df_flags = load_flags_and_adjustments(path_to_qc_files, station)
    _, _, pAWS_tx, pAWS_raw = load_L1(path_to_l0, station)
    pAWS_raw.getL2()
    pAWS_tx.getL2()
    # pAWS_raw.getL3()
# %%
    ds = pAWS_raw.L2
    from pypromice.pipeline.resample import resample_dataset
    import matplotlib.dates as mdates
    L2_raw_h=resample_dataset(ds, '60min')
    L2_raw_d=resample_dataset(ds, '1D')
    L2_raw_m=resample_dataset(ds, 'MS')

    var='p_u'

    fig, ax = plt.subplots()
    ds[var].plot(marker='^',label='raw or tx', alpha=0.7)
    L2_raw_h[var].plot(drawstyle="steps-post", marker='o',label='hour', alpha=0.7)
    L2_raw_d[var].plot(drawstyle="steps-post", marker='o',label='day', alpha=0.7)
    L2_raw_m[var].plot(drawstyle="steps-post", marker='o',label='month', alpha=0.7)
    plt.legend()

    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.xaxis.set_minor_locator(mdates.AutoDateLocator())

    ax.grid(True, which="both", linestyle="--", alpha=0.4)
    # L1a_h=resample_dataset(pAWS_tx.L1A, '60min')
    plt.title(station)
