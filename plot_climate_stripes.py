# -*- coding: utf-8 -*-
"""
@author: bav@geus.dk

Plots the annual air temperature of a list of PROMICE and/or GC-Net
stations as "climate stripes": one horizontal bar per year, colored from
blue (colder than the station's long-term mean) to red (warmer), in the
style of showyourstripes.info. All stations share the same color scale
and colorbar (temperature anomaly relative to each station's own mean).

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""
import os
import copy
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import xarray as xr

path_month = '../thredds-data/level_3_sites/netcdf/month'

# Stations to plot (both PROMICE and GC-Net stations are unified in the
# same netcdf/month files, e.g. 'KAN_M', 'KAN_U' are PROMICE and 'SUM',
# 'DY2', 'EGP' are GC-Net)
station_list = [ 'DY2',  'CP1', 'TUN','NAU']

# minimum number of monthly values required within a year to keep its mean
min_months_per_year = 8


def load_annual_air_temp(station):
    ds = xr.open_dataset(path_month + '/' + station + '_month.nc')
    temp = ds['t_u'].to_series()
    ds.close()

    # number of real (non-gapfilled) monthly values available per year
    annual_count = temp.resample('YS').count()

    # gapfill missing months with that calendar month's median before averaging
    climatology = temp.groupby(temp.index.month).median()
    fill_values = pd.Series(temp.index.month, index=temp.index).map(climatology)
    temp_filled = temp.fillna(fill_values)

    annual_mean = temp_filled.resample('YS').mean()
    annual_mean[annual_count < min_months_per_year] = np.nan
    return annual_mean


os.makedirs('figures/climate_stripes', exist_ok=True)

# first pass: load all stations and compute each one's anomaly relative
# to its own long-term mean, so different absolute climates are comparable
annual_temp_dict = {}
anomaly_dict = {}
for station in station_list:
    print(station)
    annual_temp = load_annual_air_temp(station)
    annual_temp_dict[station] = annual_temp
    anomaly_dict[station] = annual_temp.values - np.nanmean(annual_temp.values)

# shared color scale across all stations
all_anomalies = np.concatenate(list(anomaly_dict.values()))
vmax = 2.6 * np.nanstd(all_anomalies)
vmin = -vmax
norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)

cmap = copy.copy(plt.get_cmap('RdBu_r'))
cmap.set_bad(color='lightgray')

fig, ax_list = plt.subplots(len(station_list), 1, sharex=True,
                             figsize=(8, 1.2 * len(station_list)))
fig.subplots_adjust(hspace=0.6, left=0.15, top=0.92, bottom=0.08)
if len(station_list) == 1:
    ax_list = [ax_list]

for station, ax in zip(station_list, ax_list):
    annual_temp = annual_temp_dict[station]
    if annual_temp.dropna().empty:
        print(station, 'has no usable air temperature data')
        continue

    years = annual_temp.index.year.values
    anomaly = anomaly_dict[station]

    full_years = np.arange(years.min(), years.max() + 1)
    full_anomaly = np.full(full_years.shape, np.nan)
    full_anomaly[np.isin(full_years, years)] = anomaly
    full_values = np.full(full_years.shape, np.nan)
    full_values[np.isin(full_years, years)] = annual_temp.values

    ax.pcolormesh(np.append(full_years, full_years[-1] + 1), [0, 1],
                  np.ma.masked_invalid(full_anomaly)[np.newaxis, :],
                  cmap=cmap, norm=norm, shading='flat')
    ax.set_yticks([])
    ax.set_ylabel(station, rotation=0, ha='right', va='center')
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax2 = ax.twinx()
    ax2.plot(full_years + 0.5, full_values, color='k', lw=1.2,
              marker='o', markersize=3)
    ax2.set_ylabel('°C', fontsize=8)
    ax2.tick_params(labelsize=8)

ax_list[-1].set_xlabel('Year')
plt.suptitle('Air temperature climate stripes')

sm = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([])
fig.colorbar(sm, ax=ax_list, label='Temperature anomaly (°C)',
             fraction=0.03, pad=0.02)

fig.savefig('figures/climate_stripes/climate_stripes.png', dpi=300, bbox_inches='tight')
