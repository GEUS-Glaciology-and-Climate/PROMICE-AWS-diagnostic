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
import os
import numpy as np
data_type = 'sites'
if data_type == 'sites':
    path_new = '../thredds-data/level_3_sites/csv/day/'
else:
    path_new = 'C:/Users/bav/Downloads/level_2_stations/day/'

df_meta = pd.read_csv('../thredds-data/metadata/AWS_' + data_type + '_metadata.csv')
df_meta = df_meta.set_index(data_type[:-1] + '_id')

station_list = [v for v in df_meta.index if v not in [
    'CP1','CEN','DY2','HUM','NAE','NAU','NEM','NSE', 'SDM','SDL','TUN','EGP',
    'NUK_K','LYN_L','LYN_T','ZAC_A','ZAC_L','ZAC_U','MIT','FRE',
    'KAN_B','WEG_B','SER_B','NUK_P','NUK_B','RED_L',
    'ORO','UWN']]

results = []

for station in station_list:
    file_path = os.path.join(path_new, f"{station}_day.csv")
    if not os.path.isfile(file_path):
        continue

    df = pd.read_csv(file_path)
    if not {'z_surf_combined', 'snow_height'}.issubset(df.columns):
        continue

    df['time'] = pd.to_datetime(df['time'], utc=True)
    df = df.set_index('time')
    df = df[['z_surf_combined', 'snow_height']].dropna()

    # Define max_snow_height as max from Sept Y-1 to June Y
    df['year'] = df.index.year
    df['month'] = df.index.month
    df['snow_year'] = df['year']
    df.loc[df['month'] >= 9, 'snow_year'] += 1
    snow_groups = df[(df['month'] >= 9) | (df['month'] <= 6)].groupby('snow_year')['snow_height']
    max_snow_height = snow_groups.max()

    yearly = df.resample('YE')
    min_surface = yearly.min()['z_surf_combined']
    ablation = min_surface.shift(1) - min_surface

    if not max_snow_height.dropna().empty and not ablation.dropna().empty:
        results.append({
            'station': station,
            'median_max_snow_height': max_snow_height.median(),
            'median_annual_ablation': ablation.median() * 917 / 1000,
            'median_SWE_max': max_snow_height.median() * 450 / 1000
        })

df_result = pd.DataFrame(results)

df_result.median_annual_ablation = np.maximum(0, df_result.median_annual_ablation)
df_result['SWE / ablation [%]'] = df_result.median_SWE_max / (df_result.median_SWE_max+df_result.median_annual_ablation) *100


# %%
import pandas as pd
import os
import matplotlib.pyplot as plt


for station in station_list:
    file_path = os.path.join(path_new, f"{station}_day.csv")
    df = pd.read_csv(file_path)
    if not {'z_surf_combined', 'snow_height', 'time'}.issubset(df.columns):
        continue

    df['time'] = pd.to_datetime(df['time'], utc=True)
    df = df.set_index('time')
    df = df[['z_surf_combined', 'snow_height']].dropna()

    df['year'] = df.index.year
    df['month'] = df.index.month
    df['snow_year'] = df['year']
    df.loc[df['month'] >= 9, 'snow_year'] += 1

    snow_groups = df[(df['month'] >= 9) | (df['month'] <= 6)].groupby('snow_year')['snow_height']
    max_snow_height = snow_groups.max()

    yearly = df.resample('YE')
    min_surface = yearly.min()['z_surf_combined']
    ablation = min_surface.shift(1) - min_surface

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    ax1.plot(df.index, df['snow_height'], label='snow_height', alpha=0.5)
    for y, v in max_snow_height.items():
        ax1.hlines(v, pd.Timestamp(f'{y-1}-09-01'), pd.Timestamp(f'{y}-06-30'),
                   colors='blue', linewidth=2, label='Max snow height' if y == max_snow_height.index[0] else "")
    ax1.set_ylabel('Snow height (m)')
    ax1.legend(loc='upper left')
    ax1.grid(True)
    ax1.set_title(f'{station} - Snow Height and Ablation')

    ax2.plot(df.index, df['z_surf_combined'], label='z_surf_combined', alpha=0.5)
    for y, v in ablation.items():
        y  = y.year-1
        if pd.Timestamp(f'{y}-09-01T00:00:00+00') in df.index:
            base = df.loc[pd.Timestamp(f'{y}-09-01T00:00:00+00'), 'z_surf_combined']
            ax2.annotate('', xy=(pd.Timestamp(f'{y}-09-01'), base - v),
                         xytext=(pd.Timestamp(f'{y}-09-01'), base),
                         arrowprops=dict(arrowstyle='-|>', color='black', linewidth=1.5))
    ax2.set_ylabel('Surface height / Ablation (m)')
    ax2.set_xlabel('Year')
    ax2.legend(loc='upper left')
    ax2.grid(True)

    fig.tight_layout()

# %% SWE vs ablation
import matplotlib.pyplot as plt
import numpy as np

df_plot = df_result.copy()
df_plot['SWE / ablation [%]'] = df_plot['SWE / ablation [%]'].replace([np.inf, -np.inf], 100)
inf_mask = df_result['SWE / ablation [%]'] >= 100

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(df_plot['station'], df_plot['SWE / ablation [%]'], color='skyblue')

# Annotate bars with "no ice ablation" where original value was inf
for i, is_inf in enumerate(inf_mask):
    if is_inf:
        ax.text(i, 50, 'no ice ablation', ha='center', va='bottom', fontsize=8, rotation=90)

ax.set_ylabel('Part of snow in total annual melt [%]')
ax.set_ylim(0, 100)
ax.set_xticks(range(len(df_plot['station'])))
ax.set_xticklabels(df_plot['station'], rotation=90)

fig.tight_layout()
fig.savefig('figures/surface_height/SWE_vs_ablation.png', dpi=150)

(df_result['SWE / ablation [%]'] > 50).sum()

# %%
import matplotlib.pyplot as plt

import pandas as pd
import os
import numpy as np
data_type = 'sites'
if data_type == 'sites':
    path_new = '../thredds-data/level_3_sites/csv/day/'
else:
    path_new = 'C:/Users/bav/Downloads/level_2_stations/day/'

df_meta = pd.read_csv('../thredds-data/metadata/AWS_' + data_type + '_metadata.csv')
df_meta = df_meta.set_index(data_type[:-1] + '_id')

station_list = [v for v in df_meta.index if v not in [
    'CP1','CEN','DY2','HUM','NAE','NAU','NEM','NSE', 'SDM','SDL','TUN','EGP',
    'NUK_K','LYN_L','LYN_T','ZAC_A','ZAC_L','ZAC_U','MIT','FRE',
    'KAN_B','WEG_B','SER_B','NUK_P','NUK_B','RED_L',
    'ORO','UWN']]

results = []

fig,axs=plt.subplots(4,4, sharex=True)
axs=axs.flatten()
for station,ax in zip(station_list,axs):
    file_path = os.path.join(path_new, f"{station}_day.csv")
    if not os.path.isfile(file_path):
        continue

    df = pd.read_csv(file_path)
    if not {'z_surf_combined', 'snow_height'}.issubset(df.columns):
        continue

    df['time'] = pd.to_datetime(df['time'], utc=True)
    df = df.set_index('time')
    df = df[['z_surf_combined', 'snow_height']].dropna()
    print(station)
    diff = -df.z_surf_combined.diff().clip(-1e12,0)*1000
    diff.hist(ax=ax)
    ax.set_title(station)
    # ax.set_xscale('log')
    ax.set_yscale('log')
