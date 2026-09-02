# -*- coding: utf-8 -*-
"""
Created on %(date)s
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""


import math
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np, pandas as pd

path_new=Path("../thredds-data")
df_meta=pd.read_csv(path_new/"metadata/AWS_sites_metadata.csv").set_index("site_id")
csv_dir=path_new/"level_3_sites/csv/hour"


stations =  ['CP1','DY2','KAN_U','NSE','SDL',] # 'ZAC_A'
# stations =  ['CEN','EGP','HUM','NAE','NAU','NEM','SDM','TUN']
# stations = df_meta.index
cmap = plt.get_cmap("tab20")
colors = {s: cmap(i % 20) for i, s in enumerate(stations)}
fig1,ax1=plt.subplots(4,1, sharex=True)
fig2,ax2=plt.subplots(4,1, sharex=True)
fig3,ax3=plt.subplots(4,1, sharex=True)

for i,s in enumerate(stations):
    d=pd.read_csv(csv_dir/f"{s}_hour.csv")
    if 'rh_l' not in d.columns: continue
    print(s)
    d["time"]=pd.to_datetime(d["time"],errors="coerce")
    d= d.set_index('time')
    d=d.loc['2021':,:].resample('D').mean()

    for ax,var in zip([ax1, ax2, ax3], ['t','rh', 'p']):
        offset = 1000 if var=='p' else 0
        d[var+"_u_l_diff"]=(d[var+"_u"] - d[var+"_l"])
        d[var+"_u_i_diff"]=(d[var+"_u"] - d[var+"_i"]-offset)
        d[var+"_l_i_diff"]=(d[var+"_l"] - d[var+"_i"]-offset)

        d[var+"_u"].plot(label='__nolegend__', ax=ax[0], color=colors[s])
        d[var+"_l"].plot(label='__nolegend__', ax=ax[0], color=colors[s], ls='--')
        d[var+"_u_l_diff"].plot(label=s, ax=ax[1], color=colors[s])
        d[var+"_u_i_diff"].plot(label=s, ax=ax[2], color=colors[s])
        d[var+"_l_i_diff"].plot(label=s, ax=ax[3], color=colors[s])

        if s == stations[-1]:
            for i in range(1,4):
                ax[i].plot(d.index[[0,-1]], [0, 0],ls=':',color='k')
                ax[i].set_ylim(-5,5)

            ax[0].set_ylabel(f'{var}_u and {var}_l')
            ax[1].set_ylabel(f'{var}_u - {var}_l')
            ax[2].set_ylabel(f'{var}_u - {var}_i')
            ax[3].set_ylabel(f'{var}_l - {var}_i')
            ax[0].plot([np.nan, np.nan], [np.nan, np.nan], color='gray', ls='-', label='upper')
            ax[0].plot([np.nan, np.nan], [np.nan, np.nan], color='gray', ls='--', label='lower')
            ax[0].legend( loc="center right",bbox_to_anchor=(1.1,0.5))
            ax[2].legend( loc="center right",bbox_to_anchor=(1.1,0.5))
