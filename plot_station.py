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

path_l3 = '../aws-l3-dev/level_3/'
path_tx = '../aws-l3-dev/tx/'
path_gcn= 'C:/Users/bav/GitHub/PROMICE data/GC-Net-Level-1-data-processing/L1/'

df_meta = pd.read_csv(path_l3+'../AWS_latest_locations.csv')
var_list = [
    # 'rh_u', 't_u','wspd_u','p_u','z_boom_u',
    # 'rh_i', 't_i','wspd_i','p_i',
            # 'dsr',
            'gps_lat', 'gps_lon', 'gps_alt']
# var_list = ['t_i_'+str(i) for i in range(1,12)]
# var_list = ['batt_v', 't_u',
#             'wspd_u',
#             # 'z_boom_u',
#             't_i_all'
#             ]
# var_list = ['p_u','p_l','p_i']
# var_list = ['rh_l','rh_i','rh_l_cor',]
# var_list = ['t_i','rh_i','p_i','wspd_i','wdir_i','z_boom_u', 'z_boom_l', 'gps_lat','gps_lon','gps_alt']
# var_list = ['gps_geounit']
# var_list = ['t_u', 't_l','ts']
# var_list = ['gps_lat', 'gps_lon','gps_alt']

# station_list = df_meta.stid#
station_list = ['NUK_L']

# plt.close('all')

for station in station_list:
    print(station)
    if 'level_3' in path_l3:
        df_l3 = pd.read_csv(path_l3+station+'/'+station+'_hour.csv')
    else:
        df_l3 = pd.read_csv(path_l3+station+'/'+station+'_10min.csv')
    df_l3.time = pd.to_datetime(df_l3.time, utc=True)
    df_l3 = df_l3.set_index('time')
    if station not in ['NUK_N', 'QAS_A','TAS_U', 'ZAK_L']:
        df_tx = pd.read_csv(path_tx+station+'/'+station+'_hour.csv')
        df_tx.time = pd.to_datetime(df_tx.time, utc=True)
        df_tx = df_tx.set_index('time')
    else:
        df_tx = pd.DataFrame()
    # try:
    #     df_l3 = df_l3.loc['2023':'2024']
    #     df_tx = df_tx.loc['2023':'2024']
    # except:
    #     print('No data for 2023-2024')
    #     continue
    var_list_list = [var_list[i:i+6] for i in range(0, len(var_list),6)]
    for k, var_list in enumerate(var_list_list):
        fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(13,13))
        if len(var_list)==1:
            ax_list = [ax_list]
    
        for var, ax in zip(var_list, ax_list):
            if (var not in df_l3.columns) & (var not in df_tx.columns):
                print(var, 'not in L3 or tx data at', station)
                if len(var_list) == 1:
                    plt.close(fig)

            print(var)

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

            ax.legend(loc='center right', bbox_to_anchor=(1.13, 0.5))
            ax.grid()
                # ax.plot(df_l3[var].index,Y_pred)
                # ax.plot(df_l3[var].index,Y_pred*0, 'k', ls=':')
                # print(station, Y_pred[-1] - Y[~np.isnan(X+Y)][0])
            
        plt.suptitle('%s %i/%i'%(station, k+1, len(var_list_list)))
        fig.savefig('figures/'+station+'_'+str( k+1)+'.png',dpi=300)

