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
from pypromice.core.qc.github_data_issues import adjustData
from pypromice.core.variables import (station_pose,
                                      radiation,
                                      air_temperature,
                                      precipitation,
                                      station_boom_height)

from pypromice.pipeline.get_l2 import get_l2
from pypromice.pipeline.join_l2 import join_l2

from pypromice.pipeline.L2toL3 import (get_thermistor_depth,
                                   hampel)


from sklearn.linear_model import LinearRegression



import matplotlib.pyplot as plt
import imageio.v2 as imageio

import logging
logger = logging.getLogger(__name__)

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



def process_surface_height(ds, data_adjustments_dir, station_config={}):
    """
    Process surface height data for different site types and create
    surface height variables.

    Parameters
    ----------
    ds : xarray.Dataset
        The dataset containing various measurements and attributes including
        'site_type' which determines the type of site (e.g., 'ablation',
        'accumulation', 'bedrock') and other relevant data variables such as
        'z_boom_u', 'z_stake', 'z_pt_cor', etc.

    Returns
    -------
    xarray.Dataset
        The dataset with additional processed surface height variables:
        'z_surf_1', 'z_surf_2', 'z_ice_surf', 'z_surf_combined', 'snow_height',
        and possibly depth variables derived from temperature measurements.
    """
    # Initialize surface height variables with NaNs
    ds['z_surf_1'] = ('time', ds['z_boom_u'].data * np.nan)
    ds['z_surf_2'] = ('time', ds['z_boom_u'].data * np.nan)

    z_boom_best_u = station_boom_height.include_uncorrected_values(
                                ds["z_boom_u"],
                                ds["z_boom_cor_u"],
                                ds["t_u"],
                                ds["t_l"] if "t_l" in ds.data_vars else None,
                                ds["t_rad"] if "t_rad" in ds.data_vars else None)



    if 'z_stake' in ds.data_vars and ds.z_stake.notnull().any():
        # Calculate stake boom height correction with uncorrected values where needed
        z_stake_best = station_boom_height.include_uncorrected_values(
                                    ds["z_stake"],
                                    ds["z_stake_cor"],
                                    ds["t_u"],
                                    ds["t_l"] if "t_l" in ds.data_vars else None,
                                    ds["t_rad"] if "t_rad" in ds.data_vars else None)

    if ds.attrs['site_type'] == 'ablation':
        # Calculate surface heights for ablation sites
        ds['z_surf_1'] = 2.6 - z_boom_best_u
        if ds.z_stake.notnull().any():
            first_valid_index = ds.time.where((z_stake_best + z_boom_best_u).notnull(), drop=True).data[0]
            ds['z_surf_2'] = ds.z_surf_1.sel(time=first_valid_index) + z_stake_best.sel(time=first_valid_index) - z_stake_best

        # Use corrected point data if available
        if 'z_pt_cor' in ds.data_vars:
            ds['z_ice_surf'] = ('time', ds['z_pt_cor'].data)

    else:
        # Calculate surface heights for other site types
        first_valid_index = ds.time.where(z_boom_best_u.notnull(), drop=True).data[0]
        ds['z_surf_1'] = z_boom_best_u.sel(time=first_valid_index) - z_boom_best_u

        if 'z_stake' in ds.data_vars and ds.z_stake.notnull().any():
            first_valid_index = ds.time.where(z_stake_best.notnull(), drop=True).data[0]
            ds['z_surf_2'] = z_stake_best.sel(time=first_valid_index) - z_stake_best

        if 'z_boom_l' in ds.data_vars:

            # Calculate lower boom height correction with uncorrected values where needed
            z_boom_best_l = station_boom_height.include_uncorrected_values(
                                        ds["z_boom_l"],
                                        ds["z_boom_cor_l"],
                                        ds["t_l"],
                                        ds["t_u"] if "t_u" in ds.data_vars else None,
                                        ds["t_rad"] if "t_rad" in ds.data_vars else None)

            # need a combine first because KAN_U switches from having a z_stake_best
            # to having a z_boom_best_l
            first_valid_index = ds.time.where(z_boom_best_l.notnull(), drop=True).data[0]
            ds['z_surf_2'] = ds['z_surf_2'].combine_first(
                z_boom_best_l.sel(time=first_valid_index) - z_boom_best_l)

    # Adjust data for the created surface height variables
    ds = adjustData(ds, data_adjustments_dir, var_list=['z_surf_1', 'z_surf_2', 'z_ice_surf'])

    # Convert to dataframe and combine surface height variables
    df_in = ds[[v for v in ['z_surf_1', 'z_surf_2', 'z_ice_surf'] if v in ds.data_vars]].to_dataframe()

    (ds['z_surf_combined'], ds['z_ice_surf'],
     ds['z_surf_1_adj'], ds['z_surf_2_adj']) = combine_surface_height(df_in, ds.attrs['site_type'], station=station_config['stid'])


    if ds.attrs['site_type'] == 'ablation':
        # Calculate rolling minimum for ice surface height and snow height
        ts_interpolated = np.minimum(
            xr.where(ds.z_ice_surf.notnull(),
                     ds.z_ice_surf,ds.z_surf_combined),
            ds.z_surf_combined).to_series().resample('h').interpolate(limit=72)

        if len(ts_interpolated)>24*7:
            # Apply the rolling window with median calculation
            z_ice_surf = (ts_interpolated
                          .rolling('14D', center=True, min_periods=1)
                          .median())
            # Overprint the first and last 7 days with interpolated values
            # because of edge effect of rolling windows
            z_ice_surf.iloc[:24*7] = (ts_interpolated.iloc[:24*7]
                                      .rolling('1D', center=True, min_periods=1)
                                      .median().values)
            z_ice_surf.iloc[-24*7:] = (ts_interpolated.iloc[-24*7:]
                                       .rolling('1D', center=True, min_periods=1)
                                       .median().values)
        else:
            z_ice_surf = (ts_interpolated
                                       .rolling('1D', center=True, min_periods=1)
                                       .median())

        z_ice_surf = z_ice_surf.reindex(ds.time,
                                        method=None).interpolate(method='time')

        # here we make sure that the periods where both z_stake_best and z_pt are
        # missing are also missing in z_ice_surf
        msk = ds['z_ice_surf'].notnull() | ds['z_surf_2_adj'].notnull()
        z_ice_surf = z_ice_surf.where(msk)

        # taking running minimum to get ice
        z_ice_surf = z_ice_surf.cummin()

        # filling gaps only if they are less than a year long and if values on both
        # sides are less than 0.01 m appart

        # Forward and backward fill to identify bounds of gaps
        df_filled = z_ice_surf.ffill().bfill()

        # Identify gaps and their start and end dates
        gaps = pd.DataFrame(index=z_ice_surf[z_ice_surf.isna()].index)
        gaps['prev_value'] = df_filled.shift(1)
        gaps['next_value'] = df_filled.shift(-1)
        gaps['gap_start'] = gaps.index.to_series().shift(1)
        gaps['gap_end'] = gaps.index.to_series().shift(-1)
        gaps['gap_duration'] = (gaps['gap_end'] - gaps['gap_start']).dt.days
        gaps['value_diff'] = (gaps['next_value'] - gaps['prev_value']).abs()

        # Determine which gaps to fill
        mask = (gaps['gap_duration'] < 365) & (gaps['value_diff'] < 0.01)
        gaps_to_fill = gaps[mask].index

        # Fill gaps in the original Series
        z_ice_surf.loc[gaps_to_fill] = df_filled.loc[gaps_to_fill]

        # bringing the variable into the dataset
        ds['z_ice_surf'] = ('time', z_ice_surf.values)

        ds['z_surf_combined'] = np.maximum(ds['z_surf_combined'], ds['z_ice_surf'])
        ds['snow_height'] = np.maximum(0, ds['z_surf_combined'] - ds['z_ice_surf'])
        ds['z_ice_surf'] = ds['z_ice_surf'].where(ds.snow_height.notnull())
    elif ds.attrs['site_type'] in ['accumulation', 'bedrock']:
        # Handle accumulation and bedrock site types
        ds['z_ice_surf'] = ('time', ds['z_surf_1'].data * np.nan)
        ds['snow_height'] = ds['z_surf_combined']
    else:
        # Log info for other site types
        logger.info('other site type')

    if ds.attrs['site_type'] != 'bedrock':
        # Process ice temperature data and create depth variables
        ice_temp_vars = [v for v in ds.data_vars if 't_i_' in v]
        vars_out = [v.replace('t', 'd_t') for v in ice_temp_vars]
        vars_out.append('t_i_10m')

        # df_out = get_thermistor_depth(
        #     ds[ice_temp_vars + ['z_surf_combined']].to_dataframe(),
        #     ds.attrs['station_id'],
        #     station_config)
        # for var in df_out.columns:
        #     ds[var] = ('time', df_out[var].values)

    return ds


