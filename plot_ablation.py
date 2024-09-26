# -*- coding: utf-8 -*-
"""
Created on %(date)s
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
import matplotlib.dates as mdates
from datetime import datetime
matplotlib.use('Agg')
import tocgen
import numpy as np

# Initialize
data_type = 'sites'
path_new = '../aws-l3-dev/' + data_type + '/'
filename = 'plot_compilations/ablation_' + data_type + '.md'
df_meta = pd.read_csv(path_new + '../AWS_' + data_type + '_metadata.csv')
df_meta = df_meta.set_index(data_type[:-1] + '_id')
f = open(filename, "w")

def Msg(txt):
    with open(filename, "a") as f:
        print(txt)
        f.write(txt + "\n")

plt.close('all')

# Loop over each station
for station in df_meta.index:
# for station in ['QAS_M']:
    Msg('## ' + station)
    
    # Check if the file exists
    if not os.path.isfile(path_new + station + '/' + station + '_day.csv'):
        continue
    
    # Read the station data
    df_new = pd.read_csv(path_new + station + '/' + station + '_day.csv')
    if df_new.loc[df_new.z_surf_combined.last_valid_index(), 'z_surf_combined'] >0:
        Msg('accumulation site')
        continue
    df_new.time = pd.to_datetime(df_new.time)
    df_new = df_new.set_index('time')
    
    # Create a figure with two panels
    fig, ax_list = plt.subplots(2, 1, sharex=False, figsize=(10, 10))
    plt.subplots_adjust(right=0.75, left=0.08, hspace=0.15)
    
    # Top panel: z_surf_combined
    if 'z_surf_combined' in df_new.columns and not df_new['z_surf_combined'].isnull().all():
        ax_list[0].plot(df_new.index, df_new['z_surf_combined'], 
                         marker='.', markeredgecolor='None', linestyle='None', label='z_surf_combined')
        ax_list[0].set_ylabel('Surface Height (m)')
        ax_list[0].set_title(station)
        ax_list[0].grid()
        ax_list[0].legend(loc='center left', bbox_to_anchor=(1, 0.5))
        
        # caluclating ice surface
        df_new['z_ice_surf'] = df_new['z_surf_combined'].cummin()
        
        # removing years with too many NaNs
        mask = df_new[df_new.index.month.isin([6, 7, 8])]['z_surf_combined'].isnull().resample('Y').sum().to_frame()
        for index, count in mask.iterrows():
            if count.iloc[0]>15:
                df_new.loc[str(index.year), 'z_ice_surf'] = np.NaN
                
        # Bottom panel: z_ice_surface as function of day of year
        for year in df_new.index.year.unique():
            # Filter data for the year range September to August Y
            start_date = pd.Timestamp(f'{year}-04-01')
            end_date = pd.Timestamp(f'{year}-10-31')
            df_year = df_new.loc[(df_new.index >= start_date) & (df_new.index < end_date), :].copy()
            
            # Calculate the day of the year
            df_year['day_of_year'] = df_year.index.dayofyear.values
            # df_year.loc[df_year['day_of_year'] < 0, 'day_of_year'] = 365 + df_year.loc[df_year['day_of_year'] < 0, 'day_of_year']

            # Plot z_surf_combined adjusted by first valid value
            if df_year['z_surf_combined'].notnull().any():
                first_valid_value = df_year['z_ice_surf'].loc[
                    slice(df_year['z_ice_surf'].first_valid_index(), 
                          df_year['z_ice_surf'].first_valid_index()+pd.to_timedelta('10 days'))].mean()
                if year == 2024:
                    ax_list[1].plot(df_year['day_of_year'], 
                                     df_year['z_ice_surf'] - first_valid_value, 
                                     label='_no_legend_', linestyle='-', color='w',lw=10, alpha=0.7)
                    ax_list[1].plot(df_year['day_of_year'], 
                                     df_year['z_ice_surf'] - first_valid_value, 
                                     label=str(year), linestyle='-', color='k',lw=4)
                else:
                    ax_list[1].plot(df_year['day_of_year'], 
                                     df_year['z_ice_surf'] - first_valid_value, 
                                     label=str(year), linestyle='-')
        
        # Set x-axis limits
        
        # Major ticks and labels every 30 days
        labels = []
        tick_positions = []
        for i in np.cumsum(np.array([30, 31, 30, 31, 31, 29, 31, 30, 31, 30, 31, 31])):
            tick_positions.append(i)
            # Determine the corresponding month and year for the label
            month_label = ''
            if i < 30: month_label = 'Jan.'
            elif i < 60: month_label = 'Feb.'
            elif i < 90: month_label = 'Mar.'
            elif i < 120: month_label = 'Apr.'
            elif i < 150: month_label = 'May'
            elif i < 180: month_label = 'Jun.'
            elif i < 210: month_label = 'Jul.'
            elif i < 240: month_label = 'Aug.'
            elif i < 270: month_label = 'Sept.'
            elif i < 300: month_label = 'Oct.'
            elif i < 330: month_label = 'Nov.'
            elif i < 360: month_label = 'Dec.'
            labels.append(month_label)
        
        ax_list[1].set_xticks(tick_positions)
        ax_list[1].set_xticklabels(labels, rotation=45, ha='right')
        ax_list[1].set_xlim(150, 290)  

        
        ax_list[1].set_ylabel('Snow Height (m)')
        ax_list[1].grid()
        ax_list[1].legend(title='Year', loc='center left', bbox_to_anchor=(1, 0.5), ncol=1)
    
    # Save the figure
    fig.savefig('figures/snow_height/%s/%s_ice_surface.png' % (data_type, station), dpi=300)
    Msg(f'![{station}](../figures/snow_height/{data_type}/{station}_ice_surface.png)')
    Msg(' ')

tocgen.processFile(filename, filename[:-3] + "_toc.md")
f.close()
