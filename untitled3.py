import numpy as np
import matplotlib.pyplot as plt

orig = ds22["t_u"].copy()
filt = filter_max_rate_iterative_bidir(orig, rmax=30.0)

t  = orig.time.values
vo = orig.values.astype(float)
vf = filt.values.astype(float)

removed = np.isfinite(vo) & ~np.isfinite(vf)

idx = np.arange(vo.size)
ok = np.isfinite(vo)
prev = np.maximum.accumulate(np.where(ok, idx, -1))
prev = np.roll(prev, 1); prev[0] = -1

ti = t.view("i8"); h = 3600e9
rate = np.full_like(vo, np.nan)
m = (prev >= 0) & ok
rate[m] = (vo[m] - vo[prev[m]]) / ((ti[m] - ti[prev[m]]) / h)

fig, ax1 = plt.subplots()
ax1.plot(t, vo, marker='o', ls='None')
ax1.plot(t, vf, marker='o', ls='None')
ax1.plot(t[removed], vo[removed], marker='o', ls='None')
ax1.set_ylabel(orig.attrs.get("units", ""))

ax2 = ax1.twinx()
ax2.plot(t[removed], rate[removed], marker='x', ls='None')
ax2.axhline(5.0, ls='--')
ax2.axhline(-5.0, ls='--')
ax2.set_ylabel("rate (unit/hour)")

plt.show()
