# -*- coding: utf-8 -*-
"""
Created on %(date)s
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
    import matplotlib.pyplot as plt
"""


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

site_metadata = pd.read_csv('../thredds-data/metadata/AWS_sites_metadata.csv')

sites_multiple_stations = {
    row.site_id: row.stations.split()
    for _, row in site_metadata.iterrows()
    if len(row.stations.split()) > 1
}

# print(sites_multiple_stations)



def correct_unventilated_temperature(df, fan_threshold=50):
    df = df.copy()

    rho = 1.2
    cp = 1004.0

    U = df['wspd_u'].clip(lower=0.1)
    T = df['t_u'] + 273.15
    DSR = df['dsr'].clip(lower=0)

    X = DSR / (rho * cp * T * U) * 1000.0
    dT = 3.1 * np.sqrt(X)

    mask = (
        (df['fan_dc_u'].isna() | (df['fan_dc_u'] < fan_threshold))
        & (df['dsr'] > 150)
        & (X >= 0.05)
    )

    df['t_u_cor'] = df['t_u']
    df.loc[mask, 't_u_cor'] = df.loc[mask, 't_u'] - dT.loc[mask]

    return df

def estimate_coefficient(df, df_ref, fan_threshold=50):
    d = df[['t_u', 'dsr', 'wspd_u', 'fan_dc_u']].join(
        df_ref[['t_u']].rename(columns={'t_u': 't_ref'}),
        how='inner'
    ).dropna(subset=['t_u', 't_ref', 'dsr', 'wspd_u'])

    rho = 1.2
    cp = 1004.0

    U = d['wspd_u'].clip(lower=0.1)
    T = d['t_u'] + 273.15

    X = d['dsr'].clip(lower=0) / (rho * cp * T * U) * 1000
    z = np.sqrt(X)

    mask = (
        (df['fan_dc_u'].isna() | (df['fan_dc_u'] < fan_threshold))
        & (df['dsr'] > 150)
        & (X >= 0.05)
    )

    y = d.loc[mask, 't_u'] - d.loc[mask, 't_ref']
    z = z.loc[mask]

    a = (z * y).sum() / (z**2).sum()
    n = mask.sum()

    print(
        f"Estimated radiation-correction coefficient: a = {a:.2f}\n"
        f"Based on {n:,} overlapping unventilated samples "
        f"(fan_dc_u < {fan_threshold} or NaN, X >= 0.05)"
    )

    return a


path_thredds = '../thredds-data/level_2_stations/csv/hour'
site = 'KAN_L'
# site = 'QAS_U'
# site = 'QAS_L'
# site = 'NUK_U'
station_list = [site, site+'v3']
print(station_list)
var_list = ['dsr', 'wspd_u','t_u', 'fan_dc_u']

fig, axes = plt.subplots(
    len(var_list), 1,
    sharex=True,
    figsize=(10, 9)
)

if len(var_list) == 1:
    axes = [axes]

dfs = {}

for station in station_list:
    df = pd.read_csv(f'{path_thredds}/{station}_hour.csv')
    df['time'] = pd.to_datetime(df['time'], utc=True)
    df = df.set_index('time')

    if 'v3' not in station:
        df = correct_unventilated_temperature(df)

    dfs[station] = df


a = estimate_coefficient(dfs[station_list[0]], dfs[station_list[1]])


t0 = max(df.index.min() for df in dfs.values())
t1 = min(df.index.max() for df in dfs.values())

for station, df in dfs.items():
    df = df.loc[t0:t1]

    for var, ax in zip(var_list, axes):
        if var in df.columns:
            ax.plot(df.index, df[var], label=station)

            if var == 't_u' and 'v3' not in station:
                ax.plot(df.index, df['t_u_cor'], label=station+' corrected', c='tab:green')

for var, ax in zip(var_list, axes):
    ax.set_ylabel(var)
    ax.grid()
    ax.legend()

axes[-1].set_xlabel('Time')
plt.tight_layout()
plt.show()
