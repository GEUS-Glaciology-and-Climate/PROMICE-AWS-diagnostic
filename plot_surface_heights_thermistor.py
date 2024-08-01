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
# for station in ['EGP']:
    Msg('## '+station)
    if not os.path.isfile(path_new+station+'/'+station+'_hour.csv'):
        continue
    df_new = pd.read_csv(path_new+station+'/'+station+'_hour.csv')
    df_new.time = pd.to_datetime(df_new.time, utc=True)
    df_new = df_new.set_index('time')
    

    fig, ax_list = plt.subplots(4,1,sharex=True, figsize=(10,15))
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
                
    var_list = ['t_i_'+str(i) for i in range(1,12) \
                      if 't_i_'+str(i) in df_new.columns]   
    for var in var_list:
        if var in df_new.columns:
            if not df_new[var].isnull().all():                
                ax_list[3].plot(df_new.index, df_new[var].values, 
                        marker='.',markeredgecolor='None', linestyle='None', 
                       label=var)
    if 't_i_10m' in df_new.columns:
        ax_list[3].plot(df_new.index, df_new['t_i_10m'].values, 
                marker='o',markeredgecolor='None', linestyle='None', 
               label='t_i_10m')  
                
    for i in range(4):
        ax_list[i].set_ylabel('Height (m)')       
        ax_list[i].grid()
        ax_list[i].legend(loc='center left', bbox_to_anchor=(1, 0.5))  
        
    ax_list[2].set_ylabel('Depth (m)')       
    ax_list[2].invert_yaxis()
    ax_list[3].set_ylabel('Temperature (°C)')
    ax_list[0].set_title(station)
    plt.tight_layout()
    fig.savefig('figures/surface_height/%s/%s.png'%(data_type, station), dpi=300)
    Msg('![%s](../figures/surface_height/%s/%s.png)'%(station,data_type, station))
    Msg(' ')
tocgen.processFile(filename, filename[:-3]+"_toc.md")
f.close()
