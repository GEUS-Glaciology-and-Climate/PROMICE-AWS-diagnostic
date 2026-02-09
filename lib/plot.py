# -*- coding: utf-8 -*-
"""
Created on %(date)s
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D

flag_colors = {
    "OK": "green",
    "NAN": "lightgray",
    "RIME": "cyan",
    "ROC": "orange",
    "PERSISTENCE": "purple",
    "OOL": "red",
    "DEPENDENCY": "brown",
    "ADJ_MIN": "blue",
    "ADJ_MAX": "darkred",
    "ADJ_HAMPEL": "magenta",
    "ADJ_GRAD": "gold",
    "ADJ_SAME_TO_OTHER_SENSOR": "black",
    "GPS_FILTER": "teal",
}

flag_handles = [
    Line2D([0], [0], marker='.', linestyle='None',
           color=c, label=f)
    for f, c in flag_colors.items()
]

DEFAULT_VAR_LIST = [ 'p_l', 'p_u', 't_l','t_u', 'rh_l',  'rh_u', 'wspd_l', 'wspd_u', 'wdir_l',
        'wdir_u', 'dsr', 'usr', 'dlr', 'ulr', 't_rad', 'z_boom_l', 'z_boom_u',
        'z_stake', 'z_pt','z_pt_cor', 't_i_1', 't_i_2', 't_i_3', 't_i_4', 't_i_5',
        't_i_6', 't_i_7', 't_i_8', 't_i_9', 't_i_10', 't_i_11', 'tilt_y',
        'tilt_x', 'rot', 'precip_l', 'precip_u', 'gps_lat', 'gps_lon', 'gps_alt',
        'fan_dc_l', 'fan_dc_u', 'batt_v', 't_log', 'p_i', 't_i', 'rh_i', 'wspd_i',
        'wdir_i', 'gps_lat_i', 'gps_lon_i']

def plot_L0(pAWS_raw, ax, var, s='+', label='in L0 tx'):
    skip_L0_var = ['dlr','ulr','gps_lat','gps_lon','gps_alt']
    if pAWS_raw is not None:
        for data in pAWS_raw.L0:
            if (var in data.data_vars) and (var not in skip_L0_var):
                if not var.endswith('_i'):
                    tmp=data[var].shift(time=-1)
                else:
                    tmp=data[var]
                ax.plot(tmp.time,
                        tmp,
                        marker=s,color='k', linestyle='None',
                        label='__nolegend__')

        ax.plot(np.nan,np.nan, marker=s,color='k',
                linestyle='None', label=label)
    return ax

def plot_identical_SR50(df_L1, ax):
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
    return ax
