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
import matplotlib
data_type = 'sites'
if data_type == 'sites':
    path_new = '../thredds-data/level_3_sites/csv/day/'
else:
    path_new = '../thredds-data//level_2_stations/csv/day/'

# %% Accumulation stations only 
import numpy as np
from scipy.stats import linregress

import pandas as pd

# df_sb = pd.read_excel("C:/Users/bav/OneDrive - Geological survey of Denmark and Greenland/Data/Snowboards/GC-NET_Snowboard_data_bav.xlsx", sheet_name=0, engine="openpyxl")
df_sb['date of placement [yyy-mm-dd]'] = pd.to_datetime(df_sb['date of placement [yyy-mm-dd]'], utc=True).dt.floor('D')
df_sb['date of measurement [yyy-mm-dd]'] = pd.to_datetime(df_sb['date of measurement [yyy-mm-dd]'], utc=True).dt.floor('D')
df_sb['SB depth [m]'] = pd.to_numeric(df_sb['SB depth [m]'], errors='coerce')
# for station in ['DY2', 'NAU', 'CEN', 'TUN', 'NAE', 'NSE', 'SDL', 'SDM']:
factors = {
    'DY2': 1.1,
    'CP1': 1.6,
    'SDM': 1.3,
    'NSE': 1.2,
    'SDL':1.2,
    
    
}

def get_series_and_trend(df, col):
    y = df[col].dropna()
    x = (y.index - y.index[0]).total_seconds() / (365.25 * 24 * 3600)
    slope, intercept, *_ = linregress(x, y.values)
    return y, x, slope, intercept


def get_period_change(df, x1, x2, col):
    y1 = df.loc[x1, col] if x1 in df.index else np.nan
    y2 = df.loc[x2, col] if x2 in df.index else np.nan
    dh = y2 - y1 if pd.notna(y1) and pd.notna(y2) else np.nan
    return y1, y2, dh


for station in ['SDL']:
    df_sb_site = df_sb.loc[df_sb.Site == station].copy()

    fig = plt.figure()
    ax = plt.gca()

    if station in ['KAN_B', 'NUK_K']:
        continue
    if not os.path.isfile(path_new + '/' + station + '_day.csv'):
        continue

    print('\n## ' + station)

    df_new = pd.read_csv(path_new + '/' + station + '_day.csv')
    df_new.time = pd.to_datetime(df_new.time, utc=True)
    df_new = df_new.set_index('time')[['z_surf_combined']].resample('D').mean().interpolate()
    df_new = df_new.loc['2022':,]

    s = df_new['z_surf_combined'].copy()
    grad = s.diff()
    grad_mod = grad * factors.get(station, 1.0)
    df_new['z_surf_combined_mod'] = s.iloc[0] + grad_mod.cumsum()

    y_unc, x_unc, slope_unc, intercept_unc = get_series_and_trend(df_new, 'z_surf_combined')
    y_cor, x_cor, slope_cor, intercept_cor = get_series_and_trend(df_new, 'z_surf_combined_mod')

    print(f"{station}: uncorrected trend = {slope_unc:.3f} m/yr")
    print(f"{station}: corrected   trend = {slope_cor:.3f} m/yr")

    ax.plot(
        y_unc.index, y_unc.values,
        marker='.', markeredgecolor='None', linestyle='None',
        color='lightgray', alpha=0.7,
        label=f"uncorrected ({slope_unc:.2f} m/yr)"
    )
    ax.plot(
        y_unc.index,
        intercept_unc + slope_unc * x_unc,
        linestyle='-',
        color='gray',
        alpha=0.8
    )

    ax.plot(
        y_cor.index, y_cor.values,
        marker='.', markeredgecolor='None', linestyle='None',
        alpha=0.7,
        label=f"corrected ({slope_cor:.2f} m/yr)"
    )
    ax.plot(
        y_cor.index,
        intercept_cor + slope_cor * x_cor,
        linestyle='-',
        alpha=0.8
    )

    for x1, x2, accum in df_sb_site[
        ['date of placement [yyy-mm-dd]',
         'date of measurement [yyy-mm-dd]',
         'SB depth [m]']
    ].itertuples(index=False, name=None):

        y1_unc, y2_unc, dh_unc = get_period_change(df_new, x1, x2, 'z_surf_combined')
        y1_cor, y2_cor, dh_cor = get_period_change(df_new, x1, x2, 'z_surf_combined_mod')

        print(
            f"{x1.date()} -> {x2.date()} | "
            f"SB = {accum:.3f} m | "
            f"uncorrected = {dh_unc:.3f} m | "
            f"corrected = {dh_cor:.3f} m"
        )

        ax.plot(
            [x1, x2],
            [y1_unc, y1_unc + accum if pd.notna(y2_unc) and pd.notna(accum) else np.nan],
            marker='o',
            markersize=10,
            color='gray'
        )
        ax.plot(
            [x1, x2],
            [y1_cor, y1_cor + accum if pd.notna(y2_cor) and pd.notna(accum) else np.nan],
            marker='o',
            markersize=10
        )

    ax.legend(loc='upper left', markerscale=2, fontsize=12)
    ax.set_title(station)
    for h in ax.get_legend().legendHandles:
        h.set_alpha(1)

    ax.grid(True)
    ax.tick_params(axis='x', rotation=45)
    ax.tick_params(axis='both', labelsize=12)
    ax.set_ylabel('Surface height relative to installation (m)', fontsize=14)
# fig.savefig('figures/surface_height/overview.png', dpi=300, bbox_inches='tight')