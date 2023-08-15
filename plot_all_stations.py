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
import os
import matplotlib
matplotlib.use('Agg')
import tocgen

def main(path_l3 = '../aws-l3/level_3/',
         path_tx = '../aws-l3/tx/'):
    
    df_meta = pd.read_csv(path_l3+'../AWS_station_locations.csv')

    f = open(filename, "w")
    def Msg(txt):
        f = open(filename, "a")
        print(txt)
        f.write(txt + "\n")
        
    
    for station in df_meta.stid:
        df_l3 = pd.read_csv(path_l3+station+'/'+station+'_hour.csv')
        df_l3.time = pd.to_datetime(df_l3.time, utc=True)
        df_l3 = df_l3.set_index('time')
        df_tx = pd.read_csv(path_tx+station+'/'+station+'_hour.csv')
        df_tx.time = pd.to_datetime(df_tx.time, utc=True)
        df_tx = df_tx.set_index('time')
        # df_l3=df_l3.loc['2021-09-01':'2022-06-10',:]
        # df_l3=df_l3.loc['2022-09-01':,:]
        # appending fieldwork date
        # df_l3 = (pd.concat([df_l3, pd.DataFrame(index=[pd.to_datetime('2023-06-10', utc=True)])]).sort_index(kind='stable', ignore_index=False))
        fig, ax_list = plt.subplots(len(var_list),1,sharex=True)
        if len(var_list)==1:
            ax_list = [ax_list]
        for var, ax in zip(var_list, ax_list):
                # X = df_l3.index.values.astype(float)
                # Y = df_l3[var].values
                # linear_regressor = LinearRegression()  # create object for the class
                # linear_regressor.fit(X[~np.isnan(X+Y)].reshape(-1, 1),
                #                      Y[~np.isnan(X+Y)].reshape(-1, 1))  # perform linear regression
                # Y_pred = linear_regressor.predict(X.reshape(-1, 1))  # make predictions
    
    
            if var in df_tx.columns:
                ax.plot(df_tx[var].index, df_tx[var].values, marker='.',linestyle='None', label='transmission')
    
            if var in df_l3.columns:
                ax.plot(df_l3[var].index, df_l3[var].values, marker='.',markeredgecolor='None', linestyle='None', label='l3',alpha=0.5)
            ax.set_ylabel(var)
            ax.legend()
                # ax.plot(df_l3[var].index,Y_pred)
                # ax.plot(df_l3[var].index,Y_pred*0, 'k', ls=':')
                # print(station, Y_pred[-1] - Y[~np.isnan(X+Y)][0])
            
        plt.suptitle(station)
    
    for station in os.listdir(path_to_qc_files+'flags'):
        station = station.replace('.csv','')
        # loading flags
        try:
            df_flags = pd.read_csv(path_to_qc_files+'flags/'+station+'.csv', skipinitialspace=True)
        except:
            print('no flag file')
            continue
        
        # Loading the L1 data:
        config_file = path_to_l0 + '/raw/config/{}.toml'.format(station)
        inpath = path_to_l0 + '/raw/{}/'.format(station)
        try:
            pAWS_gc = AWS(config_file, inpath, var_file=vari)
            pAWS_gc.getL1()
        except:
            print('no raw for',station)
            
        config_file = path_to_l0 + '/tx/config/{}.toml'.format(station)
        inpath = path_to_l0 + '/tx/'
        pAWS_tx = AWS(config_file, inpath, var_file=vari)
        pAWS_tx.getL1()
    
        pAWS_all = pAWS_tx
        df_L1 = pAWS_all.L1A.combine_first(pAWS_gc.L1A).to_dataframe()
        df_L1.index = pd.to_datetime(df_L1.index, utc=True)
        var_list = np.unique(' '.join(df_flags.variable.to_list()).split(' '))
        Msg('# '+station)
        Msg(df_flags.to_markdown())
        Msg(' ')
        
        var_list_list = [var_list[i:(i+6)] for i in range(0,len(var_list),6)]
        for i, var_list in enumerate(var_list_list):
            fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(12,len(var_list)*2))
            if len(var_list)==1:
                ax_list = [ax_list]
            for var, ax in zip(var_list, ax_list):
                ax.plot(df_L1[var].index, 
                        df_L1[var].values,
                        marker='.',color='tab:blue', linestyle='None', label='L1')
                for t0, t1, variable in zip(df_flags.t0, df_flags.t1, df_flags.variable):
                    if var in variable:
                        if not isinstance(t0, str):
                            t0 = pd.to_datetime(df_L1.index[0], utc=True)
                        if not isinstance(t1, str):
                            t1 = pd.to_datetime(df_L1.index[-1], utc=True)
                        ax.plot(df_L1.loc[t0:t1, var].index,
                                df_L1.loc[t0:t1, var].values,
                                marker='.',color='tab:red', 
                                linestyle='None', label='removed')
                ax.set_ylabel(var)
                # ax.legend()
        
            plt.suptitle(station+'_%i/%i'%(i+1,len(var_list_list)))
            fig.savefig('figures/flags/%s_%i.png'%(station,i))
            Msg('![%s](../figures/flags/%s_%i.png)'%(station, station,i))
        Msg(' ')
    tocgen.processFile(filename, filename[:-3]+"_toc.md")
    f.close()
    os.remove(filename)
    os.rename(filename[:-3]+"_toc.md", filename)

if __name__ == '__main__':
    main()
