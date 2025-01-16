
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
import matplotlib
matplotlib.use('Agg')

# Define variables
data_type = 'stations'
path_new = '../aws-l3-dev/' + data_type + '/'
filename = 'plot_compilations/RH_' + data_type + '.md'
df_meta = pd.read_csv(path_new + '../AWS_' + data_type + '_metadata.csv')
df_meta = df_meta.set_index(data_type[:-1] + '_id')

# Dictionary to store the results
results = {}

for station in df_meta.index:
    if not os.path.isfile(path_new + station + '/' + station + '_hour.csv'):
        continue

    df_new = pd.read_csv(path_new + station + '/' + station + '_hour.csv')
    df_new['time'] = pd.to_datetime(df_new['time'], utc=True)
    df_new = df_new.set_index('time')

    df_save = df_new.copy()
    for year in np.unique(df_new.index.year):
        df_new = df_save.copy()
        df_new['year'] = df_new.index.year
        df_new = df_new.loc[df_new['year'] == year, :]

        # Define bins
        bins = np.arange(-70, 12, 2)
        percentiles = []

        for i in range(len(bins) - 1):
            bin_data = df_new.loc[(df_new['t_u'] >= bins[i]) & (df_new['t_u'] < bins[i + 1])]
            if not bin_data.empty:
                percentiles.append(np.percentile(bin_data['rh_u_wrt_ice_or_water'], 95))
            else:
                percentiles.append(np.nan)

        # Extract first 5 non-NaN values and compute the mean
        first_5_non_nan = [p for p in percentiles if not np.isnan(p)][:5]
        avg_lowest_percentile = np.nan if len(first_5_non_nan) == 0 else np.mean(first_5_non_nan)

        # Store result
        if station not in results:
            results[station] = {}
        results[station][year] = avg_lowest_percentile
from matplotlib.colors import BoundaryNorm, ListedColormap


# Convert results to DataFrame, handling duplicate years
results_df = pd.DataFrame.from_dict(results, orient='index')
results_df = results_df.loc[:, ~results_df.columns.duplicated()].sort_index(axis=1)

# Define colormap and boundaries
bounds = np.arange(75, 126, 10)
norm = BoundaryNorm(bounds, ncolors=len(bounds)-1)
colors = plt.get_cmap('seismic', len(bounds)-1)
colors.set_bad(color='gray')

# Plot the tile plot
fig, ax = plt.subplots(figsize=(10, 6))
cax = ax.imshow(results_df, cmap=colors, norm=norm, aspect='auto')

# Set labels
ax.set_xticks(np.arange(len(results_df.columns)))
ax.set_xticklabels(results_df.columns, rotation=45)
ax.set_yticks(np.arange(len(results_df.index)))
ax.set_yticklabels(results_df.index)
ax.set_xlabel('Year')
ax.set_ylabel('Station')
ax.set_title('Average Lowest 5 Percentiles of RH (%)')

# Add discrete colorbar
cbar = fig.colorbar(cax, ax=ax, boundaries=bounds, ticks=bounds, label='RH (%)')

# Save plot
plt.savefig('tile_plot_rh.png', dpi=300, bbox_inches='tight')


