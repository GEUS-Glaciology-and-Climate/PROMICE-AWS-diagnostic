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
data_type = 'sites'
path_new = '../aws-l3-dev/'+data_type+'/'
filename = 'plot_compilations/GPS_'+data_type+'.md'
df_meta = pd.read_csv(path_new+'../AWS_'+data_type+'_metadata.csv')
df_meta = df_meta.set_index(data_type[:-1]+'_id')
f = open(filename, "w")
def Msg(txt):
    f = open(filename, "a")
    print(txt)
    f.write(txt + "\n")
plt.close('all')
gnss_df = pd.read_csv('ancil/GEUS_GC-Net_precise_locations.csv').set_index(data_type[:-1])
gnss_df['date'] = pd.to_datetime(gnss_df.date,dayfirst=True)
# for station in df_meta.index:
# for station in ['SCO_L']:
for station in np.unique(gnss_df.index):
    Msg('## '+station)
    if not os.path.isfile(path_new+station+'/'+station+'_hour.csv'):
        continue
    df_new = pd.read_csv(path_new+station+'/'+station+'_hour.csv')
    df_new.time = pd.to_datetime(df_new.time, utc=True)
    df_new = df_new.set_index('time')
    
    var_list_list = [['gps_lat','gps_lon','gps_alt']]
    for k, var_list in enumerate(var_list_list):
        fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(8,8))
        if len(var_list)==1:
            ax_list = [ax_list]
        
        for var, ax in zip(var_list, ax_list):
            if var in df_new.columns:
                if not df_new[var].isnull().all():                
                    ax.plot(df_new.index, df_new[var].values, 
                            marker='.',markeredgecolor='None', linestyle='None', 
                            color='tab:orange',label=var)  
            if var.replace('gps_','') in df_new.columns:
                ax.plot(df_new.index, df_new[var.replace('gps_','')].values, 
                        color='tab:green', label=var.replace('gps_',''))
            if var == 'gps_alt':
                ax.plot(gnss_df.loc[station,'date'],
                        gnss_df.loc[station,var.replace('gps_','').replace('alt','orthometric_height_m')],
                        marker='o',ls='None', label='GNSS survey: orthometric height')
                ax.plot(gnss_df.loc[station,'date'],
                        gnss_df.loc[station,var.replace('gps_','').replace('alt','ellipsoid_height_m')], 
                        marker='^',ls='None', color='tab:green', label='GNSS survey: ellipsoid height')
            else:
                ax.plot(gnss_df.loc[station,'date'],
                        gnss_df.loc[station,var.replace('gps_','')],
                        marker='o',ls='None', label='GNSS survey')
            ax.set_ylabel(var.replace('gps_',''))       
            ax.grid()
            ax.legend()        
        no_save = 1
        for ax in ax_list:
            if ax.lines: no_save=0
            if ax.collections: no_save=0
        if no_save == 1:
            continue
        plt.suptitle(station)
        fig.savefig('figures/GPS/%s/%s_%i.png'%(data_type, station,k), dpi=300)
        Msg('![%s](../figures/GPS/%s/%s_%i.png)'%(station,data_type, station,k))
    df_m = pd.read_csv(path_new+station+'/'+station+'_month.csv')
    df_m.time = pd.to_datetime(df_m.time, utc=True)
    df_m = df_m.set_index('time')
    df_m[[v for v in ['lat','lon','alt'] if v in df_m.columns]].to_csv('figures/GPS/coordinates_'+data_type+'/%s.csv'%station)
    Msg(' ')
tocgen.processFile(filename, filename[:-3]+"_toc.md")
f.close()
