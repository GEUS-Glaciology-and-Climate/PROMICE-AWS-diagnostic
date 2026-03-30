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
import os, logging, matplotlib
import lib.tocgen
# matplotlib.use('Agg')
import matplotlib.dates as mdates
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
import pypromice.resources
from pypromice.core.qc.value_clipping import clip_values
from pypromice.resources import load_variables
from pypromice.core.qc.persistence import persistence_qc
from pypromice.core.qc.rate_of_change_filter import rate_of_change_filter
from pypromice.core.qc.github_data_issues import adjustTime, adjustData, flagNAN
from lib.process import (remove_old_plots, load_flags_and_adjustments, load_L1,
                 clean_gps, smooth_pose, compute_cloud_cover,
                 solar_geometry, filter_shortwave, correct_shortwave, compute_albedo,
                 process_precip)
from lib.plot import (DEFAULT_VAR_LIST, plot_L0, plot_identical_SR50)

path_to_l0 = 'C:/Users/bav/GitHub/PROMICE data/aws-l0/'
filename = './plot_compilations/flags.md'
figure_folder='figures/flags'
os.makedirs(figure_folder, exist_ok=True)

df_metadata = pd.read_csv('../thredds-data/metadata/AWS_stations_metadata.csv')

f = open(filename, "w")
def Msg(txt):
    f = open(filename, "a"); print(txt); f.write(txt + "\n")

# plt.close('all')

path_to_qc_files = '../PROMICE-AWS-data-issues/'
all_dirs = os.listdir(path_to_qc_files+'adjustments' )+os.listdir(path_to_qc_files+'flags')
var_file = os.path.join(os.path.dirname(pypromice.resources.__file__), "variables.csv")
zoom_to_good = True

