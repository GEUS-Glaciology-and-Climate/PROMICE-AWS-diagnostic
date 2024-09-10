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
data_type = 'stations'
path_new = '../aws-l3-dev/'+data_type+'/'
df_meta = pd.read_csv(path_new+'../AWS_'+data_type+'_metadata.csv').set_index(data_type[:-1]+'_id')

# fig, ax_list = plt.subplots(8, 8, sharex=True, figsize=(20, 20), sharey=True)
# ax_list = ax_list.flatten()

# for station, ax in zip(df_meta.index, ax_list):
for station in df_meta.index:
    fig, ax = plt.subplots(1,1,figsize=(10, 10))

    if not os.path.isfile(f'{path_new}{station}/{station}_day.csv'):
        continue
    df_new = pd.read_csv(f'{path_new}{station}/{station}_day.csv')
    df_new.time = pd.to_datetime(df_new.time, utc=True)
    df_new = df_new.set_index('time')

    if 'albedo' in df_new.columns and not df_new['albedo'].isnull().all():
        ax.plot(df_new.index, df_new['albedo'], '.', color='tab:orange')

    ax.text(0.05, 0.95, station, transform=ax.transAxes, fontsize=8, 
            verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5))
    ax.grid()

fig.supylabel('albedo')
fig.savefig(f'figures/albedo/{station}.png', dpi=300)
