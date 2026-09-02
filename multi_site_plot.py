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


# can be run both for stations or for sites, sites are recommended
data_type = 'sites'
if data_type == 'sites':
    path_new = '../thredds-data/level_3_sites/csv/day/'
    df_meta = pd.read_csv('../thredds-data/metadata/AWS_sites_metadata.csv')
    os.makedirs("figures/GPS/sites", exist_ok=True)
else:
    path_new = '../thredds-data/level_2_stations/csv/month/'
    df_meta = pd.read_csv('../thredds-data/metadata/AWS_stations_metadata.csv')
    os.makedirs("figures/GPS/stations", exist_ok=True)


plt.close('all')
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Define colormap for background (red = cooling, blue = warming)
cmap = plt.cm.bwr  # Blue-White-Red colormap
norm = mcolors.Normalize(vmin=-1, vmax=1)  # Adjust range for typical trends

# User-defined setting: Choose trend type ('annual' or 'JJA')
trend_type = 'JJA'  # Change to 'JJA' for JJA trends

# First pass: Collect valid sites
valid_sites = []

for file in os.listdir(path_new):
    if not os.path.isfile(os.path.join(path_new, file)):
        continue

    df_new = pd.read_csv(os.path.join(path_new, file))
    df_new.time = pd.to_datetime(df_new.time, utc=True)

    if 't_l' in df_new.columns:
        df_new['t_u'] = df_new[['t_u', 't_l']].mean(axis=1)
    var = 't_u'

    if (df_new.time.iloc[-1] - df_new.time.iloc[0]).days / 365 >= 14:
        df_new = df_new.set_index('time')

        # Choose trend type
        if trend_type == 'annual':
            valid_years = df_new[var].resample('YE').count() >= 350
        elif trend_type == 'JJA':
            valid_years = df_new[var].loc[df_new.index.month.isin(
                [6, 7, 8])].resample('YE').count() > 90

        if valid_years.sum() > 7:
            valid_sites.append(file)

valid_sites.remove('MIT_day.csv')
valid_sites.remove('TAS_L_day.csv')

n_sites = len(valid_sites)

# Define grid layout based on valid sites
ncols = 4
nrows = (n_sites // ncols) + (n_sites % ncols > 0)

fig, axs = plt.subplots(nrows, ncols, figsize=(3.5 * ncols, 1 * nrows), sharex=True)
axs = axs.flatten()

# Iterate through valid sites
for i, file in enumerate(valid_sites):
    site = file.replace('_day.csv', '')

    df_new = pd.read_csv(os.path.join(path_new, file))
    df_new.time = pd.to_datetime(df_new.time, utc=True)
    df_new = df_new.set_index('time')

    if 't_l' in df_new.columns:
        df_new['t_u'] = df_new[['t_u', 't_l']].mean(axis=1)
    var = 't_u'

    # Choose trend type
    if trend_type == 'annual':
        df_resampled = df_new[var].resample('YE').mean()
        valid_years = df_new[var].resample('YE').count() >= 350
    elif trend_type == 'JJA':
        valid_years = df_new[var].loc[df_new.index.month.isin([6, 7, 8])].resample('YE').count() >90
        df_resampled = df_new[var].loc[df_new.index.month.isin([6, 7, 8])].resample('YE').mean()

    df_resampled = df_resampled[valid_years]

    if df_resampled.empty:
        continue

    # Compute trend
    years = df_resampled.index.year
    trend = np.polyfit(years, df_resampled.values, 1)
    slope_per_decade = trend[0] * 10  # Convert to °C per decade

    # Get subplot axis
    ax = axs[i]

    # Set background color based on slope
    color = cmap(norm(slope_per_decade))
    ax.set_facecolor(color)

    # Adjust Y-axis limits to ±5°C around the series mean
    y_mean = df_resampled.mean()
    y_min, y_max = y_mean - 5, y_mean + 10
    ax.set_ylim(y_min, y_max)

    # Plot data
    ax.plot(df_resampled.index, df_resampled.values, marker='o', markeredgecolor='lightgray',
            linestyle='None', color='black')

    # Plot trend line
    trend_line = np.poly1d(trend)
    ax.plot(df_resampled.index, trend_line(years), linestyle='--', linewidth=1.5, color='black')

    # Add site name & slope annotation inside the plot
    ax.annotate(f"{site}\n{slope_per_decade:.2f} °C dec$^{-1}$",
                xy=(0.05, 0.9), xycoords='axes fraction',
                fontsize=9, color='black', ha='left', va='top',
                bbox=dict(facecolor='white', alpha=0.6, edgecolor='none'))

    ax.grid(True, linestyle='--', alpha=0.5)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

# Remove empty subplots
for j in range(i + 1, len(axs)):
    fig.delaxes(axs[j])

# Adjust layout to avoid cropping
plt.subplots_adjust(left=0.08, right=0.85, bottom=0.05, top=0.95, wspace=0.3, hspace=0.05)

# Add a shared y-axis label
fig.text(0.02, 0.5, 'JJA mean temperature (°C)', va='center', rotation='vertical', fontsize=12)

# Add a common colorbar
cbar_ax = fig.add_axes([0.88, 0.2, 0.02, 0.6])  # (left, bottom, width, height)
cbar = plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), cax=cbar_ax)
cbar.set_label('Trend in JJA mean temperature (°C per decade)', fontsize=12)

