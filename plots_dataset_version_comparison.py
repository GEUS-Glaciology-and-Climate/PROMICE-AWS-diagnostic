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

path_old = 'C:/Users/bav/Downloads/AWS_dataverse_v12/hour'

new_version = 'aws-l3'
old_version = 'V12'

if 'dev' in new_version:
    path_l3 = 'C:/Users/bav/GitHub/PROMICE data/aws-l3-dev/level_3/'
else:
    path_l3 = 'https://thredds.geus.dk/thredds/fileServer/aws_l3_station_csv/level_3/'

    
filename = 'plot_compilations/new_version_to_dataverse_'+new_version+'.md'
figure_folder='figures/new_dataverse_upload_'+new_version
try:
    os.mkdir(figure_folder)
except:
    pass
df_meta = pd.read_csv('C:/Users/bav/GitHub/PROMICE data/aws-l3-dev/AWS_latest_locations.csv')

f = open(filename, "w")
def Msg(txt):
    f = open(filename, "a")
    print(txt)
    f.write(txt + "\n")
    
Msg('# Comparison of data '+new_version+' to v12 (old).')


#%%
# for station in ['CP1']: #
for station in df_meta.stid:
    Msg('## '+station)

        
    try:
        df_new = pd.read_csv(path_l3+station+'/'+station+'_hour.csv')
    except Exception as e:
        Msg(str(e))
    
        
    df_new.time = pd.to_datetime(df_new.time, utc=True)
    df_new = df_new.set_index('time')
    
    if not os.path.isfile(path_old+'/'+station+'_hour.csv'):
        Msg(path_old+'/'+station+'_hour.csv cannot be found in old data')
        continue
    df_old = pd.read_csv(path_old+'/'+station+'_hour.csv')
    df_old.time = pd.to_datetime(df_old.time, utc=True)
    df_old = df_old.set_index('time')
    
    Msg('Variables in new file:\n'+ ', '.join(df_new.columns.values))
    Msg('\nNew variables not in old files:\n'+ ', '.join(
        [v for v in df_new.columns if v not in df_old.columns]
        ))
    Msg('\nOld variables removed from new files:\n'+ ', '.join(
        [v for v in df_old.columns if v not in df_new.columns]
        ))
    Msg(' ')
    var_list = df_new.columns.values
    var_list_list = [var_list[i:i+5] for i in range(0, len(var_list), 5)]
    
    for k, var_list in enumerate(var_list_list):
        fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(13,13))
        if len(var_list)==1:
            ax_list = [ax_list]
    
        for var, ax in zip(var_list, ax_list):
            ax.set_ylabel(var)

            try:
                ax.plot(df_old[var].index, df_old[var].values,
                        marker='^',linestyle='None', label=old_version,
                        alpha=0.7, color='tab:blue')
            except:
                print(var,'not in old data')
        
            ax.plot(df_new[var].index, df_new[var].values, 
                    marker='.',markeredgecolor='None', linestyle='None', 
                    label=new_version, alpha=0.7,
                    color='tab:orange')            
            ax.legend()
            ax.grid()
            
        plt.suptitle('%s %i/%i'%(station, k+1, len(var_list_list)))
        fig.savefig(figure_folder+'/%s_%i.png'%(station,k))
        Msg('![%s](../%s/%s_%i.png)'%(station, figure_folder, station,k))
    Msg(' ')
tocgen.processFile(filename, filename[:-3]+"_toc.md")
f.close()
# os.remove(filename)
# os.rename(filename[:-3]+"_toc.md", filename)

# if __name__ == '__main__':
#     main()