for station in ['ZAC_Uv3']:
    # for station in df_metadata.station_id:
    station = station.replace('.csv','')
    remove_old_plots(figure_folder, station)
    df_flags = load_flags_and_adjustments(path_to_qc_files, station)
    ds, ds_save, pAWS_tx, pAWS_raw = load_L1(path_to_l0, station)

    #%% Flagging, adjusting, filtering

    ds_post_presist = persistence_qc(ds.copy())
    ds_post_roc = rate_of_change_filter(ds_post_presist.copy())

    # The following steps are from L1toL2
    ds_post_roc  = adjustTime(ds_post_roc.copy(), adj_dir=path_to_qc_files+'adjustments')
    ds_post_flag = flagNAN(ds_post_roc.copy(),  flag_dir=path_to_qc_files+'flags')
    ds_post_adjust = adjustData(ds_post_flag.copy(),
                                adj_dir=path_to_qc_files+'adjustments')

    ds_post_precip = process_precip(ds_post_adjust.copy())

    vars_df = load_variables(var_file)
    ds_post_clip = clip_values(ds_post_precip.copy(), vars_df)

    # The following steps are from L2toL3
    ds_final, baseline_elevation = clean_gps(ds_post_clip.copy())
    ds_final = smooth_pose(ds_final.copy())
    ds_final = compute_cloud_cover(ds_final.copy())

    geo = solar_geometry(ds_final)

    ds_final, flags = filter_shortwave(ds_final, geo)
    ds_final, TOA_crit_nopass_cor = correct_shortwave(ds_final, geo)
    ds_final, OKalbedos = compute_albedo(ds_final, geo)

    from pypromice.core.variables import humidity
    ds_final["rh_u_wrt_ice_or_water"] = humidity.adjust(ds_final["rh_u"], ds_final["t_u"])
    if "t_l" in ds_final.data_vars:
        ds_final["rh_l_wrt_ice_or_water"] = humidity.adjust(ds_final["rh_l"], ds_final["t_l"])


    for var in ["t", "rh","p","wspd"]:
        if (var+'_u' in ds_final.data_vars) and (var+'_l' in ds_final.data_vars):
            ds_final[var+'_diff'] = ds_final[var+'_u'] - ds_final[var+'_l']
    if ('rh_u_wrt_ice_or_water' in ds_final.data_vars) and ('rh_l_wrt_ice_or_water' in ds_final.data_vars):
        ds_final['rh_wrt_ice_or_water_diff'] = ds_final['rh_u_wrt_ice_or_water'] - ds_final['rh_l_wrt_ice_or_water']

    # %% plotting
    df_L1 = ds.to_dataframe().copy()
    Msg('# '+station)
    var_list = [v for v in DEFAULT_VAR_LIST if v in ds.data_vars]
    var_list_list = [np.array(var_list[i:(i+6)]) for i in range(0,len(var_list),6)]

    var_list_list = [np.array([
                        # 't_u','t_l','t_i',
                        # 'rh_u','rh_l','rh_i',
                        # 'p_u','p_l','p_i',
                        # 'wspd_u','wspd_l','wspd_i',
                        # 'wdir_u','wdir_l','wdir_i',
                        # 'dsr','dsr_cor','usr','albedo',
                        # 'tilt_x','tilt_y',
                        # 't_i_1','t_i_2','t_i_8',
                        'z_boom_l', 'z_boom_u', #'z_stake',
                        'z_boom_cor_l', 'z_boom_cor_u', #'z_stake_cor',
                        't_rad',
                        ])
                        ] #])]

    for i, var_list in enumerate(var_list_list):
        if len(var_list) == 0: continue
        if len(var_list[~np.isin(var_list, df_L1.columns)]) >0:
            print(var_list[~np.isin(var_list, df_L1.columns)], 'not in L1 data')
        var_list = var_list[np.isin(var_list, ds_final.data_vars)]
        fig, ax_list = plt.subplots(len(var_list),1,sharex=True,  #sharey=True,
                                    figsize=(12,len(var_list)*2.1))
        fig.subplots_adjust(top=0.83)
        if len(var_list) == 1: fig.subplots_adjust(top=0.7)
        if len(var_list)==1: ax_list = [ax_list]

        for var, ax in zip(var_list, ax_list):

            if (var in ['z_boom_u','z_boom_l','z_stake']) and ('z_stake' in df_L1.columns):
                ax = plot_identical_SR50(df_L1, ax)

            if var in ['z_boom_cor_u','z_boom_cor_l','z_stake_cor']:
                ax.plot(ds_final.time,
                        ds_final[var.replace('_cor','')].values,
                        marker='.',color='gray', linestyle='None',
                        label='uncorrected for air temperature')

            # plotting L0 TX
            ax = plot_L0(pAWS_raw, ax, var, s='x', label='in L0 raw')

            # plotting L0 RAW
            ax= plot_L0(pAWS_tx, ax, var, s='+', label='in L0 tx')

            # flagged by persistance
            if var in ds.data_vars and var in ds_post_presist.data_vars:
                mask = np.isnan(ds_post_presist[var].values) & ~np.isnan(ds[var].values)
                ax.plot(ds.time[mask],
                        ds[var].values[mask],
                        marker='.',color='tab:pink', linestyle='None',
                        label='filtered with persistence')

            # flagged by ROC
            if var in ds_post_roc.data_vars and var in ds_post_presist.data_vars:
                mask = np.isnan(ds_post_roc[var].values) & ~np.isnan(ds_post_presist[var].values)
                ax.plot(ds_post_presist.time[mask], ds_post_presist[var].values[mask],
                        marker='.',color='tab:cyan', linestyle='None',
                        label='filtered with ROC')

            # flagged by ROC
            if var in ds_post_roc.data_vars and var in ds_post_flag.data_vars:
                mask = np.isnan(ds_post_flag[var].values) & ~np.isnan(ds_post_roc[var].values)
                ax.plot(ds_post_roc.time[mask], ds_post_roc[var].values[mask],
                        marker='.',color='tab:red', linestyle='None',
                        label='filtered with manual flag')

            if var == 'albedo':
                albedo_raw = ds['usr'] / ds['dsr']
                albedo_raw = albedo_raw.where(albedo_raw>0).where(albedo_raw<1)

                ax.plot(ds.time, albedo_raw.values,
                        marker='.',color='tab:pink', linestyle='None',
                        label='unfiltered, uncorrected')

            # flagged by manual filter
            if var in ds_post_flag.data_vars:
                ax.plot(ds_post_flag.time, ds_post_flag[var].values,
                        marker='.',color='tab:orange', linestyle='None',
                        label='removed or changed by adjustment')

            # flagged by OOL and dependency
            if var in ds_post_adjust.data_vars and var in ds_post_clip.data_vars:
                mask = np.isnan(ds_post_clip[var].values) & ~np.isnan(ds_post_adjust[var].values)
                ax.plot(ds_post_adjust.time[mask], ds_post_adjust[var].values[mask],
                        marker='o',color='tab:brown', linestyle='None',
                        label='filtered with dependency')

            # various custom filters
            if var in ds_post_clip.data_vars:
                ax.plot(ds_post_clip.time, ds_post_clip[var].values,
                        marker='.',color='tab:pink', linestyle='None',
                        label='removed by custom filter (gps_alt, tilt or rot)')
                if var == 'gps_alt':
                    ax.plot(ds_post_clip.time, baseline_elevation,
                            ls='--', c='k')

            if var[:-4] in ds_final.data_vars:
                if var in ['dsr_cor','usr_cor']:
                    if var == 'dsr_cor':
                        ax.plot(ds_post_clip.time,(1.2* geo["isr_toa"] + 150),
                                c='k', alpha=0.7)
                        ax_list[0].plot(np.nan,np.nan,
                                c='k',label='TOA irradiance + margin (W m-2)')
                    else:
                        ax.plot(ds_post_clip.time, 0.8*(1.2 * geo["isr_toa"] + 150),
                                c='k', alpha=0.7)
                    ax.plot(ds.time, ds[var[:-4]].values,
                            marker='.',color='tab:red', linestyle='None',
                            label='removed by flag')
                    ax.plot(ds_post_clip.time, ds_post_clip[var[:-4]].values,
                            marker='.',color='tab:pink', linestyle='None',
                            label='value before tilt correction')
                    if var == 'dsr_cor':
                        ax.plot(ds_post_clip.time,
                                ds_post_clip[var[:-4]].where(
                                    flags.TOA_crit_nopass_dsr | TOA_crit_nopass_cor).values,
                                marker='.',color='k', linestyle='None',
                                label='removed, dsr above TOA irradiance')
                    else:
                        ax.plot(ds_post_clip.time,
                                ds_post_clip[var[:-4]].where(
                                    flags.TOA_crit_nopass_usr | TOA_crit_nopass_cor).values,
                                marker='.',color='k', linestyle='None',
                                label='removed, dsr above TOA irradiance')
                        if flags.TOA_crit_nopass_usr.any():
                            ax.plot(ds_post_clip.time,
                                ds_post_clip[var[:-4]].where(flags.TOA_crit_nopass_usr).values,
                                marker='.',color='tab:orange', linestyle='None')
                            ax_list[0].plot(np.nan,np.nan,marker='.',ls='None',
                                    c='tab:orange',label='removed, usr above TOA irradiance')

                    ax.plot(ds_post_clip.time,
                            ds_post_clip[var[:-4]].where(flags.bad).values,
                            marker='.',color='tab:green', linestyle='None',
                            label='sun below horizon zenith angle or negative reading')

            # final data
            if var in ds_final.data_vars:
                ax.plot(ds_final.time,
                        ds_final[var].values,
                        marker='.',color='tab:blue', linestyle='None',
                        label='final')

        for var, ax in zip(var_list, ax_list):
            # ax.set_xlim(pd.to_datetime(['2020-05-01','2026-03-16']))
            if zoom_to_good:
                ax.set_ylim(ds_final[var].min(), ds_final[var].max())
            else:
                xmin, xmax = ax.get_xlim()
                xmin = mdates.num2date(xmin)
                xmin = pd.Timestamp(xmin).tz_localize(None)
                xmax = mdates.num2date(xmax)
                xmax = pd.Timestamp(xmax).tz_localize(None)
                try:
                    ymin = ds.sel(time=slice(xmin, xmax))[var].min()
                    ymax = ds.sel(time=slice(xmin, xmax))[var].max()
                    ax.set_ylim(ymin, ymax)
                except:
                    pass

            ax.set_ylabel(var)
            ax.grid(True, which='minor', linestyle='--', linewidth=0.5)
            ax.grid(True, which='major', linestyle='-', linewidth=1)

        title = station+'_%i/%i'%(i+1,len(var_list_list))
        ax_list[0].legend(loc='lower left', title = title, bbox_to_anchor=(0,1.1), ncol=3)
        fig.savefig('%s/%s_%i.png'%(figure_folder, station,i), dpi=120,bbox_inches='tight')
        Msg('![](../%s/%s_%i.png)'%(figure_folder, station,i))
    Msg(' ')
# tocgen.processFile(filename, filename[:-3]+"_toc.md")
