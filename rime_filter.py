import matplotlib.pyplot as plt
import numpy as np

sigma = 5.670374419e-8

t_rad = ds["t_rad"]
t_dlr = (ds["dlr"] / sigma) ** 0.25
t_ulr = (ds["ulr"] / sigma) ** 0.25

d_dlr = np.abs(t_dlr - t_rad-273.15)
d_ulr = np.abs(t_ulr - t_rad-273.15)
d_lr = np.abs(t_ulr -t_dlr)

import numpy as np
import xarray as xr

SIGMA_SB = 5.670374419e-8


import numpy as np
import xarray as xr

def _expand_runs(flag: xr.DataArray, dt_hours: xr.DataArray, persistence_hours: float, buffer_hours: float, time_dim: str):
    f = flag.fillna(False).astype(bool)

    # run ids for flagged periods
    rid = (f != f.shift({time_dim: 1}, fill_value=False)).cumsum(time_dim)

    # start/end markers for flagged runs
    prev = f.shift({time_dim: 1}, fill_value=False)
    nxt  = f.shift({time_dim: -1}, fill_value=False)

    is_start = f & (~prev)
    is_end   = f & (~nxt)

    idx = xr.DataArray(np.arange(f.sizes[time_dim], dtype=np.int64), coords={time_dim: f[time_dim]}, dims=(time_dim,))

    # run start/end index and time (hours)
    start_idx = idx.where(is_start).groupby(rid).min()
    end_idx   = idx.where(is_end).groupby(rid).max()

    h = xr.zeros_like(idx, dtype="float64")
    h.values = np.cumsum(dt_hours.fillna(0).values)

    start_h = h.where(is_start).groupby(rid).min()
    end_h   = h.where(is_end).groupby(rid).max()

    # map per-timepoint run start/end (only for flagged points; others NaN)
    s_idx = start_idx.sel({rid.name: rid}).rename(None)
    e_idx = end_idx.sel({rid.name: rid}).rename(None)
    s_h   = start_h.sel({rid.name: rid}).rename(None)
    e_h   = end_h.sel({rid.name: rid}).rename(None)

    # within persistence_hours from run start (before start) and within buffer_hours after run end
    near_start = (idx >= (s_idx - 10_000_000)) & (idx <= s_idx) & ((s_h - h) <= persistence_hours)
    near_end   = (idx >= e_idx) & ((h - e_h) <= buffer_hours)

    return (f | near_start | near_end).rename(flag.name)


def flag_persistent_radiative_temp_close_to_body(
    ds: xr.Dataset,
    flux_var: str,
    body_temp_var: str = "t_rad",
    diff_thr_K: float = 0.5,
    persistence_hours: float = 1.0,
    sigma_sb: float = SIGMA_SB,
    emissivity: float | None = None,
    buffer_hours: float = 5.0,
    time_dim: str = "time",
) -> xr.DataArray:
    eps = 1.0 if emissivity is None else float(emissivity)

    t_rad_K = (ds[flux_var] / (eps * sigma_sb)) ** 0.25
    t_body_K = ds[body_temp_var] + 273.15
    dK = np.abs(t_rad_K - t_body_K)

    below = dK < diff_thr_K

    run_id = (below != below.shift({time_dim: 1}, fill_value=False)).cumsum(time_dim)
    consec = below.groupby(run_id).cumsum().where(below, 0)

    dt = ds[time_dim].diff(time_dim)
    dt = dt.reindex({time_dim: ds[time_dim]}, method=None).shift({time_dim: -1})
    dt[{time_dim: -1}] = dt[{time_dim: -2}]
    dt_hours = (dt / np.timedelta64(1, "h")).astype("float64")

    consec_hours = consec * dt_hours

    base_flag = (consec_hours >= persistence_hours).rename(f"{flux_var}_close_to_{body_temp_var}_flag")

    # postprocess: include all points within persistence_hours of run start, and within buffer_hours after run end
    return _expand_runs(base_flag, dt_hours, persistence_hours=persistence_hours, buffer_hours=buffer_hours, time_dim=time_dim)



# Examples:
flag_dlr = flag_persistent_radiative_temp_close_to_body(ds, "dlr", diff_thr_K=0.5, persistence_hours=3.0)
flag_ulr = flag_persistent_radiative_temp_close_to_body(ds, "ulr", diff_thr_K=0.5, persistence_hours=3.0)


fig, ax_list = plt.subplots(2, 2, sharex=True)
[ax1, ax2, ax3, ax4] = ax_list.flatten()
ax1.plot(t_dlr.time, t_dlr-273.15, color='tab:blue',label="t_dlr")
ax1.plot(t_dlr.time, t_dlr.where(flag_dlr)-273.15, label="flagged", color='tab:red', marker='o')
ax1.plot(t_rad.time, t_rad, label="t_rad",color='tab:pink', alpha=0.7)

ax2.plot(t_ulr.time, t_ulr-273.15, label="t_ulr",color='tab:orange',)
ax2.plot(t_dlr.time, t_ulr.where(flag_ulr)-273.15, label="flagged", color='tab:red', marker='o')
ax2.plot(t_rad.time, t_rad, label="t_rad",color='tab:pink', alpha=0.7)
# ax1.set_ylabel("Radiative T (K)")
# ax1.plot(t_rad.time, consec_below, label="t_rad")


ax3.plot(t_rad.time, d_dlr, label="|t_dlr - t_rad|")
ax3.plot(t_rad.time, d_dlr.where(flag_dlr), label="|t_dlr - t_rad|", color='tab:red', marker='o')
ax4.plot(t_rad.time, d_ulr, label="|t_ulr - t_rad|")
ax4.plot(t_rad.time, ds.wspd_u, label="wspd")
ax4.plot(t_rad.time, d_ulr.where(flag_ulr), label="|t_ulr - t_rad|", color='tab:red', marker='o')
# ax2.plot(t_rad.time, d_lr, label="|t_ulr - t_dlr|")
for a in [ax2, ax4]:
    a.axhline(0.5, linestyle="--")
    a.set_ylabel("Abs diff (K)")
for a in (ax1, ax2, ax3, ax4):
    a.legend()

# --- improved y-labels ---
ax1.set_ylabel("DLR brightness temperature (°C)")
ax2.set_ylabel("ULR brightness temperature (°C)")
ax3.set_ylabel("|DLR Tb − body temperature| (K)")
ax4.set_ylabel("|ULR Tb − body temperature| (K)")

# --- compute flags for shortwave as well ---
flag_dsr =flag_ulr
flag_usr = flag_ulr

# --- show flagged timesteps (example plots) ---
fig2, (ax5, ax6) = plt.subplots(2, 1, sharex=True)

ax5.plot(ds.time, ds.dsr, label="dsr")
ax5.plot(ds.time, ds.dsr.where(flag_dsr), marker="o", linestyle="none", label="flagged")
ax5.set_ylabel("Downwelling shortwave (W m$^{-2}$)")
ax5.legend()

ax6.plot(ds.time, ds.usr, label="usr")
ax6.plot(ds.time, ds.usr.where(flag_usr), marker="o", linestyle="none", label="flagged")
ax6.set_ylabel("Upwelling shortwave (W m$^{-2}$)")
ax6.legend()

plt.show()
