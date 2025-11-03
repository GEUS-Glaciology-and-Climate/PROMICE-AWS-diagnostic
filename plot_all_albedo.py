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
for file in ['KAN_L_hour.csv']:
    print(file)
    
    station = file.replace('_hour.csv', '')
    df_new = pd.read_csv(f'{path_new}/{station}_hour.csv')
    df_new['time'] = pd.to_datetime(df_new['time'], utc=True)
    df_new = df_new.set_index('time')
    
    df_new = df_new.loc['2012']

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
from dask.diagnostics import ProgressBar
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

plt.close('all')
import pyproj
from pathlib import Path

def convert_to_epsg3413(lat, lon):
    transformer = pyproj.Transformer.from_crs(4326, 3413, always_xy=True)
    return transformer.transform(lon, lat)

# Loop over each station
# for file in os.listdir(path_new):
for file in ['KAN_L_hour.csv']:
    print(file)
    station = file.replace('_hour.csv','')
    df_new = pd.read_csv(f'{path_new}/{station}_hour.csv')
    df_new['time'] = pd.to_datetime(df_new['time'], utc=True)
    df_new = df_new.set_index('time')

    folder_path = 'C:/Users/bav/OneDrive - GEUS/Data/SICE/SICEv3.0_Greenland_500m/'
    files = sorted(Path(folder_path).glob("SICEv3.0_Greenland_500m_*.nc"))


    datasets = []
    for f in tqdm(files, desc="Processing files"):
        try:
            date = f.stem.split('_')[-1]
            lat, lon = df_new.loc[date, ['lat', 'lon']]
            x, y = convert_to_epsg3413(lat, lon)

            ds = xr.open_dataset(f, lock=False)
            ds_sel = ds.sel(x=x, y=y, method='nearest')[['BBA_combination', 'albedo_bb_planar_sw']]
            datasets.append(ds_sel)
        except Exception as e:
            print(f"Failed to process {f.name}: {e}")


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
