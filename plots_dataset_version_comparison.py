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
old_version = 'aws-l3'

if old_version == 'aws-l3':
    path_old = '../aws-l3/level_3/'
else:
    path_old = 'C:/Users/bav/Downloads/V17/hour'

if 'dev' in new_version:
    path_l3 = '../aws-l3/level_3/'
    path_l3 = 'C:/Users/bav/GitHub/PROMICE data/aws-l3-dev/level_3/'
    df_meta = pd.read_csv(path_l3+'../AWS_latest_locations.csv')

else:
    path_l3 = '../aws-l3/'
    df_meta = pd.read_csv(path_l3+'/AWS_latest_locations.csv')
    # path_l3 = '../aws-l3/level_3/'
    # path_l3 = 'C:/Users/bav/Downloads/V15/hour/'
    path_l3 = 'https://thredds.geus.dk/thredds/fileServer/aws_l3_station_csv/level_3/'
    # path_l3 = 'https://thredds.geus.dk/thredds/fileServer/aws_l3_time_csv/level_3/hour/'
    # path_l3 = 'https://thredds.geus.dk/thredds/dodsC/aws_l3_time_netcdf/level_3/hour/'
    
from datetime import date
today = date.today().strftime("%Y%m%d")
    
filename = 'plot_compilations/'+old_version+'_versus_'+new_version+'_'+today+'.md'
figure_folder='figures/'+old_version+'_versus_'+new_version+'_'+today
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


#%%
from pypromice.process import getVars, getMeta, addMeta, getColNames, \
    roundValues, resampleL3, writeAll
import xarray as xr
# for station in ['FRE']: #
for station in df_meta.stid:
    Msg('## '+station)
    file = path_l3+station+'_hour.csv'
    try:
        df_new = pd.read_csv(file, index_col=0, parse_dates=True)
    except:
        file = path_l3+station+'/'+station+'_hour.csv'
        try:
            df_new = pd.read_csv(file, index_col=0, parse_dates=True)
        except:
            file = path_l3+station+'/'+station+'_10min.csv'
            df_new = pd.read_csv(file, index_col=0, parse_dates=True)
        
    # df_new = pd.read_csv('../aws-l3/'+station+'_hour.csv', index_col=0, parse_dates=True)
    # df_new = pd.read_csv(
    #     'https://thredds.geus.dk/thredds/fileServer/aws_l3_station_csv/level_3/'+station+'/'+station+'_hour.csv', 
    #     index_col=0, parse_dates=True)
    
    if not os.path.isfile(path_old+'/'+station+'_hour.csv'):
        Msg(path_old+'/'+station+'_hour.csv cannot be found in old data')
        # continue
    file = path_old+station+'/'+station+'_hour.csv'

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
    # var_list_list = [['gps_lat','gps_lon','gps_alt'],
    #                  ['dlr','ulr','t_rad'],
    #                  ['rh_u','rh_l','rh_u_cor','rh_l_cor']]
    
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
                continue
        
            ax.plot(df_new[var].index, df_new[var].values, 
                    marker='.',markeredgecolor='None', linestyle='None', 
                    label=new_version, alpha=0.7,
                    color='tab:orange')            
            ax.legend()
            ax.grid()
            
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
