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
import os, logging, sys, glob
import matplotlib.dates as mdates
import matplotlib
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

matplotlib.set_loglevel("warning")
from pypromice.qc.persistence import persistence_qc
from pypromice.process import AWS
from pypromice.process.L1toL2 import adjustTime, adjustData, flagNAN, smoothTilt, smoothRot
# import matplotlib
# matplotlib.use('Agg')
import tocgen


path_to_l0 = '../aws-l0/'
path_to_l0 = 'C:/Users/bav/GitHub/PROMICE data/aws-l0/'
path_to_l1 = 'C:/Users/bav/GitHub/PROMICE data/aws-l1/'
path_tx = '../aws-l3/tx/'

from datetime import date
today = date.today().strftime("%Y%m%d")
filename = './plot_compilations/flags.md'
figure_folder='figures/flags'
try:
    os.mkdir(figure_folder)
except:
    pass

df_metadata = pd.read_csv('../thredds-data/metadata/AWS_stations_metadata.csv')

f = open(filename, "w")
def Msg(txt):
    f = open(filename, "a")
    print(txt)
    f.write(txt + "\n")

# plt.close('all')

path_to_qc_files = '../PROMICE-AWS-data-issues/'
all_dirs = os.listdir(path_to_qc_files+'adjustments')+os.listdir(path_to_qc_files+'flags')

zoom_to_good = False

