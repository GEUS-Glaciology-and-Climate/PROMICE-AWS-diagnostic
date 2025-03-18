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
import os
import xarray as xr
# can be run both for stations or for sites, sites are recommended
data_type = 'sites'
if data_type == 'sites':
    path_new = '../thredds-data/level_3_sites/csv/day/'
    df_meta = pd.read_csv('../thredds-data/metadata/AWS_sites_metadata.csv')
    os.makedirs("figures/GPS/sites", exist_ok=True)
else:
    path_new = '../thredds-data/level_2_stations/csv/day/'
    df_meta = pd.read_csv('../thredds-data/metadata/AWS_stations_metadata.csv')
    os.makedirs("figures/GPS/stations", exist_ok=True)

from pyproj import Transformer

# Open dataset
# data_folder = 'C:/Users/bav/OneDrive - GEUS/Data/Surface height/'
data_folder = 'C:/Users/bav/OneDrive - Geological survey of Denmark and Greenland/Data/Surface height/'

import rioxarray

ds_alt = xr.open_dataset(data_folder+'ESA CCI/CCI_GrIS_RA_dSEC_dh_5km_012011_072024.nc').load()

# Define x and y coordinates from XX and YY
ds_alt = ds_alt.assign_coords({
    "x": ("lat_dim", ds_alt.XX.data[0, :].astype(float)),  # Take first row of XX
    "y": ("lon_dim", ds_alt.YY.data[:, 0].astype(float))   # Take first column of YY
})

ds_alt = ds_alt.swap_dims({"lat_dim": "x", "lon_dim": "y"})
ds_alt = ds_alt.drop_vars(["XX", "YY"], errors="ignore")
ds_alt['time'] = pd.to_datetime((ds_alt.time * 365.25 - 719529), origin='unix', unit='D')

# Coarsen resolution
ds_alt = ds_alt.coarsen(x=2, y=2, boundary="trim").mean()

# Georeference using EPSG:3413
ds_alt = ds_alt.rio.write_crs("EPSG:3413", inplace=True)
ds_alt.rio.set_spatial_dims(x_dim="x", y_dim="y", inplace=True)

ds_alt_yr = xr.open_dataset(data_folder+'ESA CCI/CCI_GrIS_RA_SEC_5km_Vers3.0_2024-05-31.nc').load()
ds_alt_yr = ds_alt_yr.swap_dims({"t": "time"})

ds_khan = xr.open_dataset(data_folder+'/Khan et al/Greenland_dhdt_icevol_1kmgrid_DB.nc').load()
# %%
import geopandas as gpd
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2, figsize=(7, 5), constrained_layout=True)

land = gpd.read_file('ancil/greenland_land_3413.shp')
ice = gpd.read_file('ancil/greenland_ice_3413.shp')

for a in ax:
    land.plot(ax=a, color='k', alpha=1)

# ESA CCI dataset
ds_alt_valid = ds_alt_yr.SEC.sum(dim='time').where(
    ds_alt_yr.SEC.isel(time=0).notnull())

p1 = ds_alt_valid.plot(ax=ax[0], cmap='seismic_r', 
                       vmin=-60, vmax=60, add_colorbar=False)
y1, y2 = ds_alt_yr.time.dt.year.data[[0,-1]]
ax[0].set_title(f"ESA CCI yearly\n{y1} - {y2}")


# Khan dataset
ds_khan_valid = ds_khan.dhdt_vol.sum(dim='time').where(
    ds_khan.dhdt_vol.isel(time=0).notnull())

p2 = ds_khan_valid.plot(ax=ax[1], cmap='seismic_r', 
                        vmin=-60, vmax=60, add_colorbar=False)
y1, y2 = ds_khan.time.dt.year.data[[0,-1]]
ax[1].set_title(f"Khan et al. 2024\n{y1} - {y2}")

# Ensure same x and y limits for both subplots
xlim = [min(ax[0].get_xlim()[0], ax[1].get_xlim()[0]), 
        max(ax[0].get_xlim()[1], ax[1].get_xlim()[1])]
ylim = [min(ax[0].get_ylim()[0], ax[1].get_ylim()[0]), 
        max(ax[0].get_ylim()[1], ax[1].get_ylim()[1])]