# Ensure labels are saved properly in the PNG
# plt.tight_layout(rect=[0.05, 0.1, 0.85, 0.95])

# Save figure with labels
filename = f'figures/{var}_trends_{trend_type}.png'
fig.savefig(filename, dpi=300, bbox_inches="tight")

plt.show()

# %% T10m
import os
import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from pyproj import Transformer

plt.close('all')

# Define colormap for background (red = cooling, blue = warming)
cmap = plt.cm.bwr  # Blue-White-Red colormap
norm = mcolors.Normalize(vmin=-1, vmax=1)  # Adjust range for typical trends

def find_valid_sites(path_new, var, trend_type):
    """Identify valid sites based on data availability and trend type."""
    valid_sites = []
    all_sites = []

    for file in os.listdir(path_new):
        if not os.path.isfile(os.path.join(path_new, file)):
            continue

        df_new = pd.read_csv(os.path.join(path_new, file))
        df_new.time = pd.to_datetime(df_new.time, utc=True)

        if var == 't_u' and 't_l' in df_new.columns:
            df_new['t_u'] = df_new[['t_u', 't_l']].mean(axis=1)
        if var not in df_new.columns or df_new.lon.mean() > 0:
            continue

        all_sites.append(file)  # Store all sites for reference
        if (df_new.time.iloc[-1] - df_new.time.iloc[0]).days / 365 >= 5:
            df_new = df_new.set_index('time')

            if trend_type == 'annual':
                valid_years = df_new[var].resample('YE').count() >= 350
                threshold = 7
            elif trend_type == 'JJA':
                valid_years = df_new[var].loc[df_new.index.month.isin([6, 7, 8])].resample('YE').count() > 90
                threshold = 7
            elif trend_type == 'monthly':
                valid_years = df_new[var].resample('ME').count() >= 28
                threshold = 7 * 12

            if valid_years.sum() > threshold:
                valid_sites.append(file)

    return valid_sites, all_sites

def compute_trend(df, var, trend_type):
    """Resample data and compute temperature trend."""
    if trend_type == 'annual':
        valid_years = df[var].resample('YE').count() >= 350
        df_resampled = df[var].resample('YE').mean()
    elif trend_type == 'JJA':
        valid_years = df[var].loc[df.index.month.isin([6, 7, 8])].resample('YE').count() > 90
        df_resampled = df[var].loc[df.index.month.isin([6, 7, 8])].resample('YE').mean()
    elif trend_type == 'monthly':
        valid_years = df[var].resample('ME').count() >= 28
        df_resampled = df[var].resample('ME').mean()

    df_resampled = df_resampled[valid_years]
    if df_resampled.empty:
        return None, None

    years = df_resampled.index.year
    trend = np.polyfit(years, df_resampled.values, 1)
    slope_per_decade = trend[0] * 10  # Convert to °C per decade
    return df_resampled, slope_per_decade

