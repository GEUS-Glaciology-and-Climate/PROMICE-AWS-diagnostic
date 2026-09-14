# -*- coding: utf-8 -*-
"""
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""
import pandas as pd
import numpy as np
import os, logging
import xarray as xr
import sys, importlib
# purge cached package + submodules
# only useful in debugging mode
for name in list(sys.modules):
    if name == "pypromice" or name.startswith("pypromice."):
        del sys.modules[name]
importlib.invalidate_caches()
from pypromice.pipeline.get_l2 import get_l2
from pypromice.pipeline.join_l2 import join_l2
from pypromice.pipeline.get_l2tol3 import get_l2tol3
from pypromice.pipeline.join_l3 import join_l3
import time


logging.getLogger('matplotlib.font_manager').disabled = True
logging.getLogger("pypromice").setLevel(logging.INFO)
logging.getLogger("pypromice.pipeline").setLevel(logging.INFO)
logging.getLogger("pypromice.pipeline.get_l2").setLevel(logging.INFO)
logging.getLogger('numba').setLevel(logging.WARNING)

config_folder = '../aws-l0/metadata/station_configurations/'
# %%
def process_l2(station):

    print(station)
    # Loading the L1 data:
    path_to_l0 = '../aws-l0/'

    config_file_tx = path_to_l0 + '/tx/config/{}.toml'.format(station)
    config_file_raw = path_to_l0 + '/raw/config/{}.toml'.format(station)
    output_path = 'data/L2_test'

    if os.path.isfile(config_file_tx):
        inpath = path_to_l0 + '/tx/'
        pAWS_tx = get_l2(config_file_tx,
                        inpath,
                         output_path+'/tx/',
                        variables=None, metadata=None,
                        data_issues_path='../PROMICE-AWS-data-issues',
                        declination_path=f"{path_to_l0}/magnetic_declination_coefs/magnetic_declination_igrf_coefs.toml",
                        write_60min=True)

    else:
        pAWS_tx = None

    if os.path.isfile(config_file_raw):
        inpath = path_to_l0 + '/raw/'+station+'/'
        pAWS_raw = get_l2(config_file_raw,
                    inpath,
                    output_path+'/raw/',
                    variables=None,
                    metadata=None,
                    data_issues_path='../PROMICE-AWS-data-issues',
                    declination_path=f"{path_to_l0}/magnetic_declination_coefs/magnetic_declination_igrf_coefs.toml",
                    write_60min=True)

    else:
        pAWS_raw = None
    return pAWS_tx, pAWS_raw


def get_join_l3(site):

    path_l3_stations = 'data/L3_test/stations/'
    folder_gcnet = '../GC-Net-level-1-data-processing/L1/hourly'
    folder_glaciobasis = '../historical-zac-data/'

    for f in [f'data/L3_test/sites/{site}/{site}_hour.nc',
              f'data/L3_test/sites/{site}/{site}_day.nc',
              f'data/L3_test/sites/{site}/{site}_month.nc']:
        if os.path.exists(f):
            os.remove(f)

    l3_merged, sorted_list_station_data = join_l3(config_folder, site, path_l3_stations,
                        folder_gcnet, folder_glaciobasis, 'data/L3_test/sites/', None, None)
    return l3_merged, sorted_list_station_data

from join_l3_old import join_l3_old
def get_join_l3_old(site):

    path_l3_stations = 'data/L3_test/stations/'
    folder_gcnet = '../GC-Net-level-1-data-processing/L1/hourly'
    folder_glaciobasis = '../historical-zac-data/'


    l3_merged, sorted_list_station_data = join_l3_old(config_folder, site, path_l3_stations,
                        folder_gcnet, folder_glaciobasis, None, None, None)
    return l3_merged, sorted_list_station_data


if __name__ == '__main__':

    station_metadata = pd.read_csv('../thredds-data/metadata/AWS_stations_metadata.csv')
    site_metadata = pd.read_csv('../thredds-data/metadata/AWS_sites_metadata.csv')
    # for site in site_metadata.site_id:
    for site in ['KPC_U', ]:
        t0 = time.perf_counter()
        # for station in site_metadata.loc[site_metadata.site_id == site, 'stations'].values[0].split(' '):
        for station in ['KPC_U','KPC_Uv3']:
            if station in station_metadata.station_id.values:
                print("\n ======== test get_l2 ========= \n")
                pAWS_tx, pAWS_raw = process_l2(station)

                print("\n ======== test join_l2 ========= \n")
                l2_merged = join_l2('data/L2_test/raw/'+station+'/'+station+'_mixed.nc',
                                    'data/L2_test/tx/'+station+'/'+station+'_mixed.nc',
                                    'data/L2_test/level_2/',None,None)

                print("\n ======== test l2tol3 ========= \n")
                l3 = get_l2tol3(config_folder,
                                'data/L2_test/level_2/'+station+'/'+station+'_mixed.nc',
                                'data/L3_test/stations/', None, None, None)
            else:
                print(f"==== skipping {station} ====")

        print(" ======== test join_l3 ========= \n")
        l3_merged, sorted_list_station_data = get_join_l3(site)
        l3_merged_old, sorted_list_station_data_old = get_join_l3_old(site)

        # %%
        import matplotlib.pyplot as plt
        import pandas as pd

        vars_to_plot = {
            "t_u": "Temperature upper",
            "t_l": "Temperature lower",
            "rh_u": "Relative humidity",
            "wspd_u": "Wind speed",
            "p_u": "Pressure",
        }

        stids = list(dict.fromkeys(info["stid"] for _, info in sorted_list_station_data))
        stids = ['KPC_U','KPC_Uv3']

        colors = dict(zip(stids, plt.rcParams["axes.prop_cycle"].by_key()["color"]))

        def plot_time_blocks(sorted_list_station_data):

            vars_to_plot = {
                "t_u": "Temperature",
                "rh_u": "Relative humidity",
                "wspd_u": "Wind speed",
                "p_u": "Pressure",
            }
            station_order = site_metadata.loc[
                site_metadata.site_id == site,
                "stations"
            ].values[0].split(" ")
            station_order = ['KPC_U','KPC_Uv3']

            cycle = plt.rcParams["axes.prop_cycle"].by_key()["color"]

            colors = {
                stid: cycle[i % len(cycle)]
                for i, stid in enumerate(station_order)
            }

            # reconstruct blocks actually retained by the old join_l3
            kept_station_data = []

            for i, (ds, info) in enumerate(sorted_list_station_data):

                start_time = ds.time.values[0]

                if i == 0:
                    # newest station is retained entirely
                    end_time = ds.time.values[-1]
                else:
                    # older station is cut at start of the next newer block
                    end_time = sorted_list_station_data[i - 1][0].time.values[0]

                ds_kept = ds.sel(time=slice(start_time, end_time))

                if ds_kept.time.size and ds_kept.time.values[-1] == end_time:
                    ds_kept = ds_kept.isel(time=slice(None, -1))

                if ds_kept.time.size:
                    kept_station_data.append((ds_kept, info))

            fig, axes = plt.subplots(
                len(vars_to_plot) + 2, 1,
                figsize=(13, 11),
                sharex=True,
                gridspec_kw={"height_ratios": [1, 1, 2, 2, 2, 2]},
            )

            # full station coverage
            ax = axes[0]

            for i, (ds, info) in enumerate(sorted_list_station_data_old[::-1]):
                stid = info["stid"]
                t0 = pd.to_datetime(ds.time.values[0])
                t1 = pd.to_datetime(ds.time.values[-1])

                ax.plot(
                    [t0, t1], [i, i],
                    lw=8,
                    color=colors[stid],
                    solid_capstyle="butt",
                )

                ax.text(
                    t0 + (t1 - t0) / 2,
                    i + 0.12,
                    stid,
                    ha="right",
                    va="bottom",
                    rotation=-45,
                    rotation_mode="anchor",
                    fontsize=9,
                )

            ax.set_yticks([])
            ax.set_ylabel("Available")
            ax.grid(axis="x", alpha=0.3)

            # blocks retained in assemblage
            ax = axes[1]

            for i, (ds, info) in enumerate(kept_station_data[::-1]):
                stid = info["stid"]
                t0 = pd.to_datetime(ds.time.values[0])
                t1 = pd.to_datetime(ds.time.values[-1])

                ax.plot(
                    [t0, t1], [i, i],
                    lw=8,
                    color=colors[stid],
                    solid_capstyle="butt",
                )

                ax.text(
                    t0 + (t1 - t0) / 2,
                    i + 0.12,
                    stid,
                    ha="right",
                    va="bottom",
                    rotation=-45,
                    rotation_mode="anchor",
                    fontsize=9,
                )

            ax.set_yticks([])
            ax.set_ylabel("Kept")
            ax.grid(axis="x", alpha=0.3)

            # variables
            for ax, (var, label) in zip(axes[2:], vars_to_plot.items()):

                for ds, info in kept_station_data:
                    if var not in ds:
                        continue

                    s = ds[var].to_series().dropna()

                    ax.plot(
                        s.index,
                        s.values,
                        ".",
                        ms=2,
                        color=colors[info["stid"]],
                    )

                ax.set_ylabel(label)
                ax.grid(alpha=0.3)

            axes[-1].set_xlabel("Time")
            fig.suptitle(f"{site} – L3 assemblage")

            plt.tight_layout()
            plt.show()

        plot_time_blocks(sorted_list_station_data)
        plot_time_blocks(sorted_list_station_data_old)
# %%
# l3_merged, sorted_list_station_data = get_join_l3(site)
# import matplotlib.pyplot as plt
# plt.figure()
# for (ds, attrs) in sorted_list_station_data:
#     ds.t_u.plot(label=attrs['stid'])
#     # l3_merged.t_u.plot()
#     plt.legend()
#     # data_version = 'L2_test/tx/'
#     data_version = 'L3_test/sites/'

#     res = 'hour'
#     res_org = res if res!='mixed' else 'hour'

#     # site = 'CEN2'
#     site_org = site.replace('v3','')

#     var = 'dsr'

#     ds_new = xr.open_dataset(f'data/{data_version}/{site}/{site}_{res}.nc',
#                              decode_times=True)
#     df_new = ds_new.to_dataframe()
#     df_new.index = df_new.index.astype('datetime64[ns]')



#     plt.figure()
#     plt.plot(df_new.index, df_new[var], marker='o', label='new')
#     plt.plot(df_new.index, df_new['z_ice_surf'], label='z_ice_surf')
#     # df_new.loc[:,'snow_height'].plot(label='snow_height')
#     plt.title(data_version + ' ' + site)
#     plt.ylabel(var)

#     station_list = ds_new.attrs['stations'].split(' ')
#     for station in station_list:
#         df_l2 = xr.open_dataset(f'data/L3_test/stations/{station}/{station}_mixed.nc',
#                                 decode_times=True).to_dataframe()
#         df_l2.index = df_l2.index.astype('datetime64[ns]')

#         plt.plot(df_l2.index, df_l2['z_surf_combined'], marker='^',
#                                       label=f'{station} z_surf_combined')


    # df_org = pd.read_csv(f'../thredds-data/level_3_sites/csv/{res_org}/{site_org}_{res_org}.csv')
    # df_org.time = pd.to_datetime(df_org.time)
    # df_org = df_org.set_index('time')
    # df_org.loc[:,var].plot(marker='^',zorder=0, c='k', label='thredds')
    # df_org.loc[:,var].plot(marker='^',zorder=0, c='k', label='thredds')
    # pAWS_tx.L1A.tilt_x.plot(marker='d',label='L1 tilt_x')
    # pAWS_tx.L2.t_rad.plot(marker='d',label='L1 t_rad')
    # plt.legend()
