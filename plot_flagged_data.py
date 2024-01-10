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
# from sklearn.linear_model import LinearRegression

from pypromice.qc.persistence import persistence_qc
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
path_to_l0 = '../aws-l0/'
path_to_l0 = 'C:/Users/bav/GitHub/PROMICE data/aws-l0/'
path_to_l1 = 'C:/Users/bav/GitHub/PROMICE data/aws-l1/'
path_l3 = '../aws-l3/level_3/'
path_l3 = 'C:/Users/bav/GitHub/PROMICE data/aws-l3-dev/level_3/'
path_tx = '../aws-l3/tx/'

from datetime import date
today = date.today().strftime("%Y%m%d")
filename = './plot_compilations/flags_'+today+'.md'
figure_folder='figures/flags_'+today
try:
    os.mkdir(figure_folder)
except:
    pass

df_meta = pd.read_csv(path_l3+'../AWS_latest_locations.csv')
df_metadata = pd.read_csv(path_l3+'../AWS_metadata.csv')

f = open(filename, "w")
def Msg(txt):
    f = open(filename, "a")
    print(txt)
    f.write(txt + "\n")
    
plt.close('all')

try:
    path_to_qc_files = 'C:/Users/bav/OneDrive - GEUS/Code/PROMICE/PROMICE-AWS-data-issues/'
    vari = 'C:/Users/bav/OneDrive - GEUS/Code/PROMICE/pypromice/src/pypromice/process/variables.csv'
    all_dirs = os.listdir(path_to_qc_files+'adjustments')+os.listdir(path_to_qc_files+'flags')
except:
    path_to_qc_files = 'C:/Users/bav/OneDrive - Geological survey of Denmark and Greenland/Code/PROMICE/PROMICE-AWS-data-issues/'
    vari = 'C:/Users/bav/OneDrive - Geological survey of Denmark and Greenland/Code/PROMICE/pypromice/src/pypromice/process/variables.csv'
    all_dirs = os.listdir(path_to_qc_files+'adjustments')+os.listdir(path_to_qc_files+'flags')
    
for station in ['CEN2', 'CP1', 'DY2', 'HUM', 'JAR_O', 'KAN_Lv3', 'NAE', 'NAU',
                'NEM', 'NSE', 'NUK_K', 'NUK_Uv3', 'QAS_Mv3', 'QAS_Uv3', 'SDL',
                'SDM', 'SWC_O', 'TUN', 'ZAK_A']:
