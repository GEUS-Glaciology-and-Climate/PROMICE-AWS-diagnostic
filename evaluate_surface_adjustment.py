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
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
from pypromice.qc.persistence import persistence_qc
from pypromice.process import AWS, resampleL3
from pypromice.process.L1toL2 import adjustTime, adjustData, flagNAN, smoothTilt, smoothRot
from pypromice.qc.percentiles.outlier_detector import ThresholdBasedOutlierDetector
from pypromice.process.L3toL4 import toL4
from pypromice.process import getVars, getMeta, addMeta, getColNames, \
    roundValues, resampleL3, writeCSV, writeNC
import xarray as xr
import os
# import matplotlib
# matplotlib.use('Agg')


path_to_l0 = '../aws-l0/'
path_to_l0 = 'C:/Users/bav/GitHub/PROMICE data/aws-l0/'
path_to_l1 = 'C:/Users/bav/GitHub/PROMICE data/aws-l1/'
path_l3 = '../aws-l3/level_3/'
path_l3 = 'C:/Users/bav/GitHub/PROMICE data/aws-l3-dev/level_3/'
path_tx = '../aws-l3/tx/'

from datetime import date
today = date.today().strftime("%Y%m%d")
figure_folder='figures/flags_'+today
try:
    os.mkdir(figure_folder)
except:
    pass

df_meta = pd.read_csv(path_l3+'../AWS_latest_locations.csv')
df_metadata = pd.read_csv(path_l3+'../AWS_metadata.csv')

plt.close('all')

vari = 'C:/Users/bav/OneDrive - GEUS/Code/PROMICE/pypromice/src/pypromice/process/variables.csv'
if not os.path.isfile(vari):
    vari = 'C:/Users/bav/OneDrive - Geological survey of Denmark and Greenland/Code/PROMICE/pypromice/src/pypromice/process/variables.csv'

def loadArr(infile):
    if infile.split('.')[-1].lower() in 'csv':
        df = pd.read_csv(infile)
        df['time'] = pd.to_datetime(df['time']).dt.tz_localize(None)
        df = df.set_index('time')
        ds = xr.Dataset.from_dataframe(df)

    elif infile.split('.')[-1].lower() in 'nc':
        with xr.open_dataset(infile) as ds:
            ds = ds.load()
    
    try:
        name = ds.attrs['station_name'] 
    except:
        name = infile.split('/')[-1].split('.')[0].split('_hour')[0].split('_10min')[0]
        
    print(f'{name} array loaded from {infile}')
    return ds, name

def makeL3(station):
    config_file = path_to_l0 + '/tx/config/{}.toml'.format(station)
    if os.path.isfile(config_file):
        inpath = path_to_l0 + '/tx/'
        pAWS_all = AWS(config_file, inpath, var_file=vari)
        pAWS_all.process()
        try:
            config_file = path_to_l0 + '/raw/config/{}.toml'.format(station)
            inpath = path_to_l0 + '/raw/'+station+'/'
            pAWS_raw = AWS(config_file, inpath)
            pAWS_raw.process()
            all_ds = pAWS_raw.L3.combine_first(pAWS_all.L3)
        except:
            print('No raw logger file for',station)
            all_ds = pAWS_all.L3
    else:
        print('No transmission toml file for',station)
        config_file = path_to_l0 + '/raw/config/{}.toml'.format(station)
        inpath = path_to_l0 + '/raw/'+station+'/'
        pAWS_raw = AWS(config_file, inpath)
        # pAWS_raw.getL1()
        pAWS_raw.process()
        ds = pAWS_raw.L1A.copy(deep=True)
        
        ds.attrs['bedrock'] = str(ds.attrs['bedrock'])
        
        all_ds = pAWS_raw.L3

    # Get hourly, daily and monthly datasets
    print('Resampling L3 data to hourly, daily and monthly resolutions...')
    l3_h = resampleL3(all_ds, '60min')
    # l3_d = resampleL3(all_ds, '1D')
    # l3_m = resampleL3(all_ds, 'M')
    
    print(f'Adding variable information...')
    # Load variables look-up table
    var = getVars()
        	
    # Round all values to specified decimals places
    l3_h = roundValues(l3_h, var)
    # l3_d = roundValues(l3_d, var)
    # l3_m = roundValues(l3_m, var)
        
    # Get columns to keep
    if hasattr(all_ds, 'p_l'):
        col_names = getColNames(var, 2, 'raw')  
    else:
        col_names = getColNames(var, 1, 'raw')    

    # Assign station id
    l3_h.attrs['station_id'] = station
    
    # Assign metadata
    print(f'Adding metadata...')
    m = getMeta()
    l3_h = addMeta(l3_h, m)
    # l3_d = addMeta(l3_d, m)
    # l3_m = addMeta(l3_m, m)
      
    # Set up output path
    outpath = os.path.join('L3_test', station)
    
    # Write to files
    if not os.path.isdir(outpath):
        os.mkdir(outpath)
    outfile_h = os.path.join(outpath, station + '_hour')

    writeCSV(outfile_h+'.csv', l3_h, csv_order=None)
    writeNC(outfile_h+'.nc', l3_h)
    

