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


def flag_persistent_radiative_temp_close_to_body(
    ds: xr.Dataset,
    flux_var: str,
    body_temp_var: str = "t_rad",
    diff_thr_K: float = 0.5,
    persistence_hours: float = 1.0,
    sigma_sb: float = SIGMA_SB,
    emissivity: float | None = None,
    time_dim: str = "time",
) -> xr.DataArray:
    """Flags periods where radiative temperature stays close to body temperature.

    Converts a longwave flux (e.g., 'dlr' or 'ulr') to a radiative brightness temperature
    using Stefan–Boltzmann, computes the absolute difference to the radiometer body
    temperature, and flags times when that difference remains below a threshold for
    longer than a specified persistence (in hours), accounting for irregular timesteps.

    Args:
        ds: Dataset containing the flux and body temperature variables.
        flux_var: Name of the longwave flux variable (W m-2), e.g. 'dlr' or 'ulr'.
        body_temp_var: Name of the radiometer body temperature variable (degC).
        diff_thr_K: Threshold for |T_rad - T_body| in Kelvin.
        persistence_hours: Minimum consecutive time below threshold to flag (hours).
        sigma_sb: Stefan–Boltzmann constant.
        emissivity: Optional emissivity (use e.g. 0.99 for surface ULR); if None, use 1.0.
        time_dim: Name of the time dimension.

    Returns:
        Boolean DataArray (same time coordinate) where True indicates persistent closeness.
    """
    # Pick emissivity (DLR typically uses 1.0; ULR may use ~0.99 for snow/ice).
    eps = 1.0 if emissivity is None else float(emissivity)

    # Radiative temperature from flux (Kelvin).
    t_rad_K = (ds[flux_var] / (eps * sigma_sb)) ** 0.25

    # Body temperature in Kelvin (input assumed degC).
    t_body_K = ds[body_temp_var] + 273.15

    # Absolute difference in Kelvin.
    dK = np.abs(t_rad_K - t_body_K)

    # Threshold test.
    below = dK < diff_thr_K
    print(diff_thr_K)

    # Identify consecutive runs of equal boolean values.
    run_id = (below != below.shift({time_dim: 1}, fill_value=False)).cumsum(time_dim)

    # Count consecutive samples within each "below" run; reset to 0 outside.
    consec = below.groupby(run_id).cumsum().where(below, 0)

    # Irregular timestep duration in hours (assign dt to the interval starting at each sample).
    dt = ds[time_dim].diff(time_dim)
    dt = dt.reindex({time_dim: ds[time_dim]}, method=None).shift({time_dim: -1})
    dt[{time_dim: -1}] = dt[{time_dim: -2}]
    dt_hours = dt / np.timedelta64(1, "h")

    # Convert consecutive counts to consecutive hours below threshold.
    consec_hours = consec * dt_hours

    # Persistence flag.
    return (consec_hours >= persistence_hours).rename(f"{flux_var}_close_to_{body_temp_var}_flag")


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

plt.show()
