# -*- coding: utf-8 -*-
"""
Created on %(date)s
@author: bav@geus.dk

tip list:
    %matplotlib inline
    %matplotlib qt
    import pdb; pdb.set_trace()
"""

plt.figure()
for ds in pAWS_raw.L1[-4:]:
    ds.tilt_x.plot(marker='o', label=str(ds.time.dt.year.isel(time=-1).item())+' '+ds.attrs['format']) 
    
pAWS_raw.L1A.tilt_x.plot(marker='x', label ='L1A_raw')


pAWS_tx.L1A.t_u.plot(marker='o', label ='L1_tx')
plt.legend()

#%%
plt.figure()
for ds in pAWS_raw.L1[-4:]:
    ds.dsr.plot(marker='o', label=str(ds.time.dt.year.isel(time=-1).item())+' '+ds.attrs['format']) 
    
pAWS_raw.L1A.dsr.plot(marker='x', label ='L1A_raw')


pAWS_tx.L1A.dsr.plot(marker='o', label ='L1_tx')
plt.legend()