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
data_type = 'stations'
path_new = '../aws-l3-dev/'+data_type+'/'
filename = 'plot_compilations/surface_height_'+data_type+'.md'
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
    Msg('## '+station)
    if not os.path.isfile(path_new+station+'/'+station+'_hour.csv'):
        continue
    df_new = pd.read_csv(path_new+station+'/'+station+'_hour.csv')
    df_new.time = pd.to_datetime(df_new.time, utc=True)
    df_new = df_new.set_index('time')
    

    fig, ax_list = plt.subplots(3,1,sharex=True, figsize=(12,8))
    plt.subplots_adjust(right=0.75,left=0.08)

    var_list = [v for v in ['z_boom_u','z_boom_l','z_stake','z_pt_cor'] \
                      if v in df_new.columns]
    for var in var_list:
        if var in df_new.columns:
            if not df_new[var].isnull().all():                
                ax_list[0].plot(df_new.index, df_new[var].values, 
                        marker='.',markeredgecolor='None', linestyle='None', 
                        label=var)  
                
    var_list = [v for v in ['z_surf_combined','z_ice_surf','snow_height'] \
                      if v in df_new.columns]       
    for var in var_list:
        if var in df_new.columns:
            if not df_new[var].isnull().all():                
                ax_list[1].plot(df_new.index, df_new[var].values, 
                        marker='.',markeredgecolor='None', linestyle='None', 
                       label=var)  
    var_list = ['d_t_i_'+str(i) for i in range(1,12) \
                      if 'd_t_i_'+str(i) in df_new.columns]       
    for var in var_list:
        if var in df_new.columns:
            if not df_new[var].isnull().all():                
                ax_list[2].plot(df_new.index, df_new[var].values, 
                        marker='.',markeredgecolor='None', linestyle='None', 
                       label=var)  
                
    for i in range(3):
        ax_list[i].set_ylabel('Height (m)')       
        ax_list[i].grid()
        ax_list[i].legend(loc='center left', bbox_to_anchor=(1, 0.5))        
    ax_list[i].set_ylabel('Depth (m)')       
    ax_list[i].invert_yaxis()

    plt.suptitle(station)
    fig.savefig('figures/surface_height/%s/%s.png'%(data_type, station), dpi=300)
    Msg('![%s](../figures/surface_height/%s/%s.png)'%(station,data_type, station))
    df_m = pd.read_csv(path_new+station+'/'+station+'_month.csv')
    df_m.time = pd.to_datetime(df_m.time, utc=True)
    df_m = df_m.set_index('time')
    df_m[[v for v in ['lat','lon','alt'] if v in df_m.columns]].to_csv('figures/GPS/coordinates_'+data_type+'/%s.csv'%station)
    Msg(' ')
tocgen.processFile(filename, filename[:-3]+"_toc.md")
f.close()
