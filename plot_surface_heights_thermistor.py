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

# %% Surface height reconstruction + thermistor depth + subsurface temperature
data_type = 'sites'
if data_type == 'sites':
    path_new = '../thredds-data/level_3_sites/csv/day/'
else:
    path_new = '../thredds-data//level_2_stations/csv/day/'

filename = 'plot_compilations/surface_height_'+data_type+'.md'

f = open(filename, "w")
def Msg(txt):
    f = open(filename, "a")
    print(txt)
    f.write(txt + "\n")
# plt.close('all')


for file in os.listdir(path_new):
# for file in ['NUK_L_day.csv']:
    try:
        station = file.replace('_day.csv','')
        Msg('## '+station)
        if not os.path.isfile(path_new+file):
            Msg("cannot find"+path_new+file)
            continue

        df_new = pd.read_csv(path_new+file)
        df_new.time = pd.to_datetime(df_new.time, utc=True)
        df_new = df_new.set_index('time')

        fig, ax_list = plt.subplots(3,1,sharex=True, figsize=(10,15))
        plt.subplots_adjust(right=0.75,left=0.08,hspace=0.02)

        var_list = [v for v in ['z_boom_u','z_boom_l','z_stake','z_pt_cor'] \
                          if v in df_new.columns]
        for var in var_list:
            if var in df_new.columns:
                if not df_new[var].isnull().all():
                    ax_list[0].plot(df_new.index, df_new[var].values,
                            marker='.',markeredgecolor='None', linestyle='None',
                            label=var)

        var_list = [v for v in ['z_surf_combined','z_ice_surf'] \
                          if v in df_new.columns]
        for var in var_list:
            if var in df_new.columns:
                if not df_new[var].isnull().all():
                    ax_list[1].plot(df_new.index, df_new[var].values,
                            marker='.',markeredgecolor='None', linestyle='None',
                           label=var)
                else:
                    print(var,'all nan')
        depth_var = ['d_t_i_'+str(i) for i in range(1,12) \
                          if 'd_t_i_'+str(i) in df_new.columns]
        for var in depth_var:
            if var in df_new.columns:
                if not df_new[var].isnull().all():
                    ax_list[1].plot(df_new.index, -df_new[var].values + df_new.z_surf_combined,

                           label=var)


        var_list = ['t_i_'+str(i) for i in range(1,12) \
                          if 't_i_'+str(i) in df_new.columns]
        for var in var_list:
            if var in df_new.columns:
                if not df_new[var].isnull().all():
                    ax_list[2].plot(df_new.index, df_new[var].values,
                            marker='.',markeredgecolor='None', linestyle='None',
                           label=var)
        if 't_i_10m' in df_new.columns:
            ax_list[2].plot(df_new.index, df_new['t_i_10m'].values,
                    marker='o',color='k',markeredgecolor='None', linestyle='None',
                   label='t_i_10m')

        for i in range(3):
            ax_list[i].set_ylabel('Height (m)')
            ax_list[i].grid()
            ax_list[i].legend(loc='center left', bbox_to_anchor=(1, 0.5))
            if i > 1:
                ax_list[i].legend(loc='center left', bbox_to_anchor=(1, 0.5),ncols=2)

        ax_list[2].set_ylabel('Depth (m)')
        ax_list[2].set_ylabel('Temperature (°C)')
        ax_list[0].set_title(station)

        # xlim1 = df_new.index[0]
        xlim1 = '2022-03-01'
        # xlim2 = df_new.index[-1]
        xlim2 = '2025-07-03'
        ax_list[0].set_xlim(pd.to_datetime([xlim1,xlim2]))
        if len(depth_var)>0:
            ax_list[1].set_ylim(
                               (df_new['z_surf_combined'].min() - df_new.loc[slice(xlim1, xlim2),depth_var].max().max())-0.5,
                                   df_new.loc[slice(xlim1, xlim2), 'z_surf_combined'].max()+0.5
                                   )

        fig.savefig('figures/surface_height/%s/%s.png' % (data_type, station), dpi=300, bbox_inches="tight")
        Msg('![%s](../figures/surface_height/%s/%s.png)'%(station,data_type, station))
        Msg(' ')
    except:
        pass
tocgen.processFile(filename, filename[:-3]+"_toc.md")
f.close()

# %% Surface height overview plot
import matplotlib.pyplot as plt
import pandas as pd
import os

