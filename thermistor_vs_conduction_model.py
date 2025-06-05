# -*- coding: utf-8 -*-
"""
Created on %(date)s
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
data_type = 'sites'
if data_type == 'sites':
    path_new = '../thredds-data/level_3_sites/csv/hour/'
else:
    path_new = 'C:/Users/bav/Downloads/level_2_stations/hour/'

df_meta = pd.read_csv('../thredds-data/metadata/AWS_' + data_type + '_metadata.csv')
df_meta = df_meta.set_index(data_type[:-1] + '_id')



results = []

for station in ['DY2']:
    file_path = os.path.join(path_new, f"{station}_hour.csv")
    if not os.path.isfile(file_path):
        continue

    df = pd.read_csv(file_path)
    if not {'z_surf_combined', 'snow_height'}.issubset(df.columns):
        continue

    df['time'] = pd.to_datetime(df['time'], utc=True)
    df = df.set_index('time')

    # %%



    # Input
    surface_temp = df.t_surf.loc[slice('2025-05-13',None)].interpolate()

    dt = 3600  # 1 hour
    nt = len(surface_temp)

    # Snow properties
    rho = 400
    c = 2100
    k = 0.2
    alpha = k / (rho * c)

    # Depth grid
    depths_out = np.array([0,0.5,1,1.5,2,3,4,5,6,8,10])
    dz = 0.1
    z_grid = np.arange(0, 10.1, dz)
    nz = len(z_grid)

    # Initialize
    T = np.zeros((nt, nz))
    init_profile = df[[f't_i_{i}' for i in range(1,12)]].loc['2025-05-13T00'].values
    T[0, :] = np.interp(z_grid, [0,0.5,1,1.5,2,3,4,5,6,8,10], init_profile)
    # Time stepping
    for t in range(1, nt):
        T[t, 0] = surface_temp.iloc[t]
        for z in range(1, nz - 1):
            T[t, z] = np.clip(
                                T[t-1, z] + alpha * dt / dz**2 * (T[t-1, z+1] - 2*T[t-1, z] + T[t-1, z-1]),
                                -60, 5
                            )
        T[t, -1] = T[t-1, -1]

    # Interpolate to requested depths
    T_out = pd.DataFrame(index=surface_temp.index)
    for d in depths_out:
        T_out[f'{d}m'] = [np.interp(d, z_grid, T[i, :]) for i in range(nt)]

    import matplotlib.pyplot as plt
    plt.figure()
    surface_temp.plot()
    ax = T_out.plot(style='-')
    for i, d in enumerate(T_out.columns):
        df[f't_i_{i+1}'].loc[slice('2025-05-13',None)].plot(ax=ax, style='--',
                              color=ax.lines[i].get_color(),
                              label=f't_i_{i+1}')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.title('Simulated Snow Temperature Profile')
    plt.grid(True)
    plt.show()

# %%
import matplotlib.pyplot as plt

fig, axs = plt.subplots(4, 3, figsize=(12, 10), sharex=True, sharey=True)
axs = axs.flatten()

for i, d in enumerate(T_out.columns):
    ax = axs[i]
    T_out[d].plot(ax=ax, label='Model', color='tab:blue')
    df[f't_i_{i+1}'].loc[slice('2025-05-13', None)].plot(ax=ax, label='Observed', color='tab:blue', linestyle='--')
    ax.set_title(f'Depth: {d}')
    ax.grid(True)
    if i % 3 == 0:
        ax.set_ylabel('Temperature (°C)')
    if i >= 9:
        ax.set_xlabel('Time')
    ax.legend()

for j in range(i+1, len(axs)):
    fig.delaxes(axs[j])

fig.tight_layout()
plt.show()
