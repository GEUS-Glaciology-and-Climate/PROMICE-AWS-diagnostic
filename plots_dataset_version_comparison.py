# -*- coding: utf-8 -*-
"""
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""
# if the first thing you want to do is downloading the remote data
# from download_ssh import main
# main()

import matplotlib.pyplot as plt
import pandas as pd
import os
import toml
import xarray as xr
import numpy as np
import matplotlib
matplotlib.use('Agg')
import tocgen

new_version = 'aws-l3-dev'
old_version = 'V27'
# %%
# res = 'hour'
for res in ['hour', 'day','month']:
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
    for station in np.unique(df_meta.site_id):
        plt.close('all')
        Msg('## '+station)

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
        # var_list = ['rainfall_u','rainfall_cor_u','rainfall_l','rainfall_cor_l']
        var_list_list = [var_list[i:i+5] for i in range(0, len(var_list), 5)]

        if res == 'month':
            size=8
        else:
            size=6

        for k, var_list in enumerate(var_list_list):
            fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(13,13))
            if len(var_list)==1:
                ax_list = [ax_list]

            for var, ax in zip(var_list, ax_list):
                ax.set_ylabel(var)

                var_old = var.replace('rainfall_cor_u','precip_u_rate').replace('rainfall_cor_l','precip_l_rate')
                var_old = var.replace('rainfall_u','precip_u_cor').replace('rainfall_l','precip_l_cor')

                if var in df_old.columns:
                    ax.plot(df_old[var].index, df_old[var].values,
                            marker='^',linestyle='None', label=old_version,
                            alpha=0.7, markersize=size*1.3, color='tab:blue')
                elif var_old in df_old.columns:
                    ax.plot(df_old[var_old].index,
                            df_old[var_old].values,
                            marker='^',linestyle='None', label=f'{old_version} - old name {var_old}',
                            alpha=0.7, markersize=size*1.3, color='tab:blue')
                else:
                    print(var,'not in old data')


                if var in df_new.columns:
                    ax.plot(df_new[var].index, df_new[var].values,
                            marker='o',markeredgecolor='None', linestyle='None',
                            label=new_version, alpha=0.7,markersize=size,
                            color='tab:orange')
                else:
                    print(var,'not in new data')
                ax.legend(loc='lower left')
                ax.grid()
                # ax.set_xlim(pd.to_datetime(['2022-02-01','2025-04-03']))

            plt.suptitle(f'{station} {k+1}/{len(var_list_list)}')
            fig.savefig(figure_folder+'/%s_%i.png'%(station,k), dpi =120)
            # plt.close(fig)
            Msg(f'![{station}](../{figure_folder}/{station}_{k}.png)')
        Msg(' ')
    tocgen.processFile(filename, filename[:-3]+"_toc.md")
    f.close()
