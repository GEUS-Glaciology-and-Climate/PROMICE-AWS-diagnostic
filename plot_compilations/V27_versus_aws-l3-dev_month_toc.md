* [Comparison of data aws-l3-dev to V27 (old).](#s1)
  * [CEN](#s1-1)
  * [CP1](#s1-2)
  * [DY2](#s1-3)
  * [EGP](#s1-4)
  * [FRE](#s1-5)
  * [HUM](#s1-6)
  * [JAR](#s1-7)
  * [KAN_B](#s1-8)
  * [KAN_L](#s1-9)
  * [KAN_M](#s1-10)
  * [KAN_T](#s1-11)
  * [KAN_U](#s1-12)
  * [KPC_L](#s1-13)
  * [KPC_U](#s1-14)
  * [LYN_L](#s1-15)
  * [LYN_T](#s1-16)
  * [MIT](#s1-17)
  * [NAE](#s1-18)
  * [NAU](#s1-19)
  * [NEM](#s1-20)
  * [NSE](#s1-21)
  * [NUK_B](#s1-22)
  * [NUK_K](#s1-23)
  * [NUK_L](#s1-24)
  * [NUK_N](#s1-25)
  * [NUK_P](#s1-26)
  * [NUK_U](#s1-27)
  * [ORO](#s1-28)
  * [QAS_A](#s1-29)
  * [QAS_L](#s1-30)
  * [QAS_M](#s1-31)
  * [QAS_U](#s1-32)
  * [RED_L](#s1-33)
  * [SCO_L](#s1-34)
  * [SCO_U](#s1-35)
  * [SDL](#s1-36)
  * [SDM](#s1-37)
  * [SER_B](#s1-38)
  * [SWC](#s1-39)
  * [TAS_A](#s1-40)
  * [TAS_L](#s1-41)
  * [TAS_U](#s1-42)
  * [THU_L](#s1-43)
  * [THU_L2](#s1-44)
  * [THU_U](#s1-45)
  * [TUN](#s1-46)
  * [UPE_L](#s1-47)
  * [UPE_U](#s1-48)
  * [UWN](#s1-49)
  * [WEG_B](#s1-50)
  * [WEG_L](#s1-51)
  * [ZAC_A](#s1-52)
  * [ZAC_L](#s1-53)
  * [ZAC_U](#s1-54)
# <a id='s1' />Comparison of data aws-l3-dev to V27 (old).
## <a id='s1-1' />CEN
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_stake, z_stake_cor, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, z_stake_cor, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![CEN](../figures/V27_versus_aws-l3-dev_month/CEN_month_0.png)
![CEN](../figures/V27_versus_aws-l3-dev_month/CEN_month_1.png)
![CEN](../figures/V27_versus_aws-l3-dev_month/CEN_month_2.png)
![CEN](../figures/V27_versus_aws-l3-dev_month/CEN_month_3.png)
![CEN](../figures/V27_versus_aws-l3-dev_month/CEN_month_4.png)
![CEN](../figures/V27_versus_aws-l3-dev_month/CEN_month_5.png)
![CEN](../figures/V27_versus_aws-l3-dev_month/CEN_month_6.png)
![CEN](../figures/V27_versus_aws-l3-dev_month/CEN_month_7.png)
![CEN](../figures/V27_versus_aws-l3-dev_month/CEN_month_8.png)
![CEN](../figures/V27_versus_aws-l3-dev_month/CEN_month_9.png)
![CEN](../figures/V27_versus_aws-l3-dev_month/CEN_month_10.png)
![CEN](../figures/V27_versus_aws-l3-dev_month/CEN_month_11.png)
![CEN](../figures/V27_versus_aws-l3-dev_month/CEN_month_12.png)
![CEN](../figures/V27_versus_aws-l3-dev_month/CEN_month_13.png)
![CEN](../figures/V27_versus_aws-l3-dev_month/CEN_month_14.png)
![CEN](../figures/V27_versus_aws-l3-dev_month/CEN_month_15.png)
![CEN](../figures/V27_versus_aws-l3-dev_month/CEN_month_16.png)
 
## <a id='s1-2' />CP1
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![CP1](../figures/V27_versus_aws-l3-dev_month/CP1_month_0.png)
![CP1](../figures/V27_versus_aws-l3-dev_month/CP1_month_1.png)
![CP1](../figures/V27_versus_aws-l3-dev_month/CP1_month_2.png)
![CP1](../figures/V27_versus_aws-l3-dev_month/CP1_month_3.png)
![CP1](../figures/V27_versus_aws-l3-dev_month/CP1_month_4.png)
![CP1](../figures/V27_versus_aws-l3-dev_month/CP1_month_5.png)
![CP1](../figures/V27_versus_aws-l3-dev_month/CP1_month_6.png)
![CP1](../figures/V27_versus_aws-l3-dev_month/CP1_month_7.png)
![CP1](../figures/V27_versus_aws-l3-dev_month/CP1_month_8.png)
![CP1](../figures/V27_versus_aws-l3-dev_month/CP1_month_9.png)
![CP1](../figures/V27_versus_aws-l3-dev_month/CP1_month_10.png)
![CP1](../figures/V27_versus_aws-l3-dev_month/CP1_month_11.png)
![CP1](../figures/V27_versus_aws-l3-dev_month/CP1_month_12.png)
![CP1](../figures/V27_versus_aws-l3-dev_month/CP1_month_13.png)
![CP1](../figures/V27_versus_aws-l3-dev_month/CP1_month_14.png)
![CP1](../figures/V27_versus_aws-l3-dev_month/CP1_month_15.png)
 
## <a id='s1-3' />DY2
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![DY2](../figures/V27_versus_aws-l3-dev_month/DY2_month_0.png)
![DY2](../figures/V27_versus_aws-l3-dev_month/DY2_month_1.png)
![DY2](../figures/V27_versus_aws-l3-dev_month/DY2_month_2.png)
![DY2](../figures/V27_versus_aws-l3-dev_month/DY2_month_3.png)
![DY2](../figures/V27_versus_aws-l3-dev_month/DY2_month_4.png)
![DY2](../figures/V27_versus_aws-l3-dev_month/DY2_month_5.png)
![DY2](../figures/V27_versus_aws-l3-dev_month/DY2_month_6.png)
![DY2](../figures/V27_versus_aws-l3-dev_month/DY2_month_7.png)
![DY2](../figures/V27_versus_aws-l3-dev_month/DY2_month_8.png)
![DY2](../figures/V27_versus_aws-l3-dev_month/DY2_month_9.png)
![DY2](../figures/V27_versus_aws-l3-dev_month/DY2_month_10.png)
![DY2](../figures/V27_versus_aws-l3-dev_month/DY2_month_11.png)
![DY2](../figures/V27_versus_aws-l3-dev_month/DY2_month_12.png)
![DY2](../figures/V27_versus_aws-l3-dev_month/DY2_month_13.png)
![DY2](../figures/V27_versus_aws-l3-dev_month/DY2_month_14.png)
![DY2](../figures/V27_versus_aws-l3-dev_month/DY2_month_15.png)
 
## <a id='s1-4' />EGP
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_stake, z_stake_cor, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
p_l, z_boom_cor_u, z_boom_cor_l, z_stake_cor, rainfall_u, rainfall_cor_u, rainfall_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![EGP](../figures/V27_versus_aws-l3-dev_month/EGP_month_0.png)
![EGP](../figures/V27_versus_aws-l3-dev_month/EGP_month_1.png)
![EGP](../figures/V27_versus_aws-l3-dev_month/EGP_month_2.png)
![EGP](../figures/V27_versus_aws-l3-dev_month/EGP_month_3.png)
![EGP](../figures/V27_versus_aws-l3-dev_month/EGP_month_4.png)
![EGP](../figures/V27_versus_aws-l3-dev_month/EGP_month_5.png)
![EGP](../figures/V27_versus_aws-l3-dev_month/EGP_month_6.png)
![EGP](../figures/V27_versus_aws-l3-dev_month/EGP_month_7.png)
![EGP](../figures/V27_versus_aws-l3-dev_month/EGP_month_8.png)
![EGP](../figures/V27_versus_aws-l3-dev_month/EGP_month_9.png)
![EGP](../figures/V27_versus_aws-l3-dev_month/EGP_month_10.png)
![EGP](../figures/V27_versus_aws-l3-dev_month/EGP_month_11.png)
![EGP](../figures/V27_versus_aws-l3-dev_month/EGP_month_12.png)
![EGP](../figures/V27_versus_aws-l3-dev_month/EGP_month_13.png)
![EGP](../figures/V27_versus_aws-l3-dev_month/EGP_month_14.png)
![EGP](../figures/V27_versus_aws-l3-dev_month/EGP_month_15.png)
 
## <a id='s1-5' />FRE
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![FRE](../figures/V27_versus_aws-l3-dev_month/FRE_month_0.png)
![FRE](../figures/V27_versus_aws-l3-dev_month/FRE_month_1.png)
![FRE](../figures/V27_versus_aws-l3-dev_month/FRE_month_2.png)
![FRE](../figures/V27_versus_aws-l3-dev_month/FRE_month_3.png)
![FRE](../figures/V27_versus_aws-l3-dev_month/FRE_month_4.png)
![FRE](../figures/V27_versus_aws-l3-dev_month/FRE_month_5.png)
![FRE](../figures/V27_versus_aws-l3-dev_month/FRE_month_6.png)
![FRE](../figures/V27_versus_aws-l3-dev_month/FRE_month_7.png)
![FRE](../figures/V27_versus_aws-l3-dev_month/FRE_month_8.png)
![FRE](../figures/V27_versus_aws-l3-dev_month/FRE_month_9.png)
![FRE](../figures/V27_versus_aws-l3-dev_month/FRE_month_10.png)
![FRE](../figures/V27_versus_aws-l3-dev_month/FRE_month_11.png)
 
## <a id='s1-6' />HUM
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![HUM](../figures/V27_versus_aws-l3-dev_month/HUM_month_0.png)
![HUM](../figures/V27_versus_aws-l3-dev_month/HUM_month_1.png)
![HUM](../figures/V27_versus_aws-l3-dev_month/HUM_month_2.png)
![HUM](../figures/V27_versus_aws-l3-dev_month/HUM_month_3.png)
![HUM](../figures/V27_versus_aws-l3-dev_month/HUM_month_4.png)
![HUM](../figures/V27_versus_aws-l3-dev_month/HUM_month_5.png)
![HUM](../figures/V27_versus_aws-l3-dev_month/HUM_month_6.png)
![HUM](../figures/V27_versus_aws-l3-dev_month/HUM_month_7.png)
![HUM](../figures/V27_versus_aws-l3-dev_month/HUM_month_8.png)
![HUM](../figures/V27_versus_aws-l3-dev_month/HUM_month_9.png)
![HUM](../figures/V27_versus_aws-l3-dev_month/HUM_month_10.png)
![HUM](../figures/V27_versus_aws-l3-dev_month/HUM_month_11.png)
![HUM](../figures/V27_versus_aws-l3-dev_month/HUM_month_12.png)
![HUM](../figures/V27_versus_aws-l3-dev_month/HUM_month_13.png)
![HUM](../figures/V27_versus_aws-l3-dev_month/HUM_month_14.png)
![HUM](../figures/V27_versus_aws-l3-dev_month/HUM_month_15.png)
 
## <a id='s1-7' />JAR
Variables in new file:
p_u, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_boom_cor_l, z_stake, z_stake_cor, z_pt, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
z_boom_l, z_pt_cor, precip_u, precip_u_cor, precip_u_rate
 
![JAR](../figures/V27_versus_aws-l3-dev_month/JAR_month_0.png)
![JAR](../figures/V27_versus_aws-l3-dev_month/JAR_month_1.png)
![JAR](../figures/V27_versus_aws-l3-dev_month/JAR_month_2.png)
![JAR](../figures/V27_versus_aws-l3-dev_month/JAR_month_3.png)
![JAR](../figures/V27_versus_aws-l3-dev_month/JAR_month_4.png)
![JAR](../figures/V27_versus_aws-l3-dev_month/JAR_month_5.png)
![JAR](../figures/V27_versus_aws-l3-dev_month/JAR_month_6.png)
![JAR](../figures/V27_versus_aws-l3-dev_month/JAR_month_7.png)
![JAR](../figures/V27_versus_aws-l3-dev_month/JAR_month_8.png)
![JAR](../figures/V27_versus_aws-l3-dev_month/JAR_month_9.png)
![JAR](../figures/V27_versus_aws-l3-dev_month/JAR_month_10.png)
![JAR](../figures/V27_versus_aws-l3-dev_month/JAR_month_11.png)
![JAR](../figures/V27_versus_aws-l3-dev_month/JAR_month_12.png)
![JAR](../figures/V27_versus_aws-l3-dev_month/JAR_month_13.png)
![JAR](../figures/V27_versus_aws-l3-dev_month/JAR_month_14.png)
 
## <a id='s1-8' />KAN_B
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, usr, albedo, dlr, ulr, t_surf, z_boom_u, z_boom_cor_u, z_stake_cor, z_surf_combined, snow_height, t_i_2, t_i_4, t_i_6, t_i_8, tilt_x, rot, gps_lon, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, t_i_2, t_i_4, t_i_6, t_i_8, rot, gps_lon

Old variables removed from new files:
dsr_cor, usr_cor, cc, z_stake, precip_u, t_i_1, t_i_3, t_i_5, t_i_7, tilt_y, gps_lat, gps_alt
 
![KAN_B](../figures/V27_versus_aws-l3-dev_month/KAN_B_month_0.png)
![KAN_B](../figures/V27_versus_aws-l3-dev_month/KAN_B_month_1.png)
![KAN_B](../figures/V27_versus_aws-l3-dev_month/KAN_B_month_2.png)
![KAN_B](../figures/V27_versus_aws-l3-dev_month/KAN_B_month_3.png)
![KAN_B](../figures/V27_versus_aws-l3-dev_month/KAN_B_month_4.png)
![KAN_B](../figures/V27_versus_aws-l3-dev_month/KAN_B_month_5.png)
![KAN_B](../figures/V27_versus_aws-l3-dev_month/KAN_B_month_6.png)
![KAN_B](../figures/V27_versus_aws-l3-dev_month/KAN_B_month_7.png)
 
## <a id='s1-9' />KAN_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![KAN_L](../figures/V27_versus_aws-l3-dev_month/KAN_L_month_0.png)
![KAN_L](../figures/V27_versus_aws-l3-dev_month/KAN_L_month_1.png)
![KAN_L](../figures/V27_versus_aws-l3-dev_month/KAN_L_month_2.png)
![KAN_L](../figures/V27_versus_aws-l3-dev_month/KAN_L_month_3.png)
![KAN_L](../figures/V27_versus_aws-l3-dev_month/KAN_L_month_4.png)
![KAN_L](../figures/V27_versus_aws-l3-dev_month/KAN_L_month_5.png)
![KAN_L](../figures/V27_versus_aws-l3-dev_month/KAN_L_month_6.png)
![KAN_L](../figures/V27_versus_aws-l3-dev_month/KAN_L_month_7.png)
![KAN_L](../figures/V27_versus_aws-l3-dev_month/KAN_L_month_8.png)
![KAN_L](../figures/V27_versus_aws-l3-dev_month/KAN_L_month_9.png)
![KAN_L](../figures/V27_versus_aws-l3-dev_month/KAN_L_month_10.png)
![KAN_L](../figures/V27_versus_aws-l3-dev_month/KAN_L_month_11.png)
![KAN_L](../figures/V27_versus_aws-l3-dev_month/KAN_L_month_12.png)
 
## <a id='s1-10' />KAN_M
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![KAN_M](../figures/V27_versus_aws-l3-dev_month/KAN_M_month_0.png)
![KAN_M](../figures/V27_versus_aws-l3-dev_month/KAN_M_month_1.png)
![KAN_M](../figures/V27_versus_aws-l3-dev_month/KAN_M_month_2.png)
![KAN_M](../figures/V27_versus_aws-l3-dev_month/KAN_M_month_3.png)
![KAN_M](../figures/V27_versus_aws-l3-dev_month/KAN_M_month_4.png)
![KAN_M](../figures/V27_versus_aws-l3-dev_month/KAN_M_month_5.png)
![KAN_M](../figures/V27_versus_aws-l3-dev_month/KAN_M_month_6.png)
![KAN_M](../figures/V27_versus_aws-l3-dev_month/KAN_M_month_7.png)
![KAN_M](../figures/V27_versus_aws-l3-dev_month/KAN_M_month_8.png)
![KAN_M](../figures/V27_versus_aws-l3-dev_month/KAN_M_month_9.png)
![KAN_M](../figures/V27_versus_aws-l3-dev_month/KAN_M_month_10.png)
![KAN_M](../figures/V27_versus_aws-l3-dev_month/KAN_M_month_11.png)
 
## <a id='s1-11' />KAN_T
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_5, t_i_7, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, t_i_4, t_i_6, t_i_8, d_t_i_1
 
![KAN_T](../figures/V27_versus_aws-l3-dev_month/KAN_T_month_0.png)
![KAN_T](../figures/V27_versus_aws-l3-dev_month/KAN_T_month_1.png)
![KAN_T](../figures/V27_versus_aws-l3-dev_month/KAN_T_month_2.png)
![KAN_T](../figures/V27_versus_aws-l3-dev_month/KAN_T_month_3.png)
![KAN_T](../figures/V27_versus_aws-l3-dev_month/KAN_T_month_4.png)
![KAN_T](../figures/V27_versus_aws-l3-dev_month/KAN_T_month_5.png)
![KAN_T](../figures/V27_versus_aws-l3-dev_month/KAN_T_month_6.png)
![KAN_T](../figures/V27_versus_aws-l3-dev_month/KAN_T_month_7.png)
![KAN_T](../figures/V27_versus_aws-l3-dev_month/KAN_T_month_8.png)
![KAN_T](../figures/V27_versus_aws-l3-dev_month/KAN_T_month_9.png)
![KAN_T](../figures/V27_versus_aws-l3-dev_month/KAN_T_month_10.png)
![KAN_T](../figures/V27_versus_aws-l3-dev_month/KAN_T_month_11.png)
 
## <a id='s1-12' />KAN_U
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_stake, z_stake_cor, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
qh_l, dlhf_l, dshf_l, z_boom_cor_u, z_boom_cor_l, z_stake_cor, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![KAN_U](../figures/V27_versus_aws-l3-dev_month/KAN_U_month_0.png)
![KAN_U](../figures/V27_versus_aws-l3-dev_month/KAN_U_month_1.png)
![KAN_U](../figures/V27_versus_aws-l3-dev_month/KAN_U_month_2.png)
![KAN_U](../figures/V27_versus_aws-l3-dev_month/KAN_U_month_3.png)
![KAN_U](../figures/V27_versus_aws-l3-dev_month/KAN_U_month_4.png)
![KAN_U](../figures/V27_versus_aws-l3-dev_month/KAN_U_month_5.png)
![KAN_U](../figures/V27_versus_aws-l3-dev_month/KAN_U_month_6.png)
![KAN_U](../figures/V27_versus_aws-l3-dev_month/KAN_U_month_7.png)
![KAN_U](../figures/V27_versus_aws-l3-dev_month/KAN_U_month_8.png)
![KAN_U](../figures/V27_versus_aws-l3-dev_month/KAN_U_month_9.png)
![KAN_U](../figures/V27_versus_aws-l3-dev_month/KAN_U_month_10.png)
![KAN_U](../figures/V27_versus_aws-l3-dev_month/KAN_U_month_11.png)
![KAN_U](../figures/V27_versus_aws-l3-dev_month/KAN_U_month_12.png)
![KAN_U](../figures/V27_versus_aws-l3-dev_month/KAN_U_month_13.png)
![KAN_U](../figures/V27_versus_aws-l3-dev_month/KAN_U_month_14.png)
![KAN_U](../figures/V27_versus_aws-l3-dev_month/KAN_U_month_15.png)
![KAN_U](../figures/V27_versus_aws-l3-dev_month/KAN_U_month_16.png)
 
## <a id='s1-13' />KPC_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![KPC_L](../figures/V27_versus_aws-l3-dev_month/KPC_L_month_0.png)
![KPC_L](../figures/V27_versus_aws-l3-dev_month/KPC_L_month_1.png)
![KPC_L](../figures/V27_versus_aws-l3-dev_month/KPC_L_month_2.png)
![KPC_L](../figures/V27_versus_aws-l3-dev_month/KPC_L_month_3.png)
![KPC_L](../figures/V27_versus_aws-l3-dev_month/KPC_L_month_4.png)
![KPC_L](../figures/V27_versus_aws-l3-dev_month/KPC_L_month_5.png)
![KPC_L](../figures/V27_versus_aws-l3-dev_month/KPC_L_month_6.png)
![KPC_L](../figures/V27_versus_aws-l3-dev_month/KPC_L_month_7.png)
![KPC_L](../figures/V27_versus_aws-l3-dev_month/KPC_L_month_8.png)
![KPC_L](../figures/V27_versus_aws-l3-dev_month/KPC_L_month_9.png)
![KPC_L](../figures/V27_versus_aws-l3-dev_month/KPC_L_month_10.png)
![KPC_L](../figures/V27_versus_aws-l3-dev_month/KPC_L_month_11.png)
 
## <a id='s1-14' />KPC_U
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![KPC_U](../figures/V27_versus_aws-l3-dev_month/KPC_U_month_0.png)
![KPC_U](../figures/V27_versus_aws-l3-dev_month/KPC_U_month_1.png)
![KPC_U](../figures/V27_versus_aws-l3-dev_month/KPC_U_month_2.png)
![KPC_U](../figures/V27_versus_aws-l3-dev_month/KPC_U_month_3.png)
![KPC_U](../figures/V27_versus_aws-l3-dev_month/KPC_U_month_4.png)
![KPC_U](../figures/V27_versus_aws-l3-dev_month/KPC_U_month_5.png)
![KPC_U](../figures/V27_versus_aws-l3-dev_month/KPC_U_month_6.png)
![KPC_U](../figures/V27_versus_aws-l3-dev_month/KPC_U_month_7.png)
![KPC_U](../figures/V27_versus_aws-l3-dev_month/KPC_U_month_8.png)
![KPC_U](../figures/V27_versus_aws-l3-dev_month/KPC_U_month_9.png)
![KPC_U](../figures/V27_versus_aws-l3-dev_month/KPC_U_month_10.png)
![KPC_U](../figures/V27_versus_aws-l3-dev_month/KPC_U_month_11.png)
 
## <a id='s1-15' />LYN_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, z_boom_cor_u, z_stake_cor, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_2, t_i_4, t_i_6, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_alt, lat, lon, alt, t_rad, rh_i_wrt_ice_or_water, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, t_i_8

Old variables removed from new files:
dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, t_i_1, t_i_3, t_i_5, t_i_7, gps_lon, batt_v, t_i, wdir_i
 
![LYN_L](../figures/V27_versus_aws-l3-dev_month/LYN_L_month_0.png)
![LYN_L](../figures/V27_versus_aws-l3-dev_month/LYN_L_month_1.png)
![LYN_L](../figures/V27_versus_aws-l3-dev_month/LYN_L_month_2.png)
![LYN_L](../figures/V27_versus_aws-l3-dev_month/LYN_L_month_3.png)
![LYN_L](../figures/V27_versus_aws-l3-dev_month/LYN_L_month_4.png)
![LYN_L](../figures/V27_versus_aws-l3-dev_month/LYN_L_month_5.png)
![LYN_L](../figures/V27_versus_aws-l3-dev_month/LYN_L_month_6.png)
![LYN_L](../figures/V27_versus_aws-l3-dev_month/LYN_L_month_7.png)
![LYN_L](../figures/V27_versus_aws-l3-dev_month/LYN_L_month_8.png)
![LYN_L](../figures/V27_versus_aws-l3-dev_month/LYN_L_month_9.png)
 
## <a id='s1-16' />LYN_T
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, z_boom_cor_u, z_stake_cor, z_surf_combined, z_ice_surf, snow_height, t_i_2, t_i_4, t_i_6, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_alt, lat, lon, alt, t_rad, rh_i_wrt_ice_or_water, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, t_i_8

Old variables removed from new files:
dlhf_u, dshf_u, z_boom_u, z_stake, t_i_1, t_i_3, t_i_5, t_i_7, gps_lon, batt_v, t_i, wdir_i
 
![LYN_T](../figures/V27_versus_aws-l3-dev_month/LYN_T_month_0.png)
![LYN_T](../figures/V27_versus_aws-l3-dev_month/LYN_T_month_1.png)
![LYN_T](../figures/V27_versus_aws-l3-dev_month/LYN_T_month_2.png)
![LYN_T](../figures/V27_versus_aws-l3-dev_month/LYN_T_month_3.png)
![LYN_T](../figures/V27_versus_aws-l3-dev_month/LYN_T_month_4.png)
![LYN_T](../figures/V27_versus_aws-l3-dev_month/LYN_T_month_5.png)
![LYN_T](../figures/V27_versus_aws-l3-dev_month/LYN_T_month_6.png)
![LYN_T](../figures/V27_versus_aws-l3-dev_month/LYN_T_month_7.png)
![LYN_T](../figures/V27_versus_aws-l3-dev_month/LYN_T_month_8.png)
![LYN_T](../figures/V27_versus_aws-l3-dev_month/LYN_T_month_9.png)
 
## <a id='s1-17' />MIT
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![MIT](../figures/V27_versus_aws-l3-dev_month/MIT_month_0.png)
![MIT](../figures/V27_versus_aws-l3-dev_month/MIT_month_1.png)
![MIT](../figures/V27_versus_aws-l3-dev_month/MIT_month_2.png)
![MIT](../figures/V27_versus_aws-l3-dev_month/MIT_month_3.png)
![MIT](../figures/V27_versus_aws-l3-dev_month/MIT_month_4.png)
![MIT](../figures/V27_versus_aws-l3-dev_month/MIT_month_5.png)
![MIT](../figures/V27_versus_aws-l3-dev_month/MIT_month_6.png)
![MIT](../figures/V27_versus_aws-l3-dev_month/MIT_month_7.png)
![MIT](../figures/V27_versus_aws-l3-dev_month/MIT_month_8.png)
![MIT](../figures/V27_versus_aws-l3-dev_month/MIT_month_9.png)
![MIT](../figures/V27_versus_aws-l3-dev_month/MIT_month_10.png)
![MIT](../figures/V27_versus_aws-l3-dev_month/MIT_month_11.png)
 
## <a id='s1-18' />NAE
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![NAE](../figures/V27_versus_aws-l3-dev_month/NAE_month_0.png)
![NAE](../figures/V27_versus_aws-l3-dev_month/NAE_month_1.png)
![NAE](../figures/V27_versus_aws-l3-dev_month/NAE_month_2.png)
![NAE](../figures/V27_versus_aws-l3-dev_month/NAE_month_3.png)
![NAE](../figures/V27_versus_aws-l3-dev_month/NAE_month_4.png)
![NAE](../figures/V27_versus_aws-l3-dev_month/NAE_month_5.png)
![NAE](../figures/V27_versus_aws-l3-dev_month/NAE_month_6.png)
![NAE](../figures/V27_versus_aws-l3-dev_month/NAE_month_7.png)
![NAE](../figures/V27_versus_aws-l3-dev_month/NAE_month_8.png)
![NAE](../figures/V27_versus_aws-l3-dev_month/NAE_month_9.png)
![NAE](../figures/V27_versus_aws-l3-dev_month/NAE_month_10.png)
![NAE](../figures/V27_versus_aws-l3-dev_month/NAE_month_11.png)
![NAE](../figures/V27_versus_aws-l3-dev_month/NAE_month_12.png)
![NAE](../figures/V27_versus_aws-l3-dev_month/NAE_month_13.png)
![NAE](../figures/V27_versus_aws-l3-dev_month/NAE_month_14.png)
![NAE](../figures/V27_versus_aws-l3-dev_month/NAE_month_15.png)
 
## <a id='s1-19' />NAU
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![NAU](../figures/V27_versus_aws-l3-dev_month/NAU_month_0.png)
![NAU](../figures/V27_versus_aws-l3-dev_month/NAU_month_1.png)
![NAU](../figures/V27_versus_aws-l3-dev_month/NAU_month_2.png)
![NAU](../figures/V27_versus_aws-l3-dev_month/NAU_month_3.png)
![NAU](../figures/V27_versus_aws-l3-dev_month/NAU_month_4.png)
![NAU](../figures/V27_versus_aws-l3-dev_month/NAU_month_5.png)
![NAU](../figures/V27_versus_aws-l3-dev_month/NAU_month_6.png)
![NAU](../figures/V27_versus_aws-l3-dev_month/NAU_month_7.png)
![NAU](../figures/V27_versus_aws-l3-dev_month/NAU_month_8.png)
![NAU](../figures/V27_versus_aws-l3-dev_month/NAU_month_9.png)
![NAU](../figures/V27_versus_aws-l3-dev_month/NAU_month_10.png)
![NAU](../figures/V27_versus_aws-l3-dev_month/NAU_month_11.png)
![NAU](../figures/V27_versus_aws-l3-dev_month/NAU_month_12.png)
![NAU](../figures/V27_versus_aws-l3-dev_month/NAU_month_13.png)
![NAU](../figures/V27_versus_aws-l3-dev_month/NAU_month_14.png)
![NAU](../figures/V27_versus_aws-l3-dev_month/NAU_month_15.png)
 
## <a id='s1-20' />NEM
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![NEM](../figures/V27_versus_aws-l3-dev_month/NEM_month_0.png)
![NEM](../figures/V27_versus_aws-l3-dev_month/NEM_month_1.png)
![NEM](../figures/V27_versus_aws-l3-dev_month/NEM_month_2.png)
![NEM](../figures/V27_versus_aws-l3-dev_month/NEM_month_3.png)
![NEM](../figures/V27_versus_aws-l3-dev_month/NEM_month_4.png)
![NEM](../figures/V27_versus_aws-l3-dev_month/NEM_month_5.png)
![NEM](../figures/V27_versus_aws-l3-dev_month/NEM_month_6.png)
![NEM](../figures/V27_versus_aws-l3-dev_month/NEM_month_7.png)
![NEM](../figures/V27_versus_aws-l3-dev_month/NEM_month_8.png)
![NEM](../figures/V27_versus_aws-l3-dev_month/NEM_month_9.png)
![NEM](../figures/V27_versus_aws-l3-dev_month/NEM_month_10.png)
![NEM](../figures/V27_versus_aws-l3-dev_month/NEM_month_11.png)
![NEM](../figures/V27_versus_aws-l3-dev_month/NEM_month_12.png)
![NEM](../figures/V27_versus_aws-l3-dev_month/NEM_month_13.png)
![NEM](../figures/V27_versus_aws-l3-dev_month/NEM_month_14.png)
![NEM](../figures/V27_versus_aws-l3-dev_month/NEM_month_15.png)
 
## <a id='s1-21' />NSE
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![NSE](../figures/V27_versus_aws-l3-dev_month/NSE_month_0.png)
![NSE](../figures/V27_versus_aws-l3-dev_month/NSE_month_1.png)
![NSE](../figures/V27_versus_aws-l3-dev_month/NSE_month_2.png)
![NSE](../figures/V27_versus_aws-l3-dev_month/NSE_month_3.png)
![NSE](../figures/V27_versus_aws-l3-dev_month/NSE_month_4.png)
![NSE](../figures/V27_versus_aws-l3-dev_month/NSE_month_5.png)
![NSE](../figures/V27_versus_aws-l3-dev_month/NSE_month_6.png)
![NSE](../figures/V27_versus_aws-l3-dev_month/NSE_month_7.png)
![NSE](../figures/V27_versus_aws-l3-dev_month/NSE_month_8.png)
![NSE](../figures/V27_versus_aws-l3-dev_month/NSE_month_9.png)
![NSE](../figures/V27_versus_aws-l3-dev_month/NSE_month_10.png)
![NSE](../figures/V27_versus_aws-l3-dev_month/NSE_month_11.png)
![NSE](../figures/V27_versus_aws-l3-dev_month/NSE_month_12.png)
![NSE](../figures/V27_versus_aws-l3-dev_month/NSE_month_13.png)
![NSE](../figures/V27_versus_aws-l3-dev_month/NSE_month_14.png)
![NSE](../figures/V27_versus_aws-l3-dev_month/NSE_month_15.png)
 
## <a id='s1-22' />NUK_B
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, usr, albedo, dlr, ulr, t_surf, z_boom_u, z_boom_cor_u, z_stake_cor, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, t_i_2, t_i_4, t_i_6, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u, t_i_2, t_i_4, t_i_6, t_i_8

Old variables removed from new files:
z_stake, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_3, t_i_5, t_i_7
 
![NUK_B](../figures/V27_versus_aws-l3-dev_month/NUK_B_month_0.png)
![NUK_B](../figures/V27_versus_aws-l3-dev_month/NUK_B_month_1.png)
![NUK_B](../figures/V27_versus_aws-l3-dev_month/NUK_B_month_2.png)
![NUK_B](../figures/V27_versus_aws-l3-dev_month/NUK_B_month_3.png)
![NUK_B](../figures/V27_versus_aws-l3-dev_month/NUK_B_month_4.png)
![NUK_B](../figures/V27_versus_aws-l3-dev_month/NUK_B_month_5.png)
![NUK_B](../figures/V27_versus_aws-l3-dev_month/NUK_B_month_6.png)
![NUK_B](../figures/V27_versus_aws-l3-dev_month/NUK_B_month_7.png)
![NUK_B](../figures/V27_versus_aws-l3-dev_month/NUK_B_month_8.png)
 
## <a id='s1-23' />NUK_K
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![NUK_K](../figures/V27_versus_aws-l3-dev_month/NUK_K_month_0.png)
![NUK_K](../figures/V27_versus_aws-l3-dev_month/NUK_K_month_1.png)
![NUK_K](../figures/V27_versus_aws-l3-dev_month/NUK_K_month_2.png)
![NUK_K](../figures/V27_versus_aws-l3-dev_month/NUK_K_month_3.png)
![NUK_K](../figures/V27_versus_aws-l3-dev_month/NUK_K_month_4.png)
![NUK_K](../figures/V27_versus_aws-l3-dev_month/NUK_K_month_5.png)
![NUK_K](../figures/V27_versus_aws-l3-dev_month/NUK_K_month_6.png)
![NUK_K](../figures/V27_versus_aws-l3-dev_month/NUK_K_month_7.png)
![NUK_K](../figures/V27_versus_aws-l3-dev_month/NUK_K_month_8.png)
![NUK_K](../figures/V27_versus_aws-l3-dev_month/NUK_K_month_9.png)
![NUK_K](../figures/V27_versus_aws-l3-dev_month/NUK_K_month_10.png)
![NUK_K](../figures/V27_versus_aws-l3-dev_month/NUK_K_month_11.png)
![NUK_K](../figures/V27_versus_aws-l3-dev_month/NUK_K_month_12.png)
 
## <a id='s1-24' />NUK_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![NUK_L](../figures/V27_versus_aws-l3-dev_month/NUK_L_month_0.png)
![NUK_L](../figures/V27_versus_aws-l3-dev_month/NUK_L_month_1.png)
![NUK_L](../figures/V27_versus_aws-l3-dev_month/NUK_L_month_2.png)
![NUK_L](../figures/V27_versus_aws-l3-dev_month/NUK_L_month_3.png)
![NUK_L](../figures/V27_versus_aws-l3-dev_month/NUK_L_month_4.png)
![NUK_L](../figures/V27_versus_aws-l3-dev_month/NUK_L_month_5.png)
![NUK_L](../figures/V27_versus_aws-l3-dev_month/NUK_L_month_6.png)
![NUK_L](../figures/V27_versus_aws-l3-dev_month/NUK_L_month_7.png)
![NUK_L](../figures/V27_versus_aws-l3-dev_month/NUK_L_month_8.png)
![NUK_L](../figures/V27_versus_aws-l3-dev_month/NUK_L_month_9.png)
![NUK_L](../figures/V27_versus_aws-l3-dev_month/NUK_L_month_10.png)
![NUK_L](../figures/V27_versus_aws-l3-dev_month/NUK_L_month_11.png)
![NUK_L](../figures/V27_versus_aws-l3-dev_month/NUK_L_month_12.png)
 
## <a id='s1-25' />NUK_N
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![NUK_N](../figures/V27_versus_aws-l3-dev_month/NUK_N_month_0.png)
![NUK_N](../figures/V27_versus_aws-l3-dev_month/NUK_N_month_1.png)
![NUK_N](../figures/V27_versus_aws-l3-dev_month/NUK_N_month_2.png)
![NUK_N](../figures/V27_versus_aws-l3-dev_month/NUK_N_month_3.png)
![NUK_N](../figures/V27_versus_aws-l3-dev_month/NUK_N_month_4.png)
![NUK_N](../figures/V27_versus_aws-l3-dev_month/NUK_N_month_5.png)
![NUK_N](../figures/V27_versus_aws-l3-dev_month/NUK_N_month_6.png)
![NUK_N](../figures/V27_versus_aws-l3-dev_month/NUK_N_month_7.png)
![NUK_N](../figures/V27_versus_aws-l3-dev_month/NUK_N_month_8.png)
![NUK_N](../figures/V27_versus_aws-l3-dev_month/NUK_N_month_9.png)
![NUK_N](../figures/V27_versus_aws-l3-dev_month/NUK_N_month_10.png)
![NUK_N](../figures/V27_versus_aws-l3-dev_month/NUK_N_month_11.png)
 
## <a id='s1-26' />NUK_P
## <a id='s1-27' />NUK_U
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![NUK_U](../figures/V27_versus_aws-l3-dev_month/NUK_U_month_0.png)
![NUK_U](../figures/V27_versus_aws-l3-dev_month/NUK_U_month_1.png)
![NUK_U](../figures/V27_versus_aws-l3-dev_month/NUK_U_month_2.png)
![NUK_U](../figures/V27_versus_aws-l3-dev_month/NUK_U_month_3.png)
![NUK_U](../figures/V27_versus_aws-l3-dev_month/NUK_U_month_4.png)
![NUK_U](../figures/V27_versus_aws-l3-dev_month/NUK_U_month_5.png)
![NUK_U](../figures/V27_versus_aws-l3-dev_month/NUK_U_month_6.png)
![NUK_U](../figures/V27_versus_aws-l3-dev_month/NUK_U_month_7.png)
![NUK_U](../figures/V27_versus_aws-l3-dev_month/NUK_U_month_8.png)
![NUK_U](../figures/V27_versus_aws-l3-dev_month/NUK_U_month_9.png)
![NUK_U](../figures/V27_versus_aws-l3-dev_month/NUK_U_month_10.png)
![NUK_U](../figures/V27_versus_aws-l3-dev_month/NUK_U_month_11.png)
![NUK_U](../figures/V27_versus_aws-l3-dev_month/NUK_U_month_12.png)
 
## <a id='s1-28' />ORO
## <a id='s1-29' />QAS_A
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:
t_i_6
 
![QAS_A](../figures/V27_versus_aws-l3-dev_month/QAS_A_month_0.png)
![QAS_A](../figures/V27_versus_aws-l3-dev_month/QAS_A_month_1.png)
![QAS_A](../figures/V27_versus_aws-l3-dev_month/QAS_A_month_2.png)
![QAS_A](../figures/V27_versus_aws-l3-dev_month/QAS_A_month_3.png)
![QAS_A](../figures/V27_versus_aws-l3-dev_month/QAS_A_month_4.png)
![QAS_A](../figures/V27_versus_aws-l3-dev_month/QAS_A_month_5.png)
![QAS_A](../figures/V27_versus_aws-l3-dev_month/QAS_A_month_6.png)
![QAS_A](../figures/V27_versus_aws-l3-dev_month/QAS_A_month_7.png)
![QAS_A](../figures/V27_versus_aws-l3-dev_month/QAS_A_month_8.png)
![QAS_A](../figures/V27_versus_aws-l3-dev_month/QAS_A_month_9.png)
![QAS_A](../figures/V27_versus_aws-l3-dev_month/QAS_A_month_10.png)
![QAS_A](../figures/V27_versus_aws-l3-dev_month/QAS_A_month_11.png)
 
## <a id='s1-30' />QAS_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![QAS_L](../figures/V27_versus_aws-l3-dev_month/QAS_L_month_0.png)
![QAS_L](../figures/V27_versus_aws-l3-dev_month/QAS_L_month_1.png)
![QAS_L](../figures/V27_versus_aws-l3-dev_month/QAS_L_month_2.png)
![QAS_L](../figures/V27_versus_aws-l3-dev_month/QAS_L_month_3.png)
![QAS_L](../figures/V27_versus_aws-l3-dev_month/QAS_L_month_4.png)
![QAS_L](../figures/V27_versus_aws-l3-dev_month/QAS_L_month_5.png)
![QAS_L](../figures/V27_versus_aws-l3-dev_month/QAS_L_month_6.png)
![QAS_L](../figures/V27_versus_aws-l3-dev_month/QAS_L_month_7.png)
![QAS_L](../figures/V27_versus_aws-l3-dev_month/QAS_L_month_8.png)
![QAS_L](../figures/V27_versus_aws-l3-dev_month/QAS_L_month_9.png)
![QAS_L](../figures/V27_versus_aws-l3-dev_month/QAS_L_month_10.png)
![QAS_L](../figures/V27_versus_aws-l3-dev_month/QAS_L_month_11.png)
![QAS_L](../figures/V27_versus_aws-l3-dev_month/QAS_L_month_12.png)
 
## <a id='s1-31' />QAS_M
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![QAS_M](../figures/V27_versus_aws-l3-dev_month/QAS_M_month_0.png)
![QAS_M](../figures/V27_versus_aws-l3-dev_month/QAS_M_month_1.png)
![QAS_M](../figures/V27_versus_aws-l3-dev_month/QAS_M_month_2.png)
![QAS_M](../figures/V27_versus_aws-l3-dev_month/QAS_M_month_3.png)
![QAS_M](../figures/V27_versus_aws-l3-dev_month/QAS_M_month_4.png)
![QAS_M](../figures/V27_versus_aws-l3-dev_month/QAS_M_month_5.png)
![QAS_M](../figures/V27_versus_aws-l3-dev_month/QAS_M_month_6.png)
![QAS_M](../figures/V27_versus_aws-l3-dev_month/QAS_M_month_7.png)
![QAS_M](../figures/V27_versus_aws-l3-dev_month/QAS_M_month_8.png)
![QAS_M](../figures/V27_versus_aws-l3-dev_month/QAS_M_month_9.png)
![QAS_M](../figures/V27_versus_aws-l3-dev_month/QAS_M_month_10.png)
![QAS_M](../figures/V27_versus_aws-l3-dev_month/QAS_M_month_11.png)
![QAS_M](../figures/V27_versus_aws-l3-dev_month/QAS_M_month_12.png)
 
## <a id='s1-32' />QAS_U
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![QAS_U](../figures/V27_versus_aws-l3-dev_month/QAS_U_month_0.png)
![QAS_U](../figures/V27_versus_aws-l3-dev_month/QAS_U_month_1.png)
![QAS_U](../figures/V27_versus_aws-l3-dev_month/QAS_U_month_2.png)
![QAS_U](../figures/V27_versus_aws-l3-dev_month/QAS_U_month_3.png)
![QAS_U](../figures/V27_versus_aws-l3-dev_month/QAS_U_month_4.png)
![QAS_U](../figures/V27_versus_aws-l3-dev_month/QAS_U_month_5.png)
![QAS_U](../figures/V27_versus_aws-l3-dev_month/QAS_U_month_6.png)
![QAS_U](../figures/V27_versus_aws-l3-dev_month/QAS_U_month_7.png)
![QAS_U](../figures/V27_versus_aws-l3-dev_month/QAS_U_month_8.png)
![QAS_U](../figures/V27_versus_aws-l3-dev_month/QAS_U_month_9.png)
![QAS_U](../figures/V27_versus_aws-l3-dev_month/QAS_U_month_10.png)
![QAS_U](../figures/V27_versus_aws-l3-dev_month/QAS_U_month_11.png)
![QAS_U](../figures/V27_versus_aws-l3-dev_month/QAS_U_month_12.png)
 
## <a id='s1-33' />RED_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![RED_L](../figures/V27_versus_aws-l3-dev_month/RED_L_month_0.png)
![RED_L](../figures/V27_versus_aws-l3-dev_month/RED_L_month_1.png)
![RED_L](../figures/V27_versus_aws-l3-dev_month/RED_L_month_2.png)
![RED_L](../figures/V27_versus_aws-l3-dev_month/RED_L_month_3.png)
![RED_L](../figures/V27_versus_aws-l3-dev_month/RED_L_month_4.png)
![RED_L](../figures/V27_versus_aws-l3-dev_month/RED_L_month_5.png)
![RED_L](../figures/V27_versus_aws-l3-dev_month/RED_L_month_6.png)
![RED_L](../figures/V27_versus_aws-l3-dev_month/RED_L_month_7.png)
![RED_L](../figures/V27_versus_aws-l3-dev_month/RED_L_month_8.png)
![RED_L](../figures/V27_versus_aws-l3-dev_month/RED_L_month_9.png)
![RED_L](../figures/V27_versus_aws-l3-dev_month/RED_L_month_10.png)
![RED_L](../figures/V27_versus_aws-l3-dev_month/RED_L_month_11.png)
![RED_L](../figures/V27_versus_aws-l3-dev_month/RED_L_month_12.png)
 
## <a id='s1-34' />SCO_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![SCO_L](../figures/V27_versus_aws-l3-dev_month/SCO_L_month_0.png)
![SCO_L](../figures/V27_versus_aws-l3-dev_month/SCO_L_month_1.png)
![SCO_L](../figures/V27_versus_aws-l3-dev_month/SCO_L_month_2.png)
![SCO_L](../figures/V27_versus_aws-l3-dev_month/SCO_L_month_3.png)
![SCO_L](../figures/V27_versus_aws-l3-dev_month/SCO_L_month_4.png)
![SCO_L](../figures/V27_versus_aws-l3-dev_month/SCO_L_month_5.png)
![SCO_L](../figures/V27_versus_aws-l3-dev_month/SCO_L_month_6.png)
![SCO_L](../figures/V27_versus_aws-l3-dev_month/SCO_L_month_7.png)
![SCO_L](../figures/V27_versus_aws-l3-dev_month/SCO_L_month_8.png)
![SCO_L](../figures/V27_versus_aws-l3-dev_month/SCO_L_month_9.png)
![SCO_L](../figures/V27_versus_aws-l3-dev_month/SCO_L_month_10.png)
![SCO_L](../figures/V27_versus_aws-l3-dev_month/SCO_L_month_11.png)
![SCO_L](../figures/V27_versus_aws-l3-dev_month/SCO_L_month_12.png)
 
## <a id='s1-35' />SCO_U
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![SCO_U](../figures/V27_versus_aws-l3-dev_month/SCO_U_month_0.png)
![SCO_U](../figures/V27_versus_aws-l3-dev_month/SCO_U_month_1.png)
![SCO_U](../figures/V27_versus_aws-l3-dev_month/SCO_U_month_2.png)
![SCO_U](../figures/V27_versus_aws-l3-dev_month/SCO_U_month_3.png)
![SCO_U](../figures/V27_versus_aws-l3-dev_month/SCO_U_month_4.png)
![SCO_U](../figures/V27_versus_aws-l3-dev_month/SCO_U_month_5.png)
![SCO_U](../figures/V27_versus_aws-l3-dev_month/SCO_U_month_6.png)
![SCO_U](../figures/V27_versus_aws-l3-dev_month/SCO_U_month_7.png)
![SCO_U](../figures/V27_versus_aws-l3-dev_month/SCO_U_month_8.png)
![SCO_U](../figures/V27_versus_aws-l3-dev_month/SCO_U_month_9.png)
![SCO_U](../figures/V27_versus_aws-l3-dev_month/SCO_U_month_10.png)
![SCO_U](../figures/V27_versus_aws-l3-dev_month/SCO_U_month_11.png)
![SCO_U](../figures/V27_versus_aws-l3-dev_month/SCO_U_month_12.png)
 
## <a id='s1-36' />SDL
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![SDL](../figures/V27_versus_aws-l3-dev_month/SDL_month_0.png)
![SDL](../figures/V27_versus_aws-l3-dev_month/SDL_month_1.png)
![SDL](../figures/V27_versus_aws-l3-dev_month/SDL_month_2.png)
![SDL](../figures/V27_versus_aws-l3-dev_month/SDL_month_3.png)
![SDL](../figures/V27_versus_aws-l3-dev_month/SDL_month_4.png)
![SDL](../figures/V27_versus_aws-l3-dev_month/SDL_month_5.png)
![SDL](../figures/V27_versus_aws-l3-dev_month/SDL_month_6.png)
![SDL](../figures/V27_versus_aws-l3-dev_month/SDL_month_7.png)
![SDL](../figures/V27_versus_aws-l3-dev_month/SDL_month_8.png)
![SDL](../figures/V27_versus_aws-l3-dev_month/SDL_month_9.png)
![SDL](../figures/V27_versus_aws-l3-dev_month/SDL_month_10.png)
![SDL](../figures/V27_versus_aws-l3-dev_month/SDL_month_11.png)
![SDL](../figures/V27_versus_aws-l3-dev_month/SDL_month_12.png)
![SDL](../figures/V27_versus_aws-l3-dev_month/SDL_month_13.png)
![SDL](../figures/V27_versus_aws-l3-dev_month/SDL_month_14.png)
![SDL](../figures/V27_versus_aws-l3-dev_month/SDL_month_15.png)
 
## <a id='s1-37' />SDM
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![SDM](../figures/V27_versus_aws-l3-dev_month/SDM_month_0.png)
![SDM](../figures/V27_versus_aws-l3-dev_month/SDM_month_1.png)
![SDM](../figures/V27_versus_aws-l3-dev_month/SDM_month_2.png)
![SDM](../figures/V27_versus_aws-l3-dev_month/SDM_month_3.png)
![SDM](../figures/V27_versus_aws-l3-dev_month/SDM_month_4.png)
![SDM](../figures/V27_versus_aws-l3-dev_month/SDM_month_5.png)
![SDM](../figures/V27_versus_aws-l3-dev_month/SDM_month_6.png)
![SDM](../figures/V27_versus_aws-l3-dev_month/SDM_month_7.png)
![SDM](../figures/V27_versus_aws-l3-dev_month/SDM_month_8.png)
![SDM](../figures/V27_versus_aws-l3-dev_month/SDM_month_9.png)
![SDM](../figures/V27_versus_aws-l3-dev_month/SDM_month_10.png)
![SDM](../figures/V27_versus_aws-l3-dev_month/SDM_month_11.png)
![SDM](../figures/V27_versus_aws-l3-dev_month/SDM_month_12.png)
![SDM](../figures/V27_versus_aws-l3-dev_month/SDM_month_13.png)
![SDM](../figures/V27_versus_aws-l3-dev_month/SDM_month_14.png)
![SDM](../figures/V27_versus_aws-l3-dev_month/SDM_month_15.png)
 
## <a id='s1-38' />SER_B
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, usr, albedo, dlr, ulr, t_surf, z_boom_u, z_boom_cor_u, z_stake_cor, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, t_i_2, t_i_4, t_i_6, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u, t_i_2, t_i_4, t_i_6, t_i_8

Old variables removed from new files:
z_stake, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_3, t_i_5, t_i_7
 
![SER_B](../figures/V27_versus_aws-l3-dev_month/SER_B_month_0.png)
![SER_B](../figures/V27_versus_aws-l3-dev_month/SER_B_month_1.png)
![SER_B](../figures/V27_versus_aws-l3-dev_month/SER_B_month_2.png)
![SER_B](../figures/V27_versus_aws-l3-dev_month/SER_B_month_3.png)
![SER_B](../figures/V27_versus_aws-l3-dev_month/SER_B_month_4.png)
![SER_B](../figures/V27_versus_aws-l3-dev_month/SER_B_month_5.png)
![SER_B](../figures/V27_versus_aws-l3-dev_month/SER_B_month_6.png)
![SER_B](../figures/V27_versus_aws-l3-dev_month/SER_B_month_7.png)
![SER_B](../figures/V27_versus_aws-l3-dev_month/SER_B_month_8.png)
 
## <a id='s1-39' />SWC
Variables in new file:
p_u, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_boom_cor_l, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
z_boom_l, precip_u, precip_u_cor, precip_u_rate
 
![SWC](../figures/V27_versus_aws-l3-dev_month/SWC_month_0.png)
![SWC](../figures/V27_versus_aws-l3-dev_month/SWC_month_1.png)
![SWC](../figures/V27_versus_aws-l3-dev_month/SWC_month_2.png)
![SWC](../figures/V27_versus_aws-l3-dev_month/SWC_month_3.png)
![SWC](../figures/V27_versus_aws-l3-dev_month/SWC_month_4.png)
![SWC](../figures/V27_versus_aws-l3-dev_month/SWC_month_5.png)
![SWC](../figures/V27_versus_aws-l3-dev_month/SWC_month_6.png)
![SWC](../figures/V27_versus_aws-l3-dev_month/SWC_month_7.png)
![SWC](../figures/V27_versus_aws-l3-dev_month/SWC_month_8.png)
![SWC](../figures/V27_versus_aws-l3-dev_month/SWC_month_9.png)
![SWC](../figures/V27_versus_aws-l3-dev_month/SWC_month_10.png)
![SWC](../figures/V27_versus_aws-l3-dev_month/SWC_month_11.png)
![SWC](../figures/V27_versus_aws-l3-dev_month/SWC_month_12.png)
![SWC](../figures/V27_versus_aws-l3-dev_month/SWC_month_13.png)
![SWC](../figures/V27_versus_aws-l3-dev_month/SWC_month_14.png)
![SWC](../figures/V27_versus_aws-l3-dev_month/SWC_month_15.png)
 
## <a id='s1-40' />TAS_A
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![TAS_A](../figures/V27_versus_aws-l3-dev_month/TAS_A_month_0.png)
![TAS_A](../figures/V27_versus_aws-l3-dev_month/TAS_A_month_1.png)
![TAS_A](../figures/V27_versus_aws-l3-dev_month/TAS_A_month_2.png)
![TAS_A](../figures/V27_versus_aws-l3-dev_month/TAS_A_month_3.png)
![TAS_A](../figures/V27_versus_aws-l3-dev_month/TAS_A_month_4.png)
![TAS_A](../figures/V27_versus_aws-l3-dev_month/TAS_A_month_5.png)
![TAS_A](../figures/V27_versus_aws-l3-dev_month/TAS_A_month_6.png)
![TAS_A](../figures/V27_versus_aws-l3-dev_month/TAS_A_month_7.png)
![TAS_A](../figures/V27_versus_aws-l3-dev_month/TAS_A_month_8.png)
![TAS_A](../figures/V27_versus_aws-l3-dev_month/TAS_A_month_9.png)
![TAS_A](../figures/V27_versus_aws-l3-dev_month/TAS_A_month_10.png)
![TAS_A](../figures/V27_versus_aws-l3-dev_month/TAS_A_month_11.png)
![TAS_A](../figures/V27_versus_aws-l3-dev_month/TAS_A_month_12.png)
 
## <a id='s1-41' />TAS_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![TAS_L](../figures/V27_versus_aws-l3-dev_month/TAS_L_month_0.png)
![TAS_L](../figures/V27_versus_aws-l3-dev_month/TAS_L_month_1.png)
![TAS_L](../figures/V27_versus_aws-l3-dev_month/TAS_L_month_2.png)
![TAS_L](../figures/V27_versus_aws-l3-dev_month/TAS_L_month_3.png)
![TAS_L](../figures/V27_versus_aws-l3-dev_month/TAS_L_month_4.png)
![TAS_L](../figures/V27_versus_aws-l3-dev_month/TAS_L_month_5.png)
![TAS_L](../figures/V27_versus_aws-l3-dev_month/TAS_L_month_6.png)
![TAS_L](../figures/V27_versus_aws-l3-dev_month/TAS_L_month_7.png)
![TAS_L](../figures/V27_versus_aws-l3-dev_month/TAS_L_month_8.png)
![TAS_L](../figures/V27_versus_aws-l3-dev_month/TAS_L_month_9.png)
![TAS_L](../figures/V27_versus_aws-l3-dev_month/TAS_L_month_10.png)
![TAS_L](../figures/V27_versus_aws-l3-dev_month/TAS_L_month_11.png)
 
## <a id='s1-42' />TAS_U
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![TAS_U](../figures/V27_versus_aws-l3-dev_month/TAS_U_month_0.png)
![TAS_U](../figures/V27_versus_aws-l3-dev_month/TAS_U_month_1.png)
![TAS_U](../figures/V27_versus_aws-l3-dev_month/TAS_U_month_2.png)
![TAS_U](../figures/V27_versus_aws-l3-dev_month/TAS_U_month_3.png)
![TAS_U](../figures/V27_versus_aws-l3-dev_month/TAS_U_month_4.png)
![TAS_U](../figures/V27_versus_aws-l3-dev_month/TAS_U_month_5.png)
![TAS_U](../figures/V27_versus_aws-l3-dev_month/TAS_U_month_6.png)
![TAS_U](../figures/V27_versus_aws-l3-dev_month/TAS_U_month_7.png)
![TAS_U](../figures/V27_versus_aws-l3-dev_month/TAS_U_month_8.png)
![TAS_U](../figures/V27_versus_aws-l3-dev_month/TAS_U_month_9.png)
![TAS_U](../figures/V27_versus_aws-l3-dev_month/TAS_U_month_10.png)
![TAS_U](../figures/V27_versus_aws-l3-dev_month/TAS_U_month_11.png)
 
## <a id='s1-43' />THU_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![THU_L](../figures/V27_versus_aws-l3-dev_month/THU_L_month_0.png)
![THU_L](../figures/V27_versus_aws-l3-dev_month/THU_L_month_1.png)
![THU_L](../figures/V27_versus_aws-l3-dev_month/THU_L_month_2.png)
![THU_L](../figures/V27_versus_aws-l3-dev_month/THU_L_month_3.png)
![THU_L](../figures/V27_versus_aws-l3-dev_month/THU_L_month_4.png)
![THU_L](../figures/V27_versus_aws-l3-dev_month/THU_L_month_5.png)
![THU_L](../figures/V27_versus_aws-l3-dev_month/THU_L_month_6.png)
![THU_L](../figures/V27_versus_aws-l3-dev_month/THU_L_month_7.png)
![THU_L](../figures/V27_versus_aws-l3-dev_month/THU_L_month_8.png)
![THU_L](../figures/V27_versus_aws-l3-dev_month/THU_L_month_9.png)
![THU_L](../figures/V27_versus_aws-l3-dev_month/THU_L_month_10.png)
![THU_L](../figures/V27_versus_aws-l3-dev_month/THU_L_month_11.png)
 
## <a id='s1-44' />THU_L2
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, rh_i_wrt_ice_or_water, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:
t_i, wdir_i
 
![THU_L2](../figures/V27_versus_aws-l3-dev_month/THU_L2_month_0.png)
![THU_L2](../figures/V27_versus_aws-l3-dev_month/THU_L2_month_1.png)
![THU_L2](../figures/V27_versus_aws-l3-dev_month/THU_L2_month_2.png)
![THU_L2](../figures/V27_versus_aws-l3-dev_month/THU_L2_month_3.png)
![THU_L2](../figures/V27_versus_aws-l3-dev_month/THU_L2_month_4.png)
![THU_L2](../figures/V27_versus_aws-l3-dev_month/THU_L2_month_5.png)
![THU_L2](../figures/V27_versus_aws-l3-dev_month/THU_L2_month_6.png)
![THU_L2](../figures/V27_versus_aws-l3-dev_month/THU_L2_month_7.png)
![THU_L2](../figures/V27_versus_aws-l3-dev_month/THU_L2_month_8.png)
![THU_L2](../figures/V27_versus_aws-l3-dev_month/THU_L2_month_9.png)
![THU_L2](../figures/V27_versus_aws-l3-dev_month/THU_L2_month_10.png)
![THU_L2](../figures/V27_versus_aws-l3-dev_month/THU_L2_month_11.png)
 
## <a id='s1-45' />THU_U
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![THU_U](../figures/V27_versus_aws-l3-dev_month/THU_U_month_0.png)
![THU_U](../figures/V27_versus_aws-l3-dev_month/THU_U_month_1.png)
![THU_U](../figures/V27_versus_aws-l3-dev_month/THU_U_month_2.png)
![THU_U](../figures/V27_versus_aws-l3-dev_month/THU_U_month_3.png)
![THU_U](../figures/V27_versus_aws-l3-dev_month/THU_U_month_4.png)
![THU_U](../figures/V27_versus_aws-l3-dev_month/THU_U_month_5.png)
![THU_U](../figures/V27_versus_aws-l3-dev_month/THU_U_month_6.png)
![THU_U](../figures/V27_versus_aws-l3-dev_month/THU_U_month_7.png)
![THU_U](../figures/V27_versus_aws-l3-dev_month/THU_U_month_8.png)
![THU_U](../figures/V27_versus_aws-l3-dev_month/THU_U_month_9.png)
![THU_U](../figures/V27_versus_aws-l3-dev_month/THU_U_month_10.png)
![THU_U](../figures/V27_versus_aws-l3-dev_month/THU_U_month_11.png)
![THU_U](../figures/V27_versus_aws-l3-dev_month/THU_U_month_12.png)
 
## <a id='s1-46' />TUN
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![TUN](../figures/V27_versus_aws-l3-dev_month/TUN_month_0.png)
![TUN](../figures/V27_versus_aws-l3-dev_month/TUN_month_1.png)
![TUN](../figures/V27_versus_aws-l3-dev_month/TUN_month_2.png)
![TUN](../figures/V27_versus_aws-l3-dev_month/TUN_month_3.png)
![TUN](../figures/V27_versus_aws-l3-dev_month/TUN_month_4.png)
![TUN](../figures/V27_versus_aws-l3-dev_month/TUN_month_5.png)
![TUN](../figures/V27_versus_aws-l3-dev_month/TUN_month_6.png)
![TUN](../figures/V27_versus_aws-l3-dev_month/TUN_month_7.png)
![TUN](../figures/V27_versus_aws-l3-dev_month/TUN_month_8.png)
![TUN](../figures/V27_versus_aws-l3-dev_month/TUN_month_9.png)
![TUN](../figures/V27_versus_aws-l3-dev_month/TUN_month_10.png)
![TUN](../figures/V27_versus_aws-l3-dev_month/TUN_month_11.png)
![TUN](../figures/V27_versus_aws-l3-dev_month/TUN_month_12.png)
![TUN](../figures/V27_versus_aws-l3-dev_month/TUN_month_13.png)
![TUN](../figures/V27_versus_aws-l3-dev_month/TUN_month_14.png)
![TUN](../figures/V27_versus_aws-l3-dev_month/TUN_month_15.png)
 
## <a id='s1-47' />UPE_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![UPE_L](../figures/V27_versus_aws-l3-dev_month/UPE_L_month_0.png)
![UPE_L](../figures/V27_versus_aws-l3-dev_month/UPE_L_month_1.png)
![UPE_L](../figures/V27_versus_aws-l3-dev_month/UPE_L_month_2.png)
![UPE_L](../figures/V27_versus_aws-l3-dev_month/UPE_L_month_3.png)
![UPE_L](../figures/V27_versus_aws-l3-dev_month/UPE_L_month_4.png)
![UPE_L](../figures/V27_versus_aws-l3-dev_month/UPE_L_month_5.png)
![UPE_L](../figures/V27_versus_aws-l3-dev_month/UPE_L_month_6.png)
![UPE_L](../figures/V27_versus_aws-l3-dev_month/UPE_L_month_7.png)
![UPE_L](../figures/V27_versus_aws-l3-dev_month/UPE_L_month_8.png)
![UPE_L](../figures/V27_versus_aws-l3-dev_month/UPE_L_month_9.png)
![UPE_L](../figures/V27_versus_aws-l3-dev_month/UPE_L_month_10.png)
![UPE_L](../figures/V27_versus_aws-l3-dev_month/UPE_L_month_11.png)
 
## <a id='s1-48' />UPE_U
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![UPE_U](../figures/V27_versus_aws-l3-dev_month/UPE_U_month_0.png)
![UPE_U](../figures/V27_versus_aws-l3-dev_month/UPE_U_month_1.png)
![UPE_U](../figures/V27_versus_aws-l3-dev_month/UPE_U_month_2.png)
![UPE_U](../figures/V27_versus_aws-l3-dev_month/UPE_U_month_3.png)
![UPE_U](../figures/V27_versus_aws-l3-dev_month/UPE_U_month_4.png)
![UPE_U](../figures/V27_versus_aws-l3-dev_month/UPE_U_month_5.png)
![UPE_U](../figures/V27_versus_aws-l3-dev_month/UPE_U_month_6.png)
![UPE_U](../figures/V27_versus_aws-l3-dev_month/UPE_U_month_7.png)
![UPE_U](../figures/V27_versus_aws-l3-dev_month/UPE_U_month_8.png)
![UPE_U](../figures/V27_versus_aws-l3-dev_month/UPE_U_month_9.png)
![UPE_U](../figures/V27_versus_aws-l3-dev_month/UPE_U_month_10.png)
![UPE_U](../figures/V27_versus_aws-l3-dev_month/UPE_U_month_11.png)
 
## <a id='s1-49' />UWN
## <a id='s1-50' />WEG_B
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, usr, albedo, dlr, ulr, t_surf, z_boom_u, z_boom_cor_u, z_stake_cor, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u, t_i_2, t_i_4, t_i_6, t_i_8

Old variables removed from new files:
z_stake, precip_u, precip_u_cor, precip_u_rate, t_i_1
 
![WEG_B](../figures/V27_versus_aws-l3-dev_month/WEG_B_month_0.png)
![WEG_B](../figures/V27_versus_aws-l3-dev_month/WEG_B_month_1.png)
![WEG_B](../figures/V27_versus_aws-l3-dev_month/WEG_B_month_2.png)
![WEG_B](../figures/V27_versus_aws-l3-dev_month/WEG_B_month_3.png)
![WEG_B](../figures/V27_versus_aws-l3-dev_month/WEG_B_month_4.png)
![WEG_B](../figures/V27_versus_aws-l3-dev_month/WEG_B_month_5.png)
![WEG_B](../figures/V27_versus_aws-l3-dev_month/WEG_B_month_6.png)
![WEG_B](../figures/V27_versus_aws-l3-dev_month/WEG_B_month_7.png)
![WEG_B](../figures/V27_versus_aws-l3-dev_month/WEG_B_month_8.png)
 
## <a id='s1-51' />WEG_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![WEG_L](../figures/V27_versus_aws-l3-dev_month/WEG_L_month_0.png)
![WEG_L](../figures/V27_versus_aws-l3-dev_month/WEG_L_month_1.png)
![WEG_L](../figures/V27_versus_aws-l3-dev_month/WEG_L_month_2.png)
![WEG_L](../figures/V27_versus_aws-l3-dev_month/WEG_L_month_3.png)
![WEG_L](../figures/V27_versus_aws-l3-dev_month/WEG_L_month_4.png)
![WEG_L](../figures/V27_versus_aws-l3-dev_month/WEG_L_month_5.png)
![WEG_L](../figures/V27_versus_aws-l3-dev_month/WEG_L_month_6.png)
![WEG_L](../figures/V27_versus_aws-l3-dev_month/WEG_L_month_7.png)
![WEG_L](../figures/V27_versus_aws-l3-dev_month/WEG_L_month_8.png)
![WEG_L](../figures/V27_versus_aws-l3-dev_month/WEG_L_month_9.png)
![WEG_L](../figures/V27_versus_aws-l3-dev_month/WEG_L_month_10.png)
![WEG_L](../figures/V27_versus_aws-l3-dev_month/WEG_L_month_11.png)
![WEG_L](../figures/V27_versus_aws-l3-dev_month/WEG_L_month_12.png)
 
## <a id='s1-52' />ZAC_A
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![ZAC_A](../figures/V27_versus_aws-l3-dev_month/ZAC_A_month_0.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev_month/ZAC_A_month_1.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev_month/ZAC_A_month_2.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev_month/ZAC_A_month_3.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev_month/ZAC_A_month_4.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev_month/ZAC_A_month_5.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev_month/ZAC_A_month_6.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev_month/ZAC_A_month_7.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev_month/ZAC_A_month_8.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev_month/ZAC_A_month_9.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev_month/ZAC_A_month_10.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev_month/ZAC_A_month_11.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev_month/ZAC_A_month_12.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev_month/ZAC_A_month_13.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev_month/ZAC_A_month_14.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev_month/ZAC_A_month_15.png)
 
## <a id='s1-53' />ZAC_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![ZAC_L](../figures/V27_versus_aws-l3-dev_month/ZAC_L_month_0.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev_month/ZAC_L_month_1.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev_month/ZAC_L_month_2.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev_month/ZAC_L_month_3.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev_month/ZAC_L_month_4.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev_month/ZAC_L_month_5.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev_month/ZAC_L_month_6.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev_month/ZAC_L_month_7.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev_month/ZAC_L_month_8.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev_month/ZAC_L_month_9.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev_month/ZAC_L_month_10.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev_month/ZAC_L_month_11.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev_month/ZAC_L_month_12.png)
 
## <a id='s1-54' />ZAC_U
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, t_i, rh_i_wrt_ice_or_water, wdir_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![ZAC_U](../figures/V27_versus_aws-l3-dev_month/ZAC_U_month_0.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev_month/ZAC_U_month_1.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev_month/ZAC_U_month_2.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev_month/ZAC_U_month_3.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev_month/ZAC_U_month_4.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev_month/ZAC_U_month_5.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev_month/ZAC_U_month_6.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev_month/ZAC_U_month_7.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev_month/ZAC_U_month_8.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev_month/ZAC_U_month_9.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev_month/ZAC_U_month_10.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev_month/ZAC_U_month_11.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev_month/ZAC_U_month_12.png)
 