from matplotlib.patches import Rectangle

def plot_series_to_frame(hs1, hs2, z, series, title, add_rectangle=True):
    fig, ax = plt.subplots(figsize=(10,8),dpi=220)
    ax.plot(hs1.index, hs1.values, color='tab:blue',  lw=2)
    ax.plot(hs2.index, hs2.values, color='tab:orange', lw=2)
    ax.plot(z.index, z.values, color='tab:green', lw=2)
    ax.plot(series.index, series.values, color='lightgray', lw=3)

    if add_rectangle:
        rect = Rectangle((series.index[0]-pd.Timedelta("60D"), series.values[0]-1.5),
                 pd.Timedelta("120D"), 3, fill=False, color='red', lw=2,
                 transform=ax.transData)
        ax.add_patch(rect)

    ax.set_title(title)
    ax.set_xlabel("Time")
    ax.set_ylabel("Height (m)")
    # ax.set_ylim(-10,10)
    fig.tight_layout()

    fig.canvas.draw()
    img = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    plt.close(fig)
    return img

def plot_final_frame(hs1, hs2, z, series, title):
    fig, ax = plt.subplots(figsize=(10,8),dpi=220)
    ax.plot(hs1.index, hs1.values, color='tab:blue',  alpha=0.5, lw=2)
    ax.plot(hs2.index, hs2.values, color='tab:orange',  alpha=0.5, lw=2)
    ax.plot(z.index, z.values, color='tab:green',  alpha=0.5, lw=2)
    ax.plot(series.index, series.values, color='k', lw=4)

    ax.set_title(title)
    ax.set_xlabel("Time")
    ax.set_ylabel("Height (m)")
    # ax.set_ylim(-10,10)
    fig.tight_layout()

    fig.canvas.draw()
    img = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    plt.close(fig)
    return img