def plot_faceted_trends(valid_sites, path_new, var, trend_type, ncols,
                        label_left, label_right):
    """Generate faceted plots for temperature trends."""
    n_sites = len(valid_sites)
    nrows = (n_sites // ncols) + (n_sites % ncols > 0)

    fig, axs = plt.subplots(nrows, ncols, figsize=(3.5 * ncols, 1 * nrows), sharex=True)
    axs = axs.flatten()

    for i, file in enumerate(valid_sites):
        site = file.replace('_day.csv', '')
        df_new = pd.read_csv(os.path.join(path_new, file))
        df_new.time = pd.to_datetime(df_new.time, utc=True)
        df_new = df_new.set_index('time')

        df_resampled, slope_per_decade = compute_trend(df_new, var, trend_type)
        if df_resampled is None:
            continue

        ax = axs[i]
        color = cmap(norm(slope_per_decade))
        ax.set_facecolor(color)
        ax.set_ylim(df_resampled.mean() - 5, df_resampled.mean() + 10)
        ax.plot(df_resampled.index, df_resampled.values, marker='o',
                markeredgecolor='None', linestyle='None', color='black',alpha=0.5)
        ax.plot(df_resampled.index,
                np.poly1d(np.polyfit(df_resampled.index.year,
                                     df_resampled.values, 1))(df_resampled.index.year),
                linestyle='--', linewidth=1.5, color='black')

        ax.annotate(f"{site}\n{slope_per_decade:.2f} °C/dec", xy=(0.05, 0.9), xycoords='axes fraction',
                    fontsize=9, color='black', ha='left', va='top',
                    bbox=dict(facecolor='white', alpha=0.6, edgecolor='none'))
        ax.grid(True, linestyle='--', alpha=0.5)
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    for j in range(i + 1, len(axs)):
        fig.delaxes(axs[j])

    plt.subplots_adjust(left=0.08, right=0.85, bottom=0.05, top=0.95, wspace=0.3, hspace=0.07)
    # Add a common colorbar
    cbar_ax = fig.add_axes([0.88, 0.2, 0.02, 0.6])  # (left, bottom, width, height)
    cbar = plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), cax=cbar_ax)
    cbar.set_label(label_right, fontsize=12)

    fig.text(0.02, 0.5, label_left, va='center', rotation='vertical', fontsize=12)
    plt.savefig(f'figures/{var}_trends_{trend_type}.png', dpi=300, bbox_inches="tight")
    plt.show()

def plot_map(valid_sites, all_sites, path_new, var, trend_type, label_legend):
    """Generate a temperature trend map without annotations."""
    fig, ax = plt.subplots(figsize=(10, 10))
    land = gpd.read_file('ancil/greenland_land_3413.shp')
    ice = gpd.read_file('ancil/greenland_ice_3413.shp')
    land.plot(ax=ax, color='k', alpha=0.5)
    ice.plot(ax=ax, color='lightblue', alpha=0.6)

    transformer = Transformer.from_crs("EPSG:4326", "EPSG:3413", always_xy=True)

    for file in all_sites:
        df_new = pd.read_csv(os.path.join(path_new, file))
        df_new.time = pd.to_datetime(df_new.time, utc=True)
        x, y = transformer.transform(df_new.lon.mean(), df_new.lat.mean())
        ax.scatter(x, y, s=50, c='gray', edgecolors='black', alpha=0.5)

    for file in valid_sites:
        df_new = pd.read_csv(os.path.join(path_new, file))
        df_new.time = pd.to_datetime(df_new.time, utc=True)
        df_new = df_new.set_index('time')

        df_resampled, slope_per_decade = compute_trend(df_new, var, trend_type)
        if df_resampled is None:
            continue

        x, y = transformer.transform(df_new.lon.mean(), df_new.lat.mean())
        ax.scatter(x, y, s=abs(slope_per_decade) * 200, c='red' if slope_per_decade > 0 else 'blue',
                   edgecolors='black', alpha=0.8)


    # **Add a legend with black dots of different sizes for scale**
    legend_sizes = [0.5, 1.0, 2.0]  # Trend magnitudes
    scaled_sizes = [s * 200 for s in legend_sizes]  # Match actual plotted marker sizes
    legend_labels = ["0.5 °C/dec", "1.0 °C/dec", "2.0 °C/dec"]

    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red',
                   ls='None', markersize=10, label="Warming Trend"),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue',
                   ls='None', markersize=10, label="Cooling Trend"),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='gray',
                   ls='None', markersize=5, label="Insufficient data")
    ]

    # Add scale for trend sizes
    for size, label in zip(legend_sizes, legend_labels):
        legend_elements.append(plt.Line2D([0], [0], marker='o', ls='None',color='w',
              markerfacecolor='black', markersize=np.sqrt(size*200), label=label))

    ax.legend(handles=legend_elements, loc='upper right', title=label_legend,
              bbox_to_anchor = (1.3,1))

    # Remove plot frame
    ax.set_frame_on(False)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.savefig(f'figures/greenland_{var}_trends_{trend_type}_no_annotation.png', dpi=300)
    plt.show()

