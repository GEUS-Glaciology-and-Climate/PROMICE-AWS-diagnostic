
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
import geopandas as gpd

# def main(
data_type = 'stations'
path_new = '../aws-l3-dev/'+data_type+'/'
filename = 'plot_compilations/RH_'+data_type+'.md'
df_meta = pd.read_csv(path_new+'../AWS_'+data_type+'_metadata.csv')
df_meta = df_meta.set_index(data_type[:-1]+'_id')
f = open(filename, "w")
def Msg(txt):
    f = open(filename, "a")
    print(txt)
    f.write(txt + "\n")
plt.close('all')


for station in df_meta.index:
# for station in ['JAR']:
# for station in np.unique(gnss_df.index):
    # Msg('## '+station)
    if not os.path.isfile(path_new+station+'/'+station+'_day.csv'):
        continue
    df_new = pd.read_csv(path_new+station+'/'+station+'_day.csv')
    df_new.time = pd.to_datetime(df_new.time, utc=True)
    df_new = df_new.set_index('time')

    var_list_list = [['rh_u_wrt_ice_or_water','rh_l_wrt_ice_or_water','rh_i_wrt_ice_or_water']]
    for k, var_list in enumerate(var_list_list):
        fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(12,8))
        plt.subplots_adjust(right=0.75,left=0.08)
        if len(var_list)==1:
            ax_list = [ax_list]

        for var, ax in zip(var_list, ax_list):
            if var in df_new.columns:
                if not df_new[var].isnull().all():
                    ax.plot(df_new.index, df_new[var].values,
                            marker='.',markeredgecolor='None', linestyle='None',
                            color='tab:orange',label=var)


            ax.set_ylabel(var.replace('gps_',''))
            ax.grid()
            ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        no_save = 1
        for ax in ax_list:
            if ax.lines: no_save=0
            if ax.collections: no_save=0
        if no_save == 1:
            continue
        plt.suptitle(station)
        fig.savefig('figures/RH/%s/%s_%i.png'%(data_type, station,k), dpi=300)
        Msg('![%s](../figures/RH/%s/%s_%i.png)'%(station,data_type, station,k))

    # Msg(' ')
tocgen.processFile(filename, filename[:-3]+"_toc.md")
f.close()
