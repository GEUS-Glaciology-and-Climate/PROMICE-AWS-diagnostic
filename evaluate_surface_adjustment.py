# -*- coding: utf-8 -*-
"""
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pandas as pd
import numpy as np
import xarray as xr
import logging, toml, os, re, tempfile

logging.getLogger('matplotlib.font_manager').disabled = True
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

import sys, importlib
# purge cached package + submodules
# only useful in debugging mode
for name in list(sys.modules):
    if name == "pypromice" or name.startswith("pypromice."):
        del sys.modules[name]
importlib.invalidate_caches()

from pypromice.core.variables import surface_height
from pathlib import Path
# import matplotlib
# matplotlib.use('Agg')

import lib.process as lib
import lib.plot as lp
logging.getLogger('numba').setLevel(logging.WARNING)
path_to_l0 = 'C:/Users/bav/GitHub/PROMICE data/aws-l0/'
config_folder = '../aws-l0/metadata/station_configurations/'
df_metadata = pd.read_csv('C:/Users/bav/GitHub/PROMICE data/thredds-data/metadata/AWS_stations_metadata.csv')

path_l2 = 'data/L2_test/'

issues_adjustments = Path('../PROMICE-AWS-data-issues')/'adjustments'
# The pipeline applies the manual shifts of PROMICE-AWS-data-issues first, then
# the automated ones (only after the time of dynamic_adjust_after, if the
# station has such a row). The automated shifts that it applies are written, as
# <station>.csv in the format of the adjustment files, to path_suggestions: they
# are the ones to review and paste in PROMICE-AWS-data-issues/adjustments. The
# file ends with the dynamic_adjust_after row (just after the last time of the
# record) to paste with them. If the station already has such a row, replace it
path_suggestions = Path('data/surface_height_suggestions/')

# True: the processor is also run without the manual surface height shifts
#       ("add" on z_surf_1, z_surf_2 and z_ice_surf) and the dynamic_adjust_after
#       row of the station (filters and other adjustments are kept), to see what
#       the automated procedure alone would do. Its result is the dashed black
#       line in the plot and its shifts are written to path_suggestions/from_scratch.
#       These shifts replace the manual ones: do not add them on top of them.
compare_from_scratch = False

# plt.close('all')

for station in ['KAN_Lv3']:
# for station in df_metadata.station_id:

    print("\n ======== Processing L2 ========= \n")
    pAWS_tx, pAWS_raw = lib.run_L2(path_to_l0, path_l2, station)

    print("\n ======== Joining L2 ========= \n")
    l2_merged = lib.join_L2(path_l2, station)

    print("\n ======== Processing L3 surface heights ========= \n")
    l2 = lib.open_l2_clean(path_l2, station)

    # %%
    # % Perform Level 3 processing
    # the processor modifies the dataset it is given
    l2_scratch = l2.copy(deep=True) if compare_from_scratch else None

    # surface height as processed by the pipeline: manual shifts of the data
    # issues repository, then the automated ones, which are written to the
    # suggestions file
    path_suggestions.mkdir(parents=True, exist_ok=True)
    file_suggestions = path_suggestions / f'{station}.csv'
    l3 = surface_height.process_surface_height(l2,
                                issues_adjustments,
                                adjustments_out=file_suggestions,
                                ).to_dataframe()
    print(f'Automated adjustments written to {file_suggestions}')

    auto_shifts = lib.read_suggestions(file_suggestions)
    manual = lib.manual_shifts(issues_adjustments, station)
    lp.print_comparison(auto_shifts, manual)

    # what the automated procedure would do without the manual shifts
    l3_auto = None
    if compare_from_scratch:
        print("\n ======== Automated surface height adjustments alone ========= \n")
        path_scratch = path_suggestions / 'from_scratch'
        path_scratch.mkdir(parents=True, exist_ok=True)
        file_scratch = path_scratch / f'{station}.csv'
        with tempfile.TemporaryDirectory() as tmp_dir:
            lib.write_adjustments_without_manual_shifts(issues_adjustments, station, tmp_dir)
            l3_auto = surface_height.process_surface_height(
                l2_scratch, Path(tmp_dir), adjustments_out=file_scratch,
            ).to_dataframe()
        print(f'Automated adjustments alone written to {file_scratch}')
        lp.print_comparison(lib.read_suggestions(file_scratch), manual)

    print('\nPlotting')
    fig, ax = plt.subplots(4,1, sharex=True, figsize=(10,13),
                           gridspec_kw=dict(height_ratios=[3,3,1.5,2]))
    plt.subplots_adjust(right=0.8)
    var_list = [v for v in ['z_boom_u','z_boom_l','z_stake','z_pt'] if v in l3.columns]
    l3[var_list].plot(ax=ax[0],marker='.', ls='None', legend='__nolabel__', x_compat=True)
    var_list_cor = [(v.replace('_u','_cor_u')
                     .replace('_l','_cor_l')
                     .replace('_stake','_stake_cor')
                     .replace('_pt','_pt_cor')) for v in var_list]
    var_list_cor = [v for v in var_list_cor if v in l3.columns]
    l3[var_list_cor].plot(ax=ax[0],marker='.', x_compat=True)
    ax[0].set_title(station)
    ax[0].set_ylabel('Height (m)')
    ax[0].grid()
    ax[0].legend(loc='center left', bbox_to_anchor=(1, 0.5))

    var_list = [v for v in ['z_surf_1','z_surf_2','z_ice_surf', 'z_surf_1_adj','z_surf_2_adj',
                            'z_surf_combined',] if v in l3.columns]
    l3[var_list].plot(ax=ax[1],marker='.',alpha=0.6, x_compat=True)
    # colour of each series, used for its adjustments
    colors = {line.get_label(): line.get_color() for line in ax[1].get_lines()}
    # result of the automated processor alone
    if l3_auto is not None and 'z_surf_combined' in l3_auto.columns:
        ax[1].plot(l3_auto.index, l3_auto['z_surf_combined'], color='k', lw=1,
                   ls='--', label='z_surf_combined (automated only)')
    ax[1].legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax[1].set_ylabel('Height (m)')
    ax[1].grid()

    var_list = [v for v in ['snow_height'] if v in l3.columns]
    l3[var_list].plot(ax=ax[2],marker='.',alpha=0.6, x_compat=True)
    if l3_auto is not None and 'snow_height' in l3_auto.columns:
        ax[2].plot(l3_auto.index, l3_auto['snow_height'], color='k', lw=1,
                   ls='--', label='snow_height (automated only)')
    ax[2].legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax[2].set_ylabel('Height (m)')
    ax[2].grid()

    # dates and magnitudes of the manual and automated adjustments
    lp.plot_shifts(ax[1], ax[3], manual, colors, 'manual', l3.index[0])
    lp.plot_shifts(ax[1], ax[3], auto_shifts, colors, 'auto', l3.index[0])
    ax[3].axhline(0, color='k', lw=0.5)
    ax[3].set_ylabel('Adjustment (m)')
    ax[3].grid()
    handles = [Line2D([], [], color=c, lw=2, label=v) for v, c in colors.items()
               if v in ['z_surf_1', 'z_surf_2', 'z_ice_surf']]
    handles += [Line2D([], [], color='gray', ls='-', marker='o', label='manual'),
                Line2D([], [], color='gray', ls='--', marker='^', mfc='none',
                       label='automated')]
    ax[3].legend(handles=handles, loc='center left', bbox_to_anchor=(1, 0.5))
    # print("saving")
    # fig.savefig('figures/surface_height_assessment/'+station+'.png', dpi=300)
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
    plt.figure()
    l3['z_ice_surf'].plot()
    abl.plot(marker='o')

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
