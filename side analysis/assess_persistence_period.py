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
import os, logging, glob
import matplotlib
# matplotlib.use('Agg')

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

matplotlib.set_loglevel("warning")
logging.getLogger('numba').setLevel(logging.WARNING)

from pypromice.qc.persistence import persistence_qc
from pypromice.process import AWS
from pypromice.process.L1toL2 import adjustTime, adjustData, flagNAN, smoothTilt, smoothRot
import tocgen

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
all_dirs = os.listdir(path_to_qc_files+'adjustments' )+os.listdir(path_to_qc_files+'flags')

zoom_to_good = False

# for station in ['CP1']:
for station in np.unique(np.array(all_dirs)):
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
    is_bedrock = (ds4.attrs['bedrock'] == True) | (ds4.attrs['bedrock']=='True')| (ds4.attrs['bedrock']=='true')
    if not is_bedrock:
        ds4['cc'] = calcCloudCoverage(ds4['t_u'], ds4['dlr'], ds4.attrs['station_id'], T_0=273.15)
    else:
        ds4['cc'] = ds['t_u'].copy() * np.nan
    ds4, (OKalbedos, sunonlowerdome, bad, isr_toa, TOA_crit_nopass_cor, TOA_crit_nopass,TOA_crit_nopass_usr) = process_sw_radiation(ds4)


    # %%
    import matplotlib.pyplot as plt
    import numpy as np

    arr = ds4.p_u.values
    time = ds4.p_u['time'].values   # get time coordinate from DataArray

    thr = 150

    mask = np.r_[True, arr[1:] != arr[:-1], True]
    idx = np.flatnonzero(mask)
    runs = np.diff(idx)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12,6), sharex=False)

    ax1.hist(runs, bins=50)
    ax1.axvline(thr, color='k', linestyle='--')
    ax1.set_ylabel("Count")
    ax1.set_xlabel("Run length")
    ax1.set_yscale("log")
    ax1.grid(True, which="both", linestyle="--", alpha=0.5)
    ax1.set_title('Length of the periods with constant value at '+station)

    ax2.plot(time, arr, color='b', marker='o')
    ax2.set_title("Pressure at "+ station)
    for start, end, length in zip(idx[:-1], idx[1:], runs):
        if length > thr:
            ax2.axvspan(time[start], time[end-1], color='orange', alpha=0.3)

    ax2.set_ylabel("p_u")
    ax2.set_xlabel("Time")

    plt.tight_layout()
    fig.savefig(f'figures/persistence/{station}_p.png', dpi=300)
