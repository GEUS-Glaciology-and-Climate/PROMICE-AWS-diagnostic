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
from pypromice.process import AWS
from pypromice.process.L1toL2 import adjustTime, adjustData, flagNAN
import xarray as xr
import os
# import matplotlib
# matplotlib.use('Agg')
import tocgen

def advanced_filters(ds2, station, station_type):
    # specific filters for tripods2
    ds3 = ds2.copy()
    if station_type == 'one boom':
        ds3['z_boom_u'] = ds3['z_boom_u'].where(ds3['z_boom_u']<2.9)
        
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
path_to_l1 = '../aws-l1/'
path_l3 = '../aws-l3/level_3/'
path_tx = '../aws-l3/tx/'
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


for station in ['QAS_U']: #os.listdir(path_to_qc_files+'flags'):
    station = station.replace('.csv','')
    # loading flags
    try:
        df_flags = pd.read_csv(path_to_qc_files+'flags/'+station+'.csv',
                               comment='#',
                               skipinitialspace=True)
    except:
        print('no flag file')
        
    if len(df_flags)==0:
        print('no flag listed in file')
        continue
    
    if not os.path.isfile(path_to_l1+'%sasfda.nc'%station):
        # Loading the L1 data:
        config_file = path_to_l0 + '/tx/config/{}.toml'.format(station)
        inpath = path_to_l0 + '/tx/'
        pAWS_tx = AWS(config_file, inpath, var_file=vari)
        pAWS_tx.getL1()
    
        try:
            config_file = path_to_l0 + '/raw/config/{}.toml'.format(station)
            inpath = path_to_l0 + '/raw/'+station+'/'
            pAWS_raw = AWS(config_file, inpath, var_file=vari)
            pAWS_raw.getL1()
            ds = pAWS_raw.L1A.combine_first(pAWS_tx.L1A)
    
        except:
            print('no raw for',station)
            ds = pAWS_tx.L1A.copy()
            pass
        
        ds = adjustTime(ds, adj_url='https://use_local_file',
                        adj_dir=path_to_qc_files+'adjustments')
        ds.to_netcdf(path_to_l1+'%s.nc'%station)
    else:
        ds = xr.open_dataset(path_to_l1+'%s.nc'%station)

    ds1 = flagNAN(ds, flag_url='https://use_local_file',
                 flag_dir=path_to_qc_files+'flags')
    ds2 = adjustData(ds1, adj_url='https://use_local_file',
                    adj_dir=path_to_qc_files+'adjustments')
    ds3 = advanced_filters(ds2, 
                          station=station,
                          station_type=df_metadata.loc[df_metadata.stid==station, 
                                                       'station_type'].values[0])
    df_L1 = ds.to_dataframe().copy()

    for ind, var_list in zip(df_flags.index, df_flags.variable):
        if var_list == '*':
            df_flags.loc[ind,'variable'] = ' '.join(df_L1.columns)
        elif '*' in var_list:
            df_flags.loc[ind,'variable'] = ' '.join(df_L1.filter(regex=var_list).columns)
    
    var_list = np.unique(' '.join(df_flags.variable.to_list()+['z_boom_u']).split(' '))
    Msg('# '+station)
    Msg(df_flags.set_index('t0').to_markdown())
    Msg(' ')

    var_list_list = [var_list[i:(i+6)] for i in range(0,len(var_list),6)]
    for i, var_list in enumerate(var_list_list):
        if len(var_list[~np.isin(var_list, df_L1.columns)]) >0:
            print(var_list[~np.isin(var_list, df_L1.columns)], 'not in L1 data')
        var_list = var_list[np.isin(var_list, df_L1.columns)]
        fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(12,len(var_list)*2))
        if len(var_list)==1:
            ax_list = [ax_list]
        for var, ax in zip(var_list, ax_list):
            
            ax.plot(ds.time, 
                    ds[var].values,
                    marker='.',color='tab:red', linestyle='None', 
                    label='before flagging')
            ax.plot(ds1.time, 
                    ds1[var].values,
                    marker='.',color='tab:orange', linestyle='None',
                    label='after flagging')
            ax.plot(ds2.time, 
                    ds2[var].values,
                    marker='.',color='tab:pink', linestyle='None',
                    label='after adjusting')
            ax.plot(ds3.time, 
                    ds3[var].values,
                    marker='.',color='tab:green', linestyle='None',
                    label='after advanced filters')

            ax.set_xlim(df_L1.index[[0,-1]])
            ax.set_ylabel(var)
        ax_list[0].legend(loc='lower left')
        plt.suptitle(station+'_%i/%i'%(i+1,len(var_list_list)))
        fig.savefig('figures/flags/%s_%i.png'%(station,i), dpi=300)
        Msg('![%s](../figures/flags/%s_%i.png)'%(station, station,i))
    Msg(' ')
tocgen.processFile(filename, filename[:-3]+"_toc.md")
# f.close()
# os.remove(filename)
# os.rename(filename[:-3]+"_toc.md", filename)

# if __name__ == '__main__':
#     main()
