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
import os
# import matplotlib
# matplotlib.use('Agg')
import tocgen

new_version = 'aws-l3-dev'
# new_version = 'level_3_sites'
# new_version = 'level_2_stations'
old_version = 'V19'

if old_version == 'aws-l3':
    path_old = '../aws-l3/level_3/'
else:
    path_old = 'C:/Users/bav/Downloads/'+old_version+'/hour/'

if 'thredds' in new_version:
    path_new = 'C:/Users/bav/GitHub/PROMICE data/thredds-dev/level_3_sites/'
    df_meta = pd.read_csv(path_new+'../AWS_latest_locations.csv')
    df_meta2 = pd.read_csv(path_new+'../AWS_stations_metadata.csv')
elif 'dev' in new_version:
    path_new = 'C:/Users/bav/GitHub/PROMICE data/aws-l3-dev/stations/'
    df_meta = pd.read_csv(path_new+'../AWS_latest_locations.csv')
    df_meta2 = pd.read_csv(path_new+'../AWS_stations_metadata.csv')

elif 'level_3' in new_version:
    path_new = 'C:/Users/bav/GitHub/PROMICE data/thredds/level_3_sites/csv/hour/'
    df_meta = pd.read_csv('C:/Users/bav/GitHub/PROMICE data/thredds/metadata/AWS_sites_metadata.csv')
elif 'level_2' in new_version:
    path_new = 'C:/Users/bav/GitHub/PROMICE data/thredds/level_2_stations/csv/hour/'
    df_meta = pd.read_csv('C:/Users/bav/GitHub/PROMICE data/thredds/metadata/AWS_stations_metadata.csv')

else:
    path_new = '../aws-l3/'
    df_meta = pd.read_csv(path_new+'/AWS_latest_locations.csv')
    df_meta2 = pd.read_csv(path_new+'/AWS_metadata.csv')
    path_new = '../aws-l3/level_3/'
    # path_new = 'C:/Users/bav/Downloads/V15/hour/'
    # path_new = 'https://thredds.geus.dk/thredds/fileServer/aws_l3_station_csv/level_3/'
    # path_new = 'https://thredds.geus.dk/thredds/fileServer/aws_l3_time_csv/level_3/hour/'
    # path_new = 'https://thredds.geus.dk/thredds/dodsC/aws_l3_time_netcdf/level_3/hour/'

from datetime import date
today = date.today().strftime("%Y%m%d")

filename = 'plot_compilations/'+old_version+'_versus_'+new_version+'.md' #'_'+today+'.md'
figure_folder='figures/'+old_version+'_versus_'+new_version #+'_'+today
try:
    os.mkdir(figure_folder)
except:
    pass

f = open(filename, "w")
def Msg(txt):
    f = open(filename, "a")
    print(txt)
    f.write(txt + "\n")

Msg('# Comparison of data '+new_version+' to '+old_version+' (old).')

plt.close('all')

#%%
import toml
import xarray as xr
import numpy as np
# plt.close('all')
# for station in ['QAS_L']: #
for station in np.unique(df_meta.stid):
    Msg('## '+station)
    # if path_new == 'aws-l3-dev':
    #     config_path = '../aws-l0/metadata/station_configurations/'+station+'.toml'
    #     with open(config_path, 'r') as file:
    #         data = toml.load(file)  # Load the TOML file
    #     station_save=station
    #     station = data.get("station_site")  # Get the station site

    file = path_new+station+'_hour.csv'
    try:
        df_new = pd.read_csv(file, index_col=0, parse_dates=True)
    except:
        file = path_new+station+'/'+station+'_hour.csv'
        if os.path.isfile(file):
            df_new = pd.read_csv(file, index_col=0, parse_dates=True)
        else:
            Msg('No new file for this station')
            continue

    # df_new = pd.read_csv('../aws-l3/'+station+'_hour.csv', index_col=0, parse_dates=True)
    # df_new = pd.read_csv(
    #     'https://thredds.geus.dk/thredds/fileServer/aws_l3_station_csv/level_3/'+station+'/'+station+'_hour.csv',
    #     index_col=0, parse_dates=True)

    # if not os.path.isfile(path_old+'/'+station+'_hour.csv'):
    #     Msg(path_old+'/'+station+'_hour.csv cannot be found in old data')
    #     continue
    # if path_l3 == 'aws-l3-dev':
    #     station = station_save

    df_old = pd.DataFrame()
    df_old['time'] = df_new.index.values

    file = path_old+station+'/'+station+'_hour.csv'
    if not os.path.isfile(file):
        file = path_old+station+'_hour.csv'
        if not os.path.isfile(file):
            Msg('cannot find old file for '+station)

    if os.path.isfile(file):
        print(file)
        df_old = pd.read_csv(file)

    df_old.time = pd.to_datetime(df_old.time, utc=True)
    df_old = df_old.set_index('time')

    Msg('Variables in new file:\n'+ ', '.join(df_new.columns.values))
    Msg('\nNew variables not in old files:\n'+ ', '.join(
        [v for v in df_new.columns if v not in df_old.columns]
        ))
    Msg('\nOld variables removed from new files:\n'+ ', '.join(
        [v for v in df_old.columns if v not in df_new.columns]
        ))
    Msg(' ')
    var_list = df_new.columns.values
    var_list_list = [var_list[i:i+5] for i in range(0, len(var_list), 5)]
    # var_list_list = [ ['gps_lat','gps_lon','gps_alt']]
    # var_list_list = [
    #     # ['t_i','p_i','rh_i_cor'],
    #                     ['tilt_x','tilt_y','z_boom_u'],
    #                    ['dlr','ulr','t_rad','dsr','usr'],
    #                     # ['rh_u','rh_l','rh_u_cor','rh_l_cor'],
    #                    # ['t_u','t_l', 'p_u','p_l'],
    #                    ]
    # df_old = df_old.loc['2024-02-01':'2024-05-01',:]
    # df_new = df_new.loc['2024-02-01':'2024-05-01',:]
    for k, var_list in enumerate(var_list_list):
        fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(13,13))
        if len(var_list)==1:
            ax_list = [ax_list]

        for var, ax in zip(var_list, ax_list):
            ax.set_ylabel(var)

            try:
                ax.plot(df_old[var].index, df_old[var].values,
                        marker='^',linestyle='None', label=old_version,
                        alpha=0.7, color='tab:blue')
            except:
                print(var,'not in old data')


            try:
                ax.plot(df_new[var].index, df_new[var].values,
                        marker='.',markeredgecolor='None', linestyle='None',
                        label=new_version, alpha=0.7,
                        color='tab:orange')
            except:
                print(var,'not in new data')
            ax.legend(loc='lower left')
            ax.grid()
            # ax.set_xlim('2024-02-01','2024-05-01')

        plt.suptitle('%s %i/%i'%(station, k+1, len(var_list_list)))
        fig.savefig(figure_folder+'/%s_%i.png'%(station,k), dpi =120)
        Msg('![%s](../%s/%s_%i.png)'%(station, figure_folder, station,k))
    Msg(' ')
