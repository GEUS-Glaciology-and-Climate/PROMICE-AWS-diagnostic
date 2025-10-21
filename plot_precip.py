
    if False:
        try:
            var_list = ['lat','lon','alt']
            fig, ax_list = plt.subplots(len(var_list),1,sharex=True, figsize=(13,13))
            if len(var_list)==1:
                ax_list = [ax_list]

            for var, ax in zip(var_list, ax_list):
                if 'gps_'+var in l3.data_vars:
                    l3['gps_'+var].plot(ax=ax,
                                  marker='.',markeredgecolor='None', linestyle='None',
                            color='tab:green', label='gps_'+var)
                l3[var].plot(ax=ax, marker='.',markeredgecolor='None', linestyle='None',
                                color='tab:orange',label=var)
                ax.set_ylabel(var.replace('gps_',''))
                ax.grid()
                ax.legend()
        except:
            pass

        try:
            plt.figure()
            for v in ['z_surf_1','z_surf_2','z_surf_combined']:
                l3[v].plot(label=v)
            plt.title(station)
            plt.legend()
        except:
            pass
        try:
            l3.to_dataframe()[[v for v in l3.keys() if 'd_t_' in v]].plot()
            plt.gca().invert_yaxis()
            l3.to_dataframe()[[v for v in l3.keys() if 'd_t_' in v]].plot()
            plt.gca().invert_yaxis()
        except:
            pass
        try:
            plt.figure()
            for v in [ 'usr', 'dsr',]:
                l3[v].plot(label=v, marker='x')
            for v in ['usr_cor', 'dsr_cor',]:
                l3[v].plot(label=v, marker='o')
            plt.title(station)
            plt.legend()
        except:
            pass
            
def fresh_load(path):
    ds = xr.open_dataset(path, lock=False, cache=False)
    ds.load()
    ds.close()
    return ds

ds_h = fresh_load(f'L3_test/sites/{site}/{site}_hour.nc')
ds_d = fresh_load(f'L3_test/sites/{site}/{site}_day.nc')
ds_m = fresh_load(f'L3_test/sites/{site}/{site}_month.nc')

var = 'albedo'

plt.figure()
ds_h[var].plot(ax=plt.gca(), marker='o', label='hour')
ds_d[var].plot(ax=plt.gca(), marker='o', label='day')
ds_m[var].plot(ax=plt.gca(), marker='o', label='month')

    # %%
if False:
    # %% Test precipitation

    # %%
    plt.figure()
    (ds_h.rainfall_cor_u*24).plot(ax=plt.gca(), marker='o')
    ds_d.rainfall_cor_u.plot(ax=plt.gca(), marker='o')
    (ds_m.rainfall_cor_u/30).plot(ax=plt.gca(), marker='o')

    plt.figure()
    l2_merged.precip_u.plot(ax=plt.gca(), marker='o')
    ds_h.rainfall_cor_u.cumsum().plot(ax=plt.gca(), marker='o')
    ds_d.rainfall_cor_u.cumsum().plot(ax=plt.gca(), marker='o')
    ds_m.rainfall_cor_u.cumsum().plot(ax=plt.gca(), marker='o')



    # %%

    import matplotlib.pyplot as plt
    import math


    vars_list = ['t_u'] #[v for v in ds_h.data_vars if ds_h[v].notnull().any()]
    nvars = len(vars_list)
    ncols = 1
    nrows = math.ceil(nvars / 6)  # groups of 6 plots per figure

    for g in range(nrows):
        fig, axes = plt.subplots(1, 1, figsize=(10, 12), sharex=True)
        axes = np.atleast_1d(axes)

        for i in range(6):
            idx = g * 6 + i
            if idx >= nvars:
                axes[i].set_visible(False)
                continue
            var = vars_list[idx]
            # ds_l2_10min[var].plot(ax=axes[i], marker=".", ls="None", label="L2 10min w/o completeness")
            # ds_l2_h[var].plot(ax=axes[i], marker=".", ls="None", label="L2 hourly w/o completeness")
            # ds_d[var].plot(ax=axes[i], marker="o", ls="None", label="L3 daily w/o completeness")
            ds_d_f[var].plot(ax=axes[i], marker="o", ls="None", label="__nolegend__")
            ds_d_f[var].plot(ax=axes[i], marker="o", ls="None", label="__nolegend__")
            ds_d_f[var].plot(ax=axes[i], marker="o", ls="None", label="L3 daily filtered")
            axes[i].set_title(var)
            axes[i].legend()

        plt.tight_layout()
        plt.show()
        break



# %%
# var_list = [ 'p_u', 't_u', 'rh_u', 'wspd_u',  'wdir_u', 'dsr', 'usr', 'dlr', 'ulr',  'z_boom_u',
#             #'t_i_1', 't_i_2', 't_i_3', 't_i_4', 't_i_5', 't_i_6', 't_i_7', 't_i_8',
#             'tilt_y', 'tilt_x', 'rot',  'precip_u', 'gps_lat', 'gps_lon', 'gps_alt',  'p_i', 't_i', 'rh_i', 'wspd_i', 'wdir_i']

# import matplotlib.pyplot as plt
# import math

# n_vars = len(var_list)
# ncols = 2
# nrows = math.ceil(n_vars / ncols)

# fig, axs = plt.subplots(nrows, ncols, figsize=(14, 4 * nrows), sharex=True)
# axs = axs.flatten()

# for i, var in enumerate(var_list):
#     for tmp in sorted_list_station_data[::-1]:
#         tmp[0][var].plot(ax=axs[i], marker='.', label=tmp[1]['stid'])
#     axs[i].set_title(var)
#     axs[i].set_ylabel('')
#     if i < len(var_list) - 2:
#         axs[i].set_xticklabels([])
#         axs[i].set_xlabel('')

# # Hide any unused subplots
# for j in range(i + 1, len(axs)):
#     axs[j].set_visible(False)

# axs[0].legend(loc='upper right')
# axs[0].set_xlim(pd.to_datetime(['2022-01-01', '2025-04-03']))
# plt.tight_layout()
