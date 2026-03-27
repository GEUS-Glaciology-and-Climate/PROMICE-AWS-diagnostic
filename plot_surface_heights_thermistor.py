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
import os
import matplotlib
matplotlib.use('Agg')
import tocgen

# %% Surface height reconstruction + thermistor depth + subsurface temperature
data_type = 'sites'
if data_type == 'sites':
    path_new = '../thredds-data/level_3_sites/csv/day/'
else:
    path_new = '../thredds-data//level_2_stations/csv/day/'

filename = 'plot_compilations/surface_height_'+data_type+'.md'

f = open(filename, "w")
def Msg(txt):
    f = open(filename, "a")
    print(txt)
    f.write(txt + "\n")
# plt.close('all')


# for file in os.listdir(path_new):
for file in ['KAN_L_day.csv']:
    station = file.replace('_day.csv','')
    Msg('## '+station)
    if not os.path.isfile(path_new+file):
        Msg("cannot find"+path_new+file)
        continue

    df_new = pd.read_csv(path_new+file)
    df_new.time = pd.to_datetime(df_new.time, utc=True)
    df_new = df_new.set_index('time')

    fig, ax_list = plt.subplots(3,1,sharex=True, figsize=(10,15))
    plt.subplots_adjust(right=0.75,left=0.08,hspace=0.02)

    var_list = [v for v in ['z_boom_u','z_boom_l','z_stake','z_pt_cor'] \
                      if v in df_new.columns]
    for var in var_list:
        if var in df_new.columns:
            if not df_new[var].isnull().all():
                ax_list[0].plot(df_new.index, df_new[var].values,
                        marker='.',markeredgecolor='None', linestyle='None',
                        label=var)

    var_list = [v for v in ['z_surf_combined','z_ice_surf'] \
                      if v in df_new.columns]
    for var in var_list:
        if var in df_new.columns:
            if not df_new[var].isnull().all():
                ax_list[1].plot(df_new.index, df_new[var].values,
                        marker='.',markeredgecolor='None', linestyle='None',
                       label=var)
            else:
                print(var,'all nan')
    depth_var = ['d_t_i_'+str(i) for i in range(1,12) \
                      if 'd_t_i_'+str(i) in df_new.columns]
    for var in depth_var:
        if var in df_new.columns:
            if not df_new[var].isnull().all():
                ax_list[1].plot(df_new.index, -df_new[var].values + df_new.z_surf_combined,

                       label=var)


    var_list = ['t_i_'+str(i) for i in range(1,12) \
                      if 't_i_'+str(i) in df_new.columns]
    for var in var_list:
        if var in df_new.columns:
            if not df_new[var].isnull().all():
                ax_list[2].plot(df_new.index, df_new[var].values,
                        marker='.',markeredgecolor='None', linestyle='None',
                       label=var)
    if 't_i_10m' in df_new.columns:
        ax_list[2].plot(df_new.index, df_new['t_i_10m'].values,
                marker='o',color='k',markeredgecolor='None', linestyle='None',
               label='t_i_10m')

    for i in range(3):
        ax_list[i].set_ylabel('Height (m)')
        ax_list[i].grid()
        ax_list[i].legend(loc='center left', bbox_to_anchor=(1, 0.5))
        if i > 1:
            ax_list[i].legend(loc='center left', bbox_to_anchor=(1, 0.5),ncols=2)

    ax_list[2].set_ylabel('Depth (m)')
    ax_list[2].set_ylabel('Temperature (°C)')
    ax_list[0].set_title(station)

    # xlim1 = df_new.index[0]
    xlim1 = pd.to_datetime('2022-03-01', utc=True)
    xlim2 = df_new.index[-1]
    xlim2 = pd.to_datetime('2026-01-10', utc=True)
    ax_list[0].set_xlim(xlim1, xlim2)
    if len(depth_var)>0:
        try:
            ax_list[1].set_ylim(
                               (df_new['z_surf_combined'].min() - df_new.loc[slice(xlim1, xlim2),depth_var].max().max())-0.5,
                                   df_new.loc[slice(xlim1, xlim2), 'z_surf_combined'].max()+0.5
                                   )
        except:
            pass

    fig.savefig('figures/surface_height/%s/%s.png' % (data_type, station), dpi=300, bbox_inches="tight")
    Msg('![%s](../figures/surface_height/%s/%s.png)'%(station,data_type, station))
    Msg(' ')

