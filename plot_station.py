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

path_l3 = 'C:/Users/bav/GitHub/PROMICE data/aws-l3/level_3/'
path_tx = 'C:/Users/bav/GitHub/PROMICE data/aws-l3/tx/'
path_gcn= 'C:/Users/bav/GitHub/PROMICE data/GC-Net-Level-1-data-processing/L1/'

# df_gcn = nead.read(path_gcn+'24-EastGRIP.csv').to_dataframe()
# df_gcn = nead.read(path_gcn+'04-GITS.csv').to_dataframe()
# df_gcn.timestamp = pd.to_datetime(df_gcn.timestamp, utc=True)
# df_gcn=df_gcn.set_index('timestamp')

df_meta = pd.read_csv(path_l3+'../AWS_latest_locations.csv')
# var_list = ['rh_u', 't_u','wspd_u','p_u','z_boom_u',
#             'rh_l','t_l','wspd_l','p_l','z_boom_l',
#             'rh_i','t_i','wspd_i','p_i','batt_v',
#             't_i_all']
# var_list = ['rh_u','t_u',
#             'rh_l','t_l',
#             'rh_i']
# var_list = ['rh_u','t_u',
#             'wspd_u','wdir_u',
#             'dsr','usr', 'z_boom_u']
# var_list = ['p_u','p_l','p_i']
# var_list = ['t_u','t_l']
# var_list = ['t_i','rh_i','p_i','wspd_i','wdir_i','gps_lat','gps_lon','gps_alt']
# var_list = ['gps_geounit']
var_list = ['t_u', 't_l','ts']

station_list = ['EGP']  #df_meta.stid  #
# var_list2 = ['RH1', 'RH2']

plt.close('all')


# for var,var2, ax in zip(var_list, var_list2, ax_list):
#     ax.plot(df_gcn.index, df_gcn[var2].values, marker='.',linestyle='None', label='GC-Net')
#     ax.plot(df_gcn.index, df_gcn[var2.replace('1','2')].values, marker='.',linestyle='None', label='GC-Net')
for station in station_list:
    df_l3 = pd.read_csv(path_l3+station+'/'+station+'_hour.csv')
    df_l3.time = pd.to_datetime(df_l3.time, utc=True)
    df_l3 = df_l3.set_index('time')
    if station not in ['NUK_N', 'QAS_A','TAS_U', 'ZAK_L']:
        df_tx = pd.read_csv(path_tx+station+'/'+station+'_hour.csv')
        df_tx.time = pd.to_datetime(df_tx.time, utc=True)
        df_tx = df_tx.set_index('time')
    else:
        df_tx = pd.DataFrame()
    # df_l3=df_l3.loc['2021-09-01':'2022-06-10',:]
    # df_l3=df_l3.loc['2022-09-01':,:]
    # appending fieldwork date
    # df_l3 = (pd.concat([df_l3, pd.DataFrame(index=[pd.to_datetime('2023-06-10', utc=True)])]).sort_index(kind='stable', ignore_index=False))
    
    var_list_list = [var_list[i:i+5] for i in range(0, len(var_list), 5)]
    for k, var_list in enumerate(var_list_list):
        fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(13,13))
        if len(var_list)==1:
            ax_list = [ax_list]
    
        for var, ax in zip(var_list, ax_list):
            if (var not in df_l3.columns) & (var not in df_tx.columns):
                print(var, 'not in L3 or tx data at', station)
                if len(var_list) == 1:
                    plt.close(fig)
                continue
            # if df_l3[var].isnull().all():
            #     print(var, 'all nan at', station)
            #     if len(var_list) == 1:
            #         plt.close(fig)
            #     continue
            print(var)
                # X = df_l3.index.values.astype(float)
                # Y = df_l3[var].values
                # linear_regressor = LinearRegression()  # create object for the class
                # linear_regressor.fit(X[~np.isnan(X+Y)].reshape(-1, 1),
                #                      Y[~np.isnan(X+Y)].reshape(-1, 1))  # perform linear regression
                # Y_pred = linear_regressor.predict(X.reshape(-1, 1))  # make predictions
            ax.set_ylabel(var)
            if var == 't_i_all':
                var = ['t_i_%i'%i for i in range(1,12) if 't_i_%i'%i in df_l3.columns]
    
                ax.plot(df_l3[var].index, df_l3[var].values, 
                        marker='.',markeredgecolor='None', 
                        linestyle='None', label=var,alpha=0.7)
            else:
                try:
                    ax.plot(df_tx[var].index, df_tx[var].values, marker='.',linestyle='None', label='transmission')
                except:
                    print(var,'not in transmission')
        
                try:
                    ax.plot(df_l3[var].index, df_l3[var].values, marker='.',markeredgecolor='None', linestyle='None', label='l3',alpha=0.5)
                except:
                    print(var,'not in L3 files')
            
            ax.legend()
            ax.grid()
                # ax.plot(df_l3[var].index,Y_pred)
                # ax.plot(df_l3[var].index,Y_pred*0, 'k', ls=':')
                # print(station, Y_pred[-1] - Y[~np.isnan(X+Y)][0])
            
        plt.suptitle('%s %i/%i'%(station, k+1, len(var_list_list)))
