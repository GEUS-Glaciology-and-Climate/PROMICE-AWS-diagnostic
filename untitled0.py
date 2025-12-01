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

path = '../thredds-data/level_3_sites/csv/hour/'
station = 'KAN_L'
vars_ = ['z_boom_cor_u','z_stake_cor','z_pt_cor']
labels = ['height SR50 on boom','height SR50 on stake','Depth pressure transducer']

df = pd.read_csv(f"{path}/{station}_hour.csv", parse_dates=['time']).set_index('time')
vars_ = [v for v in vars_ if v in df.columns]

plt.figure(figsize=(7,6))
for v, l in zip(vars_, labels):
    plt.plot(df.index, df[v], '.', ms=3, label=l)
plt.ylabel('m')
plt.grid()
plt.legend()
plt.title(station)
plt.tight_layout()
plt.show()
