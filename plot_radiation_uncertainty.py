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

for station in ['TAS_L']:
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
                                adj_dir=path_to_qc_files+'adjustments',
                                var_list = ['z_boom_cor_u'])

    vars_df = load_variables(var_file)
    ds_post_clip = clip_values(ds_post_adjust.copy(), vars_df)

    # %% making tilt perturbation
    import xarray as xr

    ds_list = {}
    var_perturb = 'tilt_x'
    for perturbation in range(-5, 6):
        print(f"Perturbating {var_perturb} by {perturbation}")
        ds_final = smooth_pose(ds_post_clip.copy())
        ds_final[var_perturb] = ds_final[var_perturb] + perturbation
        ds_final = compute_cloud_cover(ds_final.copy())

        geo = solar_geometry(ds_final.copy())

        ds_final, flags = filter_shortwave(ds_final, geo)
        ds_final, TOA_crit_nopass_cor = correct_shortwave(ds_final, geo)
        ds_final, OKalbedos = compute_albedo(ds_final, geo)
        for var in geo.keys():
            if var in ['lat','lon']: continue
            ds_final[var] = geo[var].copy()
        ds_list[perturbation] = ds_final.copy()

    # %% plotting
    df_L1 = ds.to_dataframe().copy()
    Msg('# '+station)
    var_list = [v for v in DEFAULT_VAR_LIST if v in ds.data_vars]
    var_list_list = [np.array(var_list[i:(i+6)]) for i in range(0,len(var_list),6)]

    var_list_list = [np.array([
                        'dsr','dsr_cor','usr','albedo',
                        'tilt_x','tilt_y','rot',
                        'phi_sensor_rad', 'theta_sensor_rad','Declination_rad',
                        'HourAngle_rad','ZenithAngle_rad','AngleDif_deg',
                        # 'dlr','ulr','cc',
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
            # plotting L0 TX
            # ax = plot_L0(pAWS_raw, ax, var, s='x', label='in L0 raw')

            # plotting L0 RAW
            # ax= plot_L0(pAWS_tx, ax, var, s='+', label='in L0 tx')

            # final data
            if var in ["albedo", "dsr_cor", var_perturb, 'phi_sensor_rad',
                       'theta_sensor_rad','Declination_rad',
                       'HourAngle_rad','ZenithAngle_rad','AngleDif_deg',]:
                for perturbation in list(ds_list.keys()) + [0]:
                    ds_final = ds_list[perturbation].copy()
                    if var in ds_final.data_vars:
                        if perturbation == 0 :
                            c = 'tab:blue'
                        else:
                            c = 'lightgray'
                        ax.plot(ds_final.time,
                                ds_final[var].values,
                                marker='.',color=c, #linestyle='None',
                                label='{var_perturb} {perturbation}')
            else:
                ax.plot(ds_final.time,
                        ds_final[var].values,
                        marker='.',color='tab:blue', #linestyle='None',
                        label='No perturbation')


        for var, ax in zip(var_list, ax_list):
            ax.set_xlim(pd.to_datetime(['2025-05-01','2026-04-16']))
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
