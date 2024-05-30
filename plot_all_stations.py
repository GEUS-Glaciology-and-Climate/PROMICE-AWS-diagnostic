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
# import matplotlib
# matplotlib.use('Agg')
import tocgen

# def main(
path_new = '../aws-l3/level_3/'
filename = 'plot_compilations/plot_all.md'
df_meta = pd.read_csv(path_new+'../AWS_latest_locations.csv')

f = open(filename, "w")
def Msg(txt):
    f = open(filename, "a")
    print(txt)
    f.write(txt + "\n")

# for station in df_meta.stid:
for station in ['KAN_U']:
    Msg('## '+station)
    df_new = pd.read_csv(path_new+station+'/'+station+'_hour.csv')
    df_new.time = pd.to_datetime(df_new.time, utc=True)
    df_new = df_new.set_index('time')
    df_new=df_new.loc['2024']
    var_list = ['cc','dlr','ulr','dsr','usr','t_u'] #df_new.columns.values
    # var_list = df_new.columns.values
    var_list_list = [var_list[i:i+7] for i in range(0, len(var_list), 7)]
    
    for k, var_list in enumerate(var_list_list):
        fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(13,13))
        if len(var_list)==1:
            ax_list = [ax_list]
        
        for var, ax in zip(var_list, ax_list):
            if var not in df_new.columns:
                Msg('no data for '+var)
                plt.close(fig)
                continue
            if df_new[var].isnull().all():
                Msg('no data for '+var)
                # plt.close(fig)
                # continue
            if var == 'gps_q':
                if len(df_new[var].unique())==1:
                    Msg('only one value for '+var+': '+str(df_new[var].unique()[0]))
                    plt.close(fig)
                    continue
                if len(df_new[var].unique())==2:
                    Msg('only two values for '+var+': '+str(df_new[var].unique()))
                    plt.close(fig)
                    continue
            
            ax.set_ylabel(var)       
            ax.plot(df_new[var].index, df_new[var].values, 
                    marker='o',#markeredgecolor='None', linestyle='None', 
                    # label='',alpha=0.7,
                    color='tab:orange')            
            # ax.legend()
            ax.grid()
        
        no_save = 1
        for ax in ax_list:
            if ax.lines: no_save=0
            if ax.collections: no_save=0
        if no_save == 1:
            continue
        plt.suptitle('%s %i/%i'%(station, k+1, len(var_list_list)))
        fig.savefig('figures/plot_all/%s_%i.png'%(station,k))
        Msg('![%s](../figures/plot_all/%s_%i.png)'%(station, station,k))
    Msg(' ')
# tocgen.processFile(filename, filename[:-3]+"_toc.md")
f.close()
# os.remove(filename)
# os.rename(filename[:-3]+"_toc.md", filename)

# if __name__ == '__main__':
#     main()
