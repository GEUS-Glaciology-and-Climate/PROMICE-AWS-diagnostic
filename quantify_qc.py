# -*- coding: utf-8 -*-
"""
Created on %(date)s
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


logging.getLogger('matplotlib.font_manager').disabled = True
logging.getLogger("pypromice").setLevel(logging.DEBUG)
logging.getLogger("pypromice.pipeline").setLevel(logging.DEBUG)
logging.getLogger("pypromice.pipeline.get_l2").setLevel(logging.DEBUG)
logging.getLogger('numba').setLevel(logging.WARNING)


def process_l2_no_qc(station,
                     output_path = 'L2_no_qc',
                     data_issues_path='../PROMICE-AWS-data-issues_no'):

    print(station)
    # Loading the L1 data:
    path_to_l0 = '../aws-l0/'
    config_folder = '../aws-l0/metadata/station_configurations/'
    config_file_tx = path_to_l0 + '/tx/config/{}.toml'.format(station)
    config_file_raw = path_to_l0 + '/raw/config/{}.toml'.format(station)



    print("\n ======== test get_l2 ========= \n")
    if os.path.isfile(config_file_tx):
        inpath = path_to_l0 + '/tx/'
        pAWS_tx = get_l2(config_file_tx,
                         inpath,
                         output_path+'/tx/',
                         variables=None, metadata=None,
                         data_issues_path=data_issues_path)

    else:
        pAWS_tx = None

    if os.path.isfile(config_file_raw):
        inpath = f'{path_to_l0}/raw/{station}/'
        pAWS_raw = get_l2(config_file_raw,
                          inpath,
                          output_path+'/raw/',
                         variables=None, metadata=None,
                         data_issues_path=data_issues_path)
    else:
        pAWS_raw = None

    print("\n ======== test join_l2 ========= \n")
    l2_merged = join_l2(f'{output_path}/raw/{station}/{station}_hour.nc',
                        f'{output_path}/tx/{station}/{station}_hour.nc',
                        f'{output_path}/level_2/',None,None)

if __name__ == '__main__':
    df_metadata = pd.read_csv('../thredds-data/metadata/AWS_stations_metadata.csv')
    # for station in ['CEN1']:
    for station in df_metadata.station_id[1:]:
        # process_l2_no_qc(station,
        #                       output_path = 'L2_no_qc',
        #                       data_issues_path='../PROMICE-AWS-data-issues_no')
        process_l2_no_qc(station,
                             output_path = 'L2_test',
                             data_issues_path='../PROMICE-AWS-data-issues')

# %%

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
path_no_flag = './L2_no_qc/level_2'
path_w_flag= './L2_test/level_2'


df_metadata = pd.read_csv('../thredds-data/metadata/AWS_stations_metadata.csv')
# for station in ['CEN1']:
station_list = ['CEN1', 'CEN2','EGP','HUM','KAN_M','NAE','NAU','NEM', 'NUK_L','QAS_U', 'QAS_Uv3','SDM','TAS_A','TAS_U']
for station in station_list:
# for station in np.unique(np.array(df_metadata.station_id)):
    var_list = [
            't_u','t_l','t_i'
            'p_u','p_l','p_i',
            'rh_l','rh_i','rh_l_cor',
            'dlr','ulr','dsr','usr',
            'z_boom_u','z_boom_l','z_stake'
            'wspd_u','wspd_l','wspd_i'
            ]

    print(station)
    df_no_flags = pd.read_csv(f'{path_no_flag}/{station}/{station}_hour.csv')
    df_no_flags.time = pd.to_datetime(df_no_flags.time, utc=True)
    df_no_flags = df_no_flags.set_index('time')

    df_w_flags = pd.read_csv(f'{path_w_flag}/{station}/{station}_hour.csv')
    df_w_flags.time = pd.to_datetime(df_w_flags.time, utc=True)
    df_w_flags = df_w_flags.set_index('time')

    out = {}
    expected = {}

    for v in var_list:
        if v in df_no_flags.columns and v in df_w_flags.columns:
            m = df_w_flags[v].isna() & df_no_flags[v].notna()
            out[v] = m.sum()
        else:
            out[v] = 0
        expected[v] = len(df_no_flags.index)

    pd.DataFrame({"missing": out, "expected": expected}).to_csv(f"nan_counts_{station}.csv")


    var_list = [v for v in var_list if out[v]>0]

    df_no_flags=df_no_flags.resample('D').mean()
    df_w_flags=df_w_flags.resample('D').mean()

    var_list = [v for v in var_list if v in df_w_flags.columns]

    fig, ax_list = plt.subplots(len(var_list)+1,1,sharex=True, figsize=(8,8))
    fig.subplots_adjust(top=0.85, left=0.08, right=0.98,bottom=0.08)
    if len(var_list)==0:
        continue

    for var, ax, var_label in zip(var_list, ax_list, var_list):

        ax.set_ylabel(var)

        ax.plot(df_no_flags[var].index, df_no_flags[var].values, marker='.', lw=3,
                color='tab:red', label='bad measurements'
                )

        ax.plot(df_no_flags[var].index, df_no_flags[var].values, marker='.', lw=3,
                color='tab:blue', label='good measurements'
                )

    t_i_vars = [f't_i_{i}' for i in range(1,11) if f't_i_{i}' in df_no_flags.columns]

    ax_list[-1].plot(df_no_flags[t_i_vars].index, df_no_flags[t_i_vars].values, marker='.',
            color='tab:blue',
            )
    ax_list[-1].set_ylabel('t_i_*')
    ax_list[0].legend( loc="upper center", ncols=2,
        bbox_to_anchor=(0.5, 0.98),   # 0.98 = just under top of figure
        bbox_transform=fig.transFigure,
        fontsize=12, title=station )
    fig.savefig('figures/flagged_data/'+station+'_1.png',dpi=300)

    fig, ax_list = plt.subplots(len(var_list)+1,1,sharex=True, figsize=(8,8))
    fig.subplots_adjust(top=0.85, left=0.08, right=0.98,bottom=0.08)
    for var, ax, var_label in zip(var_list, ax_list, var_list):

        ax.set_ylabel(var)

        ax.plot(df_no_flags[var].index, df_no_flags[var].values, marker='.',lw=3,
                color='tab:red', label='bad measurements')
        ax.plot(df_w_flags[var].index, df_w_flags[var].values, marker='.',lw=3,
                color='tab:blue', label='good measurements')


    t_i_vars = [f't_i_{i}' for i in range(1,11) if f't_i_{i}' in df_no_flags.columns]
    ax_list[-1].plot(df_no_flags[t_i_vars].index, df_no_flags[t_i_vars].values, marker='.',
            color='tab:red')

    ax_list[-1].plot(df_w_flags[t_i_vars].index, df_w_flags[t_i_vars].values, marker='.',
            color='tab:blue',)
    ax_list[-1].set_ylabel('t_i_*')

    ax_list[0].legend( loc="upper center", ncols=2,
        bbox_to_anchor=(0.5, 0.98),   # 0.98 = just under top of figure
        bbox_transform=fig.transFigure,
        fontsize=12, title=station )
    fig.savefig('figures/flagged_data/'+station+'_2.png',dpi=300)

#%%

import pandas as pd
df_metadata = pd.read_csv('../thredds-data/metadata/AWS_stations_metadata.csv')
df_metadata = df_metadata.loc[df_metadata.location_type=='ice sheet',:]
import imageio.v2 as imageio
import glob

files = sorted(glob.glob("figures/flagged_data/*.png"))
files = [f for f in files if f.split('\\')[-1].split('_1')[0].split('_2')[0] in \
         station_list]
images = [imageio.imread(f) for f in files]
imageio.mimsave("figures/flagged_data/all.gif", images, fps=1.2)

# %%
import pandas as pd
import matplotlib.pyplot as plt
import glob
import numpy as np

station_list = ['CEN1','CEN2','EGP','HUM','KAN_M','NEM',
                'NUK_L','QAS_U','QAS_Uv3','SDM','TAS_A','TAS_U']

files = glob.glob("logs/flagged_data_count/nan_counts_*.csv")

df_all = []
all_stations = []

for f in files:
    st = f.split("nan_counts_")[1].split(".csv")[0]
    df = pd.read_csv(f)
    df = df.rename(columns={df.columns[0]: "variable"})
    df["station"] = st
    df_all.append(df)
    all_stations.append(st)

df_all = pd.concat(df_all)

# reversed variable order
order = ["usr","dsr","ulr","dlr","z_boom_u","wspd_i","rh_i","p_i","t_u"]
variable_labels = ["Upward\nshortwave\nradiation",
                   "Downward\nshortwave\nradiation",
                   "Upward\nlongwave\nradiation",
                   "Downward\nlongwave\nradiation",
                   "Boom height",
                   "Wind speed",
                   "Relative\nhumidity",
                   "Air pressure",
                   "Air temperature"]

df_all = df_all[df_all.variable.isin(order)].copy()
df_all["variable"] = pd.Categorical(df_all.variable, categories=order, ordered=True)
df_all = df_all.sort_values("variable")

primary = set(station_list)
others = sorted(set(all_stations) - primary - {'LYN_L','NUK_B','LYN_T'})

# --- plotting
fig, ax = plt.subplots(1,1,figsize=(7,7))
fig.subplots_adjust(left=0.23, top=0.9, bottom=0.06, right=0.99)
# ---- other stations first (thin gray lines)
for st in others:
    sub = df_all[df_all.station == st]
    pct = 100 * sub.missing / sub.expected
    plt.plot(pct, sub.variable, color='lightgray', lw=1, label='__nolegend__')

# dummy for legend entry (last)

# ---- primary stations (colored, thicker, markers)
cmap = plt.cm.tab20
colors = cmap(np.linspace(0, 1, len(primary)))

for st, c in zip(primary, colors):
    sub = df_all[df_all.station == st]
    pct = 100 * sub.missing / sub.expected
    plt.plot(pct, sub.variable, marker='o', lw=2, color=c, label=st)
plt.plot(np.nan, np.nan, color='lightgray', lw=1, label='other stations')

plt.xlabel("% removed through QC", fontsize=14)

ax.xaxis.set_label_position('top')
ax.tick_params(axis="x", bottom=True, top=True, labelbottom=True, labeltop=True)
plt.grid(True, alpha=0.3)
plt.yticks(ticks=range(len(order)), labels=variable_labels)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(ncol=2, fontsize=12,
           bbox_to_anchor=(1, 0.90), loc="upper right")

plt.savefig("figures/flagged_data/all_summary.png", dpi=200)
plt.show()
# %%import pandas as pd
import matplotlib.pyplot as plt
import glob
import numpy as np
from pathlib import Path

station_list = ['CEN1','CEN2','EGP','HUM','KAN_M','NEM',
                'NUK_L','QAS_U','QAS_Uv3','SDM','TAS_A','TAS_U']

files = glob.glob("metadata/qc_info/*_flagged_pct.csv")

df_all = []
all_stations = []

for f in files:
    st = Path(f).name.replace("_flagged_pct.csv", "")
    df = pd.read_csv(f)
    df = df.rename(columns={df.columns[0]: "variable", df.columns[1]: "pct"})
    df = df.dropna(subset=["variable"]).groupby("variable", as_index=False)["pct"].max()
    df["station"] = st
    df_all.append(df)
    all_stations.append(st)

df_all = pd.concat(df_all, ignore_index=True)

order = ["usr","dsr","ulr","dlr","z_boom_u","wspd_u","rh_u","p_u","t_u"]
variable_labels = ["Upward\nshortwave\nradiation",
                   "Downward\nshortwave\nradiation",
                   "Upward\nlongwave\nradiation",
                   "Downward\nlongwave\nradiation",
                   "Boom height",
                   "Wind speed",
                   "Relative\nhumidity",
                   "Air pressure",
                   "Air temperature"]

df_all = df_all[df_all.variable.isin(order)].copy()
df_all["variable"] = pd.Categorical(df_all.variable, categories=order, ordered=True)
df_all = df_all.sort_values("variable")
df_all["y"] = df_all["variable"].cat.codes

primary = station_list
others = sorted(set(all_stations) - set(primary) - {'LYN_L','NUK_B','LYN_T'})

fig, ax = plt.subplots(figsize=(7,7))
fig.subplots_adjust(left=0.23, top=0.9, bottom=0.06, right=0.99)

# other stations: gray markers only
for st in others:
    sub = df_all[df_all.station == st]
    jitter = 0.15
    y_jittered = sub["y"] + np.random.uniform(-jitter, jitter, size=len(sub))

    ax.plot(sub["pct"], y_jittered, ls="None", marker="o", ms=4,
            color="lightgray", alpha=0.7)


# highlighted stations: varying color + marker
markers = ['o','s','^','D','v','P','X','<','>','*','h','p']
colors = plt.cm.tab20(np.linspace(0, 1, len(primary)))

for st, c, m in zip(primary, colors, markers):
    sub = df_all[df_all.station == st]
    y_jittered = sub["y"] + np.random.uniform(-jitter, jitter, size=len(sub))

    ax.plot(sub["pct"], y_jittered, ls="None", marker=m, ms=10,
            color=c, label=st)

ax.plot(np.nan, np.nan, ls="None", marker="o", ms=5, color="lightgray", label="other stations")
# mean value for each variable across all stations shown
mean_df = df_all.groupby("variable", observed=True)["pct"].mean().reindex(order).reset_index()
mean_df["y"] = np.arange(len(order))
ax.plot(mean_df["pct"], mean_df["y"],
        marker='|', ms=20, mew=4,   # mew controls thickness
        ls='None', c='k', label="mean")
ax.set_xlabel("% removed through QC", fontsize=14)
ax.xaxis.set_label_position('top')
ax.tick_params(axis="x", bottom=True, top=True, labelbottom=True, labeltop=True)
ax.grid(True, alpha=0.3)
ax.set_yticks(np.arange(len(order)), variable_labels)
ax.tick_params(axis='both', labelsize=12)
ax.legend(ncol=2, fontsize=12, loc="upper right")

plt.savefig("figures/flagged_data/all_summary.png", dpi=200)
plt.show()
