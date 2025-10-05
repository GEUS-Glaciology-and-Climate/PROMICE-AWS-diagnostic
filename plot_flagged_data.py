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
# from sklearn.linear_model import LinearRegression
import os, logging, glob
import matplotlib
# matplotlib.use('Agg')

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
import os, pypromice.resources
from pypromice.core.qc.value_clipping import clip_values
from pypromice.resources import load_variables
from pypromice.core.qc.persistence import persistence_qc
from pypromice.core.qc.github_data_issues import adjustTime, adjustData, flagNAN
from lib import (remove_old_plots, load_flags_and_adjustments, load_L1,
                 clean_gps, smooth_pose, compute_cloud_cover,
                 solar_geometry, filter_shortwave, correct_shortwave, compute_albedo,
                 process_precip)
import tocgen

path_to_l0 = 'C:/Users/bav/GitHub/PROMICE data/aws-l0/'
path_to_l1 = 'C:/Users/bav/GitHub/PROMICE data/aws-l1/'
path_tx = '../aws-l3/tx/'

from datetime import date
today = date.today().strftime("%Y%m%d")
filename = './plot_compilations/flags.md'
figure_folder='figures/flags'
try:
    os.mkdir(figure_folder)
except:
    pass

df_metadata = pd.read_csv('../thredds-data/metadata/AWS_stations_metadata.csv')

f = open(filename, "w")
def Msg(txt):
    f = open(filename, "a")
    print(txt)
    f.write(txt + "\n")

# plt.close('all')

path_to_qc_files = '../PROMICE-AWS-data-issues/'
all_dirs = os.listdir(path_to_qc_files+'adjustments' )+os.listdir(path_to_qc_files+'flags')
var_file = os.path.join(os.path.dirname(pypromice.resources.__file__), "variables.csv")
zoom_to_good = False

