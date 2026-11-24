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
    "ZERO_WSPD": "turquoise",
}

flag_handles = [
    Line2D([0], [0], marker='.', linestyle='None',
           color=c, label=f)
    for f, c in flag_colors.items()
]

DEFAULT_VAR_LIST = [ 'p_l', 'p_u', 't_l','t_u', 'rh_l',  'rh_u', 'wspd_l', 'wspd_u', 'wdir_l',
        'wdir_u', 'dsr', 'usr', 'dlr', 'ulr', 't_rad', 'z_boom_l','z_boom_cor_l', 'z_boom_u','z_boom_cor_u',
        'z_stake','z_stake_cor', 'z_pt','z_pt_cor', 't_i_1', 't_i_2', 't_i_3', 't_i_4', 't_i_5',
        't_i_6', 't_i_7', 't_i_8', 't_i_9', 't_i_10', 't_i_11', 'tilt_y',
        'tilt_x', 'rot', 'precip_l', 'precip_u', 'gps_lat', 'gps_lon', 'gps_alt',
        'fan_dc_l', 'fan_dc_u', 'batt_v', 't_log', 'p_i', 't_i', 'rh_i', 'wspd_i',
        'wdir_i', 'gps_lat_i', 'gps_lon_i']

def plot_L0(pAWS_raw, ax, var, s='+', label='in L0 tx'):
    skip_L0_var = [ # 'dlr','ulr',
                   'gps_lat','gps_lon','gps_alt']
    if pAWS_raw is not None:
        for data in pAWS_raw.L0:
            if (var in data.data_vars) and (var not in skip_L0_var):
                tmp=data[var]
                if 'tx' in label and not var.endswith('_i') and var not in ["batt_v"]:
                    tmp['time'] = tmp.time - np.timedelta64(1, 'h')

                if var not in [ 'dlr','ulr',]:
                    ax.plot(tmp.time,
                        tmp,
                        marker=s,color='k', linestyle='None',
                        label='__nolegend__')
                else:
                    ax.plot(tmp.time,
                        -10 * tmp,
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



def print_comparison(auto, manual, max_days=30):
    """For each manual shift, the closest automated shift of the same variable."""
    print(f'\n{len(manual)} manual and {len(auto)} automated surface height shifts')
    for _, m in manual.sort_values(['variable', 't0']).iterrows():
        t0 = 'start' if pd.isnull(m.t0) else f'{m.t0:%Y-%m-%d %H:%M}'
        text = f'  manual {m.variable:10s} {t0}  {m.adjust_value:+.3f} m'
        a = auto[auto.variable == m.variable]
        if len(a) > 0 and not pd.isnull(m.t0):
            dt = (a['t0'] - m.t0)
            i = dt.abs().idxmin()
            if abs(dt[i]) <= pd.Timedelta(days=max_days):
                text += (f'  <->  automated {a.loc[i, "t0"]:%Y-%m-%d %H:%M}'
                         f' ({dt[i] / pd.Timedelta(days=1):+.1f} d)'
                         f'  {a.loc[i, "adjust_value"]:+.3f} m')
            else:
                text += f'  <->  no automated shift within {max_days} d'
        print(text)
    matched = set()
    for _, m in manual.iterrows():
        a = auto[auto.variable == m.variable]
        if len(a) > 0 and not pd.isnull(m.t0):
            dt = (a['t0'] - m.t0).abs()
            if dt.min() <= pd.Timedelta(days=max_days):
                matched.add(dt.idxmin())
    for i, a in auto.drop(index=list(matched)).sort_values(['variable', 't0']).iterrows():
        print(f'  automated {a.variable:10s} {a.t0:%Y-%m-%d %H:%M}  {a.adjust_value:+.3f} m'
              f'  <->  no manual shift within {max_days} d')


def plot_shifts(ax_series, ax_shifts, shifts, colors, source, t_start):
    """Mark the shifts on the series (vertical lines) and show their magnitudes.

    Manual shifts are plain lines and filled circles, automated ones dashed
    lines and open triangles. A manual shift with a t1 is a temporary offset:
    it is shown at t0 and again at t1 with the opposite sign, the net step of
    the series.
    """
    style = {'manual': dict(ls='-', marker='o', filled=True),
             'auto': dict(ls='--', marker='^', filled=False)}[source]
    for _, s in shifts.iterrows():
        color = colors.get(s.variable, 'k')
        steps = [(t_start if pd.isnull(s.t0) else s.t0, s.adjust_value)]
        if 't1' in s and not pd.isnull(s.t1):
            steps.append((s.t1, -s.adjust_value))
        for t, v in steps:
            ax_series.axvline(t, color=color, ls=style['ls'], lw=0.8, alpha=0.6)
            ax_shifts.vlines(t, 0, v, color=color, ls=style['ls'], lw=1)
            ax_shifts.plot(t, v, ls='None', marker=style['marker'], ms=6,
                           color=color, mfc=color if style['filled'] else 'none')
            if abs(v) >= 0.1:
                ax_shifts.annotate(f'{v:+.2f}', (t, v), xytext=(0, 3 if v > 0 else -3),
                                   textcoords='offset points', rotation=90, fontsize=6,
                                   ha='center', va='bottom' if v > 0 else 'top',
                                   color=color)
