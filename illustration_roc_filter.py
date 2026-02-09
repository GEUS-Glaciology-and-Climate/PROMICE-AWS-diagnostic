# -*- coding: utf-8 -*-
"""
Created on %(date)s
@author: bav@geus.dk
"""

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
import os, logging, matplotlib
import lib.tocgen as tocgen
matplotlib.use('Agg')

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

matplotlib.set_loglevel("warning")
logging.getLogger('numba').setLevel(logging.WARNING)
import pypromice.resources
from pypromice.core.qc.value_clipping import clip_values
from pypromice.resources import load_variables
from pypromice.core.qc.persistence import persistence_qc
from pypromice.core.qc.github_data_issues import adjustTime, adjustData, flagNAN
from lib.utilities import (remove_old_plots, load_flags_and_adjustments, load_L1,
                 clean_gps, smooth_pose, compute_cloud_cover,
                 solar_geometry, filter_shortwave, correct_shortwave, compute_albedo,
                 process_precip)
from pypromice.core.qc.rate_of_change_filter import flag_high_rate_of_change, rate_of_change_fwd_bwd_and_thresholds


path_to_l0 = 'C:/Users/bav/GitHub/PROMICE data/aws-l0/'
filename = './plot_compilations/flags.md'
figure_folder='figures/flags'
os.makedirs(figure_folder, exist_ok=True)

df_metadata = pd.read_csv('../thredds-data/metadata/AWS_stations_metadata.csv')

f = open(filename, "w")
def Msg(txt):
    f = open(filename, "a"); print(txt); f.write(txt + "\n")

plt.close('all')

path_to_qc_files = '../PROMICE-AWS-data-issues/'
all_dirs = os.listdir(path_to_qc_files+'adjustments' )+os.listdir(path_to_qc_files+'flags')
var_file = os.path.join(os.path.dirname(pypromice.resources.__file__), "variables.csv")
# %%
# for station in ['TAS_Av3']: #['KAN_Lv3','QAS_Lv3','QAS_Mv3','SCO_Lv3','SCO_Uv3']:
for station in df_metadata.station_id.values[62:]:
    # %%
    station = 'ZAC_A'
    station = station.replace('.csv','')
    remove_old_plots(figure_folder, station)
    df_flags = load_flags_and_adjustments(path_to_qc_files, station)
    ds, ds_save, pAWS_tx, pAWS_raw = load_L1(path_to_l0, station)


    # The following steps are from L1toL2
    ds  = adjustTime(ds, adj_dir=path_to_qc_files+'adjustments')
    # ds1 = flagNAN(ds,  flag_dir=path_to_qc_files+'flags')
    # ds2 = adjustData(ds1, adj_dir=path_to_qc_files+'adjustments')
    ds1 = ds.copy()
    ds2 = ds1.copy()

    ds22 = persistence_qc(ds2)

    ds23 = ds22.copy(deep=True)
    #% Flagging, adjusting, filtering
    for var in ["rh_l"]:
    # for var in ["t_u","t_l","t_i",
    #             "rh_u","rh_l","rh_i",
    #             "p_u","p_l","p_i",
    #             "p_u","p_l","p_i",
    #                         ]+[f't_i_{k}' for k in range(1,12)]:
        if var not in ds22.data_vars: continue
        if ds22[var].isnull().all(): continue