def animate_adjustment(frames, hs1, hs2, z, series, idx_start, shift, title_prefix, n_snapshot=8):
    s_base = series.copy()

    for k in range(1, n_snapshot + 1):
        s_step = s_base.copy()
        partial_shift = shift * (k / n_snapshot)
        s_step.loc[idx_start:] = s_base.loc[idx_start:] + partial_shift

        title = f"{title_prefix} ({k}/{n_snapshot})"
        frame = plot_series_to_frame(hs1, hs2, z, s_step.loc[idx_start:], title)
        frames.append(frame)

def combine_surface_height(df, site_type, threshold_ablation = -0.0002, station="station"):
    '''Combines the data from three sensor: the two sonic rangers and the
    pressure transducer, to recreate the surface height, the ice surface height
    and the snow depth through the years. For the accumulation sites, it is
    only the average of the two sonic rangers (after manual adjustments to
    correct maintenance shifts). For the ablation sites, first an ablation
    period is estimated each year (either the period when z_pt_cor decreases
    or JJA if no better estimate) then different adjustmnents are conducted
    to stitch the three time series together: z_ice_surface (adjusted from
    z_pt_cor) or if unavailable, z_surf_2 (adjusted from z_stake)
    are used in the ablation period while an average of z_surf_1 and z_surf_2
    are used otherwise, after they are being adjusted to z_ice_surf at the end
    of the ablation season.

    Parameters
    ----------
    df : pandas.dataframe
        Dataframe with datetime index and variables z_surf_1, z_surf_2 and z_ice_surf
    site_type : str
        Either 'accumulation' or 'ablation'
    threshold_ablation : float
        Threshold to which a z_pt_cor hourly decrease is compared. If the decrease
        is higher, then there is ablation.
    '''
    logger.info('Combining surface height')
    frames = []      # ONE list for the whole processing


    if 'z_surf_2' not in df.columns:
        logger.info('-> did not find z_surf_2')
        df["z_surf_2"] = df["z_surf_1"].values*np.nan

    if 'z_ice_surf' not in df.columns:
        logger.info('-> did not find z_ice_surf')
        df["z_ice_surf"] = df["z_surf_1"].values*np.nan

    if site_type in ['accumulation', 'bedrock']:
        logger.info('-> no z_pt or accumulation site: averaging z_surf_1 and z_surf_2')
        df["z_surf_1_adj"] = hampel(df["z_surf_1"].interpolate(limit=72)).values
        df["z_surf_2_adj"] = hampel(df["z_surf_2"].interpolate(limit=72)).values
        # adjusting z_surf_2 to z_surf_1
        df["z_surf_2_adj"]  = df["z_surf_2_adj"]  + (df["z_surf_1_adj"]- df["z_surf_2_adj"]).mean()
        # z_surf_combined is the average of the two z_surf
        if df.z_surf_1_adj.notnull().any() & df.z_surf_2_adj.notnull().any():
            df['z_surf_combined'] = df[['z_surf_1_adj', 'z_surf_2_adj']].mean(axis = 1).values
        elif df.z_surf_1_adj.notnull().any():
            df['z_surf_combined'] = df.z_surf_1_adj.values
        elif df.z_surf_2_adj.notnull().any():
            df['z_surf_combined'] = df.z_surf_2_adj.values

        # df["z_surf_combined"] = hampel(df["z_surf_combined"].interpolate(limit=72)).values
        return (df['z_surf_combined'], df["z_surf_combined"]*np.nan,
                    df["z_surf_1_adj"], df["z_surf_2_adj"])

    else:
        logger.info('-> ablation site')
        # smoothing and filtering pressure transducer data
        df["z_ice_surf_adj"] = hampel(df["z_ice_surf"].interpolate(limit=72)).values
        df["z_surf_1_adj"] = hampel(df["z_surf_1"].interpolate(limit=72)).values
        df["z_surf_2_adj"] = hampel(df["z_surf_2"].interpolate(limit=72)).values

        df["z_surf_1_adj"] = hampel(df["z_surf_1"].interpolate(limit=72), k=24, t0=5).values
        df["z_surf_2_adj"] = hampel(df["z_surf_2"].interpolate(limit=72), k=24, t0=5).values

        # defining ice ablation period from the decrease of a smoothed version of z_pt
        # meaning when smoothed_z_pt.diff() < threshold_ablation
        hourly_interp = (df["z_ice_surf"]
                         .resample("h")
                         .interpolate(limit=72))
        once_smoothed = hourly_interp.rolling("14D", center=True, min_periods=1).mean()
        smoothed_PT = once_smoothed.rolling("14D", center=True, min_periods=1).mean()

        # ablation detection
        diff_series = smoothed_PT.diff()
        ind_ablation = np.full_like(diff_series, False, dtype=bool)
        ind_ablation = np.logical_and(diff_series.values < threshold_ablation,
                                      np.isin(diff_series.index.month, [6, 7, 8, 9]))
        # making sure that we only qualify as ablation timestamps where we actually have ablation data
        msk = np.isnan(smoothed_PT.values)
        ind_ablation[msk] = False

        # reindex back to df
        smoothed_PT = smoothed_PT.reindex(df.index, method="ffill")
        ind_ablation = pd.Series(ind_ablation, index=diff_series.index).reindex(df.index, fill_value=False).values

        # finding the beginning and end of each period with True
        idx = np.argwhere(np.diff(np.r_[False,ind_ablation, False])).reshape(-1, 2)
        idx[:, 1] -= 1

        # fill small gaps in the ice ablation periods.
        for i in range(len(idx)-1):
            ind = idx[i]
            ind_next = idx[i+1]
            # if the end of an ablation period is less than 60 days away from
            # the next ablation, then it is still considered like the same ablation
            # season
            if df.index[ind_next[0]]-df.index[ind[1]]<pd.to_timedelta('60 days'):
                ind_ablation[ind[1]:ind_next[0]]=True

        # finding the beginning and end of each period with True
        idx = np.argwhere(np.diff(np.r_[False,ind_ablation, False])).reshape(-1, 2)
        idx[:, 1] -= 1
        # because the smooth_PT sees 7 days ahead, it starts showing a decline
        # 7 days in advance, we therefore need to exclude the first few days of
        # each ablation period
        for start, end in idx:
            period_start = df.index[start]
            period_end = period_start + pd.Timedelta(days=3)
            exclusion_period = (df.index >= period_start) & (df.index < period_end)
            ind_ablation[exclusion_period] = False

        hs1=df["z_surf_1_adj"].interpolate(limit=24*2).copy()
        hs2=df["z_surf_2_adj"].interpolate(limit=24*2).copy()
        z=df["z_ice_surf_adj"].interpolate(limit=24*2).copy()

        # the surface heights are adjusted so that they start at 0
        if any(~np.isnan(hs2.iloc[:24*7])):
            hs2 = hs2 - hs2.iloc[:24*7].mean()

        if any(~np.isnan(hs2.iloc[:24*7])) & any(~np.isnan(hs1.iloc[:24*7])):
            hs2 = hs2 + hs1.iloc[:24*7].mean() - hs2.iloc[:24*7].mean()

        if any(~np.isnan(z.iloc[:24*7])):
            # expressing ice surface height relative to its mean value in the
            # first week of the record
            z = z - z.iloc[:24*7].mean()
        elif z.notnull().any():
            # if there is no data in the first week but that there are some
            # PT data afterwards
            if ((z.first_valid_index() - hs1.first_valid_index()) < pd.to_timedelta('251D')) &\
              ((z.first_valid_index() - hs1.first_valid_index()) > pd.to_timedelta('0H')):
                # if the pressure transducer is installed the year after then
                # we use the mean surface height 1 on its first week as a 0
                # for the ice height
                z = z - z.loc[
                    z.first_valid_index():(z.first_valid_index()+pd.to_timedelta('14D'))
                    ].mean() + hs1.iloc[:24*7].mean()
            else:
                # if there is more than a year (actually 251 days) between the
                # initiation of the AWS and the installation of the pressure transducer
                # we remove the intercept in the pressure transducer data.
                # Removing the intercept
                # means that we consider the ice surface height at 0 when the AWS
                # is installed, and not when the pressure transducer is installed.
                Y = z.iloc[:].values.reshape(-1, 1)
                X = z.iloc[~np.isnan(Y)].index.astype(np.int64).values.reshape(-1, 1)
                Y = Y[~np.isnan(Y)]
                linear_regressor = LinearRegression()
                linear_regressor.fit(X, Y)
                Y_pred = linear_regressor.predict(z.index.astype(np.int64).values.reshape(-1, 1) )
                z = z-Y_pred[0]

        years = df.index.year.unique().values
        ind_start = years.copy()
        ind_end =  years.copy()
        logger.debug('-> estimating ablation period for each year')
        for i, y in enumerate(years):
            # for each year
            ind_yr = df.index.year.values==y
            ind_abl_yr = np.logical_and(ind_yr, ind_ablation)

            if df.loc[
                    np.logical_and(ind_yr, df.index.month.isin([6,7,8])),
                    "z_ice_surf_adj"].isnull().all():

                ind_abl_yr = np.logical_and(ind_yr, df.index.month.isin([6,7,8]))
                ind_ablation[ind_yr] = ind_abl_yr[ind_yr]
                logger.debug(str(y)+' no z_ice_surf, just using JJA')

            else:
                logger.debug(str(y)+ ' derived from z_ice_surf')

            if np.any(ind_abl_yr):
                # if there are some ablation flagged for that year
                # then find begining and end
                ind_start[i] = np.argwhere(ind_abl_yr)[0][0]
                ind_end[i] = np.argwhere(ind_abl_yr)[-1][0]

            else:
                logger.debug(str(y) + ' could not estimate ablation season')
                # otherwise left as nan
                ind_start[i] = -999
                ind_end[i] = -999

        # adjustement loop
        missing_hs2 = 0 # if hs2 is missing then when it comes back it is adjusted to hs1
        hs2_ref = 0 # by default, the PT is the reference: hs1 and 2 will be adjusted to PT
        # but if it is missing one year or one winter, then it needs to be rajusted
        # to hs1 and hs2 the year after.

        for i, y in enumerate(years):
            logger.debug(f'{y}: Ablation from {z.index[ind_start[i]]} to {z.index[ind_end[i]]}')

            # defining subsets of hs1, hs2, z
            hs1_jja =  hs1[str(y)+'-06-01':str(y)+'-09-01']
            hs2_jja =  hs2[str(y)+'-06-01':str(y)+'-09-01']
            z_jja =  z[str(y)+'-06-01':str(y)+'-09-01']

            z_ablation = z.iloc[ind_start[i]:ind_end[i]]
            hs2_ablation = hs2.iloc[ind_start[i]:ind_end[i]]

            hs1_year = hs1[str(y)]
            hs2_year = hs2[str(y)]

            hs2_winter = hs2[str(y)+'-01-01':str(y)+'-03-01'].copy()
            z_winter = z[str(y)+'-01-01':str(y)+'-03-01'].copy()

            z_year = z[str(y)]
            if hs1_jja.isnull().all() and hs2_jja.isnull().all() and z_jja.isnull().all():
                    # if there is no height for a year between June and September
                    # then the adjustment cannot be made automatically
                    # it needs to be specified manually on the adjustment files
                    # on https://github.com/GEUS-Glaciology-and-Climate/PROMICE-AWS-data-issues
                    continue

            if all(np.isnan(z_jja)) and any(~np.isnan(hs2_jja)):
                # if there is no PT for a given year, but there is some hs2
                # then z will be adjusted to hs2 next time it is available
                hs2_ref = 1

            if all(np.isnan(z_winter)) and all(np.isnan(hs2_winter)):
                # if there is no PT nor hs2 during the winter, then again
                # we need to adjust z to match hs2 when ablation starts
                hs2_ref = 1

            # adjustment at the start of the ablation season
            if hs2_ref:
                # if hs2 has been taken as reference in the previous years
                # then we check if pressure transducer is reinstalled and needs
                # to be adjusted
                if ind_start[i] != -999:
                    # the first year there is both ablation and PT data available
                    # then PT is adjusted to hs2
                    if any(~np.isnan(z_ablation)) and any(~np.isnan(hs2_ablation)):
                        tmp1 = z_ablation.copy()
                        tmp2 = hs2_ablation.copy()
                        # tmp1[np.isnan(tmp2)] = np.nan
                        # tmp2[np.isnan(tmp1)] = np.nan

                        # in some instances, the PT data is available but no ablation
                        # is recorded, then hs2 remains the reference during that time.
                        # When eventually there is ablation, then we need to find the
                        # first index in these preceding ablation-free years
                        # the shift will be applied back from this point
                        # first_index = z[:z[str(y)].first_valid_index()].isnull().iloc[::-1].idxmax()
                        # z[first_index:] = z[first_index:] -  np.nanmean(tmp1)  +  np.nanmean(tmp2)
                        # hs2_ref = 0 # from now on PT is the reference

                        # in some other instance, z just need to be adjusted to hs2
                        # first_index = z[str(y)].first_valid_index()
                        first_index = z.iloc[ind_start[i]:].first_valid_index() # of ablation
                        if np.isnan(hs2[first_index]):
                            first_index_2 = hs2.iloc[ind_start[i]:].first_valid_index()
                            if (first_index_2 - first_index)>pd.Timedelta('30d'):
                                logger.debug('adjusting z to hs1')
                                if np.isnan(hs1[first_index]):
                                    first_index = hs1.iloc[ind_start[i]:].first_valid_index()

                                shift =-  z[first_index]   +  hs1[first_index]
                                animate_adjustment(frames,hs1, hs2, z,  z, first_index, shift, title_prefix=str(y))

                                z[first_index:] = z[first_index:] -  z[first_index]   +  hs1[first_index]
                            else:
                                logger.debug('adjusting z to hs1')
                                first_index = hs2.iloc[ind_start[i]:].first_valid_index()

                                shift =-  z[first_index]   +  hs2[first_index]
                                animate_adjustment(frames, hs1, hs2, z, z, first_index, shift, title_prefix=str(y))

                                z[first_index:] = z[first_index:] -  z[first_index]   +  hs2[first_index]
                        else:
                            logger.debug('adjusting z to hs1')

                            shift =-  z[first_index]   +  hs2[first_index]
                            animate_adjustment(frames, hs1, hs2, z, z, first_index, shift, title_prefix=str(y))

                            z[first_index:] = z[first_index:] -  z[first_index]   +  hs2[first_index]
                        hs2_ref = 0 # from now on PT is the reference


            else:
                # if z_pt is the reference and there is some ablation
                # then hs1 and hs2 are adjusted to z_pt
                if (ind_start[i] != -999) & z_year.notnull().any():
                    # calculating first index with PT, hs1 and hs2
                    first_index = z_year.first_valid_index()
                    if hs1_year.notnull().any():
                        first_index = np.max(np.array(
                            [first_index,
                             hs1_year.first_valid_index()]))
                    if hs2_year.notnull().any():
                        first_index = np.max(np.array(
                            [first_index,
                             hs2_year.first_valid_index()]))

                    # if PT, hs1 and hs2 are all nan until station is reactivated, then
                    first_day_of_year = pd.to_datetime(str(y)+'-01-01')

                    if len(z[first_day_of_year:first_index-pd.to_timedelta('1D')])>0:
                        if z[first_day_of_year:first_index-pd.to_timedelta('1D')].isnull().all() & \
                            hs1[first_day_of_year:first_index-pd.to_timedelta('1D')].isnull().all() & \
                                hs2[first_day_of_year:first_index-pd.to_timedelta('1D')].isnull().all():
                                if (~np.isnan(np.nanmean(z[first_index:first_index+pd.to_timedelta('1D')])) \
                                    and ~np.isnan(np.nanmean(hs2[first_index:first_index+pd.to_timedelta('1D')]))):
                                    logger.debug(' ======= adjusting hs1 and hs2 to z_pt')
                                    if ~np.isnan(np.nanmean(hs1[first_index:first_index+pd.to_timedelta('1D')]) ):

                                        shift = -  np.nanmean(hs1[first_index:first_index+pd.to_timedelta('1D')])  \
                                             +  np.nanmean(z[first_index:first_index+pd.to_timedelta('1D')])
                                        animate_adjustment(frames, hs1, hs2, z, hs1, first_index, shift, title_prefix=str(y))

                                        hs1[first_index:] = hs1[first_index:] \
                                            -  np.nanmean(hs1[first_index:first_index+pd.to_timedelta('1D')])  \
                                                +  np.nanmean(z[first_index:first_index+pd.to_timedelta('1D')])
                                    if ~np.isnan(np.nanmean(hs2[first_index:first_index+pd.to_timedelta('1D')]) ):

                                        shift =-  np.nanmean(hs2[first_index:first_index+pd.to_timedelta('1D')])  \
                                            +  np.nanmean(z[first_index:first_index+pd.to_timedelta('1D')])
                                        animate_adjustment(frames, hs1, hs2, z, hs2, first_index, shift, title_prefix=str(y))

                                        hs2[first_index:] = hs2[first_index:] \
                                            -  np.nanmean(hs2[first_index:first_index+pd.to_timedelta('1D')])  \
                                                +  np.nanmean(z[first_index:first_index+pd.to_timedelta('1D')])

            # adjustment taking place at the end of the ablation period
            if (ind_end[i] != -999):
                # if y == 2023:
                #     import pdb; pdb.set_trace()
                # if there's ablation and
                # if there are PT data available at the end of the melt season
                if z.iloc[(ind_end[i]-24*7):ind_end[i]].notnull().any():
                    logger.debug('adjusting hs2 to z')
                    # then we adjust hs2 to the end-of-ablation z
                    # first trying at the end of melt season
                    if ~np.isnan(np.nanmean(hs2.iloc[(ind_end[i]-24*7):(ind_end[i]+24*30)])):
                        logger.debug('using end of melt season')

                        shift = - np.nanmean(hs2.iloc[(ind_end[i]-24*7):(ind_end[i]+24*30)])  + \
                             np.nanmean(z.iloc[(ind_end[i]-24*7):(ind_end[i]+24*30)])
                        animate_adjustment(frames, hs1, hs2, z, hs2, first_index, shift, title_prefix=str(y))

                        hs2.iloc[ind_end[i]:] = hs2.iloc[ind_end[i]:] - \
                            np.nanmean(hs2.iloc[(ind_end[i]-24*7):(ind_end[i]+24*30)])  + \
                                np.nanmean(z.iloc[(ind_end[i]-24*7):(ind_end[i]+24*30)])
                    # if not possible, then trying the end of the following accumulation season
                    elif (i+1 < len(ind_start)):
                        if ind_start[i+1]!=-999 and any(~np.isnan(hs2.iloc[(ind_start[i+1]-24*7):(ind_start[i+1]+24*7)]+ z.iloc[(ind_start[i+1]-24*7):(ind_start[i+1]+24*7)])):
                            logger.debug('using end of accumulation season')

                            shift = - np.nanmean(hs2.iloc[(ind_start[i+1]-24*7):(ind_start[i+1]+24*7)])  + \
                                np.nanmean(z.iloc[(ind_start[i+1]-24*7):(ind_start[i+1]+24*7)])
                            animate_adjustment(frames, hs1, hs2, z, hs2, first_index, shift, title_prefix=str(y))

                            hs2.iloc[ind_end[i]:] = hs2.iloc[ind_end[i]:] - \
                                np.nanmean(hs2.iloc[(ind_start[i+1]-24*7):(ind_start[i+1]+24*7)])  + \
                                    np.nanmean(z.iloc[(ind_start[i+1]-24*7):(ind_start[i+1]+24*7)])
            else:
                logger.debug('no ablation data')
                hs1_following_winter = hs1[str(y)+'-09-01':str(y+1)+'-03-01'].copy()
                hs2_following_winter = hs2[str(y)+'-09-01':str(y+1)+'-03-01'].copy()
                if all(np.isnan(hs2_following_winter)):
                    logger.debug('no hs2')
                    missing_hs2 = 1
                elif missing_hs2 == 1:
                    logger.debug('adjusting hs2')
                    # and if there are some hs2 during the accumulation period
                    if any(~np.isnan(hs1_following_winter)):
                        logger.debug('to hs1')
                        # then we adjust hs1 to hs2 during the accumulation area
                        # adjustment is done so that the mean hs1 and mean hs2 match
                        # for the period when both are available
                        hs2_following_winter[np.isnan(hs1_following_winter)] = np.nan
                        hs1_following_winter[np.isnan(hs2_following_winter)] = np.nan

                        shift = -  np.nanmean(hs2_following_winter)  +  np.nanmean(hs1_following_winter)
                        animate_adjustment(frames, hs1, hs2, z, hs2, str(y)+'-01-01', shift, title_prefix=str(y))


                        hs2[str(y)+'-01-01':] = hs2[str(y)+'-01-01':] \
                            -  np.nanmean(hs2_following_winter)  +  np.nanmean(hs1_following_winter)
                        missing_hs2 = 0


                hs1_following_winter = hs1[str(y)+'-09-01':str(y+1)+'-03-01'].copy()
                hs2_following_winter = hs2[str(y)+'-09-01':str(y+1)+'-03-01'].copy()
                # adjusting hs1 to hs2 (no ablation case)
                if any(~np.isnan(hs1_following_winter)):
                    logger.debug('adjusting hs1')
                    # and if there are some hs2 during the accumulation period
                    if any(~np.isnan(hs2_following_winter)):
                        logger.debug('to hs2')
                        # then we adjust hs1 to hs2 during the accumulation area
                        # adjustment is done so that the mean hs1 and mean hs2 match
                        # for the period when both are available
                        hs1_following_winter[np.isnan(hs2_following_winter)] = np.nan
                        hs2_following_winter[np.isnan(hs1_following_winter)] = np.nan

                        shift = -  np.nanmean(hs1_following_winter)  +  np.nanmean(hs2_following_winter)
                        animate_adjustment(frames, hs1, hs2, z, hs1, str(y)+'-09-01', shift, title_prefix=str(y))

                        hs1[str(y)+'-09-01':] = hs1[str(y)+'-09-01':] \
                            -  np.nanmean(hs1_following_winter)  +  np.nanmean(hs2_following_winter)
                        hs1_following_winter = hs1[str(y)+'-09-01':str(y+1)+'-03-01'].copy()

            if ind_end[i] != -999:
                # if there is some hs1
                hs1_following_winter = hs1[str(y)+'-09-01':str(y+1)+'-03-01'].copy()
                hs2_following_winter = hs2[str(y)+'-09-01':str(y+1)+'-03-01'].copy()
                if any(~np.isnan(hs1_following_winter)):
                    logger.debug('adjusting hs1')
                    # and if there are some hs2 during the accumulation period
                    if any(~np.isnan(hs2_following_winter)):
                        logger.debug('to hs2, minimizing winter difference')
                        # then we adjust hs1 to hs2 during the accumulation area
                        # adjustment is done so that the mean hs1 and mean hs2 match
                        # for the period when both are available
                        tmp1 = hs1.iloc[ind_end[i]:min(len(hs1),ind_end[i]+24*30*9)].copy()
                        tmp2 = hs2.iloc[ind_end[i]:min(len(hs2),ind_end[i]+24*30*9)].copy()

                        tmp1[np.isnan(tmp2)] = np.nan
                        tmp2[np.isnan(tmp1)] = np.nan
                        if tmp1.isnull().all():
                            tmp1 = hs1_following_winter.copy()
                            tmp2 = hs2_following_winter.copy()

                            tmp1[np.isnan(tmp2)] = np.nan
                            tmp2[np.isnan(tmp1)] = np.nan

                            shift =  -  np.nanmean(tmp1)  +  np.nanmean(tmp2)
                            animate_adjustment(frames, hs1, hs2, z, hs1, hs1.index[ind_end[i]], shift, title_prefix=str(y))

                        hs1.iloc[ind_end[i]:] = hs1.iloc[ind_end[i]:] -  np.nanmean(tmp1)  +  np.nanmean(tmp2)

                    # if no hs2, then use PT data available at the end of the melt season
                    elif np.any(~np.isnan(z.iloc[(ind_end[i]-24*14):(ind_end[i]+24*7)])):
                        logger.debug('to z')
                        # then we adjust hs2 to the end-of-ablation z
                        # first trying at the end of melt season
                        if ~np.isnan(np.nanmean(hs1.iloc[(ind_end[i]-24*14):(ind_end[i]+24*30)])):
                            logger.debug('using end of melt season')

                            shift =  -np.nanmean(hs1.iloc[(ind_end[i]-24*14):(ind_end[i]+24*30)])  + \
                                np.nanmean(z.iloc[(ind_end[i]-24*14):(ind_end[i]+24*30)])
                            animate_adjustment(frames, hs1, hs2, z, hs1, hs1.index[ind_end[i]], shift, title_prefix=str(y))

                            hs1.iloc[ind_end[i]:] = hs1.iloc[ind_end[i]:] - \
                                np.nanmean(hs1.iloc[(ind_end[i]-24*14):(ind_end[i]+24*30)])  + \
                                    np.nanmean(z.iloc[(ind_end[i]-24*14):(ind_end[i]+24*30)])
                        # if not possible, then trying the end of the following accumulation season
                        elif ind_start[i+1]!=-999 and any(~np.isnan(hs1.iloc[(ind_start[i+1]-24*14):(ind_start[i+1]+24*7)]+ z.iloc[(ind_start[i+1]-24*14):(ind_start[i+1]+24*7)])):
                            logger.debug('using end of accumulation season')

                            shift =  -np.nanmean(hs1.iloc[(ind_start[i+1]-24*14):(ind_start[i+1]+24*7)])  + \
                                np.nanmean(z.iloc[(ind_start[i+1]-24*14):(ind_start[i+1]+24*7)])
                            animate_adjustment(frames, hs1, hs2, z, hs1, hs1.index[ind_end[i]], shift, title_prefix=str(y))

                            hs1.iloc[ind_end[i]:] = hs1.iloc[ind_end[i]:] - \
                                np.nanmean(hs1.iloc[(ind_start[i+1]-24*14):(ind_start[i+1]+24*7)])  + \
                                    np.nanmean(z.iloc[(ind_start[i+1]-24*14):(ind_start[i+1]+24*7)])
                    elif any(~np.isnan(hs2_year)):
                        logger.debug('to the last value of hs2')
                        # then we adjust hs1 to hs2 during the accumulation area
                        # adjustment is done so that the mean hs1 and mean hs2 match
                        # for the period when both are available
                        half_span = pd.to_timedelta('7D')
                        tmp1 = hs1_year.loc[(hs2_year.last_valid_index()-half_span):(hs2_year.last_valid_index()+half_span)].copy()
                        tmp2 = hs2_year.loc[(hs2_year.last_valid_index()-half_span):(hs2_year.last_valid_index()+half_span)].copy()


                        shift =   -  np.nanmean(tmp1)  +  np.nanmean(tmp2)
                        animate_adjustment(frames, hs1, hs2, z, hs1, hs1.index[ind_end[i]], shift, title_prefix=str(y))

                        hs1.iloc[ind_end[i]:] = hs1.iloc[ind_end[i]:] -  np.nanmean(tmp1)  +  np.nanmean(tmp2)

        df["z_surf_1_adj"] = hs1.interpolate(limit=2*24).values
        df["z_surf_2_adj"] = hs2.interpolate(limit=2*24).values
        df["z_ice_surf_adj"] = z.interpolate(limit=2*24).values

        # making a summary of the surface height
        df["z_surf_combined"] = np.nan

        # in winter, both SR1 and SR2 are used
        df["z_surf_combined"] = df["z_surf_2_adj"].interpolate(limit=72).values


        # in ablation season we use SR2 instead of the SR1&2 average
        # here two options:
        # 1) we ignore the SR1 and only use SR2
        # 2) we use SR1 when SR2 is not available (commented)
        # the later one can cause jumps when SR2 starts to be available few days after SR1
        data_update = df[["z_surf_1_adj", "z_surf_2_adj"]].mean(axis=1).values

        ind_update = ~ind_ablation
        #ind_update = np.logical_and(ind_ablation,  ~np.isnan(data_update))
        df.loc[ind_update,"z_surf_combined"] = data_update[ind_update]

        # in ablation season we use pressure transducer over all other options
        data_update = df[ "z_ice_surf_adj"].interpolate(limit=72).values
        ind_update = np.logical_and(ind_ablation, ~np.isnan(data_update))
        df.loc[ind_update,"z_surf_combined"] = data_update[ind_update]

    logger.info('surface height combination finished')
    frame = plot_series_to_frame(hs1, hs2, z, z*np.nan, "final")
    frames.append(frame)
    frames.append(frame)
    frames.append(frame)
    frame = plot_final_frame(hs1, hs2, z, df["z_surf_combined"], "final")
    for i in range(16): frames.append(frame)

    imageio.mimsave(f"figures/surface_height/{station}.gif", frames, fps=8)
    logger.info('gif produced')
    return df['z_surf_combined'], df["z_ice_surf_adj"], df["z_surf_1_adj"], df["z_surf_2_adj"]
