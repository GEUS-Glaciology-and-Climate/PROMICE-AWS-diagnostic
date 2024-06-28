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
from sklearn.linear_model import LinearRegression
import nead

path_l3 = '../aws-l3/level_3/'
path_tx = '../aws-l3/tx/'
path_gcn= '../GC-Net-Level-1-data-processing/L1/'


df_meta = pd.read_csv(path_l3+'../AWS_metadata.csv')
df_latest = pd.read_csv(path_l3+'../AWS_latest_locations.csv').set_index('stid')

station_list = ['SCO_U'] #df_latest.index
# station_list = df_latest.index
# var_list2 = ['RH1', 'RH2']

from csv2bufr import find_positions

plt.close('all')

for station in station_list:
    if station in ['KAN_B', 'NUK_N', 'QAS_A']:
        continue
    df_l3 = pd.read_csv(path_l3+station+'/'+station+'_hour.csv')
    df_l3.time = pd.to_datetime(df_l3.time, utc=True)
    df_l3 = df_l3.set_index('time')
    
    df_tx = pd.read_csv(path_tx+station+'/'+station+'_hour.csv')
    df_tx.time = pd.to_datetime(df_tx.time, utc=True)
    df_tx = df_tx.set_index('time')
    df_tx['p_i'].last_valid_index()
    df_limited, positions = find_positions(df_tx, station, time_limit='3M')
    positions = positions.iloc[[-1], :]
    # df_tx = df_tx.loc['2023':]
    fig, ax_list = plt.subplots(3,1,sharex=True, figsize=(13,13))
    var_list = [['msg_lat', 'gps_lat'],
                ['msg_lon', 'gps_lon' ],
                ['gps_alt']]
    # old position estimation
    ax_list[0].plot(pd.to_datetime(df_latest.loc[station, 'timestamp']),
             df_latest.loc[station, 'lat'], marker='x', markersize=15,
             color='tab:red',label='old position estimation', ls='None')
    ax_list[1].plot(pd.to_datetime(df_latest.loc[station, 'timestamp']),
          df_latest.loc[station, 'lon'], marker='x', markersize=15,
          color='tab:red',label='old position estimation', ls='None')
    ax_list[2].plot(pd.to_datetime(df_latest.loc[station, 'timestamp']),
          df_latest.loc[station, 'alt'], marker='x', markersize=15,
          color='tab:red',label='old position estimation', ls='None')
    # new position estimation
    # ax_list[0].plot(positions.index,
    #                 positions.gps_lat_linfit, marker='^', markersize=15,
    #          color='tab:red',label='new position estimation', ls='None')
    # ax_list[1].plot(positions.index,
    #                 positions.gps_lon_linfit, marker='^', markersize=15,
    #       color='tab:red',label='new position estimation', ls='None')
    # ax_list[2].plot(positions.index,
    #                 positions.gps_alt_linfit, marker='^', markersize=15,
    #       color='tab:red',label='new position estimation', ls='None')
    sym=['o','d']
    ax_list[0].set_ylabel('latitude')
    ax_list[1].set_ylabel('longitude')
    ax_list[2].set_ylabel('elevation')
    for var_l, ax in zip(var_list, ax_list):
        for i, var in enumerate(var_l):
            if 'gps' in var:
                X = df_tx.index.values.astype(float)
                Y = df_tx[var].values
                linear_regressor = LinearRegression()  # create object for the class
                linear_regressor.fit(X[~np.isnan(X+Y)].reshape(-1, 1),
                                      Y[~np.isnan(X+Y)].reshape(-1, 1))  # perform linear regression
                Y_pred = linear_regressor.predict(X.reshape(-1, 1))  # make predictions
                ax.plot(df_tx.index, Y_pred, color='tab:red', label=var)
            try:
                ax.plot(df_tx[var].index, df_tx[var].values, 
                        marker=sym[i],linestyle='None', label=var)
                # print(df_tx[var].mean(), df_tx[var].median())
            except:
                ax.plot(np.nan,np.nan, 
                        marker=sym[i],linestyle='None', label=var)
                pass
                # print(var,'not in transmission')
    
        
        ax.legend()
        ax.grid()

        
    plt.suptitle(station)