# Run functions
valid_sites, all_sites = find_valid_sites(path_new, var='t_i_10m', trend_type='monthly')
valid_sites.remove('THU_U_day.csv')
plot_faceted_trends(valid_sites, path_new, var='t_i_10m', trend_type='monthly', ncols=3,
                    label_left='10 m firn temperature (°C)',
                    label_right='Trend in 10 m firn temperature (°C per decade)')
plot_map(valid_sites, all_sites, path_new, var='t_i_10m', trend_type='monthly',
                     label_legend="Trend in 10 m firn temperature")
# %%
valid_sites, all_sites = find_valid_sites(path_new, var='t_u', trend_type='JJA')
valid_sites.remove('MIT_day.csv')
valid_sites.remove('TAS_L_day.csv')

plot_faceted_trends(valid_sites, path_new, var='t_u', trend_type='JJA', ncols=4,
                    label_left='JJA mean temperature (°C)',
                    label_right='Trend in JJA mean temperature (°C per decade)')
plot_map(valid_sites, all_sites, path_new, var='t_u', trend_type='JJA',
                     label_legend="Trend in JJA mean temperature")


# %% map with annotation
import os
import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from pyproj import Transformer

plt.close('all')

# Define colormap for background (red = cooling, blue = warming)
cmap = plt.cm.bwr  # Blue-White-Red colormap
norm = mcolors.Normalize(vmin=-1, vmax=1)  # Adjust range for typical trends

# User-defined setting: Choose trend type ('annual' or 'JJA')
trend_type = 'JJA'  # Change to 'annual' for yearly trends

# Load Greenland shapefiles
land = gpd.read_file('ancil/greenland_land_3413.shp')
ice = gpd.read_file('ancil/greenland_ice_3413.shp')

# Transformer for lat/lon to EPSG:3413
transformer = Transformer.from_crs("EPSG:4326", "EPSG:3413", always_xy=True)

# First pass: Collect valid and all site locations
valid_sites = []
all_sites = []  # Store all sites to plot non-annotated ones later
site_info = []  # Store site coordinates for sorting

for file in os.listdir(path_new):
    if not os.path.isfile(os.path.join(path_new, file)):
        continue

    df_new = pd.read_csv(os.path.join(path_new, file))
    df_new.time = pd.to_datetime(df_new.time, utc=True)

    if 't_l' in df_new.columns:
        df_new['t_u'] = df_new[['t_u', 't_l']].mean(axis=1)
    var = 't_u'


    if (df_new.time.iloc[-1] - df_new.time.iloc[0]).days / 365 >= 14:
        df_new = df_new.set_index('time')

        # Choose trend type
        if trend_type == 'annual':
            valid_years = df_new[var].resample('YE').count() >= 350
        elif trend_type == 'JJA':
            valid_years = df_new[var].loc[df_new.index.month.isin([6, 7, 8])].resample('YE').count() > 90


        if valid_years.sum() > 7:
            valid_sites.append(file)

# Remove specific sites from valid_sites
valid_sites = [s for s in valid_sites if s not in ['MIT_day.csv', 'TAS_L_day.csv']]
N = len(valid_sites)  # Number of stations to annotate

# Create figure
fig, ax = plt.subplots(figsize=(10, 10))
land.plot(ax=ax, color='k', alpha=0.5)  # Land in black
ice.plot(ax=ax, color='lightblue', alpha=0.6)  # Ice sheet in light blue

