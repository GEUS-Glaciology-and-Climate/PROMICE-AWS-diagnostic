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
# -*- coding: utf-8 -*-
import os
import numpy as np
import pandas as pd

res = 'day'
path_thredds = f"../thredds-data/level_3_sites/csv/{res}"

sites = {
    "EGP": "EastGRIP",
    "NAE": "NASA-East",
    "HUM": "Humboldt",
    "TUN": "Tunu-North",
    "CEN": "Century",
    "NEM": "NEEM",
}

start_date = "2016-01-01"
end_date = "2025-12-31 23:59:59"

def compass_sector(deg):
    sectors = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
               "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    return sectors[int((deg + 11.25) / 22.5) % 16]

winter_months = [12, 1, 2]

def monthly_coverage_table(df, cols):
    df_daily = df[cols].resample("D").mean()

    full_days = pd.date_range(
        start=df_daily.index.min().normalize(),
        end=df_daily.index.max().normalize(),
        freq="D",
        tz=df_daily.index.tz,
    )

    df_daily = df_daily.reindex(full_days)

    monthly = []
    for month, group in df_daily.groupby(df_daily.index.to_period("M")):
        expected_days = month.days_in_month
        available_days = group.dropna(how="all").shape[0]

        monthly.append({
            "month": month,
            "coverage": available_days / expected_days,
            "available_days": available_days,
            "expected_days": expected_days,
        })

    return pd.DataFrame(monthly)


def print_missing_periods(df, stid, cols, min_coverage=0.50):
    monthly = monthly_coverage_table(df, cols)
    monthly["is_missing"] = monthly["coverage"] < min_coverage

    groups = (monthly["is_missing"] != monthly["is_missing"].shift()).cumsum()

    for _, group in monthly[monthly["is_missing"]].groupby(groups):
        start = group["month"].iloc[0]
        end = group["month"].iloc[-1]

        available = group["available_days"].sum()
        expected = group["expected_days"].sum()
        coverage = available / expected

        if start == end:
            period_txt = f"{start}"
        else:
            period_txt = f"{start} to {end}"

        print(
            f"WARNING: {stid} missing data from {period_txt} "
            f"({coverage:.0%} coverage, {available}/{expected} days)"
        )

def circular_mean_deg(direction_deg, speed=None):
    d = np.deg2rad(direction_deg.dropna())

    if len(d) == 0:
        return np.nan

    if speed is not None:
        w = speed.loc[direction_deg.dropna().index].fillna(0).values
    else:
        w = np.ones(len(d))

    x = np.sum(w * np.sin(d))
    y = np.sum(w * np.cos(d))

    return (np.rad2deg(np.arctan2(x, y)) + 360) % 360

rows = []

for stid, site_name in sites.items():
    file_path = os.path.join(path_thredds, f"{stid}_{res}.csv")
    df = pd.read_csv(file_path)

    df["time"] = pd.to_datetime(df["time"])
    df = df.set_index("time").loc[start_date:end_date]

    t_col = "t_u" if "t_u" in df.columns else ("t_l" if "t_l" in df.columns else None)
    wspd_col = "wspd_u" if "wspd_u" in df.columns else ("wspd_l" if "wspd_l" in df.columns else None)
    wdir_col = "wdir_u" if "wdir_u" in df.columns else ("wdir_l" if "wdir_l" in df.columns else None)
    print_missing_periods(
        df,
        stid,
        cols=[t_col, wspd_col, wdir_col],
        min_coverage=0.50,
    )

    elev_col = None
    for c in ["alt"]:
        if c in df.columns:
            elev_col = c
            break

    elev = np.nanmedian(df[elev_col]) if elev_col else np.nan

    wind_dir = circular_mean_deg(df[wdir_col], speed=df[wspd_col])
    wind_dir_txt = f"{wind_dir:.0f}° ({compass_sector(wind_dir)})"

    rows.append({
        "Site": f"{site_name} ({stid})",
        "Elevation (m.a.s.l.)": f"{elev:.0f} m",
        "Temperature Mean": f"{df[t_col].mean():.1f}°C",
        "Temperature Max.": f"{df[t_col].max():.1f}°C",
        "Temperature Min.": f"{df[t_col].min():.1f}°C",
        "Wind Mean": f"{df[wspd_col].mean():.1f} m/s",
        "Wind Max.": f"{df[wspd_col].max():.1f} m/s",
        "Wind Direction": wind_dir_txt,
    })

table = pd.DataFrame(rows)

print(table.to_string(index=False))

table.to_csv("table_climatological_conditions_2020_2025.csv", index=False)
# table.to_latex(
#     "table_climatological_conditions_2020_2025.tex",
#     index=False,
#     escape=False,
# )
