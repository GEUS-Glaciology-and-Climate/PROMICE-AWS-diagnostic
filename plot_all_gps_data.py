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
import os
import tocgen
import geopandas as gpd
from shapely.ops import unary_union

# can be run both for stations or for sites, sites are recommended
data_type = 'sites'
if data_type == 'sites':
    path_new = '../thredds-data/level_3_sites/csv/day/'
    df_meta = pd.read_csv('../thredds-data/metadata/AWS_sites_metadata.csv')
    os.makedirs("figures/GPS/sites", exist_ok=True)
else:
    path_new = '../thredds-data/level_2_stations/csv/day/'
    df_meta = pd.read_csv('../thredds-data/metadata/AWS_stations_metadata.csv')
    os.makedirs("figures/GPS/stations", exist_ok=True)

os.makedirs("plot_compilations", exist_ok=True)

filename = 'plot_compilations/GPS_'+data_type+'.md'

f = open(filename, "w")
def Msg(txt):
    f = open(filename, "a")
    print(txt)
    f.write(txt + "\n")
# plt.close('all')

gnss_df = pd.read_csv('ancil/GEUS_GC-Net_precise_locations.csv').set_index(data_type[:-1])
gnss_df['date'] = pd.to_datetime(gnss_df.date,dayfirst=True)

gps_obs = pd.read_csv('ancil/GC-Net_observed_coordinates.csv').set_index('name')
gps_obs['date'] = pd.to_datetime(gps_obs.date,errors='coerce')
for v in ['lat','lon','elev']:
    gps_obs[v] = pd.to_numeric(gps_obs[v], errors='coerce')


# for file in os.listdir(path_new): # for all sites, even though where there's no GNSS survey
for file in ['SDM_day.csv']: # for a specific site
    date = '2025-05-19'
    site = file.replace('_day.csv','')

    # if you want only the sites where there's accurate GNSS survey
    # if site not in np.unique(gnss_df.index):
    #     continue

    Msg('## '+site)
    if not os.path.isfile(path_new+file):
        Msg("cannot find",path_new+file)
        continue

    df_new = pd.read_csv(path_new+file)
    df_new.time = pd.to_datetime(df_new.time, utc=True)
    df_new = df_new.set_index('time')

    last_station_at_site = df_meta.loc[df_meta.site_id == site, 'stations'].iloc[0].split(' ')[0]

    geoid_separation_station = np.nan
    if not os.path.isfile('../thredds-data/level_2_stations/csv/hour/'+site+'_hour.csv'):
        print('Cannot find level 2 station file, please download in ../thredds-data/level_2_stations/csv/hour/')
    else:
        df_l2 = pd.read_csv('../thredds-data/level_2_stations/csv/hour/'+site+'_hour.csv')
        df_l2.time = pd.to_datetime(df_l2.time, utc=True)
        df_l2 = df_l2.set_index('time')
        geoid_separation_station = df_l2.gps_geoid.dropna().unique()
        if len(geoid_separation_station)>1:
            print('Multiple geoid separation: ', geoid_separation_station)
        if len(geoid_separation_station)>0:
            geoid_separation_station=geoid_separation_station[0]

    print(site, date, df_new.loc[date,['lat','lon','alt']].values)
    #%%
    var_list_list = [['gps_lat','gps_lon','gps_alt']]
    for k, var_list in enumerate(var_list_list):
        fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(12,8))
        plt.subplots_adjust(right=0.75,left=0.08)
        if len(var_list)==1:
            ax_list = [ax_list]

        for var, ax in zip(var_list, ax_list):
            if var in df_new.columns:
                if not df_new[var].isnull().all():
                    ax.plot(df_new.index, df_new[var].values,
                            marker='.',markeredgecolor='None', linestyle='None',
                            color='tab:orange',label=var)
            if var.replace('gps_','') in df_new.columns:
                ax.plot(df_new.index, df_new[var.replace('gps_','')].values,
                        color='tab:green', label=var.replace('gps_',''))
            if site in gnss_df.index:
                if var == 'gps_alt':
                    ax.plot(gnss_df.loc[site,'date'],
                            gnss_df.loc[site,var.replace('gps_','').replace('alt','orthometric_height_m')],
                            marker='o',ls='None', label='GNSS survey: orthometric height (geoid gr2000g.06)')

                    ax.plot(gnss_df.loc[site,'date'],
                            gnss_df.loc[site,var.replace('gps_','').replace('alt','ellipsoid_height_m')],
                            marker='^',ls='None', color='tab:green', label='GNSS survey: ellipsoid height')

                    ax.plot(gnss_df.loc[site,'date'],
                            gnss_df.loc[site,var.replace('gps_','').replace('alt','ellipsoid_height_m')] \
                                -geoid_separation_station,
                            marker='d',ls='None', color='tab:purple',
                            label='GNSS survey: orthometric height (geoid EGM96?)')
                else:
                    ax.plot(gnss_df.loc[site,'date'],
                            gnss_df.loc[site,var.replace('gps_','')],
                            marker='o',ls='None', label='GNSS survey')

            if data_type=='sites' and site in gps_obs.index:
                ax.plot(gps_obs.loc[site,'date'],
                        gps_obs.loc[site,var.replace('gps_','').replace('alt','elev')],
                        marker='d',color='tab:red',ls='None', label='handheld survey')

            ax.set_ylabel(var.replace('gps_',''))
            ax.grid()
            ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        no_save = 1
        for ax in ax_list:
            if ax.lines: no_save=0
            if ax.collections: no_save=0
        if no_save == 1:
            continue
        plt.suptitle(site)
        fig.savefig('figures/GPS/%s/%s_%i.png'%(data_type, site,k), dpi=300)
        Msg('![%s](../figures/GPS/%s/%s_%i.png)'%(site,data_type, site,k))

        # determination of the range of displacement
        gdf = gpd.GeoDataFrame(df_new,
                                geometry=gpd.points_from_xy(df_new['lon'],
                                                            df_new['lat']),
                                crs="EPSG:4326")
        gdf_3413 = gdf.to_crs(epsg=3413)
        radius_km = (unary_union(gdf_3413.geometry).convex_hull.centroid
                     .hausdorff_distance(unary_union(gdf_3413.geometry))) / 1000

        print(
            f"{site} moved by: {round(radius_km*2, 1)} km from "
            f"{df_new.index[0].strftime('%Y-%m-%d')} to "
            f"{df_new.index[-1].strftime('%Y-%m-%d')}"
        )

    Msg(' ')
tocgen.processFile(filename, filename[:-3]+"_toc.md")
f.close()
