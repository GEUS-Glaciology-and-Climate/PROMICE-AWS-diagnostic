from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

folder = Path("../aws-l3-dev/csv/hour/")                        # folder with {station}.csv
folder = Path("../thredds-data/level_3_sites/csv/hour/")                        # folder with {station}.csv
TOL = 0.11                                # equality tolerance (units of z_*)
MIN_DURATION = pd.Timedelta("7D")         # min duration of equality run
PLOT_PAD = pd.Timedelta("30D")            # one month each side
MERGE_GAP = pd.Timedelta("3D")            # max gap to merge adjacent runs
PAIRS = [("z_boom_u", "z_boom_l"), ("z_boom_u", "z_stake")]

def read_station_csv(p: Path) -> pd.DataFrame:
    return pd.read_csv(p, parse_dates=[0], index_col=0).sort_index()

def equal_runs(a: pd.Series, b: pd.Series, tol: float):
    a = a.rolling("24h", center=True, min_periods=1).median()
    b = b.rolling("24h", center=True, min_periods=1).median()
    mask = a.notna() & b.notna()
    a = a[mask]
    b = b[mask]
    m = (a != 0) & (a.sub(b).abs() <= tol)
    if m.empty or not m.any():
        return []
    grp = (m != m.shift()).cumsum()
    out = []
    for _, s in m.groupby(grp):
        if not s.iloc[0]:
            continue
        t0, t1 = s.index[0], s.index[-1]
        if (t1 - t0) >= MIN_DURATION:
            out.append((t0, t1))
    return out

def merge_runs(runs, gap=MERGE_GAP):
    if not runs:
        return []
    runs = sorted(runs, key=lambda r: r[0])
    merged = [runs[0]]
    for t0, t1 in runs[1:]:
        last_t0, last_t1 = merged[-1]
        if t0 - last_t1 <= gap:
            merged[-1] = (last_t0, max(last_t1, t1))
        else:
            merged.append((t0, t1))
    return merged

def suspect_switch(a: pd.Series, b: pd.Series, t0):
    i0 = a.index.searchsorted(t0)
    if i0 == 0:
        return "unknown"
    t_prev = a.index[i0-1]
    da = (a.iloc[i0] - a.loc[t_prev]) if pd.notna(a.iloc[i0]) and pd.notna(a.loc[t_prev]) else np.nan
    db = (b.iloc[i0] - b.loc[t_prev]) if pd.notna(b.iloc[i0]) and pd.notna(b.loc[t_prev]) else np.nan
    if np.isnan(da) and np.isnan(db):
        return "unknown"
    if np.isnan(db):
        return a.name
    if np.isnan(da):
        return b.name
    return a.name if abs(da) > abs(db) else b.name

def plot_window(df, a, b, t0, t1, station, outdir: Path):
    w0 = t0 - PLOT_PAD
    w1 = t1 + PLOT_PAD
    ax = df[[a, b]].loc[w0:w1].plot(marker='.', linewidth=0.8)
    ax.axvspan(t0, t1, alpha=0.15)
    ax.set_title(f"{station}: {a} vs {b}  [{t0.date()} → {t1.date()}]")
    ax.legend()
    outdir.mkdir(parents=True, exist_ok=True)
    fn = outdir / f"{station}_{a}_vs_{b}_{t0.date()}_{t1.date()}.png"
    plt.savefig(fn, dpi=150, bbox_inches="tight")
    plt.close()

plots_dir = Path("figures/plots_equal_runs")

# for csv_path in [Path(str(folder)+'/UPE_L_hour.csv')]:  
for csv_path in sorted(folder.glob("*.csv")):
    print(csv_path)
    station = csv_path.stem
    df = read_station_csv(csv_path)
    avail = set(df.columns)
    for a, b in PAIRS:
        if a not in avail or b not in avail:
            continue
        runs = equal_runs(df[a], df[b], TOL)
        runs = merge_runs(runs, MERGE_GAP)
        for t0, t1 in runs:
            suspect = suspect_switch(df[a], df[b], t0)
            mean_diff = (df[a] - df[b]).loc[t0:t1].dropna().mean()
            print(f"{t0.isoformat()},{t1.isoformat()},{suspect},one SR50 failing and taking value of the other,https://github.com/GEUS-Glaciology-and-Climate/PROMICE-AWS-data-issues/issues/3")
            plot_window(df, a, b, t0, t1, station, plots_dir)
