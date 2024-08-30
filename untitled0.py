# -*- coding: utf-8 -*-
"""
Created on %(date)s
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""

def process_tilt(tilt, threshold=-100):
    notOKtilt = (tilt < threshold)
    OKtilt = (tilt >= threshold)
    tilt = tilt / 10

    dst = tilt
    nz = (dst != 0) & (np.abs(dst) < 40)
    
    dst = dst.where(~nz, other=dst / np.abs(dst)
                    * (-0.49
                       * (np.abs(dst))**4 + 3.6
                       * (np.abs(dst))**3 - 10.4
                       * (np.abs(dst))**2 + 21.1
                       * (np.abs(dst))))
    
    dst = dst.where(~notOKtilt)
    return dst

fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True, sharey=True)

for i, (ax, L0_ds, L1_ds, L2_ds) in enumerate(zip(axes, pAWS_raw.L0[-2:], pAWS_raw.L1[-2:], [pAWS_tx.L2,pAWS_raw.L2])):
    dst = process_tilt(L0_ds.tilt_x)
    
    dst.plot(ax=ax, marker='^',
             label='L0', ls='None') 
    dst.interpolate_na(dim='time', use_coordinate=False).plot(ax=ax, marker='o',
             label='L0 + interpolation',
             alpha=0.5) 
    L1_ds.tilt_x.plot(ax=ax, marker='o',
             label='L0 + interpolation + smoothing = L1',
             alpha=0.5)
    # L2_ds.tilt_x.plot(ax=ax, marker='o',
    #          label='L1 + more smoothing = L2',
    #          alpha=0.5)   
        
    
axes[0].legend()
axes[1].legend()
axes[0].grid()
axes[1].grid()
axes[0].set_title('in TX file: tilt available every 6h')
axes[1].set_title('in STM file: tilt available every h')


#%%
plt.figure()
(ds_1.dsr - ds_2.dsr).plot()
# %% 
plt.figure()
for ds in pAWS_raw.L1[-4:]:
    ds.dsr.plot(marker='o', label=str(ds.time.dt.year.isel(time=-1).item())+' '+ds.attrs['format']) 
    
pAWS_raw.L1A.dsr.plot(marker='x', label ='L1A_raw')


pAWS_tx.L1A.dsr.plot(marker='o', label ='L1_tx')
plt.legend()