# %%
from scipy.interpolate import interp1d
# plt.figure()
# for station in ['QAS_U', 'QAS_Uv3']:
for station in df_meta.index:
    if not os.path.isfile(path_new + station + '/' + station + '_hour.csv'):
        continue

    df_new = pd.read_csv(path_new + station + '/' + station + '_hour.csv')
    df_new['time'] = pd.to_datetime(df_new['time'], utc=True)
    df_new = df_new.set_index('time')

    df_save = df_new.copy()
    # for year in [2022]:
    for year in np.unique(df_new.index.year):
        # # %%
        # year = 2022


        # if 'rh_u' not in df_new.columns or 't_u' not in df_new.columns or 'rh_u_wrt_ice_or_water' not in df_new.columns:
            # continue

        # Extract year for coloring
        df_new = df_save.copy()
        df_new['year'] = df_new.index.year
        df_new = df_new.loc[df_new['year'] == year, :]

        # Calculate 95th percentile for 2-degree bins and plot
        bins = np.arange(-70, 12, 2)
        bin_centers = bins[:-1] + 1
        percentiles = []

        for i in range(len(bins) - 1):
            bin_data = df_new.loc[(df_new['t_u'] >= bins[i]) & (df_new['t_u'] < bins[i + 1])]
            if not bin_data.empty:
                percentiles.append(np.percentile(bin_data['rh_u_wrt_ice_or_water'], 95))
            else:
                percentiles.append(np.nan)

        percentiles_cor = np.array(percentiles).copy()

        # Interpolate NaNs (do not extrapolate edges)
        valid_idx = ~np.isnan(percentiles_cor)
        if valid_idx.sum() > 1:
            interp_func = interp1d(bin_centers[valid_idx], percentiles_cor[valid_idx], kind='linear', bounds_error=False)
            percentiles_cor[~valid_idx] = interp_func(bin_centers[~valid_idx])


        # Find index of -20 and -10 in bin_centers
        idx_neg20 = (bin_centers >= -20).argmax()
        idx_neg10 = (bin_centers >= -10).argmax()

        # Update percentiles_cor values
        percentiles_cor[idx_neg20:idx_neg10] = np.linspace(
            percentiles_cor[idx_neg20], 100, idx_neg10 - idx_neg20
        )
        percentiles_cor[idx_neg10:] = 100

        percentiles = percentiles_cor.tolist()

        df_new['rh_wrt_ice_or_water_cor'] = np.nan

        # Assign corrected values based on temperature bins
        for i in range(len(bins) - 1):
            bin_data_indices = (df_new['t_u'] >= bins[i]) & (df_new['t_u'] < bins[i + 1])
            if not bin_data_indices.empty:
                df_new.loc[bin_data_indices, 'rh_wrt_ice_or_water_cor'] = (
                    df_new.loc[bin_data_indices, 'rh_u_wrt_ice_or_water'] * 100 / percentiles[i]
                )

        # df_new['rh_u_wrt_ice_or_water'].plot(label=station+' uncorrected')
        # df_new['rh_wrt_ice_or_water_cor'].plot(label=station+' corrected')
        # plt.legend()
        # plt.grid()

        fig, ax_list = plt.subplots(3, 1, sharex=True, figsize=(12, 12))
        plt.subplots_adjust(right=0.75, left=0.08)

        # Top panel: rh_u vs t_u
        scatter1 = ax_list[0].scatter(
            df_new['t_u'], df_new['rh_u'], c=df_new['year'], cmap='viridis', s=10, alpha=0.7
        )
        ax_list[0].set_ylabel('rh_u')
        ax_list[0].set_title(f'{station}')
        ax_list[0].grid()
        cbar1 = fig.colorbar(scatter1, ax=ax_list[0], orientation='vertical')
        cbar1.set_label('Year')

        # Middle panel: rh_u_wrt_ice_or_water vs t_u
        scatter2 = ax_list[1].scatter(
            df_new['t_u'], df_new['rh_u_wrt_ice_or_water'], c=df_new['year'], cmap='viridis', s=10, alpha=0.7
        )
        ax_list[1].set_ylabel('rh_u_wrt_ice_or_water')
        ax_list[1].grid()
        cbar2 = fig.colorbar(scatter2, ax=ax_list[1], orientation='vertical')
        cbar2.set_label('Year')
        ax_list[1].plot(bin_centers, percentiles, 'r-', label='95th percentile')
        ax_list[1].set_ylim(40, 110)
        ax_list[0].set_ylim(40, 110)
        ax_list[0].set_xlim(-50, 10)
        ax_list[1].set_xlim(-50, 10)

        # Third panel: rh_wrt_ice_or_water_cor vs t_u
        scatter3 = ax_list[2].scatter(
            df_new['t_u'], df_new['rh_wrt_ice_or_water_cor'], c=df_new['year'], cmap='viridis', s=10, alpha=0.7
        )
        ax_list[2].set_xlabel('t_u (°C)')
        ax_list[2].set_ylabel('rh_wrt_ice_or_water_cor')
        ax_list[2].grid()
        cbar3 = fig.colorbar(scatter3, ax=ax_list[2], orientation='vertical')
        cbar3.set_label('Year')

        # Set consistent limits
        for ax in ax_list:
            ax.set_xlim(-50, 10)
            ax.set_ylim(40, 110)

        plt.suptitle(year)
        fig.savefig(f'figures/RH/{data_type}/{station}_scatter_'+str(year)+'.png', dpi=300)

        from pypromice.process.L2toL3 import calculate_tubulent_heat_fluxes, calculate_specific_humidity

        # Upper boom bulk calculation
        ds = df_new.to_xarray()
        T_h_u = ds['t_u'].copy()                                                   # Copy for processing
        p_h_u = ds['p_u'].copy()
        rh_h_u_wrt_ice_or_water = ds['rh_u_wrt_ice_or_water'].copy()
        T_0=273.15
        T_100=373.15

        q_h_u = calculate_specific_humidity(T_0, T_100, T_h_u, p_h_u, rh_h_u_wrt_ice_or_water)                  # Calculate specific humidity

        WS_h_u = ds['wspd_u'].copy()
        Tsurf_h = ds['t_surf'].copy()                                              # T surf from derived upper boom product. TODO is this okay to use with lower boom parameters?
        z_WS_u = ds['z_boom_u'].copy() + 0.4                                       # Get height of Anemometer
        z_T_u = ds['z_boom_u'].copy() - 0.1                                        # Get height of thermometer

        SHF_h_u, LHF_h_u= calculate_tubulent_heat_fluxes(T_0, T_h_u,
                                                         Tsurf_h, WS_h_u,            # Calculate latent and sensible heat fluxes
                                        z_WS_u, z_T_u, q_h_u, p_h_u)

        ds['dshf_u'] = (('time'), SHF_h_u.data)
        ds['dlhf_u'] = (('time'), LHF_h_u.data)

        q_h_u = 1000 * q_h_u                                                       # Convert sp.humid from kg/kg to g/kg
        ds['qh_u'] = (('time'), q_h_u.data)

        rh_h_u_wrt_ice_or_water = ds['rh_wrt_ice_or_water_cor'].copy()
        T_0=273.15
        T_100=373.15

        q_h_u = calculate_specific_humidity(T_0, T_100, T_h_u, p_h_u, rh_h_u_wrt_ice_or_water)                  # Calculate specific humidity

        WS_h_u = ds['wspd_u'].copy()
        Tsurf_h = ds['t_surf'].copy()                                              # T surf from derived upper boom product. TODO is this okay to use with lower boom parameters?
        z_WS_u = ds['z_boom_u'].copy() + 0.4                                       # Get height of Anemometer
        z_T_u = ds['z_boom_u'].copy() - 0.1                                        # Get height of thermometer

        SHF_h_u, LHF_h_u= calculate_tubulent_heat_fluxes(T_0, T_h_u,
                                                         Tsurf_h, WS_h_u,            # Calculate latent and sensible heat fluxes
                                        z_WS_u, z_T_u, q_h_u, p_h_u)

        ds['dshf_u_cor'] = (('time'), SHF_h_u.data)
        ds['dlhf_u_cor'] = (('time'), LHF_h_u.data)

        q_h_u = 1000 * q_h_u                                                       # Convert sp.humid from kg/kg to g/kg
        ds['qh_u_cor'] = (('time'), q_h_u.data)

        # Extract dataframes from the dataset
        time =ds.time.to_dataframe().index
        #
        # Create the three-panel plot
        fig, ax_list = plt.subplots(3, 1, figsize=(12, 12), sharex=True)
        plt.subplots_adjust(hspace=0.3)

        # Panel 2: dlhf_u and dlhf_u_cor
        ax2 = ax_list[1]
        ax2.plot(time, ds['dlhf_u'], label='uncorrected',alpha=0.7, color='tab:red')
        ax2.plot(time, ds['dlhf_u_cor'], label='corrected',alpha=0.7, color='tab:green')
        ax2.set_ylabel('Surface latent heat flux (dlhf)\n (W m$^{-2})$)')
        ax2.grid()
        ax2.legend()
        ax_mass = ax2.twinx()
        ax_mass.plot(time, ds['dlhf_u']/ 2.83e6*3600,color='tab:red',alpha=0.7, )
        ax_mass.plot(time, ds['dlhf_u_cor']/ 2.83e6*3600,color='tab:green',alpha=0.7)
        ax_mass.set_ylabel('Mass flux (kg/m²/h)')
        ax_mass.tick_params(axis='y')

        # Twin axis for cumulative sum
        ax2_twin = ax_list[2]
        ax2_twin.plot(time,  (ds['dlhf_u']*3600).cumsum(),label='uncorrected',color='tab:red')
        ax2_twin.plot(time,  (ds['dlhf_u_cor']*3600).cumsum(),label='corrected',color='tab:green')
        ax2_twin.set_ylabel('Cumulated latent energy\n(J m$^{-2}$)')
        ax2_twin.grid()
        ax2_twin.legend()
        ax_mass_cum = ax2_twin.twinx()
        ax_mass_cum.plot(time,  (ds['dlhf_u']*3600).cumsum()/ 2.83e6,color='tab:red',alpha=0.7, )
        ax_mass_cum.plot(time,  (ds['dlhf_u_cor']*3600).cumsum()/ 2.83e6,color='tab:green',alpha=0.7)
        ax_mass_cum.set_ylabel('Cumulated mass flux (kg/m²)')
        ax_mass_cum.tick_params(axis='y')
        print('Difference in cumulated flux:',
              ((ds['dlhf_u_cor']*3600).isel(time=-1) - (ds['dlhf_u']*3600).isel(time=-1)).item())
        print('Corresponding mass:',
              ((ds['dlhf_u_cor']*3600).cumsum().isel(time=-1)/ 2.83e6 - (ds['dlhf_u']*3600).cumsum().isel(time=-1)/ 2.83e6).item())


        # Panel 3: qh_u
        ax3 = ax_list[0]
        ax3.plot(time, ds['qh_u'], label='uncorrected', alpha=0.7, color='tab:red')
        ax3.plot(time, ds['qh_u_cor'], label='corrected', alpha=0.7, color='tab:green')
        ax3.set_ylabel('Specific humidity (qh) (g kg$^{-1}$)')
        ax3.legend()
        ax3.grid()

        plt.suptitle(station + ' '+str(year))

        fig.savefig(f'figures/RH/{data_type}/{station}_ts_'+str(year)+'.png', dpi=300)

        # %%
        import nead

        if station == 'EGP':
            path_gcn= 'C:/Users/bav/OneDrive - GEUS/Code/PROMICE/GC-Net-Level-1-data-processing/L1/'
            filename = path_gcn+"/hourly/EastGRIP.csv"

            df = nead.read(filename).to_dataframe().reset_index(drop=True)
            df.timestamp = pd.to_datetime(df.timestamp)
            df = df.set_index("timestamp").replace(-999, np.nan)

            plt.figure()
            df.RH2_cor.plot(label='CIRES/WSL uncorrected')
            df.RH2.plot(label='CIRES/WSL uncorrected')
            ds.to_dataframe()['rh_u_wrt_ice_or_water'].plot(label='GEUS uncorrected')
            ds.to_dataframe()['rh_wrt_ice_or_water_cor'].plot(label='GEUS corrected')
            plt.legend()