for station in ['EGP']:
# for station in df_metadata.stid[9:]: 
    station = station.replace('.csv','')
    infile = 'L3_test/'+station+'/'+station+'_hour.nc'
    print(station)

    if not os.path.isfile(infile):
        makeL3(station)
    ds1, n1 = loadArr(infile)
    ds1 = toL4(ds1)
    
    var_list_list = [np.array(['z_boom_u','z_boom_l','z_stake','z_pt_cor','z_surf_combined'])]
    # %%
    plt.close('all')
    fig, ax = plt.subplots(3,1,sharex=True,figsize=(8,12))
    for v in ['z_boom_u', 'z_boom_l', 'z_stake', 'z_pt_cor']:
        if v in ds1.data_vars:
            ds1[v].plot(label=v, ax=ax[0])
    
    ax[0].legend()
    ax[0].set_ylabel('height (m)')
    ax[0].grid()
    ax[0].set_title(station)
    
    
    for v in ['z_surf_1', 'z_surf_2', 'z_pt_cor']:
        if v in ds1.data_vars:
            ds1[v].plot(label=v, ax=ax[1])
    
    ax[1].legend()
    ax[1].set_ylabel('height (m)')
    ax[1].grid()
    ax[1].set_title(station)
    
    for v in ['snow_height', 'z_ice_surf', 'z_surf_combined']:
        ds1[v].plot(label=v, ax=ax[2])
    
    ax[2].legend()
    ax[2].set_ylabel('height (m)')
    ax[2].set_title('')
    ax[2].grid()
    
    # %% plot thermistor depth:
    z_surf_interp = ds1["z_surf_combined"].interpolate_na(dim='time')
    depth_cols_name = ['d_t_i'+str(i) for i in range(12) if 'd_t_i'+str(i) in ds1.data_vars]
    temp_cols_name = ['t_i'+str(i) for i in range(12) if 'tt_i'+str(i) in ds1.data_vars]
    fig.savefig('figures/surface_heights/'+station+'.png',dpi=300)

    fig, ax = plt.subplots(1, 2, figsize=(15, 6))
    plt.subplots_adjust(left=0.05, right=0.95, wspace=0.15, top=0.95)
    
    z_surf_interp.plot(
        ax=ax[0], color="lightgray", label="__nolegend__", linewidth=1
    )
    ds1["z_surf_combined"].plot(
        ax=ax[0], color="black", label="surface", linewidth=3
    )
    (z_surf_interp - 10).plot(
        ax=ax[0],  color="red", linestyle="-", linewidth=4,  
        label="10 m depth",
    )
    
    maintenance_string = pd.read_csv("fieldwork_summary_PROMICE.csv")
    maintenance_string = maintenance_string.replace("OUT", np.nan)
    maintenance_string[
        "Length of thermistor string on surface from surface marking"
    ] = maintenance_string[
        "Length of thermistor string on surface from surface marking"
    ].astype(
        float
    )
    maintenance_string["date"] = pd.to_datetime(maintenance_string["Date visit"])
    maintenance = maintenance_string.loc[maintenance_string.Station == station]

    if len(maintenance.date) > 0:
        for date in maintenance.date:
            index = ds1.time
            date2 = pd.to_datetime(index.sel(time=[date], method="nearest")[0].data)
            if np.abs(date - date2) <= pd.Timedelta("7 days"):
                depth_top_therm_found = (
                    maintenance.loc[
                        maintenance.date == date,
                        "Length of thermistor string on surface from surface marking",
                    ]
                    / 100 - 1 + z_surf_interp.sel(time=date2).item()
                )
                tmp = pd.DataFrame(depth_top_therm_found.values,
                                   index=[date],
                                   columns=['length_therm_out'])
                tmp['length_therm_out'].plot(ax = ax[0], 
                                             markersize=10, 
                                             marker="o", 
                                             linestyle="None",
                                             label='_no_legend_')
                if isinstance(
                    maintenance.loc[maintenance.date == date].depth_new_thermistor_m.values[0],
                    str,
                ):
                    ax[0].axvline(np.datetime64(date), color='r')
    for i, col in enumerate(depth_cols_name):
        (z_surf_interp - ds1[col]).plot(ax=ax[0], label="_nolegend_")

    ax[0].set_ylim(
        ds1["z_surf_combined"].min() - 11,
        ds1["z_surf_combined"].max() + 1,
    )

    for i in range(len(temp_cols_name)):
        ds1[temp_cols_name[i]].plot(
            ax=ax[1], label="_nolegend_"
        )

        tmp = df_in[temp_cols_name[i]].copy()
        # variance filter
        ind_filter = (
            df_in[temp_cols_name[i]]
            .interpolate(limit=14)
            .rolling(window=7)
            .var()
            > 0.5
        )
        month = (
            df_in[temp_cols_name[i]]
            .interpolate(limit=14)
            .index.month.values
        )
        ind_filter.loc[np.isin(month, [5, 6, 7])] = False
        if any(ind_filter):
            tmp.loc[ind_filter].plot(
                ax=ax[1], marker="o", linestyle="none",
                color="lightgray", label="_nolegend_",
            )

        # before and after maintenance adaptation filter
        if len(maintenance.date) > 0:
            for date in maintenance.date:
                if isinstance(
                    maintenance.loc[
                        maintenance.date == date
                    ].depth_new_thermistor_m.values[0],
                    str,
                ):
                    ind_adapt = np.abs(
                        tmp.interpolate(limit=14).index.values
                        - pd.to_datetime(date).to_datetime64()
                    ) < np.timedelta64(7, "D")
                    if any(ind_adapt):
                        tmp.loc[ind_adapt].plot(
                            ax=ax[1], marker="o", linestyle="none",
                            color="lightgray", label="_nolegend_",
                        )

        # surfaced thermistor
        ind_pos = ds1[depth_cols_name[i]] < 0.1
        if any(ind_pos):
            tmp.loc[ind_pos].plot(
                ax=ax[1], marker="o", linestyle="none", color="lightgray",
                label="_nolegend_",
            )
    if len(ds1["t_i_10m"]) == 0:
        print("No 10m temp for ", station)
    else:
        ds1["t_i_10m"].resample(time="D").mean().plot(ax=ax[1], 
                                                               color="red", 
                                                               linewidth=5, 
                                                               label="10 m temperature")
    ax[1].plot(
        np.nan, np.nan,  marker="o", linestyle="none", color="lightgray",
        label="filtered",
    )
    ax[1].plot(
        np.nan, np.nan, marker="o", linestyle="none",
        color="purple", label="maintenance",
    )
    ax[1].plot(
        np.nan, np.nan, marker="o", linestyle="none", color="pink", label="var filter"
    )
    ax[1].legend()
    ax[0].legend()
    ax[0].set_ylabel("Height (m)")
    ax[1].set_ylabel("Subsurface temperature ($^o$C)")
    fig.suptitle(station)
    fig.savefig("figures/string_processing/" + station + ".png", dpi=300)