tocgen.processFile(filename, filename[:-3]+"_toc.md")
f.close()

# %% Surface height overview plot
import matplotlib.pyplot as plt
import pandas as pd
import os

# Define data type and paths
data_type = 'sites'
path_new = '../thredds-data/level_3_sites/csv/day/'
filename = 'plot_compilations/ablation_' + data_type + '.md'
df_meta = pd.read_csv('../thredds-data/metadata/AWS_' + data_type + '_metadata.csv')
df_meta = df_meta.set_index(data_type[:-1] + '_id')

plt.close('all')

region_list = ['KAN', 'UPE', 'THU', 'KPC', 'SCO', 'TAS', 'QAS', 'NUK',]
station_list_list = [[v for v in df_meta.index if st in v] for st in region_list]
region_list = region_list + ['SWC-JAR']
station_list_list = station_list_list + [['SWC', 'JAR']]

fig, ax_list = plt.subplots(4, 3, figsize=(15, 15))  # Increased figure size
ax_list = ax_list.flatten()
plt.subplots_adjust(right=0.7, left=0.07, hspace=0.1, wspace=0.4)  # Increased space
abc = 'abcdefghijklmno'
# Make the last two panels (11th and 12th) invisible
for ax in ax_list[10:]:
    ax.set_visible(False)

# Create the upper 9 panels and share x-axis and ticks
for i, station_list in enumerate(station_list_list[:9]):  # Limit to the first 9 panels
    for station in station_list:
        if station in ['KAN_B', 'NUK_K','NUK_P','NUK_B']:
            continue
        print('## ' + station)
        df_new = pd.read_csv(path_new + '/' + station + '_day.csv')
        df_new.time = pd.to_datetime(df_new.time, utc=True)
        df_new = df_new.set_index('time')

        var_list = [v for v in ['z_surf_combined'] if v in df_new.columns]
        for var in var_list:
            if var in df_new.columns and not df_new[var].isnull().all():
                ax_list[i].plot(df_new.index, df_new[var].values,
                                marker='.', markeredgecolor='None', linestyle='None',
                                alpha=0.7, label=station)

    ax_list[i].legend(loc='lower left', markerscale=2, fontsize=12)
    for h in ax_list[i].get_legend().legendHandles:
        h.set_alpha(1)
    ax_list[i].grid(True)
    ax_list[i].tick_params(axis='x', rotation=45)
    ax_list[i].text( 0.03, 0.96,  # Adjust these values for fine-tuning position
                    f'({abc[i]}) '+region_list[i],
                    fontsize=14, ha='left', va='top',
                    transform=ax_list[i].transAxes)

    if i < 6:
        ax_list[i].set_xticklabels([])
    ax_list[i].set_ylim(-100, 20)
    ax_list[i].set_xlim(pd.to_datetime('1995'), pd.to_datetime('2025-07-01'))
    ax_list[i].tick_params(axis='both', labelsize=12)

# Combine the 10th panel across the 11th and 12th positions
gs = ax_list[9].get_gridspec()
ax_list[9].remove()  # Remove the 10th panel from its current spot
ax_large = fig.add_subplot(gs[3, :])  # Create a large subplot spanning 11th and 12th positions
pos = ax_large.get_position()
ax_large.set_position([pos.x0, pos.y0, pos.width, pos.height * 0.85])
for station in ['DY2', 'NAU', 'CEN', 'TUN', 'NAE', 'NSE', 'SDL', 'SDM']:
    if station in ['KAN_B', 'NUK_K']:
        continue
    if not os.path.isfile(path_new + '/' + station + '_day.csv'):
        continue
    print('## ' + station)
    df_new = pd.read_csv(path_new + '/' + station + '_day.csv')
    df_new.time = pd.to_datetime(df_new.time, utc=True)
    df_new = df_new.set_index('time')

    var_list = [v for v in ['z_surf_combined'] if v in df_new.columns]
    for var in var_list:
        if var in df_new.columns and not df_new[var].isnull().all():
            ax_large.plot(df_new.index, df_new[var].values,
                          marker='.', markeredgecolor='None', linestyle='None',
                          alpha=0.7, label=station)

ax_large.legend(loc='upper left', ncols=3, bbox_to_anchor=(0, 0.85  ), markerscale=2, fontsize=12)
for h in ax_large.get_legend().legendHandles:
    h.set_alpha(1)
