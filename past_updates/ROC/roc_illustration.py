# -*- coding: utf-8 -*-
"""
Created on %(date)s
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""

import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 1, figsize=(10, 6), sharex=True, constrained_layout=True)
ds22 = ds22.sel(time=slice("2024-01-01", "2026-01-01"))
roc_ds = roc_ds.sel(time_rate=slice("2024-01-01", "2026-01-01"))
roc_ds = roc_ds.sel(time_fwd=slice("2024-01-01", "2026-01-01"))
# --- temperature ---
ds22.t_u.plot(ax=ax[0], c='tab:blue', lw=1.5)
ax[0].set_ylabel('Air temperature (°C)')
ax[0].set_xlabel('')
ax[0].set_title('NAE')
ax[0].grid(ls='--', alpha=0.4)

# --- rate of change ---
roc_ds.roc_rate.plot(ax=ax[1], c='k', lw=1, label='Rate of change')
# roc_ds.roc_thr_fwd.plot(ax=ax[1], c='tab:orange', lw=3,  label='Threshold (~2x 95th percentile)')

ax[1].set_ylabel('Rate of change  (°C / hr)')
ax[1].grid(ls='--', alpha=0.4)
ax[1].legend(loc="upper right")

fig.savefig('roc_illustration_2.png',dpi=120)