# Define data type and paths
data_type = 'sites'
path_new = '../thredds-data/level_3_sites/csv/day/'
filename = 'plot_compilations/ablation_' + data_type + '.md'
df_meta = pd.read_csv('../thredds-data/metadata/AWS_' + data_type + '_metadata.csv')
df_meta = df_meta.set_index(data_type[:-1] + '_id')

plt.close('all')

region_list = ['KAN', 'UPE', 'THU', 'KPC', 'SCO', 'TAS', 'QAS', 'NUK',]
station_list_list = [[v for v in df_meta.index if st in v] for st in region_list]
region_list = region_list + ['SWC-JAR']
station_list_list = station_list_list + [['SWC', 'JAR']]

fig, ax_list = plt.subplots(4, 3, figsize=(12, 18))  # Increased figure size
ax_list = ax_list.flatten()
plt.subplots_adjust(right=0.7, left=0.15, hspace=0.3, wspace=0.4)  # Increased space
abc = 'abcdefghijklmno'
# Make the last two panels (11th and 12th) invisible
for ax in ax_list[10:]:
    ax.set_visible(False)

# Create the upper 9 panels and share x-axis and ticks
for i, station_list in enumerate(station_list_list[:9]):  # Limit to the first 9 panels
    for station in station_list:
        if station in ['KAN_B', 'NUK_K','NUK_P','NUK_B']:
            continue
        print('## ' + station)
        df_new = pd.read_csv(path_new + '/' + station + '_day.csv')
        df_new.time = pd.to_datetime(df_new.time, utc=True)
        df_new = df_new.set_index('time')

        var_list = [v for v in ['z_surf_combined'] if v in df_new.columns]
        for var in var_list:
            if var in df_new.columns and not df_new[var].isnull().all():
                ax_list[i].plot(df_new.index, df_new[var].values,
                                marker='.', markeredgecolor='None', linestyle='None',
                                alpha=0.7, label=station)

    ax_list[i].legend(loc='lower left', markerscale=2)
    ax_list[i].grid(True)
    ax_list[i].tick_params(axis='x', rotation=45)
    ax_list[i].text(
    0.03, 0.96,  # Adjust these values for fine-tuning position
    abc[i]+') '+region_list[i],
    fontsize=14,
    ha='left',
    va='top',
    transform=ax_list[i].transAxes,
    # bbox=dict(facecolor='white', alpha=0.8, edgecolor='none')  # Optional: add background
)

    if i < 6:
        ax_list[i].set_xticklabels([])
    ax_list[i].set_ylim(-100, 20)
    ax_list[i].set_xlim(pd.to_datetime('1995'), pd.to_datetime('2025-07-01'))

# Combine the 10th panel across the 11th and 12th positions
gs = ax_list[9].get_gridspec()
ax_list[9].remove()  # Remove the 10th panel from its current spot
ax_large = fig.add_subplot(gs[3, :])  # Create a large subplot spanning 11th and 12th positions

for station in ['DY2', 'NAU', 'CEN', 'TUN', 'NAE', 'NSE', 'SDL', 'SDM']:
    if station in ['KAN_B', 'NUK_K']:
        continue
    if not os.path.isfile(path_new + '/' + station + '_day.csv'):
        continue
    df_new = pd.read_csv(path_new + '/' + station + '_day.csv')
    df_new.time = pd.to_datetime(df_new.time, utc=True)
    df_new = df_new.set_index('time')

    var_list = [v for v in ['z_surf_combined'] if v in df_new.columns]
    for var in var_list:
        if var in df_new.columns and not df_new[var].isnull().all():
            ax_large.plot(df_new.index, df_new[var].values,
                          marker='.', markeredgecolor='None', linestyle='None',
                          alpha=0.7, label=station)

ax_large.legend(loc='upper left', ncols=3, bbox_to_anchor=(0, 0.8), markerscale=2)
ax_large.grid(True)
ax_large.tick_params(axis='x', rotation=45)
ax_large.text(
    0.02, 0.96,  # Adjust these values for fine-tuning position
    "j) Accumulation sites",
    fontsize=14,
    ha='left',
    va='top',
    transform=ax_large.transAxes,
    bbox=dict(facecolor='white', alpha=0.85, edgecolor='none')  # Optional: add background
)
ax_large.set_xlim(pd.to_datetime('1995'), pd.to_datetime('2025-07-01'))

for ax in [ax_large, ax_list[0], ax_list[3],]:
    ax.set_ylabel('Surface height relative to installation (m)')