for station in ['UPE_L']: #['KAN_Lv3','QAS_Lv3','QAS_Mv3','SCO_Lv3','SCO_Uv3']:
# for station in np.unique(np.array(all_dirs)):
    station = station.replace('.csv','')
    remove_old_plots(figure_folder, station)
    df_flags = load_flags_and_adjustments(path_to_qc_files, station)
    ds, ds_save, pAWS_tx, pAWS_raw = load_L1(path_to_l0, station)

    #%% Flagging, adjusting, filtering

    # The following steps are from L1toL2
    ds  = adjustTime(ds, adj_dir=path_to_qc_files+'adjustments')
    ds1 = flagNAN(ds,  flag_dir=path_to_qc_files+'flags')
    ds2 = adjustData(ds1, adj_dir=path_to_qc_files+'adjustments')
    ds22 = persistence_qc(ds2)

    ds22 = process_precip(ds22)

    vars_df = load_variables(var_file)
    ds3 = clip_values(ds22.copy(), vars_df)

    # The following steps are from L2toL3
    ds4, baseline_elevation = clean_gps(ds3)
    ds4 = smooth_pose(ds4)
    ds4 = compute_cloud_cover(ds4)

    geo = solar_geometry(ds4)

    ds4, flags = filter_shortwave(ds4, geo)
    ds4, TOA_crit_nopass_cor = correct_shortwave(ds4, geo)
    ds4, OKalbedos = compute_albedo(ds4, geo)

    # % plotting
    df_L1 = ds.to_dataframe().copy()

    if len(df_flags)>0:
        for ind, var_list in zip(df_flags.index, df_flags.variable):
            if var_list == '*':
                df_flags.loc[ind,'variable'] = ' '.join(df_L1.columns)
            elif '*' in var_list:
                df_flags.loc[ind,'variable'] = ' '.join(df_L1.filter(regex=var_list).columns)

        var_list = np.unique(' '.join(df_flags.variable.to_list()).split(' '))
        for v in var_list:
            if v not in ds_save.data_vars:
                Msg(v+' not in variables')
                var_list = var_list[~np.isin(var_list, v)]
                continue

            if ds_save[v].isnull().all():
                var_list = var_list[~np.isin(var_list, v)]
    else:
        var_list = [ 'p_l', 'p_u', 't_l','t_u', 'rh_l',  'rh_u', 'wspd_l', 'wspd_u', 'wdir_l', 'wdir_u', 'dsr', 'usr', 'dlr', 'ulr', 't_rad', 'z_boom_l', 'z_boom_u', 'z_stake', 'z_pt','z_pt_cor', 't_i_1', 't_i_2', 't_i_3', 't_i_4', 't_i_5', 't_i_6', 't_i_7', 't_i_8', 't_i_9', 't_i_10', 't_i_11', 'tilt_y', 'tilt_x', 'rot', 'precip_l', 'precip_u', 'gps_lat', 'gps_lon', 'gps_alt', 'fan_dc_l', 'fan_dc_u', 'batt_v', 't_log', 'p_i', 't_i', 'rh_i', 'wspd_i', 'wdir_i', 'gps_lat_i', 'gps_lon_i']
    Msg('# '+station)
    # var_list = [ 'p_l', 'p_u', 't_l','t_u', 'rh_l',  'rh_u', 'wspd_l', 'wspd_u', 'wdir_l', 'wdir_u', 'dsr', 'usr', 'dlr', 'ulr', 't_rad', 'z_boom_l', 'z_boom_u', 'z_stake', 'z_pt','z_pt_cor', 't_i_1', 't_i_2', 't_i_3', 't_i_4', 't_i_5', 't_i_6', 't_i_7', 't_i_8', 't_i_9', 't_i_10', 't_i_11', 'tilt_y', 'tilt_x', 'rot', 'precip_l', 'precip_u', 'gps_lat', 'gps_lon', 'gps_alt', 'fan_dc_l', 'fan_dc_u', 'batt_v', 't_log', 'p_i', 't_i', 'rh_i', 'wspd_i', 'wdir_i', 'gps_lat_i', 'gps_lon_i']

    var_list = [v for v in var_list if v in ds1.data_vars]

    var_list_list = [np.array(var_list[i:(i+6)]) for i in range(0,len(var_list),6)]
    # var_list_list = [['']]
    # var_list_list = ['tilt_x','tilt_y','rot'])]
    # var_list_list = ['t_u','rh_u','wspd_u','z_boom_u','dlr','ulr','dsr','usr'])]
    var_list_list = [np.array([
    #                     'tilt_x','tilt_y',
                        # 'gps_lat','gps_lon','gps_alt'
                        # 'z_boom_u', 't_u'
                        # 't_u']+['t_i_'+str(i+1) for i in range(11)
                        # 'p_u','z_pt','z_pt_cor',
                        # 'p_u','p_l','p_i',
                        # 'rh_u','rh_l','rh_i',
                        # 't_u','t_l','t_i',
                        # 'wspd_u','wspd_l','wspd_i',
                        # 'wdir_u','wdir_l','wdir_i',
                        'z_boom_l', 'z_boom_u', 'z_stake',
                        'z_boom_cor_l', 'z_boom_cor_u', 'z_stake_cor',
                        # 't_u','t_rad',
                        # 'p_u','t_u','z_pt','z_pt_cor',
                        # 'wdir_u','wdir_l','wdir_i'
                        # 't_l','p_l','rh_l','fan_dc_l'
                          # 'precip_l', 'precip_u',
                          # 'precip_l_cor', 'precip_u_cor',
                        # 'dlr','ulr','t_rad',
                        # "precip_u", "rainfall_u", "rainfall_cor_u",
                        # "precip_l", "rainfall_l", "rainfall_cor_l",
                        # 'dsr','usr',
                        # 'albedo',
                        # 'tilt_x','tilt_y','cc',
                        ])]
                      # ,'t_u','t_l','t_i', 'rh_u','rh_i','rh_l'])]

    for i, var_list in enumerate(var_list_list):
        if len(var_list) == 0: continue
        if len(var_list[~np.isin(var_list, df_L1.columns)]) >0:
            print(var_list[~np.isin(var_list, df_L1.columns)], 'not in L1 data')
        var_list = var_list[np.isin(var_list, ds4.data_vars)]
        fig, ax_list = plt.subplots(len(var_list),1,sharex=True, sharey=True, figsize=(12,len(var_list)*2.3))
        fig.subplots_adjust(top=0.83)
        if len(var_list) == 1: fig.subplots_adjust(top=0.7)

        if len(var_list)==1: ax_list = [ax_list]
        for var, ax in zip(var_list, ax_list):
            if var in ['z_boom_u','z_boom_l','z_stake']:
                valid = df_L1.z_stake.notna() & df_L1.z_boom_u.notna()
                m = valid & ((df_L1.z_stake - df_L1.z_boom_u).abs() <= 1e-6)
                
                # merge groups with small gaps
                gap = pd.Timedelta("1D")  # max gap to merge
                grp = (m != m.shift()).cumsum()
                true_runs = []
                for _, s in m.groupby(grp):
                    if not s.iloc[0]:
                        continue
                    t0, t1 = s.index[0], s.index[-1]
                    if true_runs and t0 - true_runs[-1][1] <= gap:
                        true_runs[-1] = (true_runs[-1][0], t1)
                    else:
                        true_runs.append((t0, t1))
                
                for t0, t1 in true_runs:
                    ax.axvspan(t0, t1, color="darkorange", alpha=0.3)


            if var in ['z_boom_cor_u','z_boom_cor_l','z_stake_cor']:
                ax.plot(ds4.time,
                        ds4[var.replace('_cor','')].values,
                        marker='.',color='gray', linestyle='None',
                        label='uncorrected for air temperature')
                
            if var in ds.data_vars:
                ax.plot(ds.time,
                        ds[var].values,
                        marker='.',color='tab:red', linestyle='None',
                        label='removed by flag')
                if var == 'albedo':
                    albedo_raw = ds['usr'] / ds['dsr']
                    albedo_raw = albedo_raw.where(albedo_raw>0).where(albedo_raw<1)

                    ax.plot(ds.time,
                            albedo_raw.values,
                            marker='.',color='tab:pink', linestyle='None',
                            label='unfiltered, uncorrected')

            if var in ds1.data_vars:
                ax.plot(ds1.time,
                        ds1[var].values,
                        marker='.',color='tab:orange', linestyle='None',
                        label='removed or changed by adjustment')
            if var in ds2.data_vars and var in ds22.data_vars:
                mask = np.isnan(ds22[var].values) & ~np.isnan(ds2[var].values)
                ax.plot(ds22.time[mask],
                        ds2[var].values[mask],
                        marker='.',color='tab:green', linestyle='None',
                        label='filtered with persistence')
            if var in ds22.data_vars and var in ds3.data_vars:
                mask = np.isnan(ds3[var].values) & ~np.isnan(ds22[var].values)
                ax.plot(ds3.time[mask],
                        ds22[var].values[mask],
                        marker='o',color='tab:brown', linestyle='None',
                        label='filtered with dependency')
            if var in ds3.data_vars:
                ax.plot(ds3.time,
                        ds3[var].values,
                        marker='.',color='tab:pink', linestyle='None',
                        label='removed by custom filter (gps_alt, tilt or rot)')
                if var == 'gps_alt':
                    ax.plot(ds3.time,
                            baseline_elevation,
                            ls='--', c='k')

            if var[:-4] in ds4.data_vars:
                if var in ['dsr_cor','usr_cor']:
                    if var == 'dsr_cor':
                        ax.plot(ds3.time,(1.2* geo["isr_toa"] + 150),
                                c='k', alpha=0.7)
                        ax_list[0].plot(np.nan,np.nan,
                                c='k',label='TOA irradiance + margin (W m-2)')
                    else:
                        ax.plot(ds3.time, 0.8*(1.2 * geo["isr_toa"] + 150),
                                c='k', alpha=0.7)
                    ax.plot(ds.time,
                            ds[var[:-4]].values,
                            marker='.',color='tab:red', linestyle='None',
                            label='removed by flag')
                    ax.plot(ds3.time,
                            ds3[var[:-4]].values,
                            marker='.',color='tab:pink', linestyle='None',
                            label='value before tilt correction')
                    if var == 'dsr_cor':
                        ax.plot(ds3.time,
                                ds3[var[:-4]].where(
                                    flags.TOA_crit_nopass_dsr | TOA_crit_nopass_cor).values,
                                marker='.',color='k', linestyle='None',
                                label='removed, dsr above TOA irradiance')
                    else:
                        ax.plot(ds3.time,
                                ds3[var[:-4]].where(
                                    flags.TOA_crit_nopass_usr | TOA_crit_nopass_cor).values,
                                marker='.',color='k', linestyle='None',
                                label='removed, dsr above TOA irradiance')
                        if flags.TOA_crit_nopass_usr.any():
                            ax.plot(ds3.time,
                                ds3[var[:-4]].where(flags.TOA_crit_nopass_usr).values,
                                marker='.',color='tab:orange', linestyle='None')
                            ax_list[0].plot(np.nan,np.nan,marker='.',ls='None',
                                    c='tab:orange',label='removed, usr above TOA irradiance')

                    ax.plot(ds3.time,
                            ds3[var[:-4]].where(flags.bad).values,
                            marker='.',color='tab:green', linestyle='None',
                            label='sun below horizon zenith angle or negative reading')


            if var in ds4.data_vars:
                ax.plot(ds4.time,
                        ds4[var].values,
                        marker='.',color='tab:blue', linestyle='None',
                        label='final')

        for var, ax in zip(var_list, ax_list):
            if zoom_to_good:
                ax.set_ylim(ds4[var].min(), ds4[var].max())
            ax.set_ylabel(var)
            ax.grid(True, which='minor', linestyle='--', linewidth=0.5)
            ax.grid(True, which='major', linestyle='-', linewidth=1)

        # ax.set_xlim(pd.to_datetime(['2025-06-01','2025-09-08']))
        title = station+'_%i/%i'%(i+1,len(var_list_list))
        ax_list[0].legend(loc='lower left', title = title, bbox_to_anchor=(0,1.1), ncol=3)
        fig.savefig('%s/%s_%i.png'%(figure_folder, station,i), dpi=120,bbox_inches='tight')
        Msg('![](../%s/%s_%i.png)'%(figure_folder, station,i))
    Msg(' ')
tocgen.processFile(filename, filename[:-3]+"_toc.md")
