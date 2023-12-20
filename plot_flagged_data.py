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
from pypromice.process import AWS, resampleL3
from pypromice.process.L1toL2 import adjustTime, adjustData, flagNAN
import xarray as xr
import os
import matplotlib
matplotlib.use('Agg')
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

from datetime import date
today = date.today().strftime("%Y_%m_%d")
filename = './plot_compilations/flags_'+today+'.md'

df_meta = pd.read_csv(path_l3+'../AWS_latest_locations.csv')
df_metadata = pd.read_csv(path_l3+'../AWS_metadata.csv')

f = open(filename, "w")
def Msg(txt):
    f = open(filename, "a")
    print(txt)
    f.write(txt + "\n")
    
plt.close('all')

all_dirs = os.listdir(path_to_qc_files+'adjustments')+os.listdir(path_to_qc_files+'flags')
# for station in ['EGP']:  # os.listdir(path_to_qc_files+'adjustments'): 

for station in np.unique(np.array(all_dirs)): 
    station = station.replace('.csv','')
    # loading flags
    try:
        flags = pd.read_csv(path_to_qc_files+'flags/'+station+'.csv',
                                comment='#',
                                skipinitialspace=True)
        flags['what was done'] = 'flag'
    except:
        flags = pd.DataFrame()
    
    try:
        adj = pd.read_csv(path_to_qc_files+'adjustments/'+station+'.csv',
                         comment='#',
                         skipinitialspace=True)
        adj['what was done'] = adj['adjust_function'] + ' ' + adj['adjust_value'].astype(str)
    except:
        adj = pd.DataFrame()
        
    df_flags = pd.concat((flags,adj))[['t0', 't1', 'variable', 'what was done', 'comment', 'URL_graphic']].reset_index(drop=True)
        
    if len(df_flags)==0:
        print('no flag listed in file')
        continue
    
    # Loading the L1 data:
    config_file = path_to_l0 + '/tx/config/{}.toml'.format(station)
    if False:  #os.path.isfile('../aws-l1/'+station+'.nc'):
        print('found L1 file')
        ds = xr.open_dataset('../aws-l1/'+station+'.nc')
    else:
        if os.path.isfile(config_file):
            inpath = path_to_l0 + '/tx/'
            pAWS_tx = AWS(config_file, inpath, var_file=vari)
            pAWS_tx.process()
            try:
                config_file = path_to_l0 + '/raw/config/{}.toml'.format(station)
                inpath = path_to_l0 + '/raw/'+station+'/'
                pAWS_raw = AWS(config_file, inpath)
                pAWS_raw.process()
                ds = pAWS_raw.L1A.combine_first(pAWS_tx.L1A)
            except:
                print('No raw logger file for',station)
                ds = pAWS_tx.L1A
        else:
            print('No transmission toml file for',station)
            config_file = path_to_l0 + '/raw/config/{}.toml'.format(station)
            inpath = path_to_l0 + '/raw/'+station+'/'
            pAWS_raw = AWS(config_file, inpath)
            pAWS_raw.process()
            # pAWS_raw.write('.')
            # print(wtf)
            ds = pAWS_raw.L1A
        # print('writing L1 file')
        
        ds.attrs['bedrock'] = str(ds.attrs['bedrock'])

    ds_save = ds.copy(deep=True)

#     ds = resampleL3(ds, 'H')
    
    ds = adjustTime(ds, adj_url='https://use_local_file',
                    adj_dir=path_to_qc_files+'adjustments')
    ds1 = flagNAN(ds, flag_url='https://use_local_file',
                 flag_dir=path_to_qc_files+'flags')
    ds2 = adjustData(ds1, adj_url='https://use_local_file',
                    adj_dir=path_to_qc_files+'adjustments')
    ds3 = pAWS_raw.L3
    
    df_L1 = ds.to_dataframe().copy()
#%%
    for ind, var_list in zip(df_flags.index, df_flags.variable):
        if var_list == '*':
            df_flags.loc[ind,'variable'] = ' '.join(df_L1.columns)
        elif '*' in var_list:
            df_flags.loc[ind,'variable'] = ' '.join(df_L1.filter(regex=var_list).columns)

    #%%
    var_list = np.unique(' '.join(df_flags.variable.to_list()).split(' '))
    for v in var_list:
        if v not in ds_save.data_vars:
            Msg(v+' not in variables')
            var_list = var_list[~np.isin(var_list, v)]
            continue
            
        if ds_save[v].isnull().all():
            var_list = var_list[~np.isin(var_list, v)]

    Msg('# '+station)
    Msg(df_flags.set_index('t0').to_markdown())
    Msg(' ')

    var_list_list = [var_list[i:(i+6)] for i in range(0,len(var_list),6)]
    # var_list_list = [np.array([v for v in ['z_boom_u','z_boom_l','z_stake','z_pt_cor'] if v in var_list]),
    #                   np.array([v for v in var_list if 't_i' in v])]
    for i, var_list in enumerate(var_list_list):
        if len(var_list) == 0: continue
        if len(var_list[~np.isin(var_list, df_L1.columns)]) >0:
            print(var_list[~np.isin(var_list, df_L1.columns)], 'not in L1 data')
        var_list = var_list[np.isin(var_list, df_L1.columns)]
        fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(12,len(var_list)*2.3))
        fig.subplots_adjust(top=0.83)
        if len(var_list) == 1: fig.subplots_adjust(top=0.7)
            
        if len(var_list)==1: ax_list = [ax_list]
        for var, ax in zip(var_list, ax_list):
            
            ax.plot(ds_save.time, 
                    ds_save[var].values,
                    marker='.',color='tab:red', linestyle='None', 
                    label='removed by flag')
            ax.plot(ds1.time, 
                    ds1[var].values,
                    marker='.',color='tab:orange', linestyle='None',
                    label='removed or changed by adjustment')
            ax.plot(ds2.time, 
                    ds2[var].values,
                    marker='.',color='tab:green', linestyle='None',
                    label='final')
            ax.plot(ds3.time, 
                    ds3[var].values,
                    marker='.',color='tab:pink', alpha=0.5, linestyle='None',
                    label='after advanced filters')

            ax.set_xlim(df_L1.index[[0,-1]])
            ax.set_ylabel(var)
            ax.grid()
        title = station+'_%i/%i'%(i+1,len(var_list_list))
        ax_list[0].legend(loc='lower left', title = title, bbox_to_anchor=(0,1.1), ncol=3)
        fig.savefig('figures/flags/%s_%i.png'%(station,i), dpi=300)
        Msg('![%s](../figures/flags/%s_%i.png)'%(station, station,i))
    Msg(' ')
tocgen.processFile(filename, filename[:-3]+"_toc.md")
# f.close()
# os.remove(filename)
# os.rename(filename[:-3]+"_toc.md", filename)

# if __name__ == '__main__':
#     main()