ax_large.grid(True)
ax_large.tick_params(axis='x', rotation=45)
ax_large.tick_params(axis='both', labelsize=12)

ax_large.text(
            0.02, 0.96,  # Adjust these values for fine-tuning position
            "(j) Accumulation sites",
            fontsize=14, ha='left', va='top',
            transform=ax_large.transAxes,
            bbox=dict(facecolor='white', alpha=0.85, edgecolor='none')
        )
ax_large.set_xlim(pd.to_datetime('1995'), pd.to_datetime('2025-07-01'))

fig.supylabel('Surface height relative to installation (m)', fontsize=14)

# Save the figure with tight layout to remove excess white space
fig.savefig('figures/surface_height/overview.png', dpi=300, bbox_inches='tight')

# %% gif thermistor depth
# if True

import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

out_gif = f"figures/string_processing/gif/{station}.gif"
fps = 30
future_offset = 100
link_color = "0.75"
link_lw = 0.8
drop_lw = 0.0
drop_alpha = 0.9
steps = 100

dt_vars = [f'd_t_i_{i}' for i in range(1,11) if f'd_t_i_{i}' in df_new.columns]
new_dt_vars = [s+'_new' for s in dt_vars]
times = df_new.index.values
indices = np.linspace(1, len(times)-1, steps).astype(int)

frames = []

fig, ax = plt.subplots(figsize=(10, 4), dpi=150)
ax.set_title(station)

# IMPORTANT: use Matplotlib date numbers (not python datetimes)
xdt = df_new.index.to_pydatetime()
x = mdates.date2num(xdt)
n = len(df_new)

y0 = df_new["z_surf_combined"].to_numpy()
y1 = df_new["z_pt_cor"].to_numpy()
y2 = (5 - df_new["z_stake"]).to_numpy()
y3 = (3 - df_new["z_boom_cor_u"]).to_numpy()  # replace with SR50 2 if different

# persistent artists (must be global / outer scope for plot_* to see them)
ln0, = ax.plot([], [], color="black", lw=2)
ln1, = ax.plot([], [], color="tab:orange", lw=1.6)
ln2, = ax.plot([], [], color="tab:green", lw=1.6)
ln3, = ax.plot([], [], color="tab:blue", lw=1.6)

ln1b, = ax.plot(x,y1, color="tab:orange", lw=1.6, alpha=0.3)
ln2b, = ax.plot(x,y2, color="tab:green", lw=1.6, alpha=0.3)
ln3b, = ax.plot(x,y3, color="tab:blue", lw=1.6, alpha=0.3)

lk1, = ax.plot([], [], color=link_color, lw=link_lw, zorder=4)
lk2, = ax.plot([], [], color=link_color, lw=link_lw, zorder=4)
lk3, = ax.plot([], [], color=link_color, lw=link_lw, zorder=4)

def set_axes_once():
    ax.set_xlim(x[0], x[-1])
    finite = np.isfinite(y0)
    if np.any(finite):
        ax.set_ylim(np.nanmin(y0[finite]) - 10, np.nanmax(y0[finite]) + 20)
    ax.xaxis_date()
    ax.set_ylabel('Relative height (m)')
    ax.set_xlabel('Year')

def snap(hold=1):
    fig.canvas.draw()
    img = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    for _ in range(hold):
        frames.append(img)

def make_legend():
    h0 = plt.Line2D([0], [0], color="black", lw=2)
    h1 = plt.Line2D([0], [0], color="tab:orange", lw=1.6)
    h2 = plt.Line2D([0], [0], color="tab:green", lw=1.6)
    h3 = plt.Line2D([0], [0], color="tab:blue", lw=1.6)
    ax.legend(
        [h0, h1, h2, h3],
        ["reconstructed surface", "PTA", "SR50 1", "SR50 2"],
        loc="lower left",
        frameon=True,
    )

def plot_l0(k):
    xs = x[: k + 1]
    ys = y0[: k + 1]
    m = np.isfinite(ys)
    ln0.set_data(xs[m], ys[m])

def plot_l1_l2_l3(k):
    kf = min(n, k + future_offset)
    ln1.set_data(x[kf:], y1[kf:])
    ln2.set_data(x[kf:], y2[kf:])
    ln3.set_data(x[kf:],  y3[kf:])

def clear_drops():
    lk1.set_data([], [])
    lk2.set_data([], [])
    lk3.set_data([], [])


