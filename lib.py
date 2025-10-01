# -*- coding: utf-8 -*-
"""
Created on %(date)s
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""
import numpy as np
import os, glob
import pandas as pd
from pypromice.pipeline import AWS
# from pypromice.core.variables import (station_pose,
#                                       radiation,
#                                       air_temperature,
#                                       precipitation)

from pypromice.pipeline.get_l2 import get_l2
from pypromice.pipeline.join_l2 import join_l2
from pypromice.pipeline.join_l2 import loadArr

def process_precip(ds):
    if ~ds["precip_u"].isnull().all():
        ds["precip_u"] = precipitation.filter_lufft_errors(ds["precip_u"], ds["t_u"], ds["p_u"], ds["rh_u"])
        ds["rainfall_u"] = precipitation.get_rainfall_per_timestep(ds["precip_u"], ds["t_u"])
        ds["rainfall_cor_u"] = precipitation.correct_rainfall_undercatch(ds["rainfall_u"], ds["wspd_u"])

    if ds.attrs["number_of_booms"]==2:
        if ~ds["precip_l"].isnull().all():
            ds["precip_l"] = precipitation.filter_lufft_errors(ds["precip_l"], ds["t_l"], ds["p_l"], ds["rh_l"])
            ds["rainfall_l"] = precipitation.get_rainfall_per_timestep(ds["precip_l"], ds["t_l"])
            ds["rainfall_cor_l"] = precipitation.correct_rainfall_undercatch(ds["rainfall_l"], ds["wspd_l"])
    return ds

def remove_old_plots(figure_folder, station):
    pattern = os.path.join(figure_folder, f'{station}*')
    for file_path in glob.glob(pattern):
        try:
            os.remove(file_path)
            print(f'Removed: {file_path}')
        except Exception as e:
            print(f'Error removing {file_path}: {e}')

def load_flags_and_adjustments(path_to_qc_files, station):
    try:
        flags = pd.read_csv(os.path.join(path_to_qc_files, 'flags', f'{station}.csv'),
                            comment='#', skipinitialspace=True)
        flags['what was done'] = 'flag'
    except Exception:
        flags = pd.DataFrame()

    try:
        adj = pd.read_csv(os.path.join(path_to_qc_files, 'adjustments', f'{station}.csv'),
                          comment='#', skipinitialspace=True)
        adj['what was done'] = adj['adjust_function'] + ' ' + adj['adjust_value'].astype(str)
    except Exception:
        adj = pd.DataFrame()

    try:
        cols = ['t0', 't1', 'variable', 'what was done', 'comment', 'URL_graphic']
        df_flags = pd.concat((flags, adj))[cols].reset_index(drop=True)
    except Exception:
        df_flags = pd.concat((flags, adj)).reset_index(drop=True)

    return df_flags

def load_L1(path_to_l0, station):
    config_file_tx  = os.path.join(path_to_l0, 'tx',  'config', f'{station}.toml')
    config_file_raw = os.path.join(path_to_l0, 'raw', 'config', f'{station}.toml')

    if os.path.isfile(config_file_tx):
        inpath_tx = os.path.join(path_to_l0, 'tx')
        pAWS_tx = AWS(config_file_tx, inpath_tx, var_file=None, meta_file=None,
                      data_issues_repository='../PROMICE-AWS-data-issues')
        pAWS_tx.getL1()
    else:
        pAWS_tx = None

    if os.path.isfile(config_file_raw):
        inpath_raw = os.path.join(path_to_l0, 'raw', station)
        pAWS_raw = AWS(config_file_raw, inpath_raw, var_file=None, meta_file=None,
                       data_issues_repository='../PROMICE-AWS-data-issues')
        pAWS_raw.getL1()
    else:
        pAWS_raw = None

    if pAWS_raw is None and pAWS_tx is None:
        raise FileNotFoundError(f'No raw or tx config for {station}')

    if pAWS_raw is None:
        print('No raw logger file for', station)
        ds = pAWS_tx.L1A.copy(deep=True)
    elif pAWS_tx is None:
        print('No transmission toml file for', station)
        ds = pAWS_raw.L1A.copy(deep=True)
    else:
        print('Combining L1 data for', station)
        ds = pAWS_raw.L1A.combine_first(pAWS_tx.L1A).copy(deep=True)

    ds.attrs['bedrock'] = str(ds.attrs.get('bedrock'))
    ds_save = ds.copy(deep=True)
    return ds, ds_save, pAWS_tx, pAWS_raw




def clean_gps(ds):
    out = ds.copy()
    baseline = (ds.gps_alt.to_series().resample('M').median()
                .reindex(ds.time.to_series().index, method='nearest')
                .ffill().bfill())
    mask = (np.abs(ds.gps_alt - baseline) < 100) | ds.gps_alt.isnull()
    out[['gps_alt','gps_lon','gps_lat']] = out[['gps_alt','gps_lon','gps_lat']].where(mask)
    return out, baseline

def smooth_pose(ds):
    out = ds.copy()
    out['tilt_x'] = station_pose.smooth_tilt_with_moving_window(out['tilt_x'])
    out['tilt_y'] = station_pose.smooth_tilt_with_moving_window(out['tilt_y'])
    out['rot']    = station_pose.interpolate_rotation(out['rot'])
    return out

def compute_cloud_cover(ds):
    out = ds.copy()
    is_bedrock = (out.attrs.get('bedrock') in [True, 'True', 'true'])
    if not is_bedrock:
        sid = out.attrs.get("station_id","")
        if sid == "KAN_M":
            LR_overcast = 315 + 4 * out["t_u"]
            LR_clear    = 30 + 4.6e-13 * (out["t_u"] + air_temperature.T_0) ** 6
        elif sid == "KAN_U":
            LR_overcast = 305 + 4 * out["t_u"]
            LR_clear    = 220 + 3.5 * out["t_u"]
        else:
            LR_overcast, LR_clear = air_temperature.get_cloud_coefficients(out["t_u"])
        out["cc"] = radiation.calculate_cloud_coverage(out["dlr"], LR_overcast, LR_clear)
    else:
        out['cc'] = out['t_u'].copy() * np.nan
    return out

def solar_geometry(ds):
    if 'latitude' in ds.attrs and 'longitude' in ds.attrs:
        lat, lon = ds.attrs['latitude'], ds.attrs['longitude']
    else:
        lat = float(ds['gps_lat'].mean())
        lon = float(ds['gps_lon'].mean())

    doy    = ds['time'].dt.dayofyear
    hour   = ds['time'].dt.hour
    minute = ds['time'].dt.minute

    phi_sensor_rad, theta_sensor_rad = station_pose.calculate_spherical_tilt(ds['tilt_x'], ds['tilt_y'])
    Declination_rad = station_pose.calculate_declination(doy, hour, minute)
    HourAngle_rad   = station_pose.calculate_hour_angle(hour, minute, lon)
    ZenithAngle_rad, ZenithAngle_deg = station_pose.calculate_zenith(lat, Declination_rad, HourAngle_rad)
    AngleDif_deg = station_pose.calculate_angle_difference(ZenithAngle_rad, HourAngle_rad,
                                                           phi_sensor_rad, theta_sensor_rad)
    isr_toa = radiation.calculate_TOA(ZenithAngle_deg, ZenithAngle_rad)

    return {
        "lat": lat, "lon": lon,
        "phi_sensor_rad": phi_sensor_rad,
        "theta_sensor_rad": theta_sensor_rad,
        "Declination_rad": Declination_rad,
        "HourAngle_rad": HourAngle_rad,
        "ZenithAngle_rad": ZenithAngle_rad,
        "ZenithAngle_deg": ZenithAngle_deg,
        "AngleDif_deg": AngleDif_deg,
        "isr_toa":isr_toa
    }

def filter_shortwave(ds, geo):
    ds = ds.copy()
    ds["dsr"], ds["usr"], flags = radiation.filter_sr(
        ds["dsr"], ds["usr"], ds["cc"],
        geo["ZenithAngle_rad"], geo["ZenithAngle_deg"], geo["AngleDif_deg"]
    )
    ds_flags = xr.Dataset(
        {
            "bad": flags[0],
            "sunonlowerdome": flags[1],
            "TOA_crit_nopass_dsr": flags[2],
            "TOA_crit_nopass_usr": flags[3],
        },
        coords={"time": flags[0].time},
    )
    return ds, ds_flags

def correct_shortwave(ds, geo):
    ds = ds.copy()
    ds["dsr_cor"], ds["usr_cor"], TOA_crit_nopass_cor = radiation.correct_sr(
        ds["dsr"], ds["usr"], ds["cc"],
        geo["phi_sensor_rad"], geo["theta_sensor_rad"],
        geo["lat"], geo["Declination_rad"], geo["HourAngle_rad"],
        geo["ZenithAngle_rad"], geo["ZenithAngle_deg"], geo["AngleDif_deg"]
    )
    return ds, TOA_crit_nopass_cor

def compute_albedo(ds, geo):
    ds = ds.copy()
    ds['albedo'], OKalbedos = radiation.calculate_albedo(
        ds["dsr"], ds["usr"], ds["dsr_cor"], ds["cc"],
        geo["ZenithAngle_deg"], geo["AngleDif_deg"]
    )
    return ds, OKalbedos

import xarray as xr
import toml

def run_L2(path_to_l0, path_l2, station):
    config_file_tx  = os.path.join(path_to_l0, 'tx',  'config', f'{station}.toml')
    config_file_raw = os.path.join(path_to_l0, 'raw', 'config', f'{station}.toml')

    pAWS_tx = None
    if os.path.isfile(config_file_tx):
        inpath_tx = os.path.join(path_to_l0, 'tx')
        pAWS_tx = get_l2(config_file_tx, inpath_tx, os.path.join(path_l2, 'tx'), None, None,
                         data_issues_path='../PROMICE-AWS-data-issues')

    pAWS_raw = None
    if os.path.isfile(config_file_raw):
        inpath_raw = os.path.join(path_to_l0, 'raw', station)
        pAWS_raw = get_l2(config_file_raw, inpath_raw, os.path.join(path_l2, 'raw'), None, None,
                          data_issues_path='../PROMICE-AWS-data-issues')

    return pAWS_tx, pAWS_raw

def join_L2(path_l2, station):
    inpath_raw = os.path.join(path_l2, 'raw', station, f'{station}_hour.nc')
    inpath_tx  = os.path.join(path_l2, 'tx',  station, f'{station}_hour.nc')
    return join_l2(inpath_raw, inpath_tx, os.path.join(path_l2, 'level_2'), None, None)

def open_l2_clean(path_l2, station):
    inpath = os.path.join(path_l2, 'level_2', station, f'{station}_hour.nc')
    with xr.open_dataset(inpath) as l2:
        l2.load()
    for varname in l2.variables:
        if l2[varname].encoding != {}:
            l2[varname].encoding = {}
    if 'bedrock' in l2.attrs:
        l2.attrs['bedrock'] = (l2.attrs['bedrock'] == 'True')
    if 'number_of_booms' in l2.attrs:
        l2.attrs['number_of_booms'] = int(l2.attrs['number_of_booms'])
    return l2

def load_station_config(config_folder, station_id):
    with open(os.path.join(config_folder, f'{station_id}.toml')) as fp:
        return toml.load(fp)