tocgen.processFile(filename, filename[:-3]+"_toc.md")
f.close()
# os.remove(filename)
# os.rename(filename[:-3]+"_toc.md", filename)

# if __name__ == '__main__':
#     main()
# %% scatter version

figure_folder='figures/'+old_version+'_versus_'+new_version +'_scatter'
filename = 'plot_compilations/'+old_version+'_versus_'+new_version+'_scatter.md' #'_'+today+'.md'

try:
    os.mkdir(figure_folder)
except:
    pass

f = open(filename, "w")
def Msg(txt):
    f = open(filename, "a")
    print(txt)
    f.write(txt + "\n")
import xarray as xr
import numpy as np
# for station in ['NAE']: #
for station in np.unique(pd.concat((df_meta.stid,df_meta2.station_id))):
    Msg('## '+station)
    file = path_new+station+'_hour.csv'
    try:
        df_new = pd.read_csv(file, index_col=0, parse_dates=True)
    except:
        file = path_new+station+'/'+station+'_hour.csv'
        if os.path.isfile(file):
            df_new = pd.read_csv(file, index_col=0, parse_dates=True)
        else:
            Msg('No new file for this station')
            continue

    try:
        file = path_old+station+'/'+station+'_hour.csv'
        df_old = pd.read_csv(file)
    except:
        file = path_old+station+'_hour.csv'
        if os.path.isfile(file):
            df_old = pd.read_csv(file, index_col=0, parse_dates=True)
        else:
            Msg('No old file for this station')
            continue

    Msg('Variables in new file:\n'+ ', '.join(df_new.columns.values))
    Msg('\nNew variables not in old files:\n'+ ', '.join(
        [v for v in df_new.columns if v not in df_old.columns]
        ))
    Msg('\nOld variables removed from new files:\n'+ ', '.join(
        [v for v in df_old.columns if v not in df_new.columns]
        ))
    Msg(' ')
    var_list = df_new.columns.intersection(df_old.columns)
    var_list = [v for v in var_list if df_new[v].notnull().any() and df_old[v].notnull().any()]
    var_list_list = [var_list[i:i+9] for i in range(0, len(var_list), 9)]
    # var_list_list = [['gps_lat','gps_lon','gps_alt'],
    #                  ['dlr','ulr','t_rad'],
    #                  ['rh_u','rh_l','rh_u_cor','rh_l_cor']]

    for k, var_list in enumerate(var_list_list):
        fig, ax_list = plt.subplots(3,3, figsize=(15,15))
        ax_list = ax_list.flatten()

        if len(var_list)==1:
            fig, ax_list = plt.subplots(1,1, figsize=(15,15))
            ax_list = [ax_list]

        for var, ax in zip(var_list, ax_list):
            ax.set_xlabel(var +' old')
            ax.set_ylabel(var +' new')

            try:
                msk = df_old[var].index.intersection(df_new[var].index)
                ax.plot(df_old.loc[msk, var].values, df_new.loc[msk,var].values,
                    marker='.',markeredgecolor='None', linestyle='None',
                    label='_nolegend_',  alpha=0.7, c='k')
            except:
                print('error',var)
            ax.grid()

        plt.suptitle('%s %i/%i'%(station, k+1, len(var_list_list)))
        fig.savefig(figure_folder+'/%s_%i.png'%(station,k), dpi =120)
        Msg('![%s](../%s/%s_%i.png)'%(station, figure_folder, station,k))
    Msg(' ')
tocgen.processFile(filename, filename[:-3]+"_toc.md")
f.close()
