# -*- coding: utf-8 -*-
"""
Created on %(date)s
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
    import matplotlib.pyplot as plt
"""
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

df["z_ice_surf_adj"].plot(ax=ax, label="z_ice_surf_adj")
hourly_interp.plot(ax=ax, label="hourly_interp")
once_smoothed.plot(ax=ax, label="once_smoothed")
smoothed_PT.plot(ax=ax, label="smoothed_PT")

idx = np.argwhere(
    np.diff(np.r_[False, ind_ablation, False])
).reshape(-1, 2)
idx[:, 1] -= 1

for start, end in idx:
    ax.axvspan(df.index[start], df.index[end], alpha=0.2)

ax2 = ax.twinx()
diff_series.plot(ax=ax2, label="diff", linestyle="--")
ax2.axhline(threshold_ablation, linestyle=":", label="threshold")

ax.legend(loc="upper left")
ax2.legend(loc="upper right")
