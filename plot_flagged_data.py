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
from lib.process import (load_L2, remove_old_plots)
from lib.plot import (DEFAULT_VAR_LIST, flag_handles, flag_colors, plot_L0,
                      plot_identical_SR50)

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
zoom_to_good = True

for station in ['SWC_O']:
    # for station in df_metadata.station_id:
    station = station.replace('.csv','')
    remove_old_plots(figure_folder, station)
    ds, pAWS_tx, pAWS_raw = load_L2(path_to_l0, station, keep_flagged_data=True)

    #%% Flagging, adjusting, filtering
    for var in ["t", "rh","p","wspd"]:
        if (var+'_u' in ds.data_vars) and (var+'_l' in ds.data_vars):
            ds[var+'_diff'] = ds[var+'_u'] - ds[var+'_l']
    if ('rh_u_wrt_ice_or_water' in ds.data_vars) and ('rh_l_wrt_ice_or_water' in ds.data_vars):
        ds['rh_wrt_ice_or_water_diff'] = ds['rh_u_wrt_ice_or_water'] - ds['rh_l_wrt_ice_or_water']
    # %% plotting
    df_L1 = ds.to_dataframe().copy()

    Msg('# '+station)

    var_list = [v for v in DEFAULT_VAR_LIST if v in ds.data_vars]

    var_list_list = [np.array(var_list[i:(i+6)]) for i in range(0,len(var_list),6)]
    # var_list_list = [['']]
    # var_list_list = ['tilt_x','tilt_y','rot'])]
    # var_list_list = ['t_u','rh_u','wspd_u','z_boom_u','dlr','ulr','dsr','usr'])]
    var_list_list = [np.array([
    #                     'tilt_x','tilt_y',
                        # 'gps_lat','gps_lon','gps_alt'
                        # 't_u','wspd_u',
                        # 't_u','t_l','t_i',
                        # 'p_u','z_pt','z_pt_cor',
                        'p_u', #'p_l','p_i',
                        # 't_u','t_l',"t_diff" #'t_i',
                        # 'rh_u','rh_l','rh_i',
                        # 'wspd_u','wspd_l',"wspd_diff" #'t_i',
                        # 'p_u','p_l',"p_diff"
                        # 'rh_u_wrt_ice_or_water', 'rh_l_wrt_ice_or_water',
                        # "rh_wrt_ice_or_water_diff",
                        # 'rh_i_wrt_ice_or_water',
                        # 'wspd_u','wspd_l',
                        # 'wdir_u','wdir_l',
                        # 'fan_dc_l','fan_dc_u',
                        # 'z_boom_l', 'z_boom_u', #'z_stake',
                        # 'z_boom_cor_l', 'z_boom_cor_u', #'z_stake_cor',
                        # 'z_pt','z_pt_cor',
                        # 'gps_lat', 'gps_lon','gps_alt'
                        # 'wdir_u','wdir_l','wdir_i',
                        # "precip_u", "rainfall_u", "rainfall_cor_u",
                        # "precip_l", "rainfall_l", "rainfall_cor_l",
                        # 'dsr','usr', 'dsr_cor','usr_cor', 'albedo',
                        # 'tilt_x','tilt_y','rot',
                        # 'dlr','ulr','t_rad','cc',
                        # ]), np.array( ['t_i_'+str(i+1) for i in range(11)
                        ])]
                      # ,'t_u','t_l','t_i', 'rh_u','rh_i','rh_l'])]

    for i, var_list in enumerate(var_list_list):
        if len(var_list) == 0: continue
        if len(var_list[~np.isin(var_list, df_L1.columns)]) >0:
            print(var_list[~np.isin(var_list, df_L1.columns)], 'not in L1 data')
        var_list = var_list[np.isin(var_list, ds.data_vars)]
        fig, ax_list = plt.subplots(len(var_list),1,sharex=True,  #sharey=True,
                                    figsize=(12,len(var_list)*2.1))
        fig.subplots_adjust(top=0.8)
        if len(var_list) == 1: fig.subplots_adjust(top=0.7)
        if len(var_list)==1: ax_list = [ax_list]

        for var, ax in zip(var_list, ax_list):

            if (var in ['z_boom_u','z_boom_l','z_stake']) and ('z_stake' in df_L1.columns):
                ax = plot_identical_SR50(df_L1, ax)

            if var in ['z_boom_cor_u','z_boom_cor_l','z_stake_cor']:
                ax.plot(ds.time,
                        ds[var.replace('_cor','')].values,
                        marker='.',color='gray', linestyle='None',
                        label='uncorrected for air temperature')

            # plotting L0 TX
            ax = plot_L0(pAWS_raw, ax, var, s='x', label='in L0 raw')

            # plotting L0 RAW
            ax= plot_L0(pAWS_tx, ax, var, s='+', label='in L0 tx')

            # plot data with flags
            var_qc=var+'_qc'
            if var in ds.data_vars:
                for flag, col in flag_colors.items():
                    da = ds[var].where(ds[var_qc] == flag)
                    if da.notnull().any():
                        da.plot(ax=ax, marker='.', linestyle='None',
                                color=col, label=flag)

        for var, ax in zip(var_list, ax_list):
            # ax.set_xlim(pd.to_datetime(['2020-05-01','2026-01-16']))
            if zoom_to_good:
                ax.set_ylim(ds[var].sel(time=ds[var+'_qc'] == 'OK').min(),
                            ds[var].sel(time=ds[var+'_qc'] == 'OK').max())
            else:
                xmin, xmax = ax.get_xlim()
                xmin = mdates.num2date(xmin)
                xmin = pd.Timestamp(xmin).tz_localize(None)
                xmax = mdates.num2date(xmax)
                xmax = pd.Timestamp(xmax).tz_localize(None)

            ax.set_ylabel(var)
            ax.grid(True, which='minor', linestyle='--', linewidth=0.5)
            ax.grid(True, which='major', linestyle='-', linewidth=1)

        title = station+'_%i/%i'%(i+1,len(var_list_list))
        ax_list[0].legend(handles=flag_handles,
                          loc='lower left',
                          title=title,
                          bbox_to_anchor=(0,1.1),
                          ncol=3,
                          markerscale=2)
        # fig.savefig('%s/%s_%i.png'%(figure_folder, station,i), dpi=120,bbox_inches='tight')
        # Msg('![](../%s/%s_%i.png)'%(figure_folder, station,i))
    Msg(' ')
# tocgen.processFile(filename, filename[:-3]+"_toc.md")
