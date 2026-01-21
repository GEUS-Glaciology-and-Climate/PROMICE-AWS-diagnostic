# -*- coding: utf-8 -*-
"""
Created on %(date)s
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""


        # daily average and gap-filling (could be refined)
        df_d = df.resample('D').mean().ffill().bfill()
        df_d[v] = df_d[v] - df_d.loc[df_d[v].first_valid_index(), v]
        df_d.loc[df_d[v]<0, v]=0

        # where the magic happens
        SWE_converter = SnowToSwe()
        SWE = SWE_converter.convert_list(df_d.z_surf_1.values,
                                   timestep=24,  # in hours
                                   verbose=False,
                                   )

        df_d['SWE'] = SWE
        # caluclating bulk density for time steps with df_d.z_surf_1>0.1
        df_d['bulk_snow_density_kgm3'] = np.nan
        df_d.loc[df_d.z_surf_1>0.1, 'bulk_snow_density_kgm3'] = (
            df_d.SWE.loc[df_d.z_surf_1>0.1] / df_d.z_surf_1.loc[df_d.z_surf_1>0.1]
            )
        try:
            fig, ax = plt.subplots(3,1,figsize=(10,7), sharex=True)
            df_v6.z_surf_1.plot(ax=ax[0],c='lightgray',label='hourly')
            df_d.z_surf_1.plot(ax=ax[0], label = 'daily')
            ax[0].set_xlim(df_d.index[[0,-1]])

            ax[0].legend()
            ax[0].set_ylabel('Surface height (m)')

            (df_d.SWE).plot(ax=ax[1],label = 'simulated')
            ax[1].set_ylabel('SWE (mm w.e.)')
            ax[1].legend()

            df_d['bulk_snow_density_kgm3'].plot(ax=ax[2], label='bulk density')
            ax[2].set_ylabel('simulated bulk density (kg m$^{-3}$)')
            plt.suptitle(site+' '+str(yr))
            fig.savefig('figures/SWE_calculation/%s_%i.png'%(site, yr))
        except Exception as e:
            Msg(str(e))


        # interpolating the results back to hourly values and adding it to the main
        # dataframe
        tmp = df_d.resample('H').interpolate()
        df_v6.loc[tmp.index,
                  ['SWE_mmweq','bulk_snow_density_kgm3']] = tmp[
                      ['SWE','bulk_snow_density_kgm3']
                       ].values
