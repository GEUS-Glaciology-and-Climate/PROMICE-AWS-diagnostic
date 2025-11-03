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
import matplotlib
matplotlib.use('Agg')
import tocgen, os

# Initialize
data_type = 'sites'
if data_type == 'sites':
    path_new = '../thredds-data/level_3_sites/csv//'
else:
    path_new = '../thredds-data//level_2_stations/csv//'

filename = 'plot_compilations/precipitation_' + data_type + '.md'


f = open(filename, "w")

def Msg(txt):
    with open(filename, "a") as f:
        print(txt)
        f.write(txt + "\n")

plt.close('all')

# %% Loop over each station
for file in os.listdir(path_new+'/hour')[25:]:
# for file in ['KAN_L_hour.csv']:
   
    site = file.replace('_hour.csv', '')
    Msg('## ' + site)
            
    def fresh_load(path):
        df = pd.read_csv(path)
        df['time'] = pd.to_datetime(df.time,utc=True)
        return df.set_index('time')

    var = 'rainfall_u'

    df_h = fresh_load(f'{path_new}/hour/{site}_hour.csv')
    if var not in df_h.columns:
        Msg('No rainfall measurements')
        continue

    df_h = df_h.loc[slice(df_h[var].first_valid_index(), df_h[var].last_valid_index())]
    df_d = fresh_load(f'{path_new}/day/{site}_day.csv').loc[slice(df_h[var].first_valid_index(), df_h[var].last_valid_index())]
    df_m = fresh_load(f'{path_new}/month/{site}_month.csv').loc[slice(df_h[var].first_valid_index(), df_h[var].last_valid_index())]
        
    fig, axs = plt.subplots(2, 2, figsize=(10, 8), sharex=True)
    axs=axs.flatten()
    fig.suptitle(f'{site}')
    # Panel (a): Rainfall amount per time step
    axs[0].set_title('(a) rainfall_u: \nRainfall amount per time step.')
    df_h[var].plot(ax=axs[0], marker='o',alpha=0.6, label='hourly',drawstyle="steps-post")
    df_d[var].plot(ax=axs[0], marker='x',alpha=0.6, label='daily',drawstyle="steps-post")
    df_m[var].plot(ax=axs[0], marker='o',alpha=0.6, label='monthly',drawstyle="steps-post")
    
    # Panel (b): Cumulated rainfall
    axs[2].set_title('(c) Cumulated rainfall.\n Data gaps are not filled.')
    df_h[var].cumsum().plot(ax=axs[2], marker='o',alpha=0.6, label='hourly',drawstyle="steps-post")
    df_d[var].cumsum().plot(ax=axs[2], marker='x',alpha=0.6, label='daily',drawstyle="steps-post")
    df_m[var].cumsum().plot(ax=axs[2], marker='o',alpha=0.6, label='monthly',drawstyle="steps-post")

    var = 'rainfall_cor_u'
    
    # Panel (a): Rainfall amount per time step
    axs[1].set_title('(b) rainfall_cor_u: \nCorrected rainfall amount per time step.')
    if var in df_h.columns:
        df_h[var].plot(ax=axs[1], marker='o',alpha=0.6, label='hourly',drawstyle="steps-post")
        df_h[var].cumsum().plot(ax=axs[3], marker='o',alpha=0.6, label='hourly',drawstyle="steps-post")
    if var in df_d.columns:
        df_d[var].plot(ax=axs[1], marker='x',alpha=0.6, label='daily',drawstyle="steps-post")
        df_d[var].cumsum().plot(ax=axs[3], marker='x',alpha=0.6, label='daily',drawstyle="steps-post")
    if var in df_m.columns:
        df_m[var].plot(ax=axs[1], marker='o',alpha=0.6, label='monthly',drawstyle="steps-post")
        df_m[var].cumsum().plot(ax=axs[3], marker='o',alpha=0.6, label='monthly',drawstyle="steps-post")
    
    # Panel (b): Cumulated rainfall
    axs[3].set_title('(d) Cumulated corrected rainfall.\n Data gaps are not filled.')
    for ax in axs:
        ax.set_ylabel('mm')
        ax.legend()
        ax.grid()
    fig.savefig('figures/precipitation/%s_precipitation.png' % ( site), dpi=300)
    Msg(f'![{site}](../figures/precipitation/{site}_precipitation.png)')
    Msg(' ')
    
tocgen.processFile(filename, filename[:-3] + "_toc.md")