# %%
    # %
        roc_ds, _, _ = rate_of_change_fwd_bwd_and_thresholds(ds22[var].dropna("time"), var)

        _, _, flag_combined, flag_final = flag_high_rate_of_change(ds22, var, window="7D")
        ds23[var].loc[{"time": flag_final.time[flag_final]}] = np.nan  # apply first pass

        if flag_final.any():
            roc_ds_2, _, _ = rate_of_change_fwd_bwd_and_thresholds(ds23[var].dropna("time"), var)

            _, _, flag_combined2, flag2 = flag_high_rate_of_change(ds23, var, window="7D")
            flag_combined2 = flag_combined2.reindex_like(flag_combined, fill_value=False)
            flag2 = flag2.reindex_like(flag_final, fill_value=False)

            flag_combined = (flag_combined | flag_combined2)
            flag_final = (flag_final | flag2)
        else:
            flag2 = None

        y = ds22[var]
        t = y.time
        fig, (ax1, ax2,ax3) = plt.subplots(3, 1, sharex=True, figsize=(15,10))

        ax1.plot(t, y, color="k")
        ax1.set_ylabel(var)
        ax1.set_title(station)
        ax1.grid()

        ax2.plot(roc_ds["time_rate"], roc_ds["roc_rate"], alpha=0.4, label="|dvar/dt|")
        ax2.plot(roc_ds["time_fwd"], roc_ds["roc_thr_fwd"], label="thr_fwd")
        if not (flag2 is None):
            ax2.plot(roc_ds_2["time_rate"], roc_ds_2["roc_rate"], label="|dvar/dt| second pass")
            ax2.plot(roc_ds_2["time_fwd"], roc_ds_2["roc_thr_fwd"], label="thr_fwd second pass")
        ax2.set_ylabel("Rate (°C h⁻¹)")
        ax2.legend()
        ax2.grid()

        ax3.plot(t, y, color="k",marker='.',linestyle='None',markersize=1, alpha=0.8)
        # forward-only
        # tf = flag_fwd.time[flag_fwd.values]
        # ax3.scatter(tf, y.sel(time=tf), marker="x", s=25, label='forward rate-of-change threshold')
        # backward-only
        # tb = flag_bwd.time[flag_bwd.values]
        # ax3.scatter(tb, y.sel(time=tb), marker="+", s=40, label='backward rate-of-change threshold')
        # both (override with a distinct symbol)
        # tbb = flag_combined.time[flag_combined.values]
        # ax3.scatter(tbb, y.sel(time=tbb), marker="^", s=50,  label='matching or before/after a gap')
        # both (override with a distinct symbol)
        tbf = flag_final.time[flag_final.values]
        ax3.scatter(tbf, y.sel(time=tbf), marker="o",
                    color='tab:red', s=60,
                    label='outliers first pass')
        if not (flag2 is None):
            tbf = flag2.time[flag2.values]
            ax3.scatter(tbf, y.sel(time=tbf), marker="o",
                        color='tab:orange', s=60,
                        label='outliers second pass')
        ax3.grid()
        if tbf.count()>2:
            ax3.set_xlim(tbf[0]-pd.to_timedelta( "7D"), tbf[-1]+pd.to_timedelta( "7D"))

        ax3.set_ylabel(var)
        plt.legend(loc='lower left')
        fig.savefig(f'figures/ROC_filter/{station}_{var}.png', dpi=120)


# %%
import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt


from pypromice.core.qc.rate_of_change_filter import (flag_high_rate_of_change,
                                        unflag_if_linear_interp, _get_params
                                    )

TOL = 3.
FACTOR = 2.2

def make_irregular_time(start="2024-01-01", n=200, base="10min", drop_frac=0.15, seed=0):
    rng = np.random.default_rng(seed)
    t = pd.date_range(start, periods=n, freq=base)
    keep = rng.random(n) > drop_frac
    t = t[keep].to_numpy()
    return xr.DataArray(t, dims=("time",), name="time")


def process_case(ds, var="t_u"):
    flag_fwd, flag_bwd, flag_combined, flag_final = flag_high_rate_of_change(ds, var, tol=TOL, factor=FACTOR )
    y = ds[var].sel(time=flag_combined.time)
    return dict(ds=ds, var=var, y=y,
                flag_fwd=flag_fwd, flag_bwd=flag_bwd,
                flag_combined=flag_combined, flag_final=flag_final)


def plot_four_panel(results, titles, var="t_u", figsize=(12, 8)):
    fig, axes = plt.subplots(4, 1, figsize=figsize, sharex=False)

    for ax, res, title in zip(axes, results, titles):

        ds = res["ds"]
        y = res["y"]
        fwd = res["flag_fwd"]
        bwd = res["flag_bwd"]
        comb = res["flag_combined"]
        final = res["flag_final"]

        if ("Case A" in title)|("Case D" in title):
            t = pd.to_datetime(ds.time.values)
            v_all = ds[var].values.astype("float64")

            # A = last non-flagged point in final
            ok = (~comb).values.astype(bool)
            iA = int(np.flatnonzero(ok[:-1] & ~ok[1:])[0])

            # B = first index after which all values are unflagged in comb
            iB = int(np.flatnonzero(~ok[:-1] & ok[1:])[0] + 1)

            tA, tB = t[iA], t[iB]
            vA, vB = v_all[iA], v_all[iB]

            # ax.scatter([tA], [vA], marker="D", s=70,color='k', label="last valid before flag")
            # ax.scatter([tB], [vB], marker="^", s=70,color='k', label="first valid after flag")

            tt = pd.date_range(tA, tB, periods=100)
            w = (tt.view("i8") - tA.value) / (tB.value - tA.value)
            vhat = vA + w * (vB - vA)

            ax.fill_between(tt, vhat - tol, vhat + tol, color="0.6", alpha=0.35, zorder=0)
            # ax.plot(tt, vhat - tol, color="0.5", ls="None", lw=1)
            # ax.plot(tt, vhat + tol, color="0.5", ls=":", lw=1)

        ax.plot(ds.time, ds[var], color="k", alpha=0.25, lw=1, marker='.',label=var)

        tf = fwd.time[fwd.values]
        tb = bwd.time[bwd.values]
        tc = comb.time[comb.values]
        tfin = final.time[final.values]

        ax.scatter(tf, y.sel(time=tf), marker="x", s=30, label="fwd ROC filter")
        ax.scatter(tb, y.sel(time=tb), marker="+", s=60, label="bwd ROC filter")
        ax.scatter(tc, y.sel(time=tc), marker="o", s=70, alpha=0.35, label="combined")
        ax.scatter(tfin, y.sel(time=tfin), marker="s", s=40, label="final",color='tab:red')

        ax.set_title(title)
        ax.set_ylabel(var)
        ax.grid(True, alpha=0.3)

        ax.legend(ncol=3, loc="upper left")
    ax.set_xlim(pd.to_datetime(['2024-01-01T02', '2024-01-01T22']))
    plt.tight_layout()
    plt.show()