# Save the figure with tight layout to remove excess white space
fig.savefig('figures/surface_height/overview.png', dpi=300, bbox_inches='tight')

# %% Snow height climatology plots
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
if data_type == 'sites':
    path_new = '../thredds-data/level_3_sites/csv/day/'
else:
    path_new = '../thredds-data//level_2_stations/csv/day/'

filename = 'plot_compilations/snow_height_' + data_type + '.md'


f = open(filename, "w")

def Msg(txt):
    with open(filename, "a") as f:
        print(txt)
        f.write(txt + "\n")

plt.close('all')

# Loop over each station
for file in os.listdir(path_new):
# for station in ['DY2']:
    station = file.replace('_day.csv','')

    Msg('## ' + station)

    # Check if the file exists
    if not os.path.isfile(path_new + station + '_day.csv'):
        continue

    # Read the station data
    df_new = pd.read_csv(path_new + station + '_day.csv')
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

    # Bottom panel: snow_height as function of day of year
    if 'snow_height' in df_new.columns and not df_new['snow_height'].isnull().all():
        for year in df_new.index.year.unique().tolist() + [df_new.index.year.max() + 1]:
            # Filter data for the year range September to August Y
            start_date = pd.Timestamp(f'{year-1}-09-01')
            end_date = pd.Timestamp(f'{year}-08-31')
            df_year = df_new.loc[(df_new.index >= start_date) & (df_new.index < end_date), :].copy()

            # Calculate the day of the year
            df_year['day_of_year'] = df_year.index.dayofyear.values - 244
            df_year.loc[df_year['day_of_year'] < 0, 'day_of_year'] = 365 + df_year.loc[df_year['day_of_year'] < 0, 'day_of_year']

            # Plot snow_height adjusted by first valid value
            if df_year['snow_height'].notnull().any():
                first_valid_value = df_year['snow_height'].loc[
                    slice(df_year['snow_height'].first_valid_index(),
                          df_year['snow_height'].first_valid_index()+pd.to_timedelta('30 days'))].min()
                if year == 2025:
                    ax_list[1].plot(df_year['day_of_year'],
                                     df_year['snow_height'] - first_valid_value,
                                     label='_no_legend_', linestyle='-', color='w',lw=6, alpha=0.7)
                    ax_list[1].plot(df_year['day_of_year'],
                                     df_year['snow_height'] - first_valid_value,
                                     label=str(year), linestyle='-', color='k',lw=2)
                else:
                    ax_list[1].plot(df_year['day_of_year'],
                                     df_year['snow_height'] - first_valid_value,
                                     label=str(year), linestyle='-')

        # Set x-axis limits
        ax_list[1].set_xlim(1, 365)  # Adjust for leap years if necessary

        # Major ticks and labels every 30 days
        labels = []
        tick_positions = []
        for i in np.cumsum(np.array([30, 31, 30, 31, 31, 29, 31, 30, 31, 30, 31, 31])):
            tick_positions.append(i)
            # Determine the corresponding month and year for the label
            month_label = ''
            if i < 30: month_label = 'Sept.'
            elif i < 60: month_label = 'Oct.'
            elif i < 90: month_label = 'Nov.'
            elif i < 120: month_label = 'Dec.'
            elif i < 150: month_label = 'Jan.'
            elif i < 180: month_label = 'Feb.'
            elif i < 210: month_label = 'Mar.'
            elif i < 240: month_label = 'Apr.'
            elif i < 270: month_label = 'May'
            elif i < 300: month_label = 'Jun.'
            elif i < 330: month_label = 'Jul.'
            elif i < 360: month_label = 'Aug.'
            labels.append(month_label)

        ax_list[1].set_xticks(tick_positions)
        ax_list[1].set_xticklabels(labels, rotation=45, ha='right')

        # Add vertical line at day 121
        # ax_list[1].axvline(x=121, color='red', linestyle='--', label='Day 121')

        ax_list[1].set_ylabel('Snow Height (m)')
        ax_list[1].grid()
        ax_list[1].legend(title='Year', loc='center left', bbox_to_anchor=(1, 0.5), ncol=1)

    # Save the figure
    fig.savefig('figures/snow_height/%s/%s.png' % (data_type, station), dpi=300)
    Msg(f'![{station}](../figures/snow_height/{data_type}/{station}.png)')
    Msg(' ')

tocgen.processFile(filename, filename[:-3] + "_toc.md")
f.close()