def animate_drops(k):
    y0k = y0[k]
    if not np.isfinite(y0k):
        clear_drops()
        snap()
        return

    kf = min(n - 1, k + future_offset)

    y1s, y2s, y3s = y1[kf], y2[kf], y3[kf]
    x0, xs = x[k], x[kf]

    # link lines from source (future) to target (current)
    if np.isfinite(y1s):
        lk1.set_data([xs, x0], [y1s, y0k])
    else:
        lk1.set_data([], [])
    if np.isfinite(y2s):
        lk2.set_data([xs, x0], [y2s, y0k])
    else:
        lk2.set_data([], [])
    if np.isfinite(y3s):
        lk3.set_data([xs, x0], [y3s, y0k])
    else:
        lk3.set_data([], [])
    snap()
    clear_drops()

# make_legend()
set_axes_once()

# quick sanity frame (should show full l0 immediately)
plot_l0(0)
plot_l1_l2_l3(0)
snap(hold=50)

# pass 1
for k in tqdm(indices):
    k = int(k)
    if k < 0 or k >= n:
        continue
    plot_l0(k)
    plot_l1_l2_l3(k)
    animate_drops(k)

# pass 2 (dt vars)
colors = plt.cm.tab10.colors
prev = 0
for k in tqdm(indices):
    k = int(k)
    if k < 0 or k >= n:
        continue
    for v, c in zip(new_dt_vars, colors):
        yy = df_new[v].to_numpy()
        xs = np.array(x[prev:k])
        ys = yy[prev:k]
        m = np.isfinite(ys)
        ax.plot(xs[m], ys[m], color=c, lw=1.4)
    prev = k
    snap(hold=1)
    if k == 1:
        snap(hold=11)

snap(hold=50)

target_fps = 24
keep_every = max(1, int(round(fps / target_fps)))

with imageio.get_writer(out_gif, mode="I", fps=target_fps) as w:
    for i, fr in enumerate(frames):
        if i % keep_every == 0:
            w.append_data(fr)
plt.close(fig)

# %%
import math, os
from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np, pandas as pd

data_type="sites"
path_new=Path("../thredds-data/level_3_sites/csv/day") if data_type=="sites" else Path("../thredds-data/level_2_stations/csv/day")
out=Path(f"figures/snow_height/snow_height_mosaic.png")

N_COLS=6
ticks=list(np.cumsum([30,31,30,31,31,29,31,30,31,30,31,31]))
labels=["Sept." if i<30 else "Oct." if i<60 else
        "Nov." if i<90 else "Dec." if i<120 else "Jan." if i<150 else
        "Feb." if i<180 else "Mar." if i<210 else "Apr." if i<240 else
        "May"  if i<270 else "Jun." if i<300 else
        "Jul." if i<330 else "Aug." if i<360 else "" for i in ticks]

years=np.arange(1996,2027)
cmap=plt.get_cmap("tab20",len(years))
year_color={y:cmap(i) for i,y in enumerate(years)}
year_color[2026] = 'k'

stations= [ 'KAN_T',  'KAN_L', 'KAN_M', 'KAN_U','DY2', 'EGP', 'CEN', 'HUM', 'KPC_L', 'KPC_U','NAE', 'NAU', 'NEM', 'NSE', 'NUK_L', 'NUK_U',  'QAS_L', 'QAS_M','QAS_U', 'SCO_L', 'SCO_U', 'SDL', 'SDM', 'JAR','SWC','CP1', 'TAS_A', 'TAS_L', 'TAS_U', 'THU_L2', 'THU_L', 'THU_U', 'TUN', 'UPE_L','UPE_U', 'WEG_L']

# stations= ['FRE', 'LYN_L', 'LYN_T', 'MIT',  'NUK_K', 'RED_L',  'WEG_B', 'WEG_L', 'ZAC_A', 'ZAC_L', 'ZAC_U']

n=len(stations); nrows=math.ceil(n/N_COLS)
fig,ax=plt.subplots(nrows,N_COLS,figsize=(N_COLS*3.2,nrows*2.2),sharex=True,sharey=False)
ax=np.atleast_2d(ax)

