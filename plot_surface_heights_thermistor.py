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
data_type = 'sites'
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
# for station in ['KAN_M']:
    Msg('## '+station)
    if not os.path.isfile(path_new+station+'/'+station+'_day.csv'):
        continue
    df_new = pd.read_csv(path_new+station+'/'+station+'_day.csv')
    df_new.time = pd.to_datetime(df_new.time, utc=True)
    df_new = df_new.set_index('time')
    
    fig, ax_list = plt.subplots(4,1,sharex=True, figsize=(10,15))
    plt.subplots_adjust(right=0.75,left=0.08,hspace=0.02)

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
            else:
                print(var,'all nan')
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
        if i > 1:
            ax_list[i].legend(loc='center left', bbox_to_anchor=(1, 0.5),ncols=2)  

    ax_list[2].set_ylabel('Depth (m)')       
    ax_list[2].invert_yaxis()
    ax_list[3].set_ylabel('Temperature (°C)')
    ax_list[0].set_title(station)
    fig.savefig('figures/surface_height/%s/%s.png'%(data_type, station), dpi=300)
    Msg('![%s](../figures/surface_height/%s/%s.png)'%(station,data_type, station))
    Msg(' ')
tocgen.processFile(filename, filename[:-3]+"_toc.md")
f.close()

# %% 

import matplotlib.pyplot as plt
import pandas as pd
import os
import tocgen

# def main(
data_type = 'sites'
path_new = '../aws-l3-dev/'+data_type+'/'
filename = 'plot_compilations/surface_height_'+data_type+'.md'
df_meta = pd.read_csv(path_new+'../AWS_'+data_type+'_metadata.csv')
df_meta = df_meta.set_index(data_type[:-1]+'_id')


plt.close('all')

region_list = ['KAN', 'UPE','THU','KPC','SCO','TAS','QAS','NUK']
station_list_list = [[v for v in df_meta.index if st in v] for st in region_list]
station_list_list = station_list_list+[['SWC','JAR']]

fig, ax_list = plt.subplots(5, 3, figsize=(10, 15))
ax_list = ax_list.flatten()
plt.subplots_adjust(right=0.7, left=0.08, hspace=0.02, wspace=0.3)

# Make the last two panels (11th and 12th) invisible
for ax in ax_list[10:]:
    ax.set_visible(False)

# Create the upper 9 panels and share x-axis and ticks
for i, station_list in enumerate(station_list_list[:9]):  # Limit to the first 9 panels
    for station in station_list:
        if station in ['KAN_B', 'NUK_K']:
            continue
        print('## ' + station)
        if not os.path.isfile(path_new + station + '/' + station + '_day.csv'):
            continue
        df_new = pd.read_csv(path_new + station + '/' + station + '_day.csv')
        df_new.time = pd.to_datetime(df_new.time, utc=True)
        df_new = df_new.set_index('time')

        var_list = [v for v in ['z_surf_combined'] if v in df_new.columns]
        for var in var_list:
            if var in df_new.columns:
                if not df_new[var].isnull().all():
                    ax_list[i].plot(df_new.index, df_new[var].values,
                                    marker='.', markeredgecolor='None', linestyle='None',
                                    alpha=0.5, label=station)
                else:
                    print(var, 'all nan')
    ax_list[i].legend(loc='lower left')
    ax_list[i].grid(True)
    ax_list[i].tick_params(axis='x', rotation=45)
    if i <6:
        ax_list[i].set_xticklabels([])
        


    ax_list[i].set_ylim(-100,20)
    ax_list[i].set_xlim(pd.to_datetime('1995'),
                pd.to_datetime('2025'))

# Combine the 10th panel across the 11th and 12th positions
gs = ax_list[9].get_gridspec()
ax_list[9].remove()  # Remove the 10th panel from its current spot
ax_large = fig.add_subplot(gs[4, :])  # Create a large subplot spanning 11th and 12th positions

# Plot data for the 10th panel (adjust this depending on the correct station_list)

for station in ['DY2', 'NAU','CEN','TUN',
                                       'NAE','NSE','SDL','SDM']:
    if station in ['KAN_B', 'NUK_K']:
        continue
    if not os.path.isfile(path_new + station + '/' + station + '_day.csv'):
        continue
    df_new = pd.read_csv(path_new + station + '/' + station + '_day.csv')
    df_new.time = pd.to_datetime(df_new.time, utc=True)
    df_new = df_new.set_index('time')

    var_list = [v for v in ['z_surf_combined'] if v in df_new.columns]
    for var in var_list:
        if var in df_new.columns and not df_new[var].isnull().all():
            ax_large.plot(df_new.index, df_new[var].values,
                          marker='.', markeredgecolor='None', linestyle='None',
                          alpha=0.5, label=station)

ax_large.legend(loc='lower center',ncols=3, bbox_to_anchor=(0.5, 1.05))
ax_large.grid(True)
ax_large.tick_params(axis='x', rotation=45)

# Common ylabel for all panels
for ax in ax_list[:10]:
    ax.set_ylabel('')
fig.supylabel('Surface height relative to installation (m)')

# Save the figure
fig.savefig('figures/surface_height/overview.png', dpi=300)