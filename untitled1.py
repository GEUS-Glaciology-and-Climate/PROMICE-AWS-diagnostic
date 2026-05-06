# -*- coding: utf-8 -*-
import os
import pandas as pd
import matplotlib.pyplot as plt

res = "day"
path_thredds = f"../thredds-data/level_3_sites/csv/{res}"

sites = {
    "EGP": "EastGRIP",
    "NAE": "NASA-East",
    "HUM": "Humboldt",
    "TUN": "Tunu-North",
    "CEN": "Century",
    "NEM": "NEEM",
    "NSE": "NASA-SE",
}

start_date = "1996-01-01"
end_date = "2025-12-31 23:59:59"

plt.figure(figsize=(11, 6))

for stid, site_name in sites.items():
    file_path = os.path.join(path_thredds, f"{stid}_{res}.csv")

    if not os.path.exists(file_path):
        print(f"WARNING: missing file {file_path}")
        continue

    df = pd.read_csv(file_path)
    df["time"] = pd.to_datetime(df["time"])
    df = df.set_index("time").loc[start_date:end_date]
    df = df.resample('ME').mean()

    wspd_col = None
    for col in ["wspd_l", "wspd_u"]:
        if col in df.columns:
            wspd_col = col
            break

    if wspd_col is None:
        print(f"WARNING: {stid} has no wind-speed column")
        continue

    alpha = 1.0 if stid in ["TUN","NSE"] else 0.3

    df[wspd_col].plot(
        label=f"{site_name} ({stid})",
        linewidth=1,
        alpha=alpha,
    )

plt.ylabel("Wind speed (m/s)")
plt.xlabel("")
plt.title("Daily wind speed at PROMICE/GC-Net stations, 2020–2025")
plt.legend(ncol=2)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig("wind_speed_all_stations_2020_2025.png", dpi=300)
plt.show()
