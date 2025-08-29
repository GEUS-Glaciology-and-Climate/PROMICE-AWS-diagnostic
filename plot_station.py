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
# path_l3 = '../aws-l3-dev/sites/'
# path_tx = '../aws-l3/tx/'
path_thredds = '../thredds-data/level_3_sites/csv/hour'
path_gcn= 'C:/Users/bav/GitHub/PROMICE data/GC-Net-Level-1-data-processing/L1/'

# df_meta = pd.read_csv(path_l3+'../AWS_latest_locations.csv')
var_list = [
    # 'gps_geoid']
        # 't_i_'+str(i) for i in range(1,12)
        # 'p_u','p_l','p_i',
        # 't_u','t_l','t_i'
        # 'rh_l','rh_i','rh_l_cor',
        # 't_i','rh_i','p_i','wspd_i','wdir_i',
        # 'z_boom_u', 'z_boom_l', 'gps_lat','gps_lon','gps_alt'
        # 'gps_geounit'
        # 't_u', 't_l','ts'
        # 'gps_lat', 'gps_lon','gps_alt'
        # 'z_surf_combined','z_ice_surf','snow_height','z_pt_cor'
        # 'p_u','t_u','z_surf_combined', 'lat', 'lon'
        # 't_u','z_boom_u','z_stake'
        # 'wspd_u','wspd_l',
        # 'dlr','ulr','cc', 't_u','wspd_u','t_surf'
        # 'dlr','ulr','t_rad', 'dsr_cor','usr_cor', 'dsr','usr','albedo','tilt_x','tilt_y','cc','t_surf'
        ]


# station_list = df_meta.stid
station_list = ['TAS_A']

# plt.close('all')
# gps_info=[]
for station in station_list:
    print(station)
    df_l3 = pd.read_csv(path_thredds+'/'+station+'_hour.csv')

    df_l3.time = pd.to_datetime(df_l3.time, utc=True)
    df_l3 = df_l3.set_index('time')
    df_l3=df_l3.loc['2025':]
    if len(var_list) == 0:
        var_list=df_l3.columns
    var_list = np.array(var_list)
    var_list = var_list[np.isin(var_list, df_l3.columns)]


    var_list_list = [var_list[i:i+6] for i in range(0, len(var_list),6)]
    for k, var_list in enumerate(var_list_list):
        fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(8,8))
        fig.subplots_adjust(top=0.9)
        if len(var_list)==1:
            ax_list = [ax_list]

        for var, ax, var_label in zip(var_list, ax_list, var_list):
            if (var not in df_l3.columns) :
                print(var, 'not in L3 or tx data at', station)
                if len(var_list) == 1:
                    plt.close(fig)

            print(var)

            ax.set_ylabel(var)
            if var.endswith('_i_all'):
                var = [var.replace('_all','')+'_%i'%i for i in range(1,12) if 't_i_%i'%i in df_l3.columns]

                ax.plot(df_l3[var].index, df_l3[var].values,
                        marker='.',markeredgecolor='None',
                        linestyle='None', label=var,alpha=0.7)
            else:

                try:
                    ax.plot(df_l3[var].index, df_l3[var].values, marker='.',
                            color='tab:blue', markeredgecolor='None',
                            linestyle='None')
                except:
                    print(var,'not in L3 files')
            ax.set_ylabel(var_label)
            if var == var_list[0]:
                handles, labels = ax_list[0].get_legend_handles_labels()
                plt.legend(reversed(handles), reversed(labels),
                            loc='upper left', bbox_to_anchor=(0.25, 6.2),
                            ncols=2, scatterpoints=4, markerscale=4)
            ax.grid()
                # ax.plot(df_l3[var].index,Y_pred)
                # ax.plot(df_l3[var].index,Y_pred*0, 'k', ls=':')
                # print(station, Y_pred[-1] - Y[~np.isnan(X+Y)][0])

        plt.suptitle('%s site'%(station))
        fig.savefig('figures/'+station+'_'+str( k+1)+'.png',dpi=300)
