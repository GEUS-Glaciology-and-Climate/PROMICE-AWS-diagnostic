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
from pypromice.process import AWS
import os
import matplotlib
matplotlib.use('Agg')
import tocgen

# def main(
path_new = '../aws-l3/level_3/'
path_old = 'C:/Users/bav/Downloads/dataverse_files/day'
filename = 'plot_compilations/new_version_to_dataverse_2023_08_17.md'
df_meta = pd.read_csv(path_new+'../AWS_latest_locations.csv')

f = open(filename, "w")
def Msg(txt):
    f = open(filename, "a")
    print(txt)
    f.write(txt + "\n")
    
Msg('# Comparison of data v9 (new) to v8 (old).')
Msg('~version name is as defined in AWS_changelog.txt~')

for station in df_meta.stid:
    Msg('## '+station)
    df_new = pd.read_csv(path_new+station+'/'+station+'_day.csv')
    df_new.time = pd.to_datetime(df_new.time, utc=True)
    df_new = df_new.set_index('time')
    
    if not os.path.isfile(path_old+'/'+station+'_day.csv'):
        Msg(path_old+'/'+station+'_day.csv cannot be found in old data')
        continue
    df_old = pd.read_csv(path_old+'/'+station+'_day.csv')
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
    
    for k, var_list in enumerate(var_list_list):
        fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(13,13))
        if len(var_list)==1:
            ax_list = [ax_list]
    
        for var, ax in zip(var_list, ax_list):
            ax.set_ylabel(var)

            try:
                ax.plot(df_old[var].index, df_old[var].values,
                        marker='^',linestyle='None', label='Old',
                        alpha=0.7, color='tab:blue')
            except:
                print(var,'not in old data')
        
            ax.plot(df_new[var].index, df_new[var].values, 
                    marker='.',markeredgecolor='None', linestyle='None', 
                    label='New',alpha=0.7,
                    color='tab:orange')            
            ax.legend()
            ax.grid()
            
        plt.suptitle('%s %i/%i'%(station, k+1, len(var_list_list)))
        fig.savefig('figures/new_dataverse_upload/%s_%i.png'%(station,k))
        Msg('![%s](../figures/flags/%s_%i.png)'%(station, station,k))
    Msg(' ')
tocgen.processFile(filename, filename[:-3]+"_toc.md")
f.close()
# os.remove(filename)
# os.rename(filename[:-3]+"_toc.md", filename)

# if __name__ == '__main__':
#     main()
