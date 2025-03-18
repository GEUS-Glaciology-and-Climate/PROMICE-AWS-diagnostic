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

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import xarray as xr
from pyproj import Transformer

# Open dataset
ds_alt = xr.open_dataset('C:/Users/bav/OneDrive - GEUS/Data/Surface height/ESA CCI/CCI_GrIS_RA_dSEC_dh_5km_012011_072024.nc').load()

# Define x and y coordinates from XX and YY
ds_alt = ds_alt.assign_coords({
    "x": ("lat_dim", ds_alt.XX.data[0, :].astype(float)),  # Take first row of XX
    "y": ("lon_dim", ds_alt.YY.data[:, 0].astype(float))   # Take first column of YY
})

ds_alt = ds_alt.swap_dims({"lat_dim": "x", "lon_dim": "y"})
ds_alt = ds_alt.drop_vars(["XX", "YY"], errors="ignore")
ds_alt['time'] = pd.to_datetime((ds_alt.time * 365.25 - 719529), origin='unix', unit='D')
ds_alt = ds_alt.coarsen(x=2, y=2, boundary="trim").mean()

# Now plot should work
ds_alt.ZZ.sum(dim='time').plot(size=8, aspect='auto')
plt.xlabel("Easting (EPSG:3413)")
plt.ylabel("Northing (EPSG:3413)")

# EPSG transformation
transformer = Transformer.from_crs("EPSG:4326", "EPSG:3413", always_xy=True)

file_list = ['KAN_L_day.csv', 'NUK_L_day.csv']
fig, ax_list = plt.subplots(len(file_list), 1, sharex=True, figsize=(12, 8))
plt.subplots_adjust(right=0.75, left=0.08)
var = 'z_surf_combined'

for file, ax in zip(file_list, ax_list):  # for each site
    site = file.replace('_day.csv', '')

    # Read AWS data
    df_new = pd.read_csv(path_new + file)
    df_new.time = pd.to_datetime(df_new.time, utc=False)
    df_new = df_new.set_index('time')

    # Convert lat/lon to EPSG:3413
    lat, lon = df_new.lat.mean(), df_new.lon.mean()
    x_3413, y_3413 = transformer.transform(lon, lat)

    # Sample ds_alt at the nearest x, y
    ds_sample = ds_alt.sel(x=x_3413, y=y_3413, method="nearest")

    # Plot AWS data if available
    if var in df_new.columns and not df_new[var].isnull().all():
        ax.plot(df_new.index, df_new[var].values,
                marker='o', markeredgecolor='None', linestyle='None',
                color='tab:orange', label=var)

    # Plot ds_alt ZZ data if available
    if "ZZ" in ds_sample:
        ax.plot(ds_sample.time, ds_sample.ZZ,
                linestyle='-', color='tab:blue', label="ZZ from ds_alt")

    ax.set_ylabel(var.replace('gps_', ''))
    ax.grid()
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax.set_title(site)

# Save figure
plt.savefig('figures/AWS_vs_ds_alt_ZZ.png', dpi=300, bbox_inches="tight")
plt.show()
