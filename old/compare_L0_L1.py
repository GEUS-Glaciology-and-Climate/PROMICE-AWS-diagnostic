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
from pypromice.process import AWS, resampleL3
from pypromice.process.L1toL2 import adjustTime, adjustData, flagNAN
import xarray as xr
import os
# import matplotlib
# matplotlib.use('Agg')
import tocgen

def advanced_filters(ds2, station, station_type):
    # specific filters for tripods2
    ds3 = ds2.copy()
    # if station_type == 'one boom':
    #     ds3['z_boom_u'] = ds3['z_boom_u'].where(ds3['z_boom_u']<2.9)
        
    # frozen filter on altitude
    # ds3['msk'] = np.abs(ds3['gps_alt'].ffill(dim='time').bfill(dim='time').diff(dim='time'))<0.005
    # ds3['gps_alt'] = ds3.gps_alt.where(ds3['msk'] )
    
    # # range filter on elevation
    # ds3['gps_alt'] = ds3['gps_alt'].where(ds3['gps_alt']<ds3['gps_alt'].median()+ds3['gps_alt'].std()*5)
    # ds3['gps_alt'] = ds3['gps_alt'].where(ds3['gps_alt']>ds3['gps_alt'].median()-ds3['gps_alt'].std()*5)
    
    return ds3
    
# def main(path_to_l0 = '../aws-l0/',
#          path_l3 = '../aws-l3/level_3/',
#          path_tx = '../aws-l3/tx/',
#          path_gcn= '../GC-Net-Level-1-data-processing/L1/',
#          path_to_qc_files = '../PROMICE-AWS-data-issues/',
#          vari = '../pypromice/src/pypromice/process/variables.csv',
#          filename="./plot_compilations/flags.md"):
path_to_l0 = 'C:/Users/bav/GitHub/PROMICE data/aws-l0/'
path_to_l1 = 'C:/Users/bav/GitHub/PROMICE data/aws-l1/'
path_l3 = 'C:/Users/bav/GitHub/PROMICE data/aws-l3-dev/level_3/'
path_tx = 'C:/Users/bav/GitHub/PROMICE data/aws-l3-dev/tx/'
path_gcn= '../GC-Net-Level-1-data-processing/L1/'
path_to_qc_files = '../PROMICE-AWS-data-issues/'
vari = '../pypromice/src/pypromice/process/variables.csv'
filename="./plot_compilations/flags.md"

df_meta = pd.read_csv(path_l3+'../AWS_latest_locations.csv')
df_metadata = pd.read_csv(path_l3+'../AWS_metadata.csv')

f = open(filename, "w")
def Msg(txt):
    f = open(filename, "a")
    print(txt)
    f.write(txt + "\n")
    
# plt.close('all')

from pypromice.process import AWS
path_to_l0 = 'C:/Users/bav/GitHub/PROMICE data/aws-l0/'
station='NEM'
file_type = 'tx'

# Loading the L1 data:
config_file = path_to_l0 + '/'+file_type+'/config/{}.toml'.format(station)
if file_type == 'raw':
    inpath = path_to_l0 + '/'+file_type+'/'+station+'/'
else:
    inpath = path_to_l0 + '/'+file_type+'/'
    
pAWS = AWS(config_file, inpath, var_file=vari)
pAWS.getL1()
pAWS.getL2()

# #%%
# plt.close('all')
var_list = ['t_i_2','t_i_3']
fig, ax_list = plt.subplots(len(var_list),1,sharex = True)
for i in range(len(pAWS.L0)):
    L0 = pAWS.L0[i].copy()
    L1 = pAWS.L1[i].copy()
    print(i, L0.file)
    for ax, var in zip(ax_list,var_list):
        L0[var].astype(float).plot(ax=ax, ls='None', marker ='o', color='tab:blue')
        L1[var].plot(ax=ax,marker ='o',ls='None',  color='tab:green')
    
L2 = pAWS.L2.copy()
for ax, var in zip(ax_list,var_list):
    L0[var].astype(float).plot(ax=ax, color='tab:blue', marker ='o',label='L0')
    L1[var].plot(ax=ax, color='tab:green', marker ='o',label='L1')
    L2[var].plot(ax=ax, color='tab:orange', label='L2')
    ax.legend()
    ax.set_ylabel(var)

ax_list[0].set_title(station)