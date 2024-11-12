* [Comparison of data aws-l3-dev to V19 (old).](#s1)
  * [CEN2](#s1-1)
  * [CP1](#s1-2)
  * [DY2](#s1-3)
  * [EGP](#s1-4)
  * [FRE](#s1-5)
  * [HUM](#s1-6)
  * [JAR](#s1-7)
  * [JAR_O](#s1-8)
  * [KAN_B](#s1-9)
  * [KAN_L](#s1-10)
  * [KAN_Lv3](#s1-11)
  * [KAN_M](#s1-12)
  * [KAN_Tv3](#s1-13)
  * [KAN_U](#s1-14)
  * [KPC_L](#s1-15)
  * [KPC_Lv3](#s1-16)
  * [KPC_U](#s1-17)
  * [KPC_Uv3](#s1-18)
  * [LYN_L](#s1-19)
  * [MIT](#s1-20)
  * [NAE](#s1-21)
  * [NAU](#s1-22)
  * [NEM](#s1-23)
  * [NSE](#s1-24)
  * [NUK_B](#s1-25)
  * [NUK_K](#s1-26)
  * [NUK_L](#s1-27)
  * [NUK_N](#s1-28)
  * [NUK_U](#s1-29)
  * [NUK_Uv3](#s1-30)
  * [QAS_A](#s1-31)
  * [QAS_L](#s1-32)
  * [QAS_Lv3](#s1-33)
  * [QAS_Mv3](#s1-34)
  * [QAS_Uv3](#s1-35)
  * [RED_Lv3](#s1-36)
  * [Roof_GEUS](#s1-37)
  * [SCO_L](#s1-38)
  * [SCO_Lv3](#s1-39)
  * [SCO_U](#s1-40)
  * [SCO_Uv3](#s1-41)
  * [SDL](#s1-42)
  * [SDM](#s1-43)
  * [SER_B](#s1-44)
  * [SWC](#s1-45)
  * [SWC_O](#s1-46)
  * [TAS_A](#s1-47)
  * [TAS_Av3](#s1-48)
  * [TAS_L](#s1-49)
  * [TAS_U](#s1-50)
  * [THU_L](#s1-51)
  * [THU_L2](#s1-52)
  * [THU_U2v3](#s1-53)
  * [TUN](#s1-54)
  * [UPE_L](#s1-55)
  * [UPE_U](#s1-56)
  * [UWN](#s1-57)
  * [WEG_B](#s1-58)
  * [WEG_L](#s1-59)
  * [XXX](#s1-60)
  * [ZAC_A](#s1-61)
  * [ZAC_Lv3](#s1-62)
  * [ZAC_Uv3](#s1-63)
  * [ZAK_A](#s1-64)
  * [ZAK_Lv3](#s1-65)
  * [ZAK_Uv3](#s1-66)
# <a id='s1' />Comparison of data aws-l3-dev to V19 (old).
## <a id='s1-1' />CEN2
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, rh_l_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, rh_l_cor, gps_time, gps_hdop, fan_dc_u, fan_dc_l, rh_i_cor
 
![CEN2](../figures/V19_versus_aws-l3-dev/CEN2_0.png)
![CEN2](../figures/V19_versus_aws-l3-dev/CEN2_1.png)
![CEN2](../figures/V19_versus_aws-l3-dev/CEN2_2.png)
![CEN2](../figures/V19_versus_aws-l3-dev/CEN2_3.png)
![CEN2](../figures/V19_versus_aws-l3-dev/CEN2_4.png)
![CEN2](../figures/V19_versus_aws-l3-dev/CEN2_5.png)
![CEN2](../figures/V19_versus_aws-l3-dev/CEN2_6.png)
![CEN2](../figures/V19_versus_aws-l3-dev/CEN2_7.png)
![CEN2](../figures/V19_versus_aws-l3-dev/CEN2_8.png)
![CEN2](../figures/V19_versus_aws-l3-dev/CEN2_9.png)
![CEN2](../figures/V19_versus_aws-l3-dev/CEN2_10.png)
![CEN2](../figures/V19_versus_aws-l3-dev/CEN2_11.png)
![CEN2](../figures/V19_versus_aws-l3-dev/CEN2_12.png)
![CEN2](../figures/V19_versus_aws-l3-dev/CEN2_13.png)
![CEN2](../figures/V19_versus_aws-l3-dev/CEN2_14.png)
![CEN2](../figures/V19_versus_aws-l3-dev/CEN2_15.png)
![CEN2](../figures/V19_versus_aws-l3-dev/CEN2_16.png)
 
## <a id='s1-2' />CP1
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, rh_l_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, rh_l_cor, gps_time, gps_hdop, fan_dc_u, fan_dc_l, rh_i_cor
 
![CP1](../figures/V19_versus_aws-l3-dev/CP1_0.png)
![CP1](../figures/V19_versus_aws-l3-dev/CP1_1.png)
![CP1](../figures/V19_versus_aws-l3-dev/CP1_2.png)
![CP1](../figures/V19_versus_aws-l3-dev/CP1_3.png)
![CP1](../figures/V19_versus_aws-l3-dev/CP1_4.png)
![CP1](../figures/V19_versus_aws-l3-dev/CP1_5.png)
![CP1](../figures/V19_versus_aws-l3-dev/CP1_6.png)
![CP1](../figures/V19_versus_aws-l3-dev/CP1_7.png)
![CP1](../figures/V19_versus_aws-l3-dev/CP1_8.png)
![CP1](../figures/V19_versus_aws-l3-dev/CP1_9.png)
![CP1](../figures/V19_versus_aws-l3-dev/CP1_10.png)
![CP1](../figures/V19_versus_aws-l3-dev/CP1_11.png)
![CP1](../figures/V19_versus_aws-l3-dev/CP1_12.png)
![CP1](../figures/V19_versus_aws-l3-dev/CP1_13.png)
![CP1](../figures/V19_versus_aws-l3-dev/CP1_14.png)
![CP1](../figures/V19_versus_aws-l3-dev/CP1_15.png)
![CP1](../figures/V19_versus_aws-l3-dev/CP1_16.png)
 
## <a id='s1-3' />DY2
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, rh_l_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, rh_l_cor, gps_time, gps_hdop, fan_dc_u, fan_dc_l, rh_i_cor
 
![DY2](../figures/V19_versus_aws-l3-dev/DY2_0.png)
![DY2](../figures/V19_versus_aws-l3-dev/DY2_1.png)
![DY2](../figures/V19_versus_aws-l3-dev/DY2_2.png)
![DY2](../figures/V19_versus_aws-l3-dev/DY2_3.png)
![DY2](../figures/V19_versus_aws-l3-dev/DY2_4.png)
![DY2](../figures/V19_versus_aws-l3-dev/DY2_5.png)
![DY2](../figures/V19_versus_aws-l3-dev/DY2_6.png)
![DY2](../figures/V19_versus_aws-l3-dev/DY2_7.png)
![DY2](../figures/V19_versus_aws-l3-dev/DY2_8.png)
![DY2](../figures/V19_versus_aws-l3-dev/DY2_9.png)
![DY2](../figures/V19_versus_aws-l3-dev/DY2_10.png)
![DY2](../figures/V19_versus_aws-l3-dev/DY2_11.png)
![DY2](../figures/V19_versus_aws-l3-dev/DY2_12.png)
![DY2](../figures/V19_versus_aws-l3-dev/DY2_13.png)
![DY2](../figures/V19_versus_aws-l3-dev/DY2_14.png)
![DY2](../figures/V19_versus_aws-l3-dev/DY2_15.png)
![DY2](../figures/V19_versus_aws-l3-dev/DY2_16.png)
 
## <a id='s1-4' />EGP
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_l, z_stake, z_pt, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
p_l, t_l, rh_u_wrt_ice_or_water, rh_l, rh_l_wrt_ice_or_water, wspd_l, wdir_l, wspd_x_l, wspd_y_l, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_l, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, z_pt_cor, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![EGP](../figures/V19_versus_aws-l3-dev/EGP_0.png)
![EGP](../figures/V19_versus_aws-l3-dev/EGP_1.png)
![EGP](../figures/V19_versus_aws-l3-dev/EGP_2.png)
![EGP](../figures/V19_versus_aws-l3-dev/EGP_3.png)
![EGP](../figures/V19_versus_aws-l3-dev/EGP_4.png)
![EGP](../figures/V19_versus_aws-l3-dev/EGP_5.png)
![EGP](../figures/V19_versus_aws-l3-dev/EGP_6.png)
![EGP](../figures/V19_versus_aws-l3-dev/EGP_7.png)
![EGP](../figures/V19_versus_aws-l3-dev/EGP_8.png)
![EGP](../figures/V19_versus_aws-l3-dev/EGP_9.png)
![EGP](../figures/V19_versus_aws-l3-dev/EGP_10.png)
![EGP](../figures/V19_versus_aws-l3-dev/EGP_11.png)
![EGP](../figures/V19_versus_aws-l3-dev/EGP_12.png)
![EGP](../figures/V19_versus_aws-l3-dev/EGP_13.png)
![EGP](../figures/V19_versus_aws-l3-dev/EGP_14.png)
![EGP](../figures/V19_versus_aws-l3-dev/EGP_15.png)
![EGP](../figures/V19_versus_aws-l3-dev/EGP_16.png)
 
## <a id='s1-5' />FRE
cannot find old file for FRE
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

Old variables removed from new files:

 
![FRE](../figures/V19_versus_aws-l3-dev/FRE_0.png)
![FRE](../figures/V19_versus_aws-l3-dev/FRE_1.png)
![FRE](../figures/V19_versus_aws-l3-dev/FRE_2.png)
![FRE](../figures/V19_versus_aws-l3-dev/FRE_3.png)
![FRE](../figures/V19_versus_aws-l3-dev/FRE_4.png)
![FRE](../figures/V19_versus_aws-l3-dev/FRE_5.png)
![FRE](../figures/V19_versus_aws-l3-dev/FRE_6.png)
![FRE](../figures/V19_versus_aws-l3-dev/FRE_7.png)
![FRE](../figures/V19_versus_aws-l3-dev/FRE_8.png)
![FRE](../figures/V19_versus_aws-l3-dev/FRE_9.png)
![FRE](../figures/V19_versus_aws-l3-dev/FRE_10.png)
![FRE](../figures/V19_versus_aws-l3-dev/FRE_11.png)
![FRE](../figures/V19_versus_aws-l3-dev/FRE_12.png)
 
## <a id='s1-6' />HUM
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, rh_l_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, rh_l_cor, gps_time, gps_hdop, fan_dc_u, fan_dc_l, rh_i_cor
 
![HUM](../figures/V19_versus_aws-l3-dev/HUM_0.png)
![HUM](../figures/V19_versus_aws-l3-dev/HUM_1.png)
![HUM](../figures/V19_versus_aws-l3-dev/HUM_2.png)
![HUM](../figures/V19_versus_aws-l3-dev/HUM_3.png)
![HUM](../figures/V19_versus_aws-l3-dev/HUM_4.png)
![HUM](../figures/V19_versus_aws-l3-dev/HUM_5.png)
![HUM](../figures/V19_versus_aws-l3-dev/HUM_6.png)
![HUM](../figures/V19_versus_aws-l3-dev/HUM_7.png)
![HUM](../figures/V19_versus_aws-l3-dev/HUM_8.png)
![HUM](../figures/V19_versus_aws-l3-dev/HUM_9.png)
![HUM](../figures/V19_versus_aws-l3-dev/HUM_10.png)
![HUM](../figures/V19_versus_aws-l3-dev/HUM_11.png)
![HUM](../figures/V19_versus_aws-l3-dev/HUM_12.png)
![HUM](../figures/V19_versus_aws-l3-dev/HUM_13.png)
![HUM](../figures/V19_versus_aws-l3-dev/HUM_14.png)
![HUM](../figures/V19_versus_aws-l3-dev/HUM_15.png)
![HUM](../figures/V19_versus_aws-l3-dev/HUM_16.png)
 
## <a id='s1-7' />JAR
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![JAR](../figures/V19_versus_aws-l3-dev/JAR_0.png)
![JAR](../figures/V19_versus_aws-l3-dev/JAR_1.png)
![JAR](../figures/V19_versus_aws-l3-dev/JAR_2.png)
![JAR](../figures/V19_versus_aws-l3-dev/JAR_3.png)
![JAR](../figures/V19_versus_aws-l3-dev/JAR_4.png)
![JAR](../figures/V19_versus_aws-l3-dev/JAR_5.png)
![JAR](../figures/V19_versus_aws-l3-dev/JAR_6.png)
![JAR](../figures/V19_versus_aws-l3-dev/JAR_7.png)
![JAR](../figures/V19_versus_aws-l3-dev/JAR_8.png)
![JAR](../figures/V19_versus_aws-l3-dev/JAR_9.png)
![JAR](../figures/V19_versus_aws-l3-dev/JAR_10.png)
![JAR](../figures/V19_versus_aws-l3-dev/JAR_11.png)
![JAR](../figures/V19_versus_aws-l3-dev/JAR_12.png)
![JAR](../figures/V19_versus_aws-l3-dev/JAR_13.png)
 
## <a id='s1-8' />JAR_O
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![JAR_O](../figures/V19_versus_aws-l3-dev/JAR_O_0.png)
![JAR_O](../figures/V19_versus_aws-l3-dev/JAR_O_1.png)
![JAR_O](../figures/V19_versus_aws-l3-dev/JAR_O_2.png)
![JAR_O](../figures/V19_versus_aws-l3-dev/JAR_O_3.png)
![JAR_O](../figures/V19_versus_aws-l3-dev/JAR_O_4.png)
![JAR_O](../figures/V19_versus_aws-l3-dev/JAR_O_5.png)
![JAR_O](../figures/V19_versus_aws-l3-dev/JAR_O_6.png)
![JAR_O](../figures/V19_versus_aws-l3-dev/JAR_O_7.png)
![JAR_O](../figures/V19_versus_aws-l3-dev/JAR_O_8.png)
![JAR_O](../figures/V19_versus_aws-l3-dev/JAR_O_9.png)
![JAR_O](../figures/V19_versus_aws-l3-dev/JAR_O_10.png)
![JAR_O](../figures/V19_versus_aws-l3-dev/JAR_O_11.png)
![JAR_O](../figures/V19_versus_aws-l3-dev/JAR_O_12.png)
![JAR_O](../figures/V19_versus_aws-l3-dev/JAR_O_13.png)
 
## <a id='s1-9' />KAN_B
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, z_boom_u, z_stake, z_pt, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, cc, z_surf_combined, z_ice_surf, snow_height, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, z_pt_cor, precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![KAN_B](../figures/V19_versus_aws-l3-dev/KAN_B_0.png)
![KAN_B](../figures/V19_versus_aws-l3-dev/KAN_B_1.png)
![KAN_B](../figures/V19_versus_aws-l3-dev/KAN_B_2.png)
![KAN_B](../figures/V19_versus_aws-l3-dev/KAN_B_3.png)
![KAN_B](../figures/V19_versus_aws-l3-dev/KAN_B_4.png)
![KAN_B](../figures/V19_versus_aws-l3-dev/KAN_B_5.png)
![KAN_B](../figures/V19_versus_aws-l3-dev/KAN_B_6.png)
![KAN_B](../figures/V19_versus_aws-l3-dev/KAN_B_7.png)
![KAN_B](../figures/V19_versus_aws-l3-dev/KAN_B_8.png)
![KAN_B](../figures/V19_versus_aws-l3-dev/KAN_B_9.png)
![KAN_B](../figures/V19_versus_aws-l3-dev/KAN_B_10.png)
 
## <a id='s1-10' />KAN_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![KAN_L](../figures/V19_versus_aws-l3-dev/KAN_L_0.png)
![KAN_L](../figures/V19_versus_aws-l3-dev/KAN_L_1.png)
![KAN_L](../figures/V19_versus_aws-l3-dev/KAN_L_2.png)
![KAN_L](../figures/V19_versus_aws-l3-dev/KAN_L_3.png)
![KAN_L](../figures/V19_versus_aws-l3-dev/KAN_L_4.png)
![KAN_L](../figures/V19_versus_aws-l3-dev/KAN_L_5.png)
![KAN_L](../figures/V19_versus_aws-l3-dev/KAN_L_6.png)
![KAN_L](../figures/V19_versus_aws-l3-dev/KAN_L_7.png)
![KAN_L](../figures/V19_versus_aws-l3-dev/KAN_L_8.png)
![KAN_L](../figures/V19_versus_aws-l3-dev/KAN_L_9.png)
![KAN_L](../figures/V19_versus_aws-l3-dev/KAN_L_10.png)
![KAN_L](../figures/V19_versus_aws-l3-dev/KAN_L_11.png)
![KAN_L](../figures/V19_versus_aws-l3-dev/KAN_L_12.png)
 
## <a id='s1-11' />KAN_Lv3
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![KAN_Lv3](../figures/V19_versus_aws-l3-dev/KAN_Lv3_0.png)
![KAN_Lv3](../figures/V19_versus_aws-l3-dev/KAN_Lv3_1.png)
![KAN_Lv3](../figures/V19_versus_aws-l3-dev/KAN_Lv3_2.png)
![KAN_Lv3](../figures/V19_versus_aws-l3-dev/KAN_Lv3_3.png)
![KAN_Lv3](../figures/V19_versus_aws-l3-dev/KAN_Lv3_4.png)
![KAN_Lv3](../figures/V19_versus_aws-l3-dev/KAN_Lv3_5.png)
![KAN_Lv3](../figures/V19_versus_aws-l3-dev/KAN_Lv3_6.png)
![KAN_Lv3](../figures/V19_versus_aws-l3-dev/KAN_Lv3_7.png)
![KAN_Lv3](../figures/V19_versus_aws-l3-dev/KAN_Lv3_8.png)
![KAN_Lv3](../figures/V19_versus_aws-l3-dev/KAN_Lv3_9.png)
![KAN_Lv3](../figures/V19_versus_aws-l3-dev/KAN_Lv3_10.png)
![KAN_Lv3](../figures/V19_versus_aws-l3-dev/KAN_Lv3_11.png)
![KAN_Lv3](../figures/V19_versus_aws-l3-dev/KAN_Lv3_12.png)
![KAN_Lv3](../figures/V19_versus_aws-l3-dev/KAN_Lv3_13.png)
 
## <a id='s1-12' />KAN_M
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![KAN_M](../figures/V19_versus_aws-l3-dev/KAN_M_0.png)
![KAN_M](../figures/V19_versus_aws-l3-dev/KAN_M_1.png)
![KAN_M](../figures/V19_versus_aws-l3-dev/KAN_M_2.png)
![KAN_M](../figures/V19_versus_aws-l3-dev/KAN_M_3.png)
![KAN_M](../figures/V19_versus_aws-l3-dev/KAN_M_4.png)
![KAN_M](../figures/V19_versus_aws-l3-dev/KAN_M_5.png)
![KAN_M](../figures/V19_versus_aws-l3-dev/KAN_M_6.png)
![KAN_M](../figures/V19_versus_aws-l3-dev/KAN_M_7.png)
![KAN_M](../figures/V19_versus_aws-l3-dev/KAN_M_8.png)
![KAN_M](../figures/V19_versus_aws-l3-dev/KAN_M_9.png)
![KAN_M](../figures/V19_versus_aws-l3-dev/KAN_M_10.png)
![KAN_M](../figures/V19_versus_aws-l3-dev/KAN_M_11.png)
![KAN_M](../figures/V19_versus_aws-l3-dev/KAN_M_12.png)
 
## <a id='s1-13' />KAN_Tv3
cannot find old file for KAN_Tv3
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

Old variables removed from new files:

 
![KAN_Tv3](../figures/V19_versus_aws-l3-dev/KAN_Tv3_0.png)
![KAN_Tv3](../figures/V19_versus_aws-l3-dev/KAN_Tv3_1.png)
![KAN_Tv3](../figures/V19_versus_aws-l3-dev/KAN_Tv3_2.png)
![KAN_Tv3](../figures/V19_versus_aws-l3-dev/KAN_Tv3_3.png)
![KAN_Tv3](../figures/V19_versus_aws-l3-dev/KAN_Tv3_4.png)
![KAN_Tv3](../figures/V19_versus_aws-l3-dev/KAN_Tv3_5.png)
![KAN_Tv3](../figures/V19_versus_aws-l3-dev/KAN_Tv3_6.png)
![KAN_Tv3](../figures/V19_versus_aws-l3-dev/KAN_Tv3_7.png)
![KAN_Tv3](../figures/V19_versus_aws-l3-dev/KAN_Tv3_8.png)
![KAN_Tv3](../figures/V19_versus_aws-l3-dev/KAN_Tv3_9.png)
![KAN_Tv3](../figures/V19_versus_aws-l3-dev/KAN_Tv3_10.png)
![KAN_Tv3](../figures/V19_versus_aws-l3-dev/KAN_Tv3_11.png)
![KAN_Tv3](../figures/V19_versus_aws-l3-dev/KAN_Tv3_12.png)
![KAN_Tv3](../figures/V19_versus_aws-l3-dev/KAN_Tv3_13.png)
 
## <a id='s1-14' />KAN_U
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_l, z_stake, z_pt, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
p_l, t_l, rh_u_wrt_ice_or_water, rh_l, rh_l_wrt_ice_or_water, wspd_l, wdir_l, wspd_x_l, wspd_y_l, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_l, precip_l_cor, precip_l_rate, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, z_pt_cor, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![KAN_U](../figures/V19_versus_aws-l3-dev/KAN_U_0.png)
![KAN_U](../figures/V19_versus_aws-l3-dev/KAN_U_1.png)
![KAN_U](../figures/V19_versus_aws-l3-dev/KAN_U_2.png)
![KAN_U](../figures/V19_versus_aws-l3-dev/KAN_U_3.png)
![KAN_U](../figures/V19_versus_aws-l3-dev/KAN_U_4.png)
![KAN_U](../figures/V19_versus_aws-l3-dev/KAN_U_5.png)
![KAN_U](../figures/V19_versus_aws-l3-dev/KAN_U_6.png)
![KAN_U](../figures/V19_versus_aws-l3-dev/KAN_U_7.png)
![KAN_U](../figures/V19_versus_aws-l3-dev/KAN_U_8.png)
![KAN_U](../figures/V19_versus_aws-l3-dev/KAN_U_9.png)
![KAN_U](../figures/V19_versus_aws-l3-dev/KAN_U_10.png)
![KAN_U](../figures/V19_versus_aws-l3-dev/KAN_U_11.png)
![KAN_U](../figures/V19_versus_aws-l3-dev/KAN_U_12.png)
![KAN_U](../figures/V19_versus_aws-l3-dev/KAN_U_13.png)
![KAN_U](../figures/V19_versus_aws-l3-dev/KAN_U_14.png)
![KAN_U](../figures/V19_versus_aws-l3-dev/KAN_U_15.png)
![KAN_U](../figures/V19_versus_aws-l3-dev/KAN_U_16.png)
 
## <a id='s1-15' />KPC_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![KPC_L](../figures/V19_versus_aws-l3-dev/KPC_L_0.png)
![KPC_L](../figures/V19_versus_aws-l3-dev/KPC_L_1.png)
![KPC_L](../figures/V19_versus_aws-l3-dev/KPC_L_2.png)
![KPC_L](../figures/V19_versus_aws-l3-dev/KPC_L_3.png)
![KPC_L](../figures/V19_versus_aws-l3-dev/KPC_L_4.png)
![KPC_L](../figures/V19_versus_aws-l3-dev/KPC_L_5.png)
![KPC_L](../figures/V19_versus_aws-l3-dev/KPC_L_6.png)
![KPC_L](../figures/V19_versus_aws-l3-dev/KPC_L_7.png)
![KPC_L](../figures/V19_versus_aws-l3-dev/KPC_L_8.png)
![KPC_L](../figures/V19_versus_aws-l3-dev/KPC_L_9.png)
![KPC_L](../figures/V19_versus_aws-l3-dev/KPC_L_10.png)
![KPC_L](../figures/V19_versus_aws-l3-dev/KPC_L_11.png)
![KPC_L](../figures/V19_versus_aws-l3-dev/KPC_L_12.png)
 
## <a id='s1-16' />KPC_Lv3
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![KPC_Lv3](../figures/V19_versus_aws-l3-dev/KPC_Lv3_0.png)
![KPC_Lv3](../figures/V19_versus_aws-l3-dev/KPC_Lv3_1.png)
![KPC_Lv3](../figures/V19_versus_aws-l3-dev/KPC_Lv3_2.png)
![KPC_Lv3](../figures/V19_versus_aws-l3-dev/KPC_Lv3_3.png)
![KPC_Lv3](../figures/V19_versus_aws-l3-dev/KPC_Lv3_4.png)
![KPC_Lv3](../figures/V19_versus_aws-l3-dev/KPC_Lv3_5.png)
![KPC_Lv3](../figures/V19_versus_aws-l3-dev/KPC_Lv3_6.png)
![KPC_Lv3](../figures/V19_versus_aws-l3-dev/KPC_Lv3_7.png)
![KPC_Lv3](../figures/V19_versus_aws-l3-dev/KPC_Lv3_8.png)
![KPC_Lv3](../figures/V19_versus_aws-l3-dev/KPC_Lv3_9.png)
![KPC_Lv3](../figures/V19_versus_aws-l3-dev/KPC_Lv3_10.png)
![KPC_Lv3](../figures/V19_versus_aws-l3-dev/KPC_Lv3_11.png)
![KPC_Lv3](../figures/V19_versus_aws-l3-dev/KPC_Lv3_12.png)
![KPC_Lv3](../figures/V19_versus_aws-l3-dev/KPC_Lv3_13.png)
 
## <a id='s1-17' />KPC_U
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![KPC_U](../figures/V19_versus_aws-l3-dev/KPC_U_0.png)
![KPC_U](../figures/V19_versus_aws-l3-dev/KPC_U_1.png)
![KPC_U](../figures/V19_versus_aws-l3-dev/KPC_U_2.png)
![KPC_U](../figures/V19_versus_aws-l3-dev/KPC_U_3.png)
![KPC_U](../figures/V19_versus_aws-l3-dev/KPC_U_4.png)
![KPC_U](../figures/V19_versus_aws-l3-dev/KPC_U_5.png)
![KPC_U](../figures/V19_versus_aws-l3-dev/KPC_U_6.png)
![KPC_U](../figures/V19_versus_aws-l3-dev/KPC_U_7.png)
![KPC_U](../figures/V19_versus_aws-l3-dev/KPC_U_8.png)
![KPC_U](../figures/V19_versus_aws-l3-dev/KPC_U_9.png)
![KPC_U](../figures/V19_versus_aws-l3-dev/KPC_U_10.png)
![KPC_U](../figures/V19_versus_aws-l3-dev/KPC_U_11.png)
![KPC_U](../figures/V19_versus_aws-l3-dev/KPC_U_12.png)
 
## <a id='s1-18' />KPC_Uv3
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor, wspd_x_i, wspd_y_i
 
![KPC_Uv3](../figures/V19_versus_aws-l3-dev/KPC_Uv3_0.png)
![KPC_Uv3](../figures/V19_versus_aws-l3-dev/KPC_Uv3_1.png)
![KPC_Uv3](../figures/V19_versus_aws-l3-dev/KPC_Uv3_2.png)
![KPC_Uv3](../figures/V19_versus_aws-l3-dev/KPC_Uv3_3.png)
![KPC_Uv3](../figures/V19_versus_aws-l3-dev/KPC_Uv3_4.png)
![KPC_Uv3](../figures/V19_versus_aws-l3-dev/KPC_Uv3_5.png)
![KPC_Uv3](../figures/V19_versus_aws-l3-dev/KPC_Uv3_6.png)
![KPC_Uv3](../figures/V19_versus_aws-l3-dev/KPC_Uv3_7.png)
![KPC_Uv3](../figures/V19_versus_aws-l3-dev/KPC_Uv3_8.png)
![KPC_Uv3](../figures/V19_versus_aws-l3-dev/KPC_Uv3_9.png)
![KPC_Uv3](../figures/V19_versus_aws-l3-dev/KPC_Uv3_10.png)
![KPC_Uv3](../figures/V19_versus_aws-l3-dev/KPC_Uv3_11.png)
![KPC_Uv3](../figures/V19_versus_aws-l3-dev/KPC_Uv3_12.png)
 
## <a id='s1-19' />LYN_L
cannot find old file for LYN_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

Old variables removed from new files:

 
![LYN_L](../figures/V19_versus_aws-l3-dev/LYN_L_0.png)
![LYN_L](../figures/V19_versus_aws-l3-dev/LYN_L_1.png)
![LYN_L](../figures/V19_versus_aws-l3-dev/LYN_L_2.png)
![LYN_L](../figures/V19_versus_aws-l3-dev/LYN_L_3.png)
![LYN_L](../figures/V19_versus_aws-l3-dev/LYN_L_4.png)
![LYN_L](../figures/V19_versus_aws-l3-dev/LYN_L_5.png)
![LYN_L](../figures/V19_versus_aws-l3-dev/LYN_L_6.png)
![LYN_L](../figures/V19_versus_aws-l3-dev/LYN_L_7.png)
![LYN_L](../figures/V19_versus_aws-l3-dev/LYN_L_8.png)
![LYN_L](../figures/V19_versus_aws-l3-dev/LYN_L_9.png)
![LYN_L](../figures/V19_versus_aws-l3-dev/LYN_L_10.png)
![LYN_L](../figures/V19_versus_aws-l3-dev/LYN_L_11.png)
![LYN_L](../figures/V19_versus_aws-l3-dev/LYN_L_12.png)
 
## <a id='s1-20' />MIT
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![MIT](../figures/V19_versus_aws-l3-dev/MIT_0.png)
![MIT](../figures/V19_versus_aws-l3-dev/MIT_1.png)
![MIT](../figures/V19_versus_aws-l3-dev/MIT_2.png)
![MIT](../figures/V19_versus_aws-l3-dev/MIT_3.png)
![MIT](../figures/V19_versus_aws-l3-dev/MIT_4.png)
![MIT](../figures/V19_versus_aws-l3-dev/MIT_5.png)
![MIT](../figures/V19_versus_aws-l3-dev/MIT_6.png)
![MIT](../figures/V19_versus_aws-l3-dev/MIT_7.png)
![MIT](../figures/V19_versus_aws-l3-dev/MIT_8.png)
![MIT](../figures/V19_versus_aws-l3-dev/MIT_9.png)
![MIT](../figures/V19_versus_aws-l3-dev/MIT_10.png)
![MIT](../figures/V19_versus_aws-l3-dev/MIT_11.png)
![MIT](../figures/V19_versus_aws-l3-dev/MIT_12.png)
 
## <a id='s1-21' />NAE
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, rh_l_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, rh_l_cor, gps_time, gps_hdop, fan_dc_u, fan_dc_l, rh_i_cor
 
![NAE](../figures/V19_versus_aws-l3-dev/NAE_0.png)
![NAE](../figures/V19_versus_aws-l3-dev/NAE_1.png)
![NAE](../figures/V19_versus_aws-l3-dev/NAE_2.png)
![NAE](../figures/V19_versus_aws-l3-dev/NAE_3.png)
![NAE](../figures/V19_versus_aws-l3-dev/NAE_4.png)
![NAE](../figures/V19_versus_aws-l3-dev/NAE_5.png)
![NAE](../figures/V19_versus_aws-l3-dev/NAE_6.png)
![NAE](../figures/V19_versus_aws-l3-dev/NAE_7.png)
![NAE](../figures/V19_versus_aws-l3-dev/NAE_8.png)
![NAE](../figures/V19_versus_aws-l3-dev/NAE_9.png)
![NAE](../figures/V19_versus_aws-l3-dev/NAE_10.png)
![NAE](../figures/V19_versus_aws-l3-dev/NAE_11.png)
![NAE](../figures/V19_versus_aws-l3-dev/NAE_12.png)
![NAE](../figures/V19_versus_aws-l3-dev/NAE_13.png)
![NAE](../figures/V19_versus_aws-l3-dev/NAE_14.png)
![NAE](../figures/V19_versus_aws-l3-dev/NAE_15.png)
![NAE](../figures/V19_versus_aws-l3-dev/NAE_16.png)
 
## <a id='s1-22' />NAU
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, rh_l_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, rh_l_cor, gps_time, gps_hdop, fan_dc_u, fan_dc_l, rh_i_cor
 
![NAU](../figures/V19_versus_aws-l3-dev/NAU_0.png)
![NAU](../figures/V19_versus_aws-l3-dev/NAU_1.png)
![NAU](../figures/V19_versus_aws-l3-dev/NAU_2.png)
![NAU](../figures/V19_versus_aws-l3-dev/NAU_3.png)
![NAU](../figures/V19_versus_aws-l3-dev/NAU_4.png)
![NAU](../figures/V19_versus_aws-l3-dev/NAU_5.png)
![NAU](../figures/V19_versus_aws-l3-dev/NAU_6.png)
![NAU](../figures/V19_versus_aws-l3-dev/NAU_7.png)
![NAU](../figures/V19_versus_aws-l3-dev/NAU_8.png)
![NAU](../figures/V19_versus_aws-l3-dev/NAU_9.png)
![NAU](../figures/V19_versus_aws-l3-dev/NAU_10.png)
![NAU](../figures/V19_versus_aws-l3-dev/NAU_11.png)
![NAU](../figures/V19_versus_aws-l3-dev/NAU_12.png)
![NAU](../figures/V19_versus_aws-l3-dev/NAU_13.png)
![NAU](../figures/V19_versus_aws-l3-dev/NAU_14.png)
![NAU](../figures/V19_versus_aws-l3-dev/NAU_15.png)
![NAU](../figures/V19_versus_aws-l3-dev/NAU_16.png)
 
## <a id='s1-23' />NEM
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, rh_l_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, rh_l_cor, gps_time, gps_hdop, fan_dc_u, fan_dc_l, rh_i_cor
 
![NEM](../figures/V19_versus_aws-l3-dev/NEM_0.png)
![NEM](../figures/V19_versus_aws-l3-dev/NEM_1.png)
![NEM](../figures/V19_versus_aws-l3-dev/NEM_2.png)
![NEM](../figures/V19_versus_aws-l3-dev/NEM_3.png)
![NEM](../figures/V19_versus_aws-l3-dev/NEM_4.png)
![NEM](../figures/V19_versus_aws-l3-dev/NEM_5.png)
![NEM](../figures/V19_versus_aws-l3-dev/NEM_6.png)
![NEM](../figures/V19_versus_aws-l3-dev/NEM_7.png)
![NEM](../figures/V19_versus_aws-l3-dev/NEM_8.png)
![NEM](../figures/V19_versus_aws-l3-dev/NEM_9.png)
![NEM](../figures/V19_versus_aws-l3-dev/NEM_10.png)
![NEM](../figures/V19_versus_aws-l3-dev/NEM_11.png)
![NEM](../figures/V19_versus_aws-l3-dev/NEM_12.png)
![NEM](../figures/V19_versus_aws-l3-dev/NEM_13.png)
![NEM](../figures/V19_versus_aws-l3-dev/NEM_14.png)
![NEM](../figures/V19_versus_aws-l3-dev/NEM_15.png)
![NEM](../figures/V19_versus_aws-l3-dev/NEM_16.png)
 
## <a id='s1-24' />NSE
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, rh_l_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, rh_l_cor, gps_time, gps_hdop, fan_dc_u, fan_dc_l, rh_i_cor
 
![NSE](../figures/V19_versus_aws-l3-dev/NSE_0.png)
![NSE](../figures/V19_versus_aws-l3-dev/NSE_1.png)
![NSE](../figures/V19_versus_aws-l3-dev/NSE_2.png)
![NSE](../figures/V19_versus_aws-l3-dev/NSE_3.png)
![NSE](../figures/V19_versus_aws-l3-dev/NSE_4.png)
![NSE](../figures/V19_versus_aws-l3-dev/NSE_5.png)
![NSE](../figures/V19_versus_aws-l3-dev/NSE_6.png)
![NSE](../figures/V19_versus_aws-l3-dev/NSE_7.png)
![NSE](../figures/V19_versus_aws-l3-dev/NSE_8.png)
![NSE](../figures/V19_versus_aws-l3-dev/NSE_9.png)
![NSE](../figures/V19_versus_aws-l3-dev/NSE_10.png)
![NSE](../figures/V19_versus_aws-l3-dev/NSE_11.png)
![NSE](../figures/V19_versus_aws-l3-dev/NSE_12.png)
![NSE](../figures/V19_versus_aws-l3-dev/NSE_13.png)
![NSE](../figures/V19_versus_aws-l3-dev/NSE_14.png)
![NSE](../figures/V19_versus_aws-l3-dev/NSE_15.png)
![NSE](../figures/V19_versus_aws-l3-dev/NSE_16.png)
 
## <a id='s1-25' />NUK_B
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, z_boom_u, z_stake, z_pt, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, cc, z_surf_combined, z_ice_surf, snow_height, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, z_pt_cor, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![NUK_B](../figures/V19_versus_aws-l3-dev/NUK_B_0.png)
![NUK_B](../figures/V19_versus_aws-l3-dev/NUK_B_1.png)
![NUK_B](../figures/V19_versus_aws-l3-dev/NUK_B_2.png)
![NUK_B](../figures/V19_versus_aws-l3-dev/NUK_B_3.png)
![NUK_B](../figures/V19_versus_aws-l3-dev/NUK_B_4.png)
![NUK_B](../figures/V19_versus_aws-l3-dev/NUK_B_5.png)
![NUK_B](../figures/V19_versus_aws-l3-dev/NUK_B_6.png)
![NUK_B](../figures/V19_versus_aws-l3-dev/NUK_B_7.png)
![NUK_B](../figures/V19_versus_aws-l3-dev/NUK_B_8.png)
![NUK_B](../figures/V19_versus_aws-l3-dev/NUK_B_9.png)
![NUK_B](../figures/V19_versus_aws-l3-dev/NUK_B_10.png)
 
## <a id='s1-26' />NUK_K
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![NUK_K](../figures/V19_versus_aws-l3-dev/NUK_K_0.png)
![NUK_K](../figures/V19_versus_aws-l3-dev/NUK_K_1.png)
![NUK_K](../figures/V19_versus_aws-l3-dev/NUK_K_2.png)
![NUK_K](../figures/V19_versus_aws-l3-dev/NUK_K_3.png)
![NUK_K](../figures/V19_versus_aws-l3-dev/NUK_K_4.png)
![NUK_K](../figures/V19_versus_aws-l3-dev/NUK_K_5.png)
![NUK_K](../figures/V19_versus_aws-l3-dev/NUK_K_6.png)
![NUK_K](../figures/V19_versus_aws-l3-dev/NUK_K_7.png)
![NUK_K](../figures/V19_versus_aws-l3-dev/NUK_K_8.png)
![NUK_K](../figures/V19_versus_aws-l3-dev/NUK_K_9.png)
![NUK_K](../figures/V19_versus_aws-l3-dev/NUK_K_10.png)
![NUK_K](../figures/V19_versus_aws-l3-dev/NUK_K_11.png)
![NUK_K](../figures/V19_versus_aws-l3-dev/NUK_K_12.png)
![NUK_K](../figures/V19_versus_aws-l3-dev/NUK_K_13.png)
 
## <a id='s1-27' />NUK_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![NUK_L](../figures/V19_versus_aws-l3-dev/NUK_L_0.png)
![NUK_L](../figures/V19_versus_aws-l3-dev/NUK_L_1.png)
![NUK_L](../figures/V19_versus_aws-l3-dev/NUK_L_2.png)
![NUK_L](../figures/V19_versus_aws-l3-dev/NUK_L_3.png)
![NUK_L](../figures/V19_versus_aws-l3-dev/NUK_L_4.png)
![NUK_L](../figures/V19_versus_aws-l3-dev/NUK_L_5.png)
![NUK_L](../figures/V19_versus_aws-l3-dev/NUK_L_6.png)
![NUK_L](../figures/V19_versus_aws-l3-dev/NUK_L_7.png)
![NUK_L](../figures/V19_versus_aws-l3-dev/NUK_L_8.png)
![NUK_L](../figures/V19_versus_aws-l3-dev/NUK_L_9.png)
![NUK_L](../figures/V19_versus_aws-l3-dev/NUK_L_10.png)
![NUK_L](../figures/V19_versus_aws-l3-dev/NUK_L_11.png)
![NUK_L](../figures/V19_versus_aws-l3-dev/NUK_L_12.png)
 
## <a id='s1-28' />NUK_N
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![NUK_N](../figures/V19_versus_aws-l3-dev/NUK_N_0.png)
![NUK_N](../figures/V19_versus_aws-l3-dev/NUK_N_1.png)
![NUK_N](../figures/V19_versus_aws-l3-dev/NUK_N_2.png)
![NUK_N](../figures/V19_versus_aws-l3-dev/NUK_N_3.png)
![NUK_N](../figures/V19_versus_aws-l3-dev/NUK_N_4.png)
![NUK_N](../figures/V19_versus_aws-l3-dev/NUK_N_5.png)
![NUK_N](../figures/V19_versus_aws-l3-dev/NUK_N_6.png)
![NUK_N](../figures/V19_versus_aws-l3-dev/NUK_N_7.png)
![NUK_N](../figures/V19_versus_aws-l3-dev/NUK_N_8.png)
![NUK_N](../figures/V19_versus_aws-l3-dev/NUK_N_9.png)
![NUK_N](../figures/V19_versus_aws-l3-dev/NUK_N_10.png)
![NUK_N](../figures/V19_versus_aws-l3-dev/NUK_N_11.png)
![NUK_N](../figures/V19_versus_aws-l3-dev/NUK_N_12.png)
 
## <a id='s1-29' />NUK_U
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![NUK_U](../figures/V19_versus_aws-l3-dev/NUK_U_0.png)
![NUK_U](../figures/V19_versus_aws-l3-dev/NUK_U_1.png)
![NUK_U](../figures/V19_versus_aws-l3-dev/NUK_U_2.png)
![NUK_U](../figures/V19_versus_aws-l3-dev/NUK_U_3.png)
![NUK_U](../figures/V19_versus_aws-l3-dev/NUK_U_4.png)
![NUK_U](../figures/V19_versus_aws-l3-dev/NUK_U_5.png)
![NUK_U](../figures/V19_versus_aws-l3-dev/NUK_U_6.png)
![NUK_U](../figures/V19_versus_aws-l3-dev/NUK_U_7.png)
![NUK_U](../figures/V19_versus_aws-l3-dev/NUK_U_8.png)
![NUK_U](../figures/V19_versus_aws-l3-dev/NUK_U_9.png)
![NUK_U](../figures/V19_versus_aws-l3-dev/NUK_U_10.png)
![NUK_U](../figures/V19_versus_aws-l3-dev/NUK_U_11.png)
![NUK_U](../figures/V19_versus_aws-l3-dev/NUK_U_12.png)
 
## <a id='s1-30' />NUK_Uv3
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![NUK_Uv3](../figures/V19_versus_aws-l3-dev/NUK_Uv3_0.png)
![NUK_Uv3](../figures/V19_versus_aws-l3-dev/NUK_Uv3_1.png)
![NUK_Uv3](../figures/V19_versus_aws-l3-dev/NUK_Uv3_2.png)
![NUK_Uv3](../figures/V19_versus_aws-l3-dev/NUK_Uv3_3.png)
![NUK_Uv3](../figures/V19_versus_aws-l3-dev/NUK_Uv3_4.png)
![NUK_Uv3](../figures/V19_versus_aws-l3-dev/NUK_Uv3_5.png)
![NUK_Uv3](../figures/V19_versus_aws-l3-dev/NUK_Uv3_6.png)
![NUK_Uv3](../figures/V19_versus_aws-l3-dev/NUK_Uv3_7.png)
![NUK_Uv3](../figures/V19_versus_aws-l3-dev/NUK_Uv3_8.png)
![NUK_Uv3](../figures/V19_versus_aws-l3-dev/NUK_Uv3_9.png)
![NUK_Uv3](../figures/V19_versus_aws-l3-dev/NUK_Uv3_10.png)
![NUK_Uv3](../figures/V19_versus_aws-l3-dev/NUK_Uv3_11.png)
![NUK_Uv3](../figures/V19_versus_aws-l3-dev/NUK_Uv3_12.png)
![NUK_Uv3](../figures/V19_versus_aws-l3-dev/NUK_Uv3_13.png)
 
## <a id='s1-31' />QAS_A
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![QAS_A](../figures/V19_versus_aws-l3-dev/QAS_A_0.png)
![QAS_A](../figures/V19_versus_aws-l3-dev/QAS_A_1.png)
![QAS_A](../figures/V19_versus_aws-l3-dev/QAS_A_2.png)
![QAS_A](../figures/V19_versus_aws-l3-dev/QAS_A_3.png)
![QAS_A](../figures/V19_versus_aws-l3-dev/QAS_A_4.png)
![QAS_A](../figures/V19_versus_aws-l3-dev/QAS_A_5.png)
![QAS_A](../figures/V19_versus_aws-l3-dev/QAS_A_6.png)
![QAS_A](../figures/V19_versus_aws-l3-dev/QAS_A_7.png)
![QAS_A](../figures/V19_versus_aws-l3-dev/QAS_A_8.png)
![QAS_A](../figures/V19_versus_aws-l3-dev/QAS_A_9.png)
![QAS_A](../figures/V19_versus_aws-l3-dev/QAS_A_10.png)
![QAS_A](../figures/V19_versus_aws-l3-dev/QAS_A_11.png)
![QAS_A](../figures/V19_versus_aws-l3-dev/QAS_A_12.png)
 
## <a id='s1-32' />QAS_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![QAS_L](../figures/V19_versus_aws-l3-dev/QAS_L_0.png)
![QAS_L](../figures/V19_versus_aws-l3-dev/QAS_L_1.png)
![QAS_L](../figures/V19_versus_aws-l3-dev/QAS_L_2.png)
![QAS_L](../figures/V19_versus_aws-l3-dev/QAS_L_3.png)
![QAS_L](../figures/V19_versus_aws-l3-dev/QAS_L_4.png)
![QAS_L](../figures/V19_versus_aws-l3-dev/QAS_L_5.png)
![QAS_L](../figures/V19_versus_aws-l3-dev/QAS_L_6.png)
![QAS_L](../figures/V19_versus_aws-l3-dev/QAS_L_7.png)
![QAS_L](../figures/V19_versus_aws-l3-dev/QAS_L_8.png)
![QAS_L](../figures/V19_versus_aws-l3-dev/QAS_L_9.png)
![QAS_L](../figures/V19_versus_aws-l3-dev/QAS_L_10.png)
![QAS_L](../figures/V19_versus_aws-l3-dev/QAS_L_11.png)
![QAS_L](../figures/V19_versus_aws-l3-dev/QAS_L_12.png)
 
## <a id='s1-33' />QAS_Lv3
cannot find old file for QAS_Lv3
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

Old variables removed from new files:

 
![QAS_Lv3](../figures/V19_versus_aws-l3-dev/QAS_Lv3_0.png)
![QAS_Lv3](../figures/V19_versus_aws-l3-dev/QAS_Lv3_1.png)
![QAS_Lv3](../figures/V19_versus_aws-l3-dev/QAS_Lv3_2.png)
![QAS_Lv3](../figures/V19_versus_aws-l3-dev/QAS_Lv3_3.png)
![QAS_Lv3](../figures/V19_versus_aws-l3-dev/QAS_Lv3_4.png)
![QAS_Lv3](../figures/V19_versus_aws-l3-dev/QAS_Lv3_5.png)
![QAS_Lv3](../figures/V19_versus_aws-l3-dev/QAS_Lv3_6.png)
![QAS_Lv3](../figures/V19_versus_aws-l3-dev/QAS_Lv3_7.png)
![QAS_Lv3](../figures/V19_versus_aws-l3-dev/QAS_Lv3_8.png)
![QAS_Lv3](../figures/V19_versus_aws-l3-dev/QAS_Lv3_9.png)
![QAS_Lv3](../figures/V19_versus_aws-l3-dev/QAS_Lv3_10.png)
![QAS_Lv3](../figures/V19_versus_aws-l3-dev/QAS_Lv3_11.png)
![QAS_Lv3](../figures/V19_versus_aws-l3-dev/QAS_Lv3_12.png)
![QAS_Lv3](../figures/V19_versus_aws-l3-dev/QAS_Lv3_13.png)
 
## <a id='s1-34' />QAS_Mv3
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![QAS_Mv3](../figures/V19_versus_aws-l3-dev/QAS_Mv3_0.png)
![QAS_Mv3](../figures/V19_versus_aws-l3-dev/QAS_Mv3_1.png)
![QAS_Mv3](../figures/V19_versus_aws-l3-dev/QAS_Mv3_2.png)
![QAS_Mv3](../figures/V19_versus_aws-l3-dev/QAS_Mv3_3.png)
![QAS_Mv3](../figures/V19_versus_aws-l3-dev/QAS_Mv3_4.png)
![QAS_Mv3](../figures/V19_versus_aws-l3-dev/QAS_Mv3_5.png)
![QAS_Mv3](../figures/V19_versus_aws-l3-dev/QAS_Mv3_6.png)
![QAS_Mv3](../figures/V19_versus_aws-l3-dev/QAS_Mv3_7.png)
![QAS_Mv3](../figures/V19_versus_aws-l3-dev/QAS_Mv3_8.png)
![QAS_Mv3](../figures/V19_versus_aws-l3-dev/QAS_Mv3_9.png)
![QAS_Mv3](../figures/V19_versus_aws-l3-dev/QAS_Mv3_10.png)
![QAS_Mv3](../figures/V19_versus_aws-l3-dev/QAS_Mv3_11.png)
![QAS_Mv3](../figures/V19_versus_aws-l3-dev/QAS_Mv3_12.png)
![QAS_Mv3](../figures/V19_versus_aws-l3-dev/QAS_Mv3_13.png)
 
## <a id='s1-35' />QAS_Uv3
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![QAS_Uv3](../figures/V19_versus_aws-l3-dev/QAS_Uv3_0.png)
![QAS_Uv3](../figures/V19_versus_aws-l3-dev/QAS_Uv3_1.png)
![QAS_Uv3](../figures/V19_versus_aws-l3-dev/QAS_Uv3_2.png)
![QAS_Uv3](../figures/V19_versus_aws-l3-dev/QAS_Uv3_3.png)
![QAS_Uv3](../figures/V19_versus_aws-l3-dev/QAS_Uv3_4.png)
![QAS_Uv3](../figures/V19_versus_aws-l3-dev/QAS_Uv3_5.png)
![QAS_Uv3](../figures/V19_versus_aws-l3-dev/QAS_Uv3_6.png)
![QAS_Uv3](../figures/V19_versus_aws-l3-dev/QAS_Uv3_7.png)
![QAS_Uv3](../figures/V19_versus_aws-l3-dev/QAS_Uv3_8.png)
![QAS_Uv3](../figures/V19_versus_aws-l3-dev/QAS_Uv3_9.png)
![QAS_Uv3](../figures/V19_versus_aws-l3-dev/QAS_Uv3_10.png)
![QAS_Uv3](../figures/V19_versus_aws-l3-dev/QAS_Uv3_11.png)
![QAS_Uv3](../figures/V19_versus_aws-l3-dev/QAS_Uv3_12.png)
![QAS_Uv3](../figures/V19_versus_aws-l3-dev/QAS_Uv3_13.png)
 
## <a id='s1-36' />RED_Lv3
cannot find old file for RED_Lv3
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

Old variables removed from new files:

 
![RED_Lv3](../figures/V19_versus_aws-l3-dev/RED_Lv3_0.png)
![RED_Lv3](../figures/V19_versus_aws-l3-dev/RED_Lv3_1.png)
![RED_Lv3](../figures/V19_versus_aws-l3-dev/RED_Lv3_2.png)
![RED_Lv3](../figures/V19_versus_aws-l3-dev/RED_Lv3_3.png)
![RED_Lv3](../figures/V19_versus_aws-l3-dev/RED_Lv3_4.png)
![RED_Lv3](../figures/V19_versus_aws-l3-dev/RED_Lv3_5.png)
![RED_Lv3](../figures/V19_versus_aws-l3-dev/RED_Lv3_6.png)
![RED_Lv3](../figures/V19_versus_aws-l3-dev/RED_Lv3_7.png)
![RED_Lv3](../figures/V19_versus_aws-l3-dev/RED_Lv3_8.png)
![RED_Lv3](../figures/V19_versus_aws-l3-dev/RED_Lv3_9.png)
![RED_Lv3](../figures/V19_versus_aws-l3-dev/RED_Lv3_10.png)
![RED_Lv3](../figures/V19_versus_aws-l3-dev/RED_Lv3_11.png)
![RED_Lv3](../figures/V19_versus_aws-l3-dev/RED_Lv3_12.png)
![RED_Lv3](../figures/V19_versus_aws-l3-dev/RED_Lv3_13.png)
 
## <a id='s1-37' />Roof_GEUS
cannot find old file for Roof_GEUS
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

Old variables removed from new files:

 
![Roof_GEUS](../figures/V19_versus_aws-l3-dev/Roof_GEUS_0.png)
![Roof_GEUS](../figures/V19_versus_aws-l3-dev/Roof_GEUS_1.png)
![Roof_GEUS](../figures/V19_versus_aws-l3-dev/Roof_GEUS_2.png)
![Roof_GEUS](../figures/V19_versus_aws-l3-dev/Roof_GEUS_3.png)
![Roof_GEUS](../figures/V19_versus_aws-l3-dev/Roof_GEUS_4.png)
![Roof_GEUS](../figures/V19_versus_aws-l3-dev/Roof_GEUS_5.png)
![Roof_GEUS](../figures/V19_versus_aws-l3-dev/Roof_GEUS_6.png)
![Roof_GEUS](../figures/V19_versus_aws-l3-dev/Roof_GEUS_7.png)
![Roof_GEUS](../figures/V19_versus_aws-l3-dev/Roof_GEUS_8.png)
![Roof_GEUS](../figures/V19_versus_aws-l3-dev/Roof_GEUS_9.png)
![Roof_GEUS](../figures/V19_versus_aws-l3-dev/Roof_GEUS_10.png)
![Roof_GEUS](../figures/V19_versus_aws-l3-dev/Roof_GEUS_11.png)
![Roof_GEUS](../figures/V19_versus_aws-l3-dev/Roof_GEUS_12.png)
![Roof_GEUS](../figures/V19_versus_aws-l3-dev/Roof_GEUS_13.png)
![Roof_GEUS](../figures/V19_versus_aws-l3-dev/Roof_GEUS_14.png)
![Roof_GEUS](../figures/V19_versus_aws-l3-dev/Roof_GEUS_15.png)
![Roof_GEUS](../figures/V19_versus_aws-l3-dev/Roof_GEUS_16.png)
 
## <a id='s1-38' />SCO_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![SCO_L](../figures/V19_versus_aws-l3-dev/SCO_L_0.png)
![SCO_L](../figures/V19_versus_aws-l3-dev/SCO_L_1.png)
![SCO_L](../figures/V19_versus_aws-l3-dev/SCO_L_2.png)
![SCO_L](../figures/V19_versus_aws-l3-dev/SCO_L_3.png)
![SCO_L](../figures/V19_versus_aws-l3-dev/SCO_L_4.png)
![SCO_L](../figures/V19_versus_aws-l3-dev/SCO_L_5.png)
![SCO_L](../figures/V19_versus_aws-l3-dev/SCO_L_6.png)
![SCO_L](../figures/V19_versus_aws-l3-dev/SCO_L_7.png)
![SCO_L](../figures/V19_versus_aws-l3-dev/SCO_L_8.png)
![SCO_L](../figures/V19_versus_aws-l3-dev/SCO_L_9.png)
![SCO_L](../figures/V19_versus_aws-l3-dev/SCO_L_10.png)
![SCO_L](../figures/V19_versus_aws-l3-dev/SCO_L_11.png)
![SCO_L](../figures/V19_versus_aws-l3-dev/SCO_L_12.png)
 
## <a id='s1-39' />SCO_Lv3
cannot find old file for SCO_Lv3
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

Old variables removed from new files:

 
![SCO_Lv3](../figures/V19_versus_aws-l3-dev/SCO_Lv3_0.png)
![SCO_Lv3](../figures/V19_versus_aws-l3-dev/SCO_Lv3_1.png)
![SCO_Lv3](../figures/V19_versus_aws-l3-dev/SCO_Lv3_2.png)
![SCO_Lv3](../figures/V19_versus_aws-l3-dev/SCO_Lv3_3.png)
![SCO_Lv3](../figures/V19_versus_aws-l3-dev/SCO_Lv3_4.png)
![SCO_Lv3](../figures/V19_versus_aws-l3-dev/SCO_Lv3_5.png)
![SCO_Lv3](../figures/V19_versus_aws-l3-dev/SCO_Lv3_6.png)
![SCO_Lv3](../figures/V19_versus_aws-l3-dev/SCO_Lv3_7.png)
![SCO_Lv3](../figures/V19_versus_aws-l3-dev/SCO_Lv3_8.png)
![SCO_Lv3](../figures/V19_versus_aws-l3-dev/SCO_Lv3_9.png)
![SCO_Lv3](../figures/V19_versus_aws-l3-dev/SCO_Lv3_10.png)
![SCO_Lv3](../figures/V19_versus_aws-l3-dev/SCO_Lv3_11.png)
![SCO_Lv3](../figures/V19_versus_aws-l3-dev/SCO_Lv3_12.png)
![SCO_Lv3](../figures/V19_versus_aws-l3-dev/SCO_Lv3_13.png)
 
## <a id='s1-40' />SCO_U
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![SCO_U](../figures/V19_versus_aws-l3-dev/SCO_U_0.png)
![SCO_U](../figures/V19_versus_aws-l3-dev/SCO_U_1.png)
![SCO_U](../figures/V19_versus_aws-l3-dev/SCO_U_2.png)
![SCO_U](../figures/V19_versus_aws-l3-dev/SCO_U_3.png)
![SCO_U](../figures/V19_versus_aws-l3-dev/SCO_U_4.png)
![SCO_U](../figures/V19_versus_aws-l3-dev/SCO_U_5.png)
![SCO_U](../figures/V19_versus_aws-l3-dev/SCO_U_6.png)
![SCO_U](../figures/V19_versus_aws-l3-dev/SCO_U_7.png)
![SCO_U](../figures/V19_versus_aws-l3-dev/SCO_U_8.png)
![SCO_U](../figures/V19_versus_aws-l3-dev/SCO_U_9.png)
![SCO_U](../figures/V19_versus_aws-l3-dev/SCO_U_10.png)
![SCO_U](../figures/V19_versus_aws-l3-dev/SCO_U_11.png)
![SCO_U](../figures/V19_versus_aws-l3-dev/SCO_U_12.png)
 
## <a id='s1-41' />SCO_Uv3
cannot find old file for SCO_Uv3
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

Old variables removed from new files:

 
![SCO_Uv3](../figures/V19_versus_aws-l3-dev/SCO_Uv3_0.png)
![SCO_Uv3](../figures/V19_versus_aws-l3-dev/SCO_Uv3_1.png)
![SCO_Uv3](../figures/V19_versus_aws-l3-dev/SCO_Uv3_2.png)
![SCO_Uv3](../figures/V19_versus_aws-l3-dev/SCO_Uv3_3.png)
![SCO_Uv3](../figures/V19_versus_aws-l3-dev/SCO_Uv3_4.png)
![SCO_Uv3](../figures/V19_versus_aws-l3-dev/SCO_Uv3_5.png)
![SCO_Uv3](../figures/V19_versus_aws-l3-dev/SCO_Uv3_6.png)
![SCO_Uv3](../figures/V19_versus_aws-l3-dev/SCO_Uv3_7.png)
![SCO_Uv3](../figures/V19_versus_aws-l3-dev/SCO_Uv3_8.png)
![SCO_Uv3](../figures/V19_versus_aws-l3-dev/SCO_Uv3_9.png)
![SCO_Uv3](../figures/V19_versus_aws-l3-dev/SCO_Uv3_10.png)
![SCO_Uv3](../figures/V19_versus_aws-l3-dev/SCO_Uv3_11.png)
![SCO_Uv3](../figures/V19_versus_aws-l3-dev/SCO_Uv3_12.png)
![SCO_Uv3](../figures/V19_versus_aws-l3-dev/SCO_Uv3_13.png)
 
## <a id='s1-42' />SDL
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, rh_l_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, rh_l_cor, gps_time, gps_hdop, fan_dc_u, fan_dc_l, rh_i_cor
 
![SDL](../figures/V19_versus_aws-l3-dev/SDL_0.png)
![SDL](../figures/V19_versus_aws-l3-dev/SDL_1.png)
![SDL](../figures/V19_versus_aws-l3-dev/SDL_2.png)
![SDL](../figures/V19_versus_aws-l3-dev/SDL_3.png)
![SDL](../figures/V19_versus_aws-l3-dev/SDL_4.png)
![SDL](../figures/V19_versus_aws-l3-dev/SDL_5.png)
![SDL](../figures/V19_versus_aws-l3-dev/SDL_6.png)
![SDL](../figures/V19_versus_aws-l3-dev/SDL_7.png)
![SDL](../figures/V19_versus_aws-l3-dev/SDL_8.png)
![SDL](../figures/V19_versus_aws-l3-dev/SDL_9.png)
![SDL](../figures/V19_versus_aws-l3-dev/SDL_10.png)
![SDL](../figures/V19_versus_aws-l3-dev/SDL_11.png)
![SDL](../figures/V19_versus_aws-l3-dev/SDL_12.png)
![SDL](../figures/V19_versus_aws-l3-dev/SDL_13.png)
![SDL](../figures/V19_versus_aws-l3-dev/SDL_14.png)
![SDL](../figures/V19_versus_aws-l3-dev/SDL_15.png)
![SDL](../figures/V19_versus_aws-l3-dev/SDL_16.png)
 
## <a id='s1-43' />SDM
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, rh_l_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, rh_l_cor, gps_time, gps_hdop, fan_dc_u, fan_dc_l, rh_i_cor
 
![SDM](../figures/V19_versus_aws-l3-dev/SDM_0.png)
![SDM](../figures/V19_versus_aws-l3-dev/SDM_1.png)
![SDM](../figures/V19_versus_aws-l3-dev/SDM_2.png)
![SDM](../figures/V19_versus_aws-l3-dev/SDM_3.png)
![SDM](../figures/V19_versus_aws-l3-dev/SDM_4.png)
![SDM](../figures/V19_versus_aws-l3-dev/SDM_5.png)
![SDM](../figures/V19_versus_aws-l3-dev/SDM_6.png)
![SDM](../figures/V19_versus_aws-l3-dev/SDM_7.png)
![SDM](../figures/V19_versus_aws-l3-dev/SDM_8.png)
![SDM](../figures/V19_versus_aws-l3-dev/SDM_9.png)
![SDM](../figures/V19_versus_aws-l3-dev/SDM_10.png)
![SDM](../figures/V19_versus_aws-l3-dev/SDM_11.png)
![SDM](../figures/V19_versus_aws-l3-dev/SDM_12.png)
![SDM](../figures/V19_versus_aws-l3-dev/SDM_13.png)
![SDM](../figures/V19_versus_aws-l3-dev/SDM_14.png)
![SDM](../figures/V19_versus_aws-l3-dev/SDM_15.png)
![SDM](../figures/V19_versus_aws-l3-dev/SDM_16.png)
 
## <a id='s1-44' />SER_B
cannot find old file for SER_B
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, z_boom_u, z_stake, z_pt, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, z_boom_u, z_stake, z_pt, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

Old variables removed from new files:

 
![SER_B](../figures/V19_versus_aws-l3-dev/SER_B_0.png)
![SER_B](../figures/V19_versus_aws-l3-dev/SER_B_1.png)
![SER_B](../figures/V19_versus_aws-l3-dev/SER_B_2.png)
![SER_B](../figures/V19_versus_aws-l3-dev/SER_B_3.png)
![SER_B](../figures/V19_versus_aws-l3-dev/SER_B_4.png)
![SER_B](../figures/V19_versus_aws-l3-dev/SER_B_5.png)
![SER_B](../figures/V19_versus_aws-l3-dev/SER_B_6.png)
![SER_B](../figures/V19_versus_aws-l3-dev/SER_B_7.png)
![SER_B](../figures/V19_versus_aws-l3-dev/SER_B_8.png)
![SER_B](../figures/V19_versus_aws-l3-dev/SER_B_9.png)
![SER_B](../figures/V19_versus_aws-l3-dev/SER_B_10.png)
 
## <a id='s1-45' />SWC
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![SWC](../figures/V19_versus_aws-l3-dev/SWC_0.png)
![SWC](../figures/V19_versus_aws-l3-dev/SWC_1.png)
![SWC](../figures/V19_versus_aws-l3-dev/SWC_2.png)
![SWC](../figures/V19_versus_aws-l3-dev/SWC_3.png)
![SWC](../figures/V19_versus_aws-l3-dev/SWC_4.png)
![SWC](../figures/V19_versus_aws-l3-dev/SWC_5.png)
![SWC](../figures/V19_versus_aws-l3-dev/SWC_6.png)
![SWC](../figures/V19_versus_aws-l3-dev/SWC_7.png)
![SWC](../figures/V19_versus_aws-l3-dev/SWC_8.png)
![SWC](../figures/V19_versus_aws-l3-dev/SWC_9.png)
![SWC](../figures/V19_versus_aws-l3-dev/SWC_10.png)
![SWC](../figures/V19_versus_aws-l3-dev/SWC_11.png)
![SWC](../figures/V19_versus_aws-l3-dev/SWC_12.png)
![SWC](../figures/V19_versus_aws-l3-dev/SWC_13.png)
 
## <a id='s1-46' />SWC_O
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![SWC_O](../figures/V19_versus_aws-l3-dev/SWC_O_0.png)
![SWC_O](../figures/V19_versus_aws-l3-dev/SWC_O_1.png)
![SWC_O](../figures/V19_versus_aws-l3-dev/SWC_O_2.png)
![SWC_O](../figures/V19_versus_aws-l3-dev/SWC_O_3.png)
![SWC_O](../figures/V19_versus_aws-l3-dev/SWC_O_4.png)
![SWC_O](../figures/V19_versus_aws-l3-dev/SWC_O_5.png)
![SWC_O](../figures/V19_versus_aws-l3-dev/SWC_O_6.png)
![SWC_O](../figures/V19_versus_aws-l3-dev/SWC_O_7.png)
![SWC_O](../figures/V19_versus_aws-l3-dev/SWC_O_8.png)
![SWC_O](../figures/V19_versus_aws-l3-dev/SWC_O_9.png)
![SWC_O](../figures/V19_versus_aws-l3-dev/SWC_O_10.png)
![SWC_O](../figures/V19_versus_aws-l3-dev/SWC_O_11.png)
![SWC_O](../figures/V19_versus_aws-l3-dev/SWC_O_12.png)
![SWC_O](../figures/V19_versus_aws-l3-dev/SWC_O_13.png)
 
## <a id='s1-47' />TAS_A
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![TAS_A](../figures/V19_versus_aws-l3-dev/TAS_A_0.png)
![TAS_A](../figures/V19_versus_aws-l3-dev/TAS_A_1.png)
![TAS_A](../figures/V19_versus_aws-l3-dev/TAS_A_2.png)
![TAS_A](../figures/V19_versus_aws-l3-dev/TAS_A_3.png)
![TAS_A](../figures/V19_versus_aws-l3-dev/TAS_A_4.png)
![TAS_A](../figures/V19_versus_aws-l3-dev/TAS_A_5.png)
![TAS_A](../figures/V19_versus_aws-l3-dev/TAS_A_6.png)
![TAS_A](../figures/V19_versus_aws-l3-dev/TAS_A_7.png)
![TAS_A](../figures/V19_versus_aws-l3-dev/TAS_A_8.png)
![TAS_A](../figures/V19_versus_aws-l3-dev/TAS_A_9.png)
![TAS_A](../figures/V19_versus_aws-l3-dev/TAS_A_10.png)
![TAS_A](../figures/V19_versus_aws-l3-dev/TAS_A_11.png)
![TAS_A](../figures/V19_versus_aws-l3-dev/TAS_A_12.png)
 
## <a id='s1-48' />TAS_Av3
cannot find old file for TAS_Av3
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

Old variables removed from new files:

 
![TAS_Av3](../figures/V19_versus_aws-l3-dev/TAS_Av3_0.png)
![TAS_Av3](../figures/V19_versus_aws-l3-dev/TAS_Av3_1.png)
![TAS_Av3](../figures/V19_versus_aws-l3-dev/TAS_Av3_2.png)
![TAS_Av3](../figures/V19_versus_aws-l3-dev/TAS_Av3_3.png)
![TAS_Av3](../figures/V19_versus_aws-l3-dev/TAS_Av3_4.png)
![TAS_Av3](../figures/V19_versus_aws-l3-dev/TAS_Av3_5.png)
![TAS_Av3](../figures/V19_versus_aws-l3-dev/TAS_Av3_6.png)
![TAS_Av3](../figures/V19_versus_aws-l3-dev/TAS_Av3_7.png)
![TAS_Av3](../figures/V19_versus_aws-l3-dev/TAS_Av3_8.png)
![TAS_Av3](../figures/V19_versus_aws-l3-dev/TAS_Av3_9.png)
![TAS_Av3](../figures/V19_versus_aws-l3-dev/TAS_Av3_10.png)
![TAS_Av3](../figures/V19_versus_aws-l3-dev/TAS_Av3_11.png)
![TAS_Av3](../figures/V19_versus_aws-l3-dev/TAS_Av3_12.png)
![TAS_Av3](../figures/V19_versus_aws-l3-dev/TAS_Av3_13.png)
 
## <a id='s1-49' />TAS_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![TAS_L](../figures/V19_versus_aws-l3-dev/TAS_L_0.png)
![TAS_L](../figures/V19_versus_aws-l3-dev/TAS_L_1.png)
![TAS_L](../figures/V19_versus_aws-l3-dev/TAS_L_2.png)
![TAS_L](../figures/V19_versus_aws-l3-dev/TAS_L_3.png)
![TAS_L](../figures/V19_versus_aws-l3-dev/TAS_L_4.png)
![TAS_L](../figures/V19_versus_aws-l3-dev/TAS_L_5.png)
![TAS_L](../figures/V19_versus_aws-l3-dev/TAS_L_6.png)
![TAS_L](../figures/V19_versus_aws-l3-dev/TAS_L_7.png)
![TAS_L](../figures/V19_versus_aws-l3-dev/TAS_L_8.png)
![TAS_L](../figures/V19_versus_aws-l3-dev/TAS_L_9.png)
![TAS_L](../figures/V19_versus_aws-l3-dev/TAS_L_10.png)
![TAS_L](../figures/V19_versus_aws-l3-dev/TAS_L_11.png)
![TAS_L](../figures/V19_versus_aws-l3-dev/TAS_L_12.png)
 
## <a id='s1-50' />TAS_U
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![TAS_U](../figures/V19_versus_aws-l3-dev/TAS_U_0.png)
![TAS_U](../figures/V19_versus_aws-l3-dev/TAS_U_1.png)
![TAS_U](../figures/V19_versus_aws-l3-dev/TAS_U_2.png)
![TAS_U](../figures/V19_versus_aws-l3-dev/TAS_U_3.png)
![TAS_U](../figures/V19_versus_aws-l3-dev/TAS_U_4.png)
![TAS_U](../figures/V19_versus_aws-l3-dev/TAS_U_5.png)
![TAS_U](../figures/V19_versus_aws-l3-dev/TAS_U_6.png)
![TAS_U](../figures/V19_versus_aws-l3-dev/TAS_U_7.png)
![TAS_U](../figures/V19_versus_aws-l3-dev/TAS_U_8.png)
![TAS_U](../figures/V19_versus_aws-l3-dev/TAS_U_9.png)
![TAS_U](../figures/V19_versus_aws-l3-dev/TAS_U_10.png)
![TAS_U](../figures/V19_versus_aws-l3-dev/TAS_U_11.png)
![TAS_U](../figures/V19_versus_aws-l3-dev/TAS_U_12.png)
 
## <a id='s1-51' />THU_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![THU_L](../figures/V19_versus_aws-l3-dev/THU_L_0.png)
![THU_L](../figures/V19_versus_aws-l3-dev/THU_L_1.png)
![THU_L](../figures/V19_versus_aws-l3-dev/THU_L_2.png)
![THU_L](../figures/V19_versus_aws-l3-dev/THU_L_3.png)
![THU_L](../figures/V19_versus_aws-l3-dev/THU_L_4.png)
![THU_L](../figures/V19_versus_aws-l3-dev/THU_L_5.png)
![THU_L](../figures/V19_versus_aws-l3-dev/THU_L_6.png)
![THU_L](../figures/V19_versus_aws-l3-dev/THU_L_7.png)
![THU_L](../figures/V19_versus_aws-l3-dev/THU_L_8.png)
![THU_L](../figures/V19_versus_aws-l3-dev/THU_L_9.png)
![THU_L](../figures/V19_versus_aws-l3-dev/THU_L_10.png)
![THU_L](../figures/V19_versus_aws-l3-dev/THU_L_11.png)
![THU_L](../figures/V19_versus_aws-l3-dev/THU_L_12.png)
 
## <a id='s1-52' />THU_L2
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![THU_L2](../figures/V19_versus_aws-l3-dev/THU_L2_0.png)
![THU_L2](../figures/V19_versus_aws-l3-dev/THU_L2_1.png)
![THU_L2](../figures/V19_versus_aws-l3-dev/THU_L2_2.png)
![THU_L2](../figures/V19_versus_aws-l3-dev/THU_L2_3.png)
![THU_L2](../figures/V19_versus_aws-l3-dev/THU_L2_4.png)
![THU_L2](../figures/V19_versus_aws-l3-dev/THU_L2_5.png)
![THU_L2](../figures/V19_versus_aws-l3-dev/THU_L2_6.png)
![THU_L2](../figures/V19_versus_aws-l3-dev/THU_L2_7.png)
![THU_L2](../figures/V19_versus_aws-l3-dev/THU_L2_8.png)
![THU_L2](../figures/V19_versus_aws-l3-dev/THU_L2_9.png)
![THU_L2](../figures/V19_versus_aws-l3-dev/THU_L2_10.png)
![THU_L2](../figures/V19_versus_aws-l3-dev/THU_L2_11.png)
![THU_L2](../figures/V19_versus_aws-l3-dev/THU_L2_12.png)
 
## <a id='s1-53' />THU_U2v3
cannot find old file for THU_U2v3
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

Old variables removed from new files:

 
![THU_U2v3](../figures/V19_versus_aws-l3-dev/THU_U2v3_0.png)
![THU_U2v3](../figures/V19_versus_aws-l3-dev/THU_U2v3_1.png)
![THU_U2v3](../figures/V19_versus_aws-l3-dev/THU_U2v3_2.png)
![THU_U2v3](../figures/V19_versus_aws-l3-dev/THU_U2v3_3.png)
![THU_U2v3](../figures/V19_versus_aws-l3-dev/THU_U2v3_4.png)
![THU_U2v3](../figures/V19_versus_aws-l3-dev/THU_U2v3_5.png)
![THU_U2v3](../figures/V19_versus_aws-l3-dev/THU_U2v3_6.png)
![THU_U2v3](../figures/V19_versus_aws-l3-dev/THU_U2v3_7.png)
![THU_U2v3](../figures/V19_versus_aws-l3-dev/THU_U2v3_8.png)
![THU_U2v3](../figures/V19_versus_aws-l3-dev/THU_U2v3_9.png)
![THU_U2v3](../figures/V19_versus_aws-l3-dev/THU_U2v3_10.png)
![THU_U2v3](../figures/V19_versus_aws-l3-dev/THU_U2v3_11.png)
![THU_U2v3](../figures/V19_versus_aws-l3-dev/THU_U2v3_12.png)
![THU_U2v3](../figures/V19_versus_aws-l3-dev/THU_U2v3_13.png)
 
## <a id='s1-54' />TUN
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, rh_l_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, rh_l_cor, gps_time, gps_hdop, fan_dc_u, fan_dc_l, rh_i_cor
 
![TUN](../figures/V19_versus_aws-l3-dev/TUN_0.png)
![TUN](../figures/V19_versus_aws-l3-dev/TUN_1.png)
![TUN](../figures/V19_versus_aws-l3-dev/TUN_2.png)
![TUN](../figures/V19_versus_aws-l3-dev/TUN_3.png)
![TUN](../figures/V19_versus_aws-l3-dev/TUN_4.png)
![TUN](../figures/V19_versus_aws-l3-dev/TUN_5.png)
![TUN](../figures/V19_versus_aws-l3-dev/TUN_6.png)
![TUN](../figures/V19_versus_aws-l3-dev/TUN_7.png)
![TUN](../figures/V19_versus_aws-l3-dev/TUN_8.png)
![TUN](../figures/V19_versus_aws-l3-dev/TUN_9.png)
![TUN](../figures/V19_versus_aws-l3-dev/TUN_10.png)
![TUN](../figures/V19_versus_aws-l3-dev/TUN_11.png)
![TUN](../figures/V19_versus_aws-l3-dev/TUN_12.png)
![TUN](../figures/V19_versus_aws-l3-dev/TUN_13.png)
![TUN](../figures/V19_versus_aws-l3-dev/TUN_14.png)
![TUN](../figures/V19_versus_aws-l3-dev/TUN_15.png)
![TUN](../figures/V19_versus_aws-l3-dev/TUN_16.png)
 
## <a id='s1-55' />UPE_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![UPE_L](../figures/V19_versus_aws-l3-dev/UPE_L_0.png)
![UPE_L](../figures/V19_versus_aws-l3-dev/UPE_L_1.png)
![UPE_L](../figures/V19_versus_aws-l3-dev/UPE_L_2.png)
![UPE_L](../figures/V19_versus_aws-l3-dev/UPE_L_3.png)
![UPE_L](../figures/V19_versus_aws-l3-dev/UPE_L_4.png)
![UPE_L](../figures/V19_versus_aws-l3-dev/UPE_L_5.png)
![UPE_L](../figures/V19_versus_aws-l3-dev/UPE_L_6.png)
![UPE_L](../figures/V19_versus_aws-l3-dev/UPE_L_7.png)
![UPE_L](../figures/V19_versus_aws-l3-dev/UPE_L_8.png)
![UPE_L](../figures/V19_versus_aws-l3-dev/UPE_L_9.png)
![UPE_L](../figures/V19_versus_aws-l3-dev/UPE_L_10.png)
![UPE_L](../figures/V19_versus_aws-l3-dev/UPE_L_11.png)
![UPE_L](../figures/V19_versus_aws-l3-dev/UPE_L_12.png)
 
## <a id='s1-56' />UPE_U
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![UPE_U](../figures/V19_versus_aws-l3-dev/UPE_U_0.png)
![UPE_U](../figures/V19_versus_aws-l3-dev/UPE_U_1.png)
![UPE_U](../figures/V19_versus_aws-l3-dev/UPE_U_2.png)
![UPE_U](../figures/V19_versus_aws-l3-dev/UPE_U_3.png)
![UPE_U](../figures/V19_versus_aws-l3-dev/UPE_U_4.png)
![UPE_U](../figures/V19_versus_aws-l3-dev/UPE_U_5.png)
![UPE_U](../figures/V19_versus_aws-l3-dev/UPE_U_6.png)
![UPE_U](../figures/V19_versus_aws-l3-dev/UPE_U_7.png)
![UPE_U](../figures/V19_versus_aws-l3-dev/UPE_U_8.png)
![UPE_U](../figures/V19_versus_aws-l3-dev/UPE_U_9.png)
![UPE_U](../figures/V19_versus_aws-l3-dev/UPE_U_10.png)
![UPE_U](../figures/V19_versus_aws-l3-dev/UPE_U_11.png)
![UPE_U](../figures/V19_versus_aws-l3-dev/UPE_U_12.png)
 
## <a id='s1-57' />UWN
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![UWN](../figures/V19_versus_aws-l3-dev/UWN_0.png)
![UWN](../figures/V19_versus_aws-l3-dev/UWN_1.png)
![UWN](../figures/V19_versus_aws-l3-dev/UWN_2.png)
![UWN](../figures/V19_versus_aws-l3-dev/UWN_3.png)
![UWN](../figures/V19_versus_aws-l3-dev/UWN_4.png)
![UWN](../figures/V19_versus_aws-l3-dev/UWN_5.png)
![UWN](../figures/V19_versus_aws-l3-dev/UWN_6.png)
![UWN](../figures/V19_versus_aws-l3-dev/UWN_7.png)
![UWN](../figures/V19_versus_aws-l3-dev/UWN_8.png)
![UWN](../figures/V19_versus_aws-l3-dev/UWN_9.png)
![UWN](../figures/V19_versus_aws-l3-dev/UWN_10.png)
![UWN](../figures/V19_versus_aws-l3-dev/UWN_11.png)
![UWN](../figures/V19_versus_aws-l3-dev/UWN_12.png)
 
## <a id='s1-58' />WEG_B
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, z_boom_u, z_stake, z_pt, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
rh_u_wrt_ice_or_water, cc, z_surf_combined, z_ice_surf, snow_height, lat, lon, alt, rh_i_wrt_ice_or_water

Old variables removed from new files:
rh_u_cor, z_pt_cor, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, rh_i_cor
 
![WEG_B](../figures/V19_versus_aws-l3-dev/WEG_B_0.png)
![WEG_B](../figures/V19_versus_aws-l3-dev/WEG_B_1.png)
![WEG_B](../figures/V19_versus_aws-l3-dev/WEG_B_2.png)
![WEG_B](../figures/V19_versus_aws-l3-dev/WEG_B_3.png)
![WEG_B](../figures/V19_versus_aws-l3-dev/WEG_B_4.png)
![WEG_B](../figures/V19_versus_aws-l3-dev/WEG_B_5.png)
![WEG_B](../figures/V19_versus_aws-l3-dev/WEG_B_6.png)
![WEG_B](../figures/V19_versus_aws-l3-dev/WEG_B_7.png)
![WEG_B](../figures/V19_versus_aws-l3-dev/WEG_B_8.png)
![WEG_B](../figures/V19_versus_aws-l3-dev/WEG_B_9.png)
![WEG_B](../figures/V19_versus_aws-l3-dev/WEG_B_10.png)
 
## <a id='s1-59' />WEG_L
cannot find old file for WEG_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

Old variables removed from new files:

 
![WEG_L](../figures/V19_versus_aws-l3-dev/WEG_L_0.png)
![WEG_L](../figures/V19_versus_aws-l3-dev/WEG_L_1.png)
![WEG_L](../figures/V19_versus_aws-l3-dev/WEG_L_2.png)
![WEG_L](../figures/V19_versus_aws-l3-dev/WEG_L_3.png)
![WEG_L](../figures/V19_versus_aws-l3-dev/WEG_L_4.png)
![WEG_L](../figures/V19_versus_aws-l3-dev/WEG_L_5.png)
![WEG_L](../figures/V19_versus_aws-l3-dev/WEG_L_6.png)
![WEG_L](../figures/V19_versus_aws-l3-dev/WEG_L_7.png)
![WEG_L](../figures/V19_versus_aws-l3-dev/WEG_L_8.png)
![WEG_L](../figures/V19_versus_aws-l3-dev/WEG_L_9.png)
![WEG_L](../figures/V19_versus_aws-l3-dev/WEG_L_10.png)
![WEG_L](../figures/V19_versus_aws-l3-dev/WEG_L_11.png)
![WEG_L](../figures/V19_versus_aws-l3-dev/WEG_L_12.png)
![WEG_L](../figures/V19_versus_aws-l3-dev/WEG_L_13.png)
 
## <a id='s1-60' />XXX
cannot find old file for XXX
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, wspd_i, wdir_i

New variables not in old files:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, wspd_i, wdir_i

Old variables removed from new files:

 
![XXX](../figures/V19_versus_aws-l3-dev/XXX_0.png)
![XXX](../figures/V19_versus_aws-l3-dev/XXX_1.png)
![XXX](../figures/V19_versus_aws-l3-dev/XXX_2.png)
![XXX](../figures/V19_versus_aws-l3-dev/XXX_3.png)
![XXX](../figures/V19_versus_aws-l3-dev/XXX_4.png)
![XXX](../figures/V19_versus_aws-l3-dev/XXX_5.png)
![XXX](../figures/V19_versus_aws-l3-dev/XXX_6.png)
![XXX](../figures/V19_versus_aws-l3-dev/XXX_7.png)
![XXX](../figures/V19_versus_aws-l3-dev/XXX_8.png)
![XXX](../figures/V19_versus_aws-l3-dev/XXX_9.png)
![XXX](../figures/V19_versus_aws-l3-dev/XXX_10.png)
![XXX](../figures/V19_versus_aws-l3-dev/XXX_11.png)
 
## <a id='s1-61' />ZAC_A
cannot find old file for ZAC_A
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

Old variables removed from new files:

 
![ZAC_A](../figures/V19_versus_aws-l3-dev/ZAC_A_0.png)
![ZAC_A](../figures/V19_versus_aws-l3-dev/ZAC_A_1.png)
![ZAC_A](../figures/V19_versus_aws-l3-dev/ZAC_A_2.png)
![ZAC_A](../figures/V19_versus_aws-l3-dev/ZAC_A_3.png)
![ZAC_A](../figures/V19_versus_aws-l3-dev/ZAC_A_4.png)
![ZAC_A](../figures/V19_versus_aws-l3-dev/ZAC_A_5.png)
![ZAC_A](../figures/V19_versus_aws-l3-dev/ZAC_A_6.png)
![ZAC_A](../figures/V19_versus_aws-l3-dev/ZAC_A_7.png)
![ZAC_A](../figures/V19_versus_aws-l3-dev/ZAC_A_8.png)
![ZAC_A](../figures/V19_versus_aws-l3-dev/ZAC_A_9.png)
![ZAC_A](../figures/V19_versus_aws-l3-dev/ZAC_A_10.png)
![ZAC_A](../figures/V19_versus_aws-l3-dev/ZAC_A_11.png)
![ZAC_A](../figures/V19_versus_aws-l3-dev/ZAC_A_12.png)
![ZAC_A](../figures/V19_versus_aws-l3-dev/ZAC_A_13.png)
![ZAC_A](../figures/V19_versus_aws-l3-dev/ZAC_A_14.png)
![ZAC_A](../figures/V19_versus_aws-l3-dev/ZAC_A_15.png)
![ZAC_A](../figures/V19_versus_aws-l3-dev/ZAC_A_16.png)
 
## <a id='s1-62' />ZAC_Lv3
cannot find old file for ZAC_Lv3
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

Old variables removed from new files:

 
![ZAC_Lv3](../figures/V19_versus_aws-l3-dev/ZAC_Lv3_0.png)
![ZAC_Lv3](../figures/V19_versus_aws-l3-dev/ZAC_Lv3_1.png)
![ZAC_Lv3](../figures/V19_versus_aws-l3-dev/ZAC_Lv3_2.png)
![ZAC_Lv3](../figures/V19_versus_aws-l3-dev/ZAC_Lv3_3.png)
![ZAC_Lv3](../figures/V19_versus_aws-l3-dev/ZAC_Lv3_4.png)
![ZAC_Lv3](../figures/V19_versus_aws-l3-dev/ZAC_Lv3_5.png)
![ZAC_Lv3](../figures/V19_versus_aws-l3-dev/ZAC_Lv3_6.png)
![ZAC_Lv3](../figures/V19_versus_aws-l3-dev/ZAC_Lv3_7.png)
![ZAC_Lv3](../figures/V19_versus_aws-l3-dev/ZAC_Lv3_8.png)
![ZAC_Lv3](../figures/V19_versus_aws-l3-dev/ZAC_Lv3_9.png)
![ZAC_Lv3](../figures/V19_versus_aws-l3-dev/ZAC_Lv3_10.png)
![ZAC_Lv3](../figures/V19_versus_aws-l3-dev/ZAC_Lv3_11.png)
![ZAC_Lv3](../figures/V19_versus_aws-l3-dev/ZAC_Lv3_12.png)
![ZAC_Lv3](../figures/V19_versus_aws-l3-dev/ZAC_Lv3_13.png)
 
## <a id='s1-63' />ZAC_Uv3
cannot find old file for ZAC_Uv3
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

Old variables removed from new files:

 
![ZAC_Uv3](../figures/V19_versus_aws-l3-dev/ZAC_Uv3_0.png)
![ZAC_Uv3](../figures/V19_versus_aws-l3-dev/ZAC_Uv3_1.png)
![ZAC_Uv3](../figures/V19_versus_aws-l3-dev/ZAC_Uv3_2.png)
![ZAC_Uv3](../figures/V19_versus_aws-l3-dev/ZAC_Uv3_3.png)
![ZAC_Uv3](../figures/V19_versus_aws-l3-dev/ZAC_Uv3_4.png)
![ZAC_Uv3](../figures/V19_versus_aws-l3-dev/ZAC_Uv3_5.png)
![ZAC_Uv3](../figures/V19_versus_aws-l3-dev/ZAC_Uv3_6.png)
![ZAC_Uv3](../figures/V19_versus_aws-l3-dev/ZAC_Uv3_7.png)
![ZAC_Uv3](../figures/V19_versus_aws-l3-dev/ZAC_Uv3_8.png)
![ZAC_Uv3](../figures/V19_versus_aws-l3-dev/ZAC_Uv3_9.png)
![ZAC_Uv3](../figures/V19_versus_aws-l3-dev/ZAC_Uv3_10.png)
![ZAC_Uv3](../figures/V19_versus_aws-l3-dev/ZAC_Uv3_11.png)
![ZAC_Uv3](../figures/V19_versus_aws-l3-dev/ZAC_Uv3_12.png)
![ZAC_Uv3](../figures/V19_versus_aws-l3-dev/ZAC_Uv3_13.png)
 
## <a id='s1-64' />ZAK_A
No new file for this station
## <a id='s1-65' />ZAK_Lv3
No new file for this station
## <a id='s1-66' />ZAK_Uv3
No new file for this station