for station in ['NUK_B']:
# for station in np.unique(np.array(all_dirs)):
    station = station.replace('.csv','')

    # removing older plots
    pattern = os.path.join(figure_folder, f'{station}*')
    for file_path in glob.glob(pattern):
        try:
            os.remove(file_path)
            print(f'Removed: {file_path}')
        except Exception as e:
            print(f'Error removing {file_path}: {e}')

    # loading flags
    try:
        flags = pd.read_csv(path_to_qc_files+'flags/'+station+'.csv', comment='#', skipinitialspace=True)
        flags['what was done'] = 'flag'
    except:
        flags = pd.DataFrame()

    try:
        adj = pd.read_csv(path_to_qc_files+'adjustments/'+station+'.csv', comment='#', skipinitialspace=True)
        adj['what was done'] = adj['adjust_function'] + ' ' + adj['adjust_value'].astype(str)
    except:
        adj = pd.DataFrame()

    try:
        df_flags = pd.concat((flags,adj))[['t0', 't1', 'variable', 'what was done', 'comment', 'URL_graphic']].reset_index(drop=True)
    except:
        df_flags = pd.concat((flags,adj))

    # Loading the L1 data:
    config_file_tx = path_to_l0 + '/tx/config/{}.toml'.format(station)
    config_file_raw = path_to_l0 + '/raw/config/{}.toml'.format(station)
    if os.path.isfile(config_file_tx):
        inpath = path_to_l0 + '/tx/'
        pAWS_tx = AWS(config_file_tx,
                      inpath,
                      var_file=None,
                      meta_file=None,
                      data_issues_repository='../PROMICE-AWS-data-issues')
        pAWS_tx.getL1()

    else:
        pAWS_tx = None

    if os.path.isfile(config_file_raw):
        inpath = path_to_l0 + '/raw/'+station+'/'
        pAWS_raw = AWS(config_file_raw,
                      inpath,
                      var_file=None,
                      meta_file=None,
                      data_issues_repository='../PROMICE-AWS-data-issues')
        pAWS_raw.getL1()

    else:
        pAWS_raw = None

    if pAWS_raw == None:
        print('No raw logger file for',station)
        ds = pAWS_tx.L1A.copy(deep=True)
    elif  pAWS_tx == None:
        print('No transmission toml file for',station)
        ds = pAWS_raw.L1A.copy(deep=True)
    else:
        print('Combining L1 data for',station)
        ds = pAWS_raw.L1A.combine_first(pAWS_tx.L1A).copy(deep=True)


    ds.attrs['bedrock'] = str(ds.attrs['bedrock'])

    ds_save = ds.copy(deep=True)

    # try:
    #     pAWS_tx.getL2()
    # except:
    #     pass

    #%% Flagging, adjusting, filtering

    ds = adjustTime(ds, adj_dir=path_to_qc_files+'adjustments')
    ds1 = flagNAN(ds,  flag_dir=path_to_qc_files+'flags')
    ds2 = adjustData(ds1, adj_dir=path_to_qc_files+'adjustments')
    ds3 = persistence_qc(ds2)

    ds4 = ds3.copy()
    baseline_elevation = (ds3.gps_alt.to_series().resample('M').median()
                          .reindex(ds3.time.to_series().index, method='nearest')
                          .ffill().bfill())
    mask = (np.abs(ds3.gps_alt - baseline_elevation) < 100) | ds3.gps_alt.isnull()
    ds4[['gps_alt','gps_lon', 'gps_lat']] = ds4[['gps_alt','gps_lon', 'gps_lat']].where(mask)

    # smoothing tilt
    ds4['tilt_x'] = smoothTilt(ds4['tilt_x'])
    ds4['tilt_y'] = smoothTilt(ds4['tilt_y'])
    ds4['rot'] = smoothRot(ds4['rot'])

    from pypromice.process.L1toL2 import  calcCloudCoverage, process_sw_radiation
    ds4['cc'] = calcCloudCoverage(ds4['t_u'], ds4['dlr'], ds4.attrs['station_id'], T_0=273.15)
    ds4, (OKalbedos, sunonlowerdome, bad, isr_toa, TOA_crit_nopass_cor, TOA_crit_nopass) = process_sw_radiation(ds4)

    # %%  plotting
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
    Msg('# '+station)
    var_list = [ 'p_l', 'p_u', 't_l','t_u', 'rh_l',  'rh_u', 'wspd_l', 'wspd_u', 'wdir_l', 'wdir_u', 'dsr', 'usr', 'dlr', 'ulr', 't_rad', 'z_boom_l', 'z_boom_u', 'z_stake', 'z_pt','z_pt_cor', 't_i_1', 't_i_2', 't_i_3', 't_i_4', 't_i_5', 't_i_6', 't_i_7', 't_i_8', 't_i_9', 't_i_10', 't_i_11', 'tilt_y', 'tilt_x', 'rot', 'precip_l', 'precip_u', 'gps_lat', 'gps_lon', 'gps_alt', 'fan_dc_l', 'fan_dc_u', 'batt_v', 't_log', 'p_i', 't_i', 'rh_i', 'wspd_i', 'wdir_i', 'gps_lat_i', 'gps_lon_i']

    # var_list = [ 'wspd_u', 'wdir_l', 'wdir_u', 'dsr', 'usr', 'dlr', 'ulr', 't_rad', 'z_boom_l', 'z_boom_u',  'tilt_y', 'tilt_x', 'rot',  'gps_lat', 'gps_lon', 'gps_alt',  'batt_v',]
    var_list = [v for v in var_list if v in ds1.data_vars]

    var_list_list = [np.array(var_list[i:(i+6)]) for i in range(0,len(var_list),6)]
    # var_list_list = [['']]
    # var_list_list = [np.array(['tilt_x','tilt_y','rot'])]
    var_list_list = [np.array([#'dlr','ulr','t_rad',
                               'dsr_cor','usr_cor', 'albedo','tilt_x','tilt_y','cc'])]
    # var_list_list = [np.array(['t_u','rh_u','wspd_u','z_boom_u','dlr','ulr','dsr','usr'])]
    # var_list_list = [
    #                     np.array(['tilt_x','tilt_y']),
    #                     np.array(['gps_lat','gps_lon','gps_alt']),
                        # np.array(['z_boom_u','z_boom_l','z_stake']),
                        # np.array(['t_u']+['t_i_'+str(i+1) for i in range(11)]),
                        # np.array(['p_u','p_l','p_i']),
                        # np.array(['rh_u','rh_l','rh_i']),
                        # np.array(['wspd_u','wspd_l','wspd_i']),
                        # np.array(['wdir_u','wdir_l','wdir_i']),
                        # np.array(['t_l','p_l','rh_l','fan_dc_l']),
                        # ]
                      # ,'t_u','t_l','t_i', 'rh_u','rh_i','rh_l'])]
    for i, var_list in enumerate(var_list_list):
        if len(var_list) == 0: continue
        if len(var_list[~np.isin(var_list, df_L1.columns)]) >0:
            print(var_list[~np.isin(var_list, df_L1.columns)], 'not in L1 data')
        # var_list = var_list[np.isin(var_list, df_L1.columns)]
        fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(12,len(var_list)*2.3))
        fig.subplots_adjust(top=0.83)
        if len(var_list) == 1: fig.subplots_adjust(top=0.7)

        if len(var_list)==1: ax_list = [ax_list]
        for var, ax in zip(var_list, ax_list):
            # if var in ds.data_vars:
            #     ax.plot( pAWS_raw.L0[-2].time,
            #             -pAWS_raw.L0[-2][var].values,
            #             marker='.',color='gray', linestyle='None',
            #             label='L0')
            if var in ds.data_vars:
                ax.plot(ds.time,
                        ds[var].values,
                        marker='.',color='tab:red', linestyle='None',
                        label='removed by flag')
                if var == 'albedo':
                    albedo_raw = ds['usr'] / ds['dsr']
                    albedo_raw = albedo_raw.where(albedo_raw>0).where(albedo_raw<1)

                    ax.plot(ds.time,
                            albedo_raw.values,
                            marker='.',color='tab:pink', linestyle='None',
                            label='unfiltered, uncorrected')

            if var in ds1.data_vars:
                ax.plot(ds1.time,
                        ds1[var].values,
                        marker='.',color='tab:orange', linestyle='None',
                        label='removed or changed by adjustment')
            if var in ds2.data_vars:
                ax.plot(ds2.time,
                        ds2[var].values,
                        marker='.',color='tab:green', linestyle='None',
                        label='filtered with persistence')
            if var in ds3.data_vars:
                ax.plot(ds3.time,
                        ds3[var].values,
                        marker='.',color='tab:pink', linestyle='None',
                        label='removed by custom filter (gps_alt, tilt or rot)')
                if var == 'gps_alt':
                    ax.plot(ds3.time,
                            baseline_elevation,
                            ls='--', c='k')

            if var[:-4] in ds4.data_vars:
                if var in ['dsr_cor','usr_cor']:
                    if var == 'dsr_cor':
                        ax.plot(ds3.time,(1.3* isr_toa + 50),
                                c='k', alpha=0.7)
                        ax_list[0].plot(np.nan,np.nan,
                                c='tab:red',label='TOA irradiance + margin of 10 (W m-2)')
                    ax.plot(ds.time,
                            ds[var[:-4]].values,
                            marker='.',color='tab:red', linestyle='None',
                            label='removed by flag')
                    ax.plot(ds3.time,
                            ds3[var[:-4]].values,
                            marker='.',color='tab:pink', linestyle='None',
                            label='value before tilt correction')
                    ax.plot(ds3.time,
                            ds3[var[:-4]].where(TOA_crit_nopass | TOA_crit_nopass_cor).values,
                            marker='.',color='k', linestyle='None',
                            label='removed, above TOA irradiance')

                    ax.plot(ds3.time,
                            ds3[var[:-4]].where(bad).values,
                            marker='.',color='tab:green', linestyle='None',
                            label='sun below horizon zenith angle or negative reading')


            if var in ds4.data_vars:
                ax.plot(ds4.time,
                        ds4[var].values,
                        marker='.',color='tab:blue', linestyle='None',
                        label='final')

        for var, ax in zip(var_list, ax_list):
            if zoom_to_good:
                ax.set_ylim(ds4[var].min(), ds4[var].max())
            ax.set_ylabel(var)
            ax.grid(True, which='minor', linestyle='--', linewidth=0.5)
            ax.grid(True, which='major', linestyle='-', linewidth=1)

        # ax.set_xlim(pd.to_datetime(['2024-05-01','2025-04-13']))
        title = station+'_%i/%i'%(i+1,len(var_list_list))
        ax_list[0].legend(loc='lower left', title = title, bbox_to_anchor=(0,1.1), ncol=3)
        fig.savefig('%s/%s_%i.png'%(figure_folder, station,i), dpi=120,bbox_inches='tight')
        Msg('![](../%s/%s_%i.png)'%(figure_folder, station,i))
    Msg(' ')
tocgen.processFile(filename, filename[:-3]+"_toc.md")