# Get map center from axis limits
plt.draw()  # Ensure the figure is rendered before getting limits
xlim, ylim = ax.get_xlim(), ax.get_ylim()
map_center_x = (xlim[0] + xlim[1]) / 2
map_center_y = (ylim[0] + ylim[1]) / 2

# **Generate N annotation points on a circle (radius = 1,500,000 m)**
radius = 1_500_000  # 1.5 million meters
angles = np.linspace(np.pi, np.pi - 2 * np.pi, N, endpoint=False)  # Start at 12 o'clock, go clockwise
annotation_points = np.array([
    (map_center_x + radius * np.cos(a), map_center_y + radius * np.sin(a)) for a in angles
])

# **Compute angles of each site relative to the center**
for file in all_sites:
    site = file.replace('_month.csv', '')

    df_new = pd.read_csv(os.path.join(path_new, file))
    df_new.time = pd.to_datetime(df_new.time, utc=True)

    if 't_l' in df_new.columns:
        df_new['t_u'] = df_new[['t_u', 't_l']].mean(axis=1)
    var = 't_u'

    # Get latitude & longitude
    lat = df_new.lat.mean()
    lon = df_new.lon.mean()

    # Convert to EPSG:3413
    x, y = transformer.transform(lon, lat)

    # Compute angle from center (for clockwise sorting)
    angle = np.arctan2(y - map_center_y, x - map_center_x)

    site_info.append((angle, site, x, y, file))

# **Sort sites by angle (clockwise starting from 12 o’clock)**
site_info.sort(key=lambda s: -s[0])  # Sort in descending order (clockwise)

# Iterate through all sites to plot non-annotated ones as gray markers
for angle, site, x, y, file in site_info:
    if file not in valid_sites:
        ax.scatter(x, y, s=50, c='gray', edgecolors='black', alpha=0.5)  # Non-annotated sites

# Iterate through sorted valid sites, assigning them to annotation points
for i, (angle, site, x, y, file) in enumerate([s for s in site_info if s[4] in valid_sites]):
    # Compute JJA temperature trend
    df_new = pd.read_csv(os.path.join(path_new, file))
    df_new.time = pd.to_datetime(df_new.time, utc=True)
    df_new = df_new.set_index('time')

    df_resampled = df_new[var].loc[df_new.index.month.isin([6, 7, 8])].resample('YE').mean()
    valid_years = df_new[var].loc[df_new.index.month.isin([6, 7, 8])].resample('YE').count() > 90
    df_resampled = df_resampled[valid_years]

    if df_resampled.empty:
        continue

    # Get start & end years
    start_year = df_resampled.index.year.min()
    end_year = df_resampled.index.year.max()

    # Calculate trend (JJA)
    years = df_resampled.index.year
    trend = np.polyfit(years, df_resampled.values, 1)
    slope_per_decade = trend[0] * 10  # Convert to °C per decade

    # Define marker color based on warming (red) or cooling (blue)
    marker_color = 'red' if slope_per_decade > 0 else 'blue'

    # Assign the next available annotation point on the circle
    x_shift, y_shift = annotation_points[i]
    if i % 2 == 1:
        x_shift += 500000 * np.cos(angle)
        y_shift += 500000 * np.sin(angle)

    # Plot site marker (increased size by 2x)
    ax.scatter(x, y, s=abs(slope_per_decade) * 200, c=marker_color,
               edgecolors='black', alpha=0.8, label=site)

    # Draw line linking marker to annotation
    ax.plot([x, x_shift], [y, y_shift], color='gray', linewidth=0.8, alpha=0.7)

    # Annotate site name, trend, and time span at the assigned circle position
    annotation_text = f"{site}\n{slope_per_decade:.2f} °C/dec\n{start_year}–{end_year}"
    ax.annotate(annotation_text, (x_shift, y_shift),
                fontsize=9, color=marker_color, ha='center', va='center',
                bbox=dict(facecolor='white', alpha=0.6, edgecolor='none'))

# **Legend explaining marker size and color**
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label="Warming Trend"),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label="Cooling Trend"),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='gray', markersize=5, label="Non-annotated Sites")
]
ax.legend(handles=legend_elements, loc='upper right')

# Formatting
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)

# Save figure
plt.savefig('figures/greenland_temperature_trends_JJA.png', dpi=300)
plt.show()
