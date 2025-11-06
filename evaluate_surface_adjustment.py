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
import xarray as xr
import logging, toml, os

import sys, importlib
# purge cached package + submodules
# only useful in debugging mode
for name in list(sys.modules):
    if name == "pypromice" or name.startswith("pypromice."):
        del sys.modules[name]
importlib.invalidate_caches()

from pypromice.pipeline.L2toL3 import process_surface_height
from pathlib import Path
# import matplotlib
# matplotlib.use('Agg')

logging.getLogger('matplotlib.font_manager').disabled = True
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
import logging, lib
logging.getLogger('numba').setLevel(logging.WARNING)
path_to_l0 = 'C:/Users/bav/GitHub/PROMICE data/aws-l0/'
config_folder = '../aws-l0/metadata/station_configurations/'
df_metadata = pd.read_csv('C:/Users/bav/GitHub/PROMICE data/thredds-data/metadata/AWS_stations_metadata.csv')

path_l2 = 'L2_test/'

# plt.close('all')

for station in ['UPE_L']:
# for station in df_metadata.station_id:
#
    print("\n ======== Processing L2 ========= \n")
    pAWS_tx, pAWS_raw = lib.run_L2(path_to_l0, path_l2, station)

    print("\n ======== Joining L2 ========= \n")
    l2_merged = lib.join_L2(path_l2, station)

    print("\n ======== Processing L3 surface heights ========= \n")
    l2 = lib.open_l2_clean(path_l2, station)
    station_config = lib.load_station_config(config_folder, l2.attrs['station_id'])


    # %% Perform Level 3 processing
    l3 = process_surface_height(l2,
                                Path('../PROMICE-AWS-data-issues')/'adjustments',
                                station_config).to_dataframe()

    # %%

    fig, ax = plt.subplots(3,1, sharex=True, figsize=(10,10))
    plt.subplots_adjust(right=0.8)
    var_list = [v for v in ['z_boom_u','z_boom_l','z_stake','z_pt'] if v in l3.columns]
    l3[var_list].plot(ax=ax[0],marker='.',color='lightgray', ls='None', legend='__nolabel__')
    var_list_cor = [(v.replace('_u','_cor_u')
                     .replace('_l','_cor_l')
                     .replace('_stake','_stake_cor')
                     .replace('_pt','_pt_cor')) for v in var_list]
    var_list_cor = [v for v in var_list_cor if v in l3.columns]
    l3[var_list_cor].plot(ax=ax[0],marker='.')
    ax[0].set_title(station)
    ax[0].set_ylabel('Height (m)')
    ax[0].grid()
    ax[0].legend(loc='center left', bbox_to_anchor=(1, 0.5))

    var_list = [v for v in ['z_surf_1','z_surf_2','z_ice_surf', 'z_surf_1_adj','z_surf_2_adj',
                            'z_surf_combined',] if v in l3.columns]
    l3[var_list].plot(ax=ax[1],marker='.',alpha=0.6)
    ax[1].legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax[1].set_ylabel('Height (m)')
    ax[1].grid()

    var_list = [v for v in ['snow_height'] if v in l3.columns]
    l3[var_list].plot(ax=ax[2],marker='.',alpha=0.6)
    ax[2].set_ylabel('Height (m)')
    ax[2].grid()
    fig.savefig('figures/surface_height_assessment/'+station+'.png', dpi=300)
# %%
calc_yearly_abaltion = False
if calc_yearly_abaltion:
    time = pd.DatetimeIndex(l3.index.values)

    # all September 1st from first to last timestamp
    sel = (l3.index.month == 9) & (l3.index.day == 19) & (l3.index.hour == 00)
    abl = l3.loc[sel, 'z_ice_surf']
    abl = pd.concat([
        pd.Series([0], index=[abl.index.min() - pd.Timedelta(365, "D")]),
        abl
    ])
    # plt.figure()
    # l3['z_ice_surf'].plot()
    # abl.plot(marker='o')

    print("Yearly ice ablation:")
    for t, v in abl.diff().dropna().items():
        print(f"{t.year}: {v:.2f} m")

# %%
plot_thermistor_depth = False
if plot_thermistor_depth:
    df_new=l3.copy()

    fig, ax_list = plt.subplots(3,1,sharex=True, figsize=(10,15))
    plt.subplots_adjust(right=0.75,left=0.08,hspace=0.02)

    var_list = [v for v in ['z_boom_u','z_boom_l','z_stake','z_pt_cor'] \
                      if v in df_new.columns]
    for var in var_list:
        if var in df_new.columns:
            if not df_new[var].isnull().all():
                ax_list[0].plot(df_new.index, df_new[var].values,
                        marker='.',markeredgecolor='None', linestyle='None',
                        label=var)

    var_list = [v for v in ['z_surf_combined','z_ice_surf'] \
                      if v in df_new.columns]
    for var in var_list:
        if var in df_new.columns:
            if not df_new[var].isnull().all():
                ax_list[1].plot(df_new.index, df_new[var].values,
                        marker='.',markeredgecolor='None', linestyle='None',
                        label=var)
            else:
                print(var,'all nan')
    depth_var = ['d_t_i_'+str(i) for i in range(1,12) \
                      if 'd_t_i_'+str(i) in df_new.columns]
    for var in depth_var:
        if var in df_new.columns:
            if not df_new[var].isnull().all():
                ax_list[1].plot(df_new.index, -df_new[var].values + df_new.z_surf_combined,

                        label=var)


    var_list = ['t_i_'+str(i) for i in range(1,12) \
                      if 't_i_'+str(i) in df_new.columns]
    for var in var_list:
        if var in df_new.columns:
            if not df_new[var].isnull().all():
                ax_list[2].plot(df_new.index, df_new[var].values,
                        marker='.',markeredgecolor='None', linestyle='None',
                        label=var)
    if 't_i_10m' in df_new.columns:
        ax_list[2].plot(df_new.index, df_new['t_i_10m'].values,
                marker='o',color='k',markeredgecolor='None', linestyle='None',
                label='t_i_10m')

    for i in range(3):
        ax_list[i].set_ylabel('Height (m)')
        ax_list[i].grid()
        ax_list[i].legend(loc='center left', bbox_to_anchor=(1, 0.5))
        if i > 1:
            ax_list[i].legend(loc='center left', bbox_to_anchor=(1, 0.5),ncols=2)

    ax_list[2].set_ylabel('Depth (m)')
    ax_list[2].set_ylabel('Temperature (°C)')
    ax_list[0].set_title(station)

    # xlim1 = df_new.index[0]
    # xlim1 = '2022-03-01'
    # xlim2 = df_new.index[-1]
    # xlim2 = '2025-09-20'
    # ax_list[0].set_xlim(pd.to_datetime([xlim1,xlim2]))
    # if len(depth_var)>0:
    #     ax_list[1].set_ylim(
    #                        (df_new['z_surf_combined'].min() - df_new.loc[slice(xlim1, xlim2),depth_var].max().max())-0.5,
    #                            df_new.loc[slice(xlim1, xlim2), 'z_surf_combined'].max()+0.5
    #                            )