for a in ax:
    a.set_xlim(xlim)
    a.set_ylim(ylim)
    a.set_xticks([])
    a.set_yticks([])
    a.set_xlabel("")
    a.set_ylabel("")
    a.spines['top'].set_visible(False)
    a.spines['right'].set_visible(False)
    a.spines['left'].set_visible(False)
    a.spines['bottom'].set_visible(False)
    a.set_aspect('equal')  # Force same aspect ratio

# Shared colorbar
cbar = fig.colorbar(p2, ax=ax, orientation="vertical", shrink=0.8, aspect=30)
cbar.set_label("Cumulated surface height change (m)")
fig.savefig('figures/altimetry_outlook.png', dpi=300)
plt.show()



# %% 
# EPSG transformation
transformer = Transformer.from_crs("EPSG:4326", "EPSG:3413", always_xy=True)

file_list = ['KAN_L_day.csv', 'NUK_L_day.csv']
file_list =  ['JAR_day.csv',  'KAN_L_day.csv',  'KAN_M_day.csv',  'KAN_U_day.csv',
              'KPC_L_day.csv',  'KPC_U_day.csv', 
              'NUK_L_day.csv',  'NUK_N_day.csv',  'NUK_U_day.csv',  'QAS_A_day.csv', 
              'QAS_L_day.csv',  'QAS_M_day.csv',  'QAS_U_day.csv',  'SCO_L_day.csv',
              'SCO_U_day.csv',  'SWC_day.csv',  'TAS_A_day.csv',  'TAS_L_day.csv',
              'TAS_U_day.csv',  'THU_L2_day.csv',  'THU_L_day.csv',  'THU_U_day.csv',
               'UPE_L_day.csv',  'UPE_U_day.csv']

n_sites = len(file_list)
ncols = 4
nrows = (n_sites // ncols) + (n_sites % ncols > 0)

fig, ax_list = plt.subplots(nrows, ncols, figsize=(15, 10))
plt.subplots_adjust(right=0.75, left=0.08, hspace=0.7)  # Added hspace

var = 'z_surf_combined'
ax_list = ax_list.flatten()

for file, ax in zip(file_list, ax_list):  # for each site
    site = file.replace('_day.csv', '')

    # Read AWS data
    df_new = pd.read_csv(path_new + file)
    df_new.time = pd.to_datetime(df_new.time, utc=False)
    df_new = df_new.set_index('time')

    # Convert lat/lon to EPSG:3413
    lat, lon = df_new.lat.mean(), df_new.lon.mean()
    x_3413, y_3413 = transformer.transform(lon, lat)

    # Plot AWS data if available
    if var in df_new.columns and not df_new[var].isnull().all():
        ax.plot(df_new.index, df_new[var].values,
                marker='.', markeredgecolor='None', linestyle='None',
                color='k', label=var)

    # ESA CCI
    # ds_cci = ds_alt.sel(x=x_3413, y=y_3413, method="nearest").sel(
    #     time=slice(df_new.z_surf_combined.first_valid_index(),
    #                df_new.z_surf_combined.last_valid_index()))
    # ax.plot(ds_cci.time, (ds_cci.ZZ / 100).cumsum(),
    #         linestyle='-', lw=3, label="ESA CCI")

    # ESA CCI yr
    ds_cci = ds_alt_yr.sel(x=x_3413, y=y_3413, method="nearest").sel(
        time=slice(df_new.z_surf_combined.first_valid_index(),
                   df_new.z_surf_combined.last_valid_index()))
    ax.plot(ds_cci.time, (ds_cci.SEC).cumsum(),
            linestyle='-', lw=3, label="ESA CCI yearly")

    # Khan
    ds_khan_selec = ds_khan.sel(x=x_3413, y=y_3413, method="nearest").sel(
        time=slice(df_new.z_surf_combined.first_valid_index(),
                   df_new.z_surf_combined.last_valid_index()))
    ax.plot(ds_khan_selec.time, ds_khan_selec.dhdt_vol.cumsum(),
            linestyle='-', lw=3, label="Khan et al. 2024")

    # Remove title, add annotation at bottom left
    ax.annotate(site, xy=(0.02, 0.07), xycoords='axes fraction', fontsize=10)

    # Rotate x-axis labels
    ax.tick_params(axis='x', rotation=45)

# Ensure legend is fully visible when saving
handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='center left', 
           bbox_to_anchor=(0.85, 0.5), markerscale=3)

# Save figure
plt.savefig('figures/SEC_evaluation.png', dpi=300, bbox_inches="tight")
plt.show()
