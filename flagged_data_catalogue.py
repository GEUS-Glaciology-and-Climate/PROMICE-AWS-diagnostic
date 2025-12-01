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
import matplotlib
matplotlib.use('Agg')
path_no_flag = './L2_no_qc/level_2'
path_w_flag= './L2_test/level_2'


df_metadata = pd.read_csv('../thredds-data/metadata/AWS_stations_metadata.csv')
# for station in ['CEN1']:
for station in np.unique(np.array(df_metadata.station_id)):

    var_list = [
            't_u','t_l','t_i'
            'p_u','p_l','p_i',
            'rh_l','rh_i','rh_l_cor',
            'dlr','ulr','dsr','usr',
            'z_boom_u','z_boom_l','z_stake'
            'wspd_u','wspd_l','wspd_i'
            ]

    print(station)
    df_no_flags = pd.read_csv(f'{path_no_flag}/{station}/{station}_hour.csv')
    df_no_flags.time = pd.to_datetime(df_no_flags.time, utc=True)
    df_no_flags = df_no_flags.set_index('time')

    df_w_flags = pd.read_csv(f'{path_w_flag}/{station}/{station}_hour.csv')
    df_w_flags.time = pd.to_datetime(df_w_flags.time, utc=True)
    df_w_flags = df_w_flags.set_index('time')

    out = {}
    expected = {}

    for v in var_list:
        if v in df_no_flags.columns and v in df_w_flags.columns:
            m = df_w_flags[v].isna() & df_no_flags[v].notna()
            out[v] = m.sum()
        else:
            out[v] = 0
        expected[v] = len(df_no_flags.index)

    pd.DataFrame({"missing": out, "expected": expected}).to_csv(f"nan_counts_{station}.csv")


    var_list = [v for v in var_list if out[v]>0]

    df_no_flags=df_no_flags.resample('D').mean()
    df_w_flags=df_w_flags.resample('D').mean()

    var_list = [v for v in var_list if v in df_w_flags.columns]

    fig, ax_list = plt.subplots(len(var_list)+1,1,sharex=True, figsize=(8,8))
    fig.subplots_adjust(top=0.85, left=0.08, right=0.98,bottom=0.08)
    if len(var_list)==0:
        continue

    for var, ax, var_label in zip(var_list, ax_list, var_list):

        ax.set_ylabel(var)

        ax.plot(df_no_flags[var].index, df_no_flags[var].values, marker='.', lw=3,
                color='tab:blue', label='all measurements'
                )

    t_i_vars = [f't_i_{i}' for i in range(1,11) if f't_i_{i}' in df_no_flags.columns]
    ax_list[-1].plot(df_no_flags[t_i_vars].index, df_no_flags[t_i_vars].values, marker='.',
            color='tab:blue',
            )
    ax_list[-1].set_ylabel('t_i_*')
    ax_list[0].legend( loc="upper center", ncols=2,
        bbox_to_anchor=(0.5, 0.98),   # 0.98 = just under top of figure
        bbox_transform=fig.transFigure,
        fontsize=12, title=station )
    fig.savefig('figures/flagged_data/'+station+'_1.png',dpi=300)

    fig, ax_list = plt.subplots(len(var_list)+1,1,sharex=True, figsize=(8,8))
    fig.subplots_adjust(top=0.85, left=0.08, right=0.98,bottom=0.08)
    for var, ax, var_label in zip(var_list, ax_list, var_list):

        ax.set_ylabel(var)

        ax.plot(df_no_flags[var].index, df_no_flags[var].values, marker='.',lw=3,
                color='tab:red', label='bad measurements')
        ax.plot(df_w_flags[var].index, df_w_flags[var].values, marker='.',lw=3,
                color='tab:blue', label='good measurements')


    t_i_vars = [f't_i_{i}' for i in range(1,11) if f't_i_{i}' in df_no_flags.columns]
    ax_list[-1].plot(df_no_flags[t_i_vars].index, df_no_flags[t_i_vars].values, marker='.',
            color='tab:red')

    ax_list[-1].plot(df_w_flags[t_i_vars].index, df_w_flags[t_i_vars].values, marker='.',
            color='tab:blue',)
    ax_list[-1].set_ylabel('t_i_*')

    ax_list[0].legend( loc="upper center", ncols=2,
        bbox_to_anchor=(0.5, 0.98),   # 0.98 = just under top of figure
        bbox_transform=fig.transFigure,
        fontsize=12, title=station )
    fig.savefig('figures/flagged_data/'+station+'_2.png',dpi=300)