# for station in np.unique(np.array(all_dirs)): 
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
        
    try:
        df_flags = pd.concat((flags,adj))[['t0', 't1', 'variable', 'what was done', 'comment', 'URL_graphic']].reset_index(drop=True)
    except:
        df_flags = pd.concat((flags,adj))
        
    # if len(df_flags)==0:
    #     print('no flag listed in file')
    #     continue
    
    # Loading the L1 data:
    if False:  #os.path.isfile('../aws-l1/'+station+'.nc'):
        print('found L1 file')
        ds = xr.open_dataset('../aws-l1/'+station+'.nc')
    else:
        config_file = path_to_l0 + '/tx/config/{}.toml'.format(station)
        if os.path.isfile(config_file):
            inpath = path_to_l0 + '/tx/'
            pAWS_tx = AWS(config_file, inpath, var_file=vari)
            pAWS_tx.getL1()
            # pAWS_tx.process()
            # pAWS_tx.write('.')
            try:
                config_file = path_to_l0 + '/raw/config/{}.toml'.format(station)
                inpath = path_to_l0 + '/raw/'+station+'/'
                pAWS_raw = AWS(config_file, inpath)
                pAWS_raw.getL1()
                # pAWS_raw.process()
                ds = pAWS_raw.L1A.combine_first(pAWS_tx.L1A).copy(deep=True)
                # ds3 = pAWS_raw.L3.combine_first(pAWS_tx.L3)
            except:
                print('No raw logger file for',station)
                ds = pAWS_tx.L1A.copy(deep=True)
                # ds3 = pAWS_tx.L3
        else:
            print('No transmission toml file for',station)
            config_file = path_to_l0 + '/raw/config/{}.toml'.format(station)
            inpath = path_to_l0 + '/raw/'+station+'/'
            pAWS_raw = AWS(config_file, inpath)
            pAWS_raw.getL1()
            # pAWS_raw.process()
            ds = pAWS_raw.L1A.copy(deep=True)
            # ds3 = pAWS_raw.L3
        
        ds.attrs['bedrock'] = str(ds.attrs['bedrock'])

    ds_save = ds.copy(deep=True)
    
    ds = adjustTime(ds, 
                    adj_dir=path_to_qc_files+'adjustments')
    ds1 = flagNAN(ds, 
                 flag_dir=path_to_qc_files+'flags')
    ds2 = adjustData(ds1,
                    adj_dir=path_to_qc_files+'adjustments')
    temp_var = ['t_i_'+str(i) for i in range(12)]
    variable_thresholds =  {x:{"max_diff": 0.0001, "period": 2} for x in temp_var}
    ds3 = persistence_qc(ds2, variable_thresholds)
    
    df_L1 = ds.to_dataframe().copy()
    
    if len(df_flags)>0:
        for ind, var_list in zip(df_flags.index, df_flags.variable):
            if var_list == '*':
                df_flags.loc[ind,'variable'] = ' '.join(df_L1.columns)
            elif '*' in var_list:
                df_flags.loc[ind,'variable'] = ' '.join(df_L1.filter(regex=var_list).columns)

        var_list = np.unique(' '.join(df_flags.variable.to_list()).split(' '))
        for v in var_list:
            if v not in ds_save.data_vars:
                Msg(v+' not in variables')
                var_list = var_list[~np.isin(var_list, v)]
                continue
                
            if ds_save[v].isnull().all():
                var_list = var_list[~np.isin(var_list, v)]
# %%
    Msg('# '+station)
    # if len(df_flags)>0: 
    #     Msg(df_flags.set_index('t0').to_markdown())
    # else:
    #     Msg('No flag defined for '+station)
    # Msg(' ')

    # var_list_list = [var_list[i:(i+6)] for i in range(0,len(var_list),6)]
    # var_list_list = [np.array(['wspd_i','wspd_u','z_pt_cor', 'z_pt'])]
    var_list_list = [np.array(['t_u']+['t_i_'+str(i+1) for i in range(12)])]
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
            
            ax.plot(ds.time, 
                    ds[var].values,
                    marker='.',color='tab:red', linestyle='None', 
                    label='removed by flag')
            ax.plot(ds1.time, 
                    ds1[var].values,
                    marker='.',color='tab:orange', linestyle='None',
                    label='removed or changed by adjustment')
            ax.plot(ds2.time, 
                    ds2[var].values,
                    marker='.',color='tab:green', linestyle='None',
                    label='before persistence')
            ax.plot(ds3.time, 
                    ds3[var].values,
                    marker='.',color='tab:pink', alpha=0.5, linestyle='None',
                    label='final')

            # ax.set_xlim(df_L1.index[[0,-1]])
            # ax.set_ylim(ds3[var].min(),ds2[var].max())
            ax.set_ylabel(var)
            ax.grid()
        title = station+'_%i/%i'%(i+1,len(var_list_list))
        ax_list[0].legend(loc='lower left', title = title, bbox_to_anchor=(0,1.1), ncol=3)
        fig.savefig('%s/%s_%i.png'%(figure_folder, station,i), dpi=120,bbox_inches='tight')
        Msg('![](../%s/%s_%i.png)'%(figure_folder, station,i))
    Msg(' ')
tocgen.processFile(filename, filename[:-3]+"_toc.md")
# f.close()
# os.remove(filename)
# os.rename(filename[:-3]+"_toc.md", filename)

# if __name__ == '__main__':
#     main()
