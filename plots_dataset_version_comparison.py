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
import matplotlib
matplotlib.use('Agg')
import tocgen

new_version = 'aws-l3-dev'
# new_version = 'thredds'
# new_version = 'level_2_stations'
old_version = 'V27'

res = 'month'
if old_version == 'aws-l3':
    path_old = '../aws-l3/level_3/'
else:
    path_old = f'C:/Users/bav/Downloads/{old_version}/{res}/'

if 'thredds' in new_version:
    path_new = f'../thredds-data/level_3_sites/csv/{res}/'
    df_meta = pd.read_csv('../thredds-data/metadata/AWS_sites_metadata.csv')
    df_meta2 = pd.read_csv('../thredds-data/metadata/AWS_stations_metadata.csv')
elif 'dev' in new_version:
    path_new = f'../aws-l3-dev/csv/{res}/'
    df_meta = pd.read_csv('../thredds-data/metadata/AWS_sites_metadata.csv')

else:
    path_new = '../aws-l3/'
    df_meta = pd.read_csv(path_new+'/AWS_latest_locations.csv')
    df_meta2 = pd.read_csv(path_new+'/AWS_metadata.csv')
    path_new = '../aws-l3/level_3/'

from datetime import date
today = date.today().strftime("%Y%m%d")

filename = f'plot_compilations/{old_version}_versus_{new_version}_{res}.md'
figure_folder=f'figures/{old_version}_versus_{new_version}_{res}'
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
# for station in ['DY2']: #
# for station in np.unique(df_meta.station_id):
for station in np.unique(df_meta.site_id):
    Msg('## '+station)
    # if path_new == 'aws-l3-dev':
    #     config_path = '../aws-l0/metadata/station_configurations/'+station+'.toml'
    #     with open(config_path, 'r') as file:
    #         data = toml.load(file)  # Load the TOML file
    #     station_save=station
    #     station = data.get("station_site")  # Get the station site

    if station in ['UWN','ORO','NUK_P']:
        continue

    file = f'{path_new}{station}_{res}.csv'
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

    file = f'{path_old}{station}_{res}.csv'
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
                        # ['dsr','usr','dsr_cor','usr_cor','albedo','tilt_x','tilt_y','cc'],
    #                     # ['rh_u','rh_l','rh_u_cor','rh_l_cor'],
    #                    # ['t_u','t_l', 'p_u','p_l'],
                        # ]
    df_old = df_old.loc['2020-02-01':'2025-08-01',:]
    df_new = df_new.loc['2020-02-01':'2025-08-01',:]
    for k, var_list in enumerate(var_list_list):
        fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(13,13))
        if len(var_list)==1:
            ax_list = [ax_list]

        for var, ax in zip(var_list, ax_list):
            ax.set_ylabel(var)

            if var in df_old.columns:
                ax.plot(df_old[var].index, df_old[var].values,
                        marker='^',linestyle='None', label=old_version,
                        alpha=0.7, color='tab:blue')
            else:
                print(var,'not in old data')


            if var in df_new.columns:
                ax.plot(df_new[var].index, df_new[var].values,
                        marker='.',markeredgecolor='None', linestyle='None',
                        label=new_version, alpha=0.7,
                        color='tab:orange')
            else:
                print(var,'not in new data')
            ax.legend(loc='lower left')
            ax.grid()
            # ax.set_xlim(pd.to_datetime(['2022-02-01','2025-04-03']))

        plt.suptitle(f'{station} {k+1}/{len(var_list_list)}')
        fig.savefig(figure_folder+'/%s_%i.png'%(station,k), dpi =120)
        plt.close(fig)
        Msg(f'![{station}](../{figure_folder}/{station}_{res}_{k}.png)')
    Msg(' ')
tocgen.processFile(filename, filename[:-3]+"_toc.md")
f.close()
# os.remove(filename)
# os.rename(filename[:-3]+"_toc.md", filename)

# if __name__ == '__main__':
#     main()