tol, factor = _get_params(var, tol=TOL, factor=FACTOR)


# -----------------------
# Case A
# -----------------------
start="2024-01-01"
n=400
base="10min"
t = pd.date_range(start, periods=n, freq=base)
x = np.arange(len(t))
slope = 1  # units per x
plateau_low = -30.0
plateau_high = -10.0
x0 = 280  # ramp crosses 0 here
ramp = slope * (x - x0)           # crosses 0 at x=100
plateau = np.clip(ramp, plateau_low, plateau_high)
base = plateau + 2*np.sin(2*np.pi*x/60)

v = base.copy()
k = x0-15
v[k] = v[k] + 10
mask = np.ones_like(v, dtype=bool)
mask[k-5:k-4] = False
mask[k+1:k+5] = False
v = v[mask]
t = t[mask]
dsA = xr.Dataset({"t_u": (("time",), v)}, coords={"time": t})

# -----------------------
# Case B
# -----------------------
time = make_irregular_time(seed=2)
t = pd.to_datetime(time.values)
x = np.arange(len(t))
v = -25 + 0.015 * x + 0.15 * np.sin(2 * np.pi * x / 80)
v[len(v)//2] = v[len(v)//2 - 1] + 8.0
dsB = xr.Dataset({"t_u": (("time",), v)}, coords={"time": t})

# -----------------------
# Case C
# -----------------------
time = make_irregular_time(seed=3, drop_frac=0.05)
t = pd.to_datetime(time.values)
x = np.arange(len(t))
v = -15 + 0.25 * np.sin(2 * np.pi * x / 50)
m0, m1 = 85, 130
v[m0:m1] = np.nan
v[m0+10] = -5.0
v[m0+15] = -10.0
dsC = xr.Dataset({"t_u": (("time",), v)}, coords={"time": t})

# -----------------------
# Case D
# -----------------------
time = make_irregular_time(seed=5)
t = pd.to_datetime(time.values)
x = np.arange(len(t))
v = -10 + 0.02 * x + 0.1 * np.sin(2 * np.pi * x / 70)
k = len(v) // 2
v[k - 1] = v[k - 1] + 6.0
v[k] = v[k] + 6.0
# v[k + 1] = 0.5 * (v[k - 1] + v[k + 2]) + 0.05
dsD = xr.Dataset({"t_u": (("time",), v)}, coords={"time": t})

# Process
resA = process_case(dsA)
resB = process_case(dsB)
resC = process_case(dsC)
resD = process_case(dsD)

# Plot
plot_four_panel(
    [resA, resB, resC, resD],
    [
        f"Case A: interpolable spike (tol={tol})",
        "Case B: true outlier",
        "Case C: isolated point near NaNs",
        "Case D: two-point event (not flagging)",
    ],
)

# run once to print expected flag times for each case
cases = {"A": dsA, "B": dsB, "C": dsC, "D": dsD}

for name, ds in cases.items():
    _, _, comb, final = flag_high_rate_of_change(ds, "t_u", tol=TOL, factor=FACTOR)
    times = pd.to_datetime(final.time.values[final.values]).strftime("%Y-%m-%dT%H:%M:%S").tolist()
    print(f"CASE_{name}_FINAL_TIMES = {times}")
