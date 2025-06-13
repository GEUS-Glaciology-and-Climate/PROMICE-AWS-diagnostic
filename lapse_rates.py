# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 14:09:50 2025

@author: bav
"""
import pandas as pd
import numpy as np
import os

# Define paths
path_new = '../thredds-data/level_3_sites/csv/month/'
df_meta = pd.read_csv('../thredds-data/metadata/AWS_sites_metadata.csv')
df_meta = df_meta.set_index('site_id')

monthly_records = []
annual_records = []
print('Extracting temperature, latitude, altitude')
for station in df_meta.index:
    fpath = os.path.join(path_new, f'{station}_month.csv')
    if not os.path.isfile(fpath) or station.endswith('_B'):
        continue
    if station in ['ORO','NUK_B','NUK_P','SER_B','KAN_B','WEG_B','UWN',
                   'NUK_K','ZAC_L','ZAC_U','ZAC_A','LYN_L','LYN_T']:
        continue
    df = pd.read_csv(fpath, parse_dates=['time'])
    df = df.set_index('time')
    df['year'] = df.index.year
    df['month'] = df.index.month
    df['lat'] = df['lat'].mean()
    df['alt'] = df['alt'].mean()

    for (y, m), group in df.groupby(['year', 'month']):
        if 't_u' in group and not group['t_u'].isna().all():
            monthly_records.append({
                'station': station,
                'year': y,
                'month': m,
                'lat': group['lat'].mean(),
                'alt': group['alt'].mean(),
                't_u': group['t_u'].mean()
            })

    for y, group in df.groupby('year'):
        if 't_u' in group and not group['t_u'].isna().all():
            annual_records.append({
                'station': station,
                'year': y,
                'lat': group['lat'].mean(),
                'alt': group['alt'].mean(),
                't_u': group['t_u'].mean()
            })

df_monthly = pd.DataFrame(monthly_records)
df_annual = pd.DataFrame(annual_records)
years = sorted(df_monthly['year'].unique())
sites = sorted(df_monthly['station'].unique())

# Step 1: compute monthly latitude slopes
print('Calcualting monthly latitudinal gradients')
lat_slopes = {}

for month in range(1, 13):
    df_m = df_monthly[df_monthly['month'] == month]
    slopes = []
    for year in years:
        df_y = df_m[df_m['year'] == year]
        if len(df_y) < 2:
            continue
        slope, _ = np.polyfit(df_y['lat'], df_y['t_u'], 1)
        slopes.append(slope)
    lat_slopes[month] = np.mean(slopes) if slopes else np.nan

# Step 2:
print('apply latitude correction')
df_monthly['t_u_corr'] = df_monthly.apply(
    lambda row: row['t_u'] - lat_slopes.get(row['month'], 0) * (row['lat'] - 70),
    axis=1
)

# Step 3: 
print('compute altitudinal lapse rates before and after correction')
lapse_rate_raw = {}
lapse_rate_corr = {}

for month in range(1, 13):
    df_m = df_monthly[df_monthly['month'] == month]
    raw_slopes = []
    corr_slopes = []
    for year in years:
        df_y = df_m[df_m['year'] == year]
        if len(df_y) < 2:
            continue
        s_raw, _ = np.polyfit(df_y['alt'], df_y['t_u'], 1)
        s_corr, _ = np.polyfit(df_y['alt'], df_y['t_u_corr'], 1)
        raw_slopes.append(s_raw)
        corr_slopes.append(s_corr)
    lapse_rate_raw[month] = np.mean(raw_slopes) if raw_slopes else np.nan
    lapse_rate_corr[month] = np.mean(corr_slopes) if corr_slopes else np.nan

# Optional: store results
df_lapse_summary = pd.DataFrame({
    'month': range(1, 13),
    'lat_gradient_C_per_deg': [lat_slopes.get(m, np.nan) for m in range(1, 13)],
    'alt_lapse_raw_C_per_m': [lapse_rate_raw.get(m, np.nan) for m in range(1, 13)],
    'alt_lapse_corr_C_per_m': [lapse_rate_corr.get(m, np.nan) for m in range(1, 13)],
})

# Save to CSV if desired
# df_lapse_summary.to_csv('monthly_lapse_corrections.csv', index=False)

# Precompute everything first
precomp = {m: {'points': [], 'regressions': []} for m in range(1, 13)}
monthly_avg_slopes = {}
for m in range(1, 13):
    df_m = df_monthly[df_monthly['month'] == m]
    if df_m.empty:
        continue
    # Store scatter points
    for _, row in df_m.iterrows():
        precomp[m]['points'].append((row['alt'], row['t_u'], row['year'], row['station']))
    # Per-year regressions
    slopes = []
    for y in years:
        df_y = df_m[df_m['year'] == y]
        if len(df_y) < 2:
            continue
        slope, intercept = np.polyfit(df_y['alt'], df_y['t_u'], 1)
        slopes.append(slope)
        x_fit = [df_y['alt'].min(), df_y['alt'].max()]
        y_fit = intercept + slope * np.array(x_fit)
        precomp[m]['regressions'].append((x_fit, y_fit, y))
    # Mean slope line
    if slopes:
        mean_slope = np.mean(slopes)
        x_all = [df_m['alt'].min(), df_m['alt'].max()]
        y_mean = df_m['t_u'].mean() - mean_slope * df_m['alt'].mean()
        y_fit = mean_slope * np.array(x_all) + y_mean
        precomp[m]['mean'] = (x_all, y_fit, mean_slope)
        monthly_avg_slopes[m] = mean_slope
    else:
        precomp[m]['mean'] = ([], [], np.nan)
        monthly_avg_slopes[m] = np.nan


import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
cmap = cm.get_cmap('viridis', len(years))
norm = mcolors.Normalize(vmin=min(years), vmax=max(years))
year_colors = {y: cmap(i) for i, y in enumerate(years)}
site_markers = ['o', 's', '^', 'D', 'v', 'p', '*', 'X', '<', '>', 'H', 'P']
marker_map = {s: site_markers[i % len(site_markers)] for i, s in enumerate(sites)}

# %% latitude gradients
fig, axs = plt.subplots(3, 4, figsize=(16, 10), sharey=True, sharex=True)
fig.subplots_adjust(left=0.07, bottom=0.07, right=0.75, hspace=0.2)

for i, m in enumerate(range(1, 13)):
    ax = axs.flat[i]
    df_m = df_monthly[df_monthly['month'] == m]
    if df_m.empty:
        ax.set_visible(False)
        continue

    # Scatter points
    for _, row in df_m.iterrows():
        ax.scatter(row['lat'], row['t_u'], color=year_colors[row['year']],
                   marker=marker_map[row['station']])

    # Per-year regressions
    slopes = []
    for year in years:
        df_y = df_m[df_m['year'] == year]
        if len(df_y) < 2:
            continue
        slope, intercept = np.polyfit(df_y['lat'], df_y['t_u'], 1)
        slopes.append(slope)
        x_fit = [df_y['lat'].min(), df_y['lat'].max()]
        y_fit = intercept + slope * np.array(x_fit)
        ax.plot(x_fit, y_fit, color=year_colors[year], alpha=0.6)

    # Mean slope line
    month_str = pd.to_datetime(f'2025-{m:02d}-01').strftime('%B')

    if slopes:
        mean_slope = np.mean(slopes)
        std_slope = np.std(slopes)
        x_all = [df_m['lat'].min(), df_m['lat'].max()]
        y_mean = df_m['t_u'].mean() - mean_slope * df_m['lat'].mean()
        y_fit = mean_slope * np.array(x_all) + y_mean
        ax.plot(x_all, y_fit, 'k', lw=2)
        ax.set_title(f'{month_str}:\n {mean_slope:.2f} ± {std_slope:.2f} °C/°lat')
    else:
        ax.set_title(f'{month_str} – no data')

    ax.grid()
    if i % 4 == 0:
        ax.set_ylabel('T (°C)')
    if i >= 8:
        ax.set_xlabel('Latitude (°N)')

# Colorbar
sm = cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar_ax = fig.add_axes([0.82, 0.75, 0.02, 0.2])
cbar = fig.colorbar(sm, cax=cbar_ax)
cbar.set_label('Year')

# Legend
handles = [plt.Line2D([], [], color='k', marker=marker_map[s], linestyle='None', label=s)
           for s in sites]
fig.legend(handles=handles, title='Site', loc='center right',
           ncols=2, bbox_to_anchor=(0.95, 0.4))

plt.suptitle('Monthly Latitude Gradient of T (by Year and Station)')
plt.savefig('figures/lapse_rates/monthly_latitude_gradient.png', dpi=300)


# %% 
fig, axs = plt.subplots(3, 4, figsize=(16, 10), sharey=True, sharex=True)
fig.subplots_adjust(left=0.07, bottom=0.07, right=0.75, hspace=0.2)

for i, m in enumerate(range(1, 13)):
    ax = axs.flat[i]
    df_m = df_monthly[df_monthly['month'] == m]
    if df_m.empty:
        ax.set_visible(False)
        continue

    # Scatter points
    for _, row in df_m.iterrows():
        ax.scatter(row['alt'], row['t_u_corr'], color=year_colors[row['year']],
                   marker=marker_map[row['station']])

    raw_slopes = []
    corr_slopes = []

    for year in years:
        df_y = df_m[df_m['year'] == year]
        if len(df_y) < 2:
            continue

        # Raw regression
        s_raw, i_raw = np.polyfit(df_y['alt'], df_y['t_u'], 1)
        raw_slopes.append(s_raw)
        x_fit = np.array([df_y['alt'].min(), df_y['alt'].max()])
        # ax.plot(x_fit, s_raw * x_fit + i_raw, color=year_colors[year], alpha=0.6)

        # Corrected regression
        s_corr, i_corr = np.polyfit(df_y['alt'], df_y['t_u_corr'], 1)
        corr_slopes.append(s_corr)
        ax.plot(x_fit, s_corr * x_fit + i_corr, color=year_colors[year], alpha=0.6, linestyle='-')

    # Mean fits
    if raw_slopes:
        mean_raw = np.median(raw_slopes)
        std_raw = np.std(raw_slopes)
        mean_corr = np.median(corr_slopes)
        std_corr = np.std(corr_slopes)

        x_all = np.array([df_m['alt'].min(), df_m['alt'].max()])
        y_raw = mean_raw * x_all + df_m['t_u'].mean() - mean_raw * df_m['alt'].mean()
        y_corr = mean_corr * x_all + df_m['t_u_corr'].mean() - mean_corr * df_m['alt'].mean()

        ax.plot(x_all, y_raw, 'k--', lw=2, label='Raw mean')
        ax.plot(x_all, y_corr, 'k-', lw=2, label='Corrected mean')
        print(f'{month_str}: {mean_corr * 1000:.2f} ± {std_corr * 1000:.2f} °C/km')
        month_str = pd.to_datetime(f'2025-{m:02d}-01').strftime('%B')
        ax.set_title(f'{month_str}:\n {mean_raw * 1000:.2f} ± {std_raw * 1000:.2f} / '
                     f'{mean_corr * 1000:.2f} ± {std_corr * 1000:.2f} °C/km')
    else:
        ax.set_title(f'{month_str} – no data')

    ax.grid()
    if i % 4 == 0:
        ax.set_ylabel('T (°C)')
    if i >= 8:
        ax.set_xlabel('Elevation (m)')

# Colorbar
sm = cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar_ax = fig.add_axes([0.82, 0.75, 0.02, 0.2])
cbar = fig.colorbar(sm, cax=cbar_ax)
cbar.set_label('Year')

# Legend
handles = [plt.Line2D([], [], color='k', marker=marker_map[s], linestyle='None', label=s)
           for s in sites]
handles += [
    plt.Line2D([], [], color='k', linestyle='--', label='Median (raw)'),
    plt.Line2D([], [], color='k', linestyle='-', label='Median (corrected)')
]
fig.legend(handles=handles,  loc='center right',
           ncols=2, bbox_to_anchor=(0.95, 0.4))

plt.suptitle('Monthly lapse rates harmonized at 70°N (raw / latitude-corrected)')
plt.savefig('figures/lapse_rates/monthly_lapse_rate_corrected.png', dpi=300)

# %% 
import matplotlib.pyplot as plt

# Prepare dataframe of monthly lapse rates per year (raw and corrected)
records = []
for month in range(1, 13):
    df_m = df_monthly[df_monthly['month'] == month]
    for year in years:
        df_y = df_m[df_m['year'] == year]
        if len(df_y) < 2:
            continue
        slope_raw, _ = np.polyfit(df_y['alt'], df_y['t_u'], 1)
        slope_corr, _ = np.polyfit(df_y['alt'], df_y['t_u_corr'], 1)
        records.append({
            'month': month,
            'year': year,
            'raw': slope_raw * 1000,
            'corr': slope_corr * 1000
        })

df_slopes = pd.DataFrame(records)

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
for year in years:
    df_y = df_slopes[df_slopes['year'] == year]
    if not df_y.empty:
        ax.plot(df_y['month'], df_y['corr'], label=str(year), alpha=0.5)

# Plot mean
df_mean = df_slopes.groupby('month')['corr'].median()
ax.plot(df_mean.index, df_mean.values, color='k', lw=2, label='Median')

ax.set_xticks(range(1, 13))
ax.set_xticklabels([pd.to_datetime(f'2025-{m:02d}-01').strftime('%b') for m in range(1, 13)])
ax.set_ylabel('Lapse rate (°C/km)')
ax.set_title('Monthly Lapse Rate')
ax.grid(True)
ax.legend(title='Year', bbox_to_anchor=(1.02, 1),ncols=2, loc='upper left')
plt.tight_layout()
plt.savefig('figures/lapse_rates/monthly_lapse_rate_by_year_with_mean.png', dpi=300)