handles={}
for i,st in enumerate(stations):
    r,c=divmod(i,N_COLS); a=ax[r,c]
    fp=path_new/f"{st}_day.csv"
    d=pd.read_csv(fp,usecols=lambda c:c in["time","snow_height"])
    if "snow_height" not in d.columns: a.axis("off"); continue
    d["time"]=pd.to_datetime(d["time"],errors="coerce")
    d["snow_height"]=pd.to_numeric(d["snow_height"],errors="coerce")
    d=d.dropna(subset=["time"]).set_index("time").sort_index()
    if d["snow_height"].dropna().empty: a.axis("off"); continue

    for y in sorted(d.index.year.unique().tolist()+[d.index.year.max()+1]):
        start=pd.Timestamp(f"{y-1}-09-01"); end=pd.Timestamp(f"{y}-08-31")
        dy=d.loc[(d.index>=start)&(d.index<end),["snow_height"]].copy()
        if dy.empty or dy["snow_height"].isnull().all(): continue
        dy["doy"]=dy.index.dayofyear.values-244
        dy.loc[dy["doy"]<0,"doy"]=365+dy.loc[dy["doy"]<0,"doy"]
        fvi=dy["snow_height"].first_valid_index()
        if fvi is None: continue
        ref=dy["snow_height"].loc[slice(fvi,fvi+pd.to_timedelta("30D"))].min()
        yy=dy["snow_height"]-ref
        if y in year_color:
            if y == 2026:
                a.plot(dy["doy"],yy,color='w',lw=5)[0]
            ln=a.plot(dy["doy"],yy,color=year_color[y],lw=1.2 if year != 2026 else 4.5)[0]
            handles.setdefault(y,ln)

    a.set_title(st)
    a.grid(True)
    a.set_xlim(1,365)
    a.set_ylim(0, 2.8)
    a.tick_params(axis="x", labelbottom=True)
    a.set_xticks(ticks)
    a.set_xticklabels(labels, rotation=45, ha="right")

for j in range(n,nrows*N_COLS):
    r,c=divmod(j,N_COLS); ax[r,c].axis("off")



handles=dict(sorted(handles.items(),reverse=True))
fig.legend(handles.values(),[str(y) for y in handles.keys()],
           loc="center right",bbox_to_anchor=(1,0.5),title="Year",ncol=1)

fig.text(0.01,0.5,"Snow Height (m)",va="center",rotation="vertical")
fig.tight_layout(rect=[0.03,0.02,0.95,1])
out.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(out,dpi=300)
plt.close(fig)


# %%
if True:
    import matplotlib.pyplot as plt
    import numpy as np

    data_type = 'sites'
    if data_type == 'sites':
        path_new = '../thredds-data/level_3_sites/csv/day/'
    else:
        path_new = '../thredds-data//level_2_stations/csv/day/'

    filename = 'plot_compilations/surface_height_'+data_type+'.md'

    # for file in os.listdir(path_new):
    for file in ['KAN_L_day.csv','NUK_L_day.csv','KPC_L_day.csv','NAU_day.csv']:
        station = file.replace('_day.csv','')
        if not os.path.isfile(path_new+file):
            Msg("cannot find"+path_new+file)
            continue

        df_new = pd.read_csv(path_new+file)
        df_new.time = pd.to_datetime(df_new.time, utc=True)
        df_new = df_new.set_index('time')

        if df_new.index.year[0]<2000:
            df_new=df_new.loc['2021':,:]

        dt_vars = [f'd_t_i_{i}' for i in range(1,11) if f'd_t_i_{i}' in df_new.columns]
        temp_vars = [f't_i_{i}' for i in range(1,11) if f't_i_{i}' in df_new.columns]
        new_dt_vars = [s+'_new' for s in dt_vars]
        for v in dt_vars:
            df_new[v+'_new'] =  df_new.z_surf_combined-df_new[v]

        times = df_new.index.values

        fig, ax = plt.subplots(figsize=(10,4), dpi=150)
        ax.set_title(station)
        sc = None
        for depth, temp in zip(dt_vars, temp_vars):
            sc = ax.scatter(df_new.index,
                            df_new[depth],
                            c=df_new[temp],
                            cmap='plasma',
                            s=8)
        plt.plot(df_new.index[[0, -1]],[0, 0],'k')
        ax.set_xlim(df_new.index[[0, -1]])
        ax.set_ylabel('Depth (m)')
        ax.invert_yaxis()
        plt.colorbar(sc, ax=ax, label="Temperature (°C)")


        fig.savefig(f"figures/string_processing/scatters/{station}.png", dpi=300)
        plt.close(fig)
