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
import numpy as np
from sklearn.linear_model import LinearRegression
import nead
from pypromice.process import AWS
import os
# import matplotlib
# matplotlib.use('Agg')
import tocgen
import geopandas as gpd

# def main(
data_type = 'sites'
if data_type == 'sites':
    path_new = 'C:/Users/bav/Downloads/level_3_sites/day/'
else:
    path_new = 'C:/Users/bav/Downloads/level_2_stations/day/'

filename = 'plot_compilations/GPS_'+data_type+'.md'

f = open(filename, "w")
def Msg(txt):
    f = open(filename, "a")
    print(txt)
    f.write(txt + "\n")
# plt.close('all')

fig = plt.figure(figsize=(10, 18))
gs = fig.add_gridspec(2, 1, height_ratios=[2, 1])  # Now it correctly has 2 rows

ax_list = [fig.add_subplot(gs[0]),  # Upper panel (3/4 height)
           fig.add_subplot(gs[1])]  # Lower panel (1/4 height)

plt.subplots_adjust(left=0.27, right=0.97, top=0.98, bottom=0.1, wspace=0.3, hspace=0.2)

count = 0
col = ['tab:orange','tab:purple', 'tab:red','tab:blue', 'tab:pink','tab:cyan',]
xtick_loc = np.array([1.5])

file_list_GCNet = ['CEN_day.csv', 'CP1_day.csv', 'DY2_day.csv', 'EGP_day.csv',
   'HUM_day.csv',  'JAR_day.csv', 'NAE_day.csv',
 'NAU_day.csv', 'NEM_day.csv',  'NSE_day.csv', 'SDL_day.csv',
 'SDM_day.csv', 'SWC_day.csv',  'TUN_day.csv',]
skip_station = [ 'UWN_day.csv', 'WEG_B_day.csv', 'WEG_L_day.csv',
                'SER_B_day.csv', 'RED_L_day.csv', 'ORO_day.csv',
                'NUK_P_day.csv', 'NUK_B_day.csv','FRE_day.csv',
 'ZAC_A_day.csv', 'ZAC_L_day.csv', 'ZAC_U_day.csv',
 'LYN_L_day.csv',
 'LYN_T_day.csv',
 ]
file_list_PROMICE = [f for f in os.listdir(path_new) if f not in file_list_GCNet and f not in skip_station]

for ax, file_list in zip(ax_list,[file_list_PROMICE,file_list_GCNet]):
    PROMICE_sites = [f.replace('_day.csv','') for f in file_list]
    count = 0
    for file in file_list:
    # for file in ['NSE_day.csv']:
        site = file.replace('_day.csv','')

        Msg('## '+site)
        if not os.path.isfile(path_new+file):
            Msg("cannot find",path_new+file)
            continue

        df = pd.read_csv(path_new+file)
        df.time = pd.to_datetime(df.time, utc=True)
        df = df.set_index('time')

        if 'dsr' in df.columns:
            df['sw_rad'] = df[['dsr_cor','usr_cor']].mean(axis=1)
        else:
            df['sw_rad'] = np.nan
        if 'dlr' in df.columns:
            df['lw_rad'] = df[['dlr','ulr']].mean(axis=1)
        else:
            df['lw_rad'] = np.nan
        df['t'] = df[[v for v in ['t_u','t_l'] if v in df.columns]].mean(axis=1)
        df['rh'] = df[[v for v in ['rh_u','rh_l'] if v in df.columns]].mean(axis=1)
        df['ws'] = df[[v for v in ['wspd_u','wspd_l'] if v in df.columns]].mean(axis=1)
        fields = ['t', 'p_u', 'rh', 'ws', 'sw_rad', 'lw_rad']
        percentages = [np.round(df[field].notnull().sum() / df['t'].shape[0] * 100, 1) for field in fields]
        print(site, *percentages)

        for i, var in enumerate(['sw_rad','lw_rad','t','rh','ws','p_u']):
            # print(site, var,df[var].first_valid_index(), df[var].last_valid_index())
            tmp = df[var].notnull() *(-count + (i-2)/9)
            tmp[tmp==0] = np.nan
            ax.plot(tmp.index, tmp.values, color = col[i], marker='s',markersize=2)
            count = count+1

    ax.set_yticks(np.arange(len(PROMICE_sites))*(-6) - 1.5,
               PROMICE_sites, fontsize=18)
    from matplotlib.ticker import AutoMinorLocator
    labels = ['shortwave irradiance', 'longwave irradiance', 'temperature',
              'humidity', 'wind', 'pressure']
    for i, label in enumerate(labels):
        ax.plot(np.nan, np.nan, color=col[i], label=label, linewidth=4.5)
    ax.xaxis.set_minor_locator(AutoMinorLocator(5))
    if len(file_list) >14:
        ax.legend(loc='lower center', fontsize=14, bbox_to_anchor=(0.5,1))
        ax.set_xlim(pd.to_datetime('2005'),pd.to_datetime('2025'))
        ax.set_xticks([pd.to_datetime(str(y)) for y in range(2007,2026,5)],
                   [(str(y)) for y in range(2007,2026,5)],
                   fontsize=18)
    else:
        ax.set_xticks([pd.to_datetime(str(y)) for y in range(1990,2026,5)],
                   [(str(y)) for y in range(1990,2026,5)],
                   fontsize=18)
        ax.set_xlim(pd.to_datetime('1990'),pd.to_datetime('2025'))

    ax.grid(axis='x')
    ax.grid(which='minor', color='lightgray', linestyle=':')
    ax.set_ylim(-count+1/4, 1)
    ax.set_xlabel('Year', fontsize=18)
    # ax.set_tick_params(labelbottom=True, which="both", labeltop=True, bottom=True, top=True)
    for y in np.arange(len(PROMICE_sites))*(-4) - 3.65:
      ax.axhline(y=y, color='gray', alpha=0.5)
fig.savefig("figures/data_availability.png",
    bbox_inches="tight", dpi=300)
