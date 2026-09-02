# -*- coding: utf-8 -*-
"""
Created on %(date)s
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""

# %% plot all ablation and surface height time series
import matplotlib.pyplot as plt
import pandas as pd
import os
import matplotlib
matplotlib.use('Agg')
import tocgen
import numpy as np

# Initialize
data_type = 'sites'
path_new = '../thredds-data/level_3_sites/'
filename = 'plot_compilations/ablation_' + data_type + '.md'
df_meta = pd.read_csv(path_new + '../metadata/AWS_' + data_type + '_metadata.csv')
df_meta = df_meta.set_index(data_type[:-1] + '_id')
f = open(filename, "w")

def Msg(txt):
    with open(filename, "a") as f:
        print(txt)
        f.write(txt + "\n")

plt.close('all')

# Loop over each station
for station in df_meta.index:
# for station in ['QAS_M']:
    Msg('## ' + station)

    # Check if the file exists
    # if not os.path.isfile(path_new + station + '/' + station + '_day.csv'):
    #     continue

    # Read the station data
    df_new = pd.read_csv(path_new +'/csv/day/' + station + '_day.csv')
    if df_new.loc[df_new.z_surf_combined.last_valid_index(), 'z_surf_combined'] >0:
        Msg('accumulation site')
        continue
    df_new.time = pd.to_datetime(df_new.time)
    df_new = df_new.set_index('time')

    # Create a figure with two panels
    fig, ax_list = plt.subplots(2, 1, sharex=False, figsize=(10, 10))
    plt.subplots_adjust(right=0.75, left=0.08, hspace=0.15)

    # Top panel: z_surf_combined
    if 'z_surf_combined' in df_new.columns and not df_new['z_surf_combined'].isnull().all():
        ax_list[0].plot(df_new.index, df_new['z_surf_combined'],
                         marker='.', markeredgecolor='None', linestyle='None', label='z_surf_combined')
        ax_list[0].set_ylabel('Surface Height (m)')
        ax_list[0].set_title(station)
        ax_list[0].grid()
        ax_list[0].legend(loc='center left', bbox_to_anchor=(1, 0.5))

        # caluclating ice surface
        df_new['z_ice_surf'] = df_new['z_surf_combined'].cummin()

        # removing years with too many NaNs in JJA
        mask = df_new[df_new.index.month.isin([6, 7, 8])]['z_surf_combined'].isnull().resample('YE').sum().to_frame()
        for index, count in mask.iterrows():
            if count.iloc[0]>15:
                df_new.loc[str(index.year), 'z_ice_surf'] = np.NaN

        # Bottom panel: z_ice_surface as function of day of year
        for year in df_new.index.year.unique():
            # Filter data for the year range September to August Y
            start_date = pd.Timestamp(f'{year}-04-01')
            end_date = pd.Timestamp(f'{year}-10-31')
            df_year = df_new.loc[(df_new.index >= start_date) & (df_new.index < end_date), :].copy()

            # Calculate the day of the year
            df_year['day_of_year'] = df_year.index.dayofyear.values
            # df_year.loc[df_year['day_of_year'] < 0, 'day_of_year'] = 365 + df_year.loc[df_year['day_of_year'] < 0, 'day_of_year']

            # Plot z_surf_combined adjusted by first valid value
            if df_year['z_surf_combined'].notnull().any():
                first_valid_value = df_year['z_ice_surf'].loc[
                    slice(df_year['z_ice_surf'].first_valid_index(),
                          df_year['z_ice_surf'].first_valid_index()+pd.to_timedelta('10 days'))].mean()
                if year == 2025:
                    ax_list[1].plot(df_year['day_of_year'],
                                     df_year['z_ice_surf'] - first_valid_value,
                                     label='_no_legend_', linestyle='-', color='w',lw=10, alpha=0.7)
                    ax_list[1].plot(df_year['day_of_year'],
                                     df_year['z_ice_surf'] - first_valid_value,
                                     label=str(year), linestyle='-', color='k',lw=4)
                else:
                    ax_list[1].plot(df_year['day_of_year'],
                                     df_year['z_ice_surf'] - first_valid_value,
                                     label=str(year), linestyle='-')

        # Set x-axis limits

        # Major ticks and labels every 30 days
        labels = []
        tick_positions = []
        for i in np.cumsum(np.array([30, 31, 30, 31, 31, 29, 31, 30, 31, 30, 31, 31])):
            tick_positions.append(i)
            # Determine the corresponding month and year for the label
            month_label = ''
            if i < 30: month_label = 'Jan.'
            elif i < 60: month_label = 'Feb.'
            elif i < 90: month_label = 'Mar.'
            elif i < 120: month_label = 'Apr.'
            elif i < 150: month_label = 'May'
            elif i < 180: month_label = 'Jun.'
            elif i < 210: month_label = 'Jul.'
            elif i < 240: month_label = 'Aug.'
            elif i < 270: month_label = 'Sept.'
            elif i < 300: month_label = 'Oct.'
            elif i < 330: month_label = 'Nov.'
            elif i < 360: month_label = 'Dec.'
            labels.append(month_label)

        ax_list[1].set_xticks(tick_positions)
        ax_list[1].set_xticklabels(labels, rotation=45, ha='right')
        ax_list[1].set_xlim(120, 290)


        ax_list[1].set_ylabel('Snow Height (m)')
        ax_list[1].grid()
        ax_list[1].legend(title='Year', loc='center left', bbox_to_anchor=(1, 0.5), ncol=1)

    # Save the figure
    fig.savefig('figures/ablation/%s_ice_surface.png' % ( station), dpi=300)
    Msg(f'![{station}](../figures/ablation/{station}_ice_surface.png)')
    Msg(' ')

tocgen.processFile(filename, filename[:-3] + "_toc.md")
f.close()

# %% Mosaic
import math
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np, pandas as pd

path_new=Path("../thredds-data/level_3_sites")
df_meta=pd.read_csv(path_new/"../metadata/AWS_sites_metadata.csv").set_index("site_id")
csv_dir=path_new/"csv/day"
out=Path("figures/ablation/ablation_mosaic.png")

N_COLS=4; XMIN,XMAX=120,290
ticks=list(np.cumsum([30,31,30,31,31,29,31,30,31,30,31,31]))
def labs(ts):
    return ["Jan." if i<30 else "Feb." if i<60 else "Mar." if i<90 else
            "Apr." if i<120 else "May" if i<150 else
            "Jun." if i<180 else "Jul." if i<210 else
            "Aug." if i<240 else "Sept." if i<270 else "Oct." if i<300 else
            "Nov." if i<330 else "Dec." if i<360 else "" for i in ts]

labels=labs(ticks)

years=np.arange(1996,2026)
cmap=plt.get_cmap("tab20",len(years))
year_color={y:cmap(i) for i,y in enumerate(years)}
year_color[2025] = 'k'
stations = [
 'KAN_T','KAN_L','KAN_M','KPC_L','KPC_U',
 #'MIT','NUK_B','NUK_K', 'SER_B',
 # 'NUK_N','QAS_A',
 # 'RED_L','ZAC_L', 'ZAC_U','FRE',
 'NUK_L','NUK_U','QAS_L','QAS_M','QAS_U', 'SCO_L', 'SCO_U',
 'SWC', 'JAR','TAS_A','TAS_L', 'THU_L', 'THU_L2', 'THU_U',
 'UPE_L', 'UPE_U', 'WEG_L',]

n=len(stations); nrows=math.ceil(n/N_COLS)
fig,ax=plt.subplots(nrows,N_COLS,figsize=(N_COLS*3.2,nrows*2.2),sharex=True)
ax=np.atleast_2d(ax)

handles={}
for i,s in enumerate(stations):
    r,c=divmod(i,N_COLS); a=ax[r,c]
    d=pd.read_csv(csv_dir/f"{s}_day.csv",usecols=lambda c:c in["time","z_surf_combined"])
    d["time"]=pd.to_datetime(d["time"],errors="coerce")
    d["z_surf_combined"]=pd.to_numeric(d["z_surf_combined"],errors="coerce")
    d=d.dropna(subset=["time"]).set_index("time").sort_index()
    d["z_ice_surf"]=d["z_surf_combined"].cummin()
    m=d[d.index.month.isin([6,7,8])]["z_surf_combined"].isnull().resample("YE").sum()
    for t,v in m.items():
        if v>15: d.loc[str(t.year),"z_ice_surf"]=np.nan
    for y in np.sort(d.index.year.unique()):
        # if y<2007 or y not in year_color: continue
        dy=d.loc[(d.index>=f"{y}-04-01")&(d.index<f"{y}-10-31"),["z_surf_combined","z_ice_surf"]].copy()
        if dy.empty or dy["z_surf_combined"].isnull().all(): continue
        dy["doy"]=dy.index.dayofyear
        fvi=dy["z_ice_surf"].first_valid_index()
        if fvi is None: continue
        z0=dy["z_ice_surf"].loc[slice(fvi,fvi+pd.to_timedelta("10D"))].mean()
        ln=a.plot(dy["doy"],dy["z_ice_surf"]-z0,
                  color=year_color[y], lw=1.2 if year != 2025 else 3)[0]
        handles.setdefault(y,ln)
    a.set_title(s); a.grid(True); a.set_xlim(XMIN,XMAX)

for j in range(n,nrows*N_COLS):
    r,c=divmod(j,N_COLS)
    ax[r,c].axis("off")

for a in ax[-1,:2].tolist() + ax[-2,-2:].tolist():
    a.tick_params(axis="x", labelbottom=True)
    a.set_xticks(ticks)
    a.set_xticklabels(labels, rotation=45, ha="right")
handles = dict(sorted(handles.items(), reverse=True))
fig.legend(handles.values(),[str(y) for y in handles.keys()],
           loc="center right",bbox_to_anchor=(0.9,0.11),title="Year",ncol=4)
fig.text(0.01,0.5,"Ice surface height (m)",va="center",rotation="vertical")
fig.tight_layout(rect=[0.03,0.02,0.95,1])
out.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(out,dpi=300)


# %% Comparison ablation with Robert's product
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
# Initialize
data_type = 'sites'
path_new = '../thredds-data/level_3_sites/csv/day/'
filename = 'plot_compilations/ablation_' + data_type + '.md'
df_meta = pd.read_csv('../thredds-data/metadata/AWS_' + data_type + '_metadata.csv')
df_meta = df_meta.set_index(data_type[:-1] + '_id')
f = open(filename, "w")

# Load the ablation data
df_ablation = pd.read_csv('ancil/promice_ice_ablation_2025.txt', delim_whitespace=True, na_values=-999).set_index('Year')

def Msg(txt):
    with open(filename, "a") as f:
        print(txt)
        f.write(txt + "\n")

plt.close('all')

# Loop over each station
for station in df_meta.index:
# for station in ['KAN_L']:
    Msg('## ' + station)

    # Read the station data
    df_new = pd.read_csv(path_new + '/' + station + '_day.csv')
    if df_new.loc[df_new.z_surf_combined.last_valid_index(), 'z_surf_combined'] > 0:
        Msg('accumulation site')
        continue
    df_new.time = pd.to_datetime(df_new.time)
    df_new = df_new.set_index('time')

    # Filter the ablation data for the current station
    if station not in df_ablation.columns:
        continue
    df_selec = df_ablation[station].dropna()

    # Set up subplots
    years = df_new.index.year.unique()
    num_years = len(years)
    fig, ax_list = plt.subplots(round(num_years**0.5)+1, round(num_years**0.5), sharex=True, sharey=True, figsize=(15, 10))
    ax_list = ax_list.flatten()
    plt.subplots_adjust(right=0.85, left=0.04, hspace=0.3,wspace=0.1)

    if num_years == 1:
        ax_list = [ax_list]  # To keep it consistent for single year

    # Iterate over each year
    for i, year in enumerate(years):
        start_date = pd.Timestamp(f'{year}-04-01')
        end_date = pd.Timestamp(f'{year}-10-31')
        df_year = df_new.loc[(df_new.index >= start_date) & (df_new.index < end_date), :].copy()

        if df_year.empty:
            continue

        # Calculate the day of the year and first valid value
        df_year['day_of_year'] = df_year.index.dayofyear.values
        df_year = df_year.loc[df_year.day_of_year > 150]
        first_valid_value = (df_year['z_surf_combined'].loc[
            slice(df_year['z_surf_combined'].first_valid_index(),
                  df_year['z_surf_combined'].first_valid_index() + pd.to_timedelta('10 days'))
        ] - df_year['snow_height'].loc[
            slice(df_year['z_surf_combined'].first_valid_index(),
                  df_year['z_surf_combined'].first_valid_index() + pd.to_timedelta('10 days'))
        ]).mean()

        # Plot z_surf_combined adjusted by first valid value
        ax_list[i].plot(df_year['day_of_year'], df_year['z_surf_combined'] - first_valid_value,
                        label="Surface height", linestyle='-')
        # Plot snow_height
        ax_list[i].plot(df_year['day_of_year'], df_year['snow_height'],
                        label="Snow height", linestyle='-')

        ax_list[i].hlines(0, xmin=0, xmax=350, color='k')

        if year in df_selec.index:
            ax_list[i].annotate('', xy=(255, -df_selec[year] * 1000 / 917),
                                xytext=(255, 0),
                                arrowprops=dict(facecolor='black', shrink=0.05, width=2, headwidth=10),
                                label=f'{year}: {df_selec[year]:.2f} m')
        if i % round(num_years**0.5) == 0:
            ax_list[i].set_ylabel('Height (m)')
        ax_list[i].set_title(f'{station} - {year}')
        ax_list[i].grid()

        # Set x-axis limits to show from DOY 150 to 250
        tick_positions = np.arange(150, 270, 20)
        ax_list[i].set_xticks(tick_positions)
        ax_list[i].set_xlim(150, 270)

    from matplotlib.lines import Line2D  # Import for custom legend marker

    # Add a custom legend with arrow marker for "Expert assessment"
    arrow_marker = Line2D([0], [0], color='k', marker='v', markersize=3, linestyle='None', label='Expert assessment')

    # Add a single legend on the right side with custom arrow marker
    handles, labels = ax_list[0].get_legend_handles_labels()
    handles.append(arrow_marker)  # Add custom arrow marker to legend
    labels.append('RSF assessment')  # Add custom arrow marker to legend
    fig.legend(handles, labels, loc='center right', bbox_to_anchor=(0.99, 0.5), title='Legend')

    # Save the figure
    fig.savefig(f'figures/ablation/evaluation/{station}_ablation.png', dpi=300)
    Msg(f'![{station}](../figures/snow_height/{data_type}/{station}_ablation.png)')
    Msg(' ')

f.close()

# %% Map ablation
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# load shapefile (epsg:3413)
land = gpd.read_file("ancil/greenland_land_3413.shp")
ice = gpd.read_file("ancil/greenland_ice_3413.shp")

# station metadata
df = df_meta.copy()
df['geometry'] = gpd.points_from_xy(df.longitude_last_valid, df.latitude_last_valid, crs=4326)
gdf = gpd.GeoDataFrame(df).to_crs(3413)

records = []
for station in gdf.index:
    d = pd.read_csv(f"{path_new}/csv/day/{station}_day.csv", parse_dates=['time']).set_index('time')
    if 'z_surf_combined' not in d: continue
    d['z_ice_surf'] = d['z_surf_combined'].cummin()
    z = d['z_ice_surf'].resample('YE').last() - d['z_ice_surf'].resample('YE').first()
    yearly = z.dropna()
    if len(yearly)==0: continue
    med = yearly.median()
    mn = yearly.min()
    mx = yearly.max()
    y2025 = np.nan
    if yearly.index.year.isin([2025]).any():
        y2025 = yearly[yearly.index.year==2025].values[0]
    records.append([station, med, mn, mx, y2025])

df_ab = pd.DataFrame(records, columns=['station','med','min','max','y2025']).set_index('station')
gdf = gdf.join(df_ab)

# %%
fig, ax = plt.subplots(figsize=(6,6))
land.plot(ax=ax, color='lightgrey')
ice.plot(ax=ax, color='white', edgecolor='grey')

for i, row in gdf.dropna(subset=['med']).iterrows():
    if row.stations in ['UWN','ORO','SER_B','NUK_B','KAN_B']:
        continue
    x, y = row.geometry.x, row.geometry.y

    # scale factor for visibility
    s = 100  # increase if too small

    ax.plot([x, x],
            [y + s*row['min'], y + s*row['max']],
            color='k', lw=1)

    ax.plot([x - 2000, x + 2000],
            [y + s*row['med'], y + s*row['med']],
            color='k', lw=3)

    if not np.isnan(row['y2025']):
        ax.plot(x, y + s*row['y2025'], 'o', color='red')


ax.set_axis_off()
plt.tight_layout()
plt.savefig("ablation_map.png", dpi=300)
