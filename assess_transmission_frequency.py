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
import os
import xarray as xr
from tqdm import tqdm
import xarray as xr
from dask.diagnostics import ProgressBar
# import matplotlib
# matplotlib.use('Agg')

# Initialize
data_type = 'sites'
if data_type == 'sites':
    path_new = '../thredds-data/level_3_sites/csv/hour/'
else:
    path_new = '../thredds-data//level_2_stations/csv/hour/'

station_list=['CEN_day.csv', 'HUM_day.csv',
              'Roof_GEUS_day.csv',
              'NAU_day.csv','NSE_day.csv','SDL_day.csv',
              'SDM_day.csv','CP1_day.csv','ORO_day.csv',
              ]


fig, axs = plt.subplots(len(station_list), 1, figsize=(10, 10), sharex=True)
for i, file in enumerate(station_list):
    station = file.replace('_day.csv','')
    df_new = pd.read_csv(f'{path_new}/{station}_hour.csv')
    df_new['time'] = pd.to_datetime(df_new['time'], utc=True)
    df_new = df_new.set_index('time')[['t_u','rh_u','p_u']].resample('D').count()
    df_new=df_new.iloc[:-1,:]

    df_new.t_u.plot(ax=axs[i], marker='d', label='t_u')
    df_new.rh_u.plot(ax=axs[i], marker='o', label='rh_u')
    df_new.p_u.plot(ax=axs[i], marker='+', label='p_u')
    axs[i].set_xlim(pd.to_datetime(['2024-06-01','2025-04-03']))
    if i < len(station_list) - 1:
        axs[i].set_xticklabels([])
    axs[i].text(0.01, 0.05, station, transform=axs[i].transAxes,
                fontsize=10, fontweight='bold', bbox=dict(facecolor='white', edgecolor='black'))

fig.text(0.04, 0.5, 'Counts of daily transmissions', va='center', rotation='vertical')

handles, labels = axs[0].get_legend_handles_labels()
axs[0].legend(handles, labels, loc='lower center', bbox_to_anchor=(0.5, 1.05), ncol=3)
