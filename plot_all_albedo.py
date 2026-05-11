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
import os
import xarray as xr
from tqdm import tqdm
import xarray as xr
from dask.diagnostics import ProgressBar
# import matplotlib
# matplotlib.use('Agg')
import pandas as pd
import xarray as xr
from pyproj import Transformer
from pathlib import Path
# Initialize
data_type = 'sites'
if data_type == 'sites':
    path_new = '../thredds-data/level_3_sites/csv/hour/'
else:
    path_new = '../thredds-data//level_2_stations/csv/hour/'

filename = 'plot_compilations/albedo_' + data_type + '.md'


f = open(filename, "w")

def Msg(txt):
    with open(filename, "a") as f:
        print(txt)
        f.write(txt + "\n")

plt.close('all')
from pathlib import Path

# Loop over each station
# for file in os.listdir(path_new):
for file in ['KAN_U_hour.csv']:
    print(file)

    station = file.replace('_hour.csv', '')
    df_new = pd.read_csv(f'{path_new}/{station}_hour.csv')
    df_new['time'] = pd.to_datetime(df_new['time'], utc=True)
    df_new = df_new.set_index('time')

    df_new = df_new.loc['2024':]

    # Create a 4-panel figure
    fig, axs = plt.subplots(4, 1, figsize=(10, 12), sharex=True)

    # Panel 1: tilt_x, tilt_y
    axs[0].plot(df_new.index, df_new['tilt_x'], '.', label='tilt_x')
    axs[0].plot(df_new.index, df_new['tilt_y'], '.', label='tilt_y')
    axs[0].legend(title=station, loc='lower left')
    axs[0].grid()
    axs[0].set_ylabel('Tilt')

    # Panel 2: dsr, dsr_cor
    axs[1].plot(df_new.index, df_new['dsr'], '.', label='dsr')
    axs[1].plot(df_new.index, df_new['dsr_cor'], '.', label='dsr_cor')
    axs[1].legend(title=station, loc='lower left')
    axs[1].grid()
    axs[1].set_ylabel('DSR')

    # Panel 3: usr, usr_cor
    axs[2].plot(df_new.index, df_new['usr'], '.', label='usr')
    axs[2].plot(df_new.index, df_new['usr_cor'], '.', label='usr_cor')
    axs[2].legend(title=station, loc='lower left')
    axs[2].grid()
    axs[2].set_ylabel('USR')

    # Panel 4: albedo
    axs[3].plot(df_new.index, df_new['albedo'], '.', label='albedo')
    axs[3].legend(title=station, loc='lower left')
    axs[3].grid()
    axs[3].set_ylabel('Albedo')
    fig.savefig(f'figures/albedo/{station}.png', dpi=300)

# %% Comparison with SICE

import matplotlib.pyplot as plt
import pandas as pd
import os
import xarray as xr
from tqdm import tqdm
import xarray as xr
import numpy as np
# import matplotlib
# matplotlib.use('Agg')

# Initialize
data_type = 'sites'
if data_type == 'sites':
    path_new = '../thredds-data/level_3_sites/csv/hour/'
else:
    path_new = '../thredds-data//level_2_stations/csv/hour/'

filename = 'plot_compilations/albedo_' + data_type + '.md'


f = open(filename, "w")

def Msg(txt):
    with open(filename, "a") as f:
        print(txt)
        f.write(txt + "\n")


def load_sice(lat0, lon0):
    base = "https://thredds.geus.dk/thredds/dodsC/SICE_500m/Greenland"
    dates = pd.date_range("2017-04-01", pd.Timestamp.today().normalize(), freq="D")
    x0, y0 = Transformer.from_crs(4326, 3413, always_xy=True).transform(lon0, lat0)

    def get_albedo(date):
        try:
            url = f"{base}/SICEv3.0_Greenland_500m_{date:%Y-%m-%d}.nc"
            with xr.open_dataset(url) as d:
                a = d["albedo"].sel(x=x0, y=y0, method="nearest").load()
            return float(a), float(a.x), float(a.y)
        except Exception:
            return np.nan, x0, y0

    return pd.DataFrame(
        [(d, *get_albedo(d)) for d in tqdm(dates, desc="Loading SICE")],
        columns=["time", "albedo", "x", "y"],
    ).set_index("time")

# Loop over each station
# for file in os.listdir(path_new):
for file in ['TAS_A_hour.csv']:
    print(file)
    station = file.replace('_hour.csv','')
    df_new = pd.read_csv(f'{path_new}/{station}_hour.csv')
    df_new['time'] = pd.to_datetime(df_new['time'], utc=True)
    df_new = df_new.set_index('time')

    df_sice = load_sice(df_new.lat.mean(), df_new.lon.mean())





    with ProgressBar():
        ds_sice = xr.concat(datasets, dim='time').load()


    fig, axs = plt.subplots(2,1,figsize=(10, 10))

    for ax in axs:
        ax.plot(df_new.index, df_new['albedo'], '.', label='AWS')
        ds_sice.BBA_combination.plot(ax=ax, marker='d', ls='None', label='SICE combination', alpha=0.7)
        ds_sice.albedo_bb_planar_sw.plot(ax=ax, marker='o', ls='None', label='SICE ART retrieval', alpha=0.7)
        ax.legend(title = station, loc='lower left')
        ax.grid()
    ax.set_xlim(pd.to_datetime(['2017-01-01','2025-06-01']))

    fig.savefig(f'figures/albedo/{station}.png', dpi=300)
