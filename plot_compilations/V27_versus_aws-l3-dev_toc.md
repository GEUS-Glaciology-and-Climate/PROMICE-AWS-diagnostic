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
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_stake, z_stake_cor, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, z_stake_cor, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![CEN](../figures/V27_versus_aws-l3-dev/CEN_0.png)
![CEN](../figures/V27_versus_aws-l3-dev/CEN_1.png)
![CEN](../figures/V27_versus_aws-l3-dev/CEN_2.png)
![CEN](../figures/V27_versus_aws-l3-dev/CEN_3.png)
![CEN](../figures/V27_versus_aws-l3-dev/CEN_4.png)
![CEN](../figures/V27_versus_aws-l3-dev/CEN_5.png)
![CEN](../figures/V27_versus_aws-l3-dev/CEN_6.png)
![CEN](../figures/V27_versus_aws-l3-dev/CEN_7.png)
![CEN](../figures/V27_versus_aws-l3-dev/CEN_8.png)
![CEN](../figures/V27_versus_aws-l3-dev/CEN_9.png)
![CEN](../figures/V27_versus_aws-l3-dev/CEN_10.png)
![CEN](../figures/V27_versus_aws-l3-dev/CEN_11.png)
![CEN](../figures/V27_versus_aws-l3-dev/CEN_12.png)
![CEN](../figures/V27_versus_aws-l3-dev/CEN_13.png)
![CEN](../figures/V27_versus_aws-l3-dev/CEN_14.png)
![CEN](../figures/V27_versus_aws-l3-dev/CEN_15.png)
![CEN](../figures/V27_versus_aws-l3-dev/CEN_16.png)
 
## <a id='s1-2' />CP1
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![CP1](../figures/V27_versus_aws-l3-dev/CP1_0.png)
![CP1](../figures/V27_versus_aws-l3-dev/CP1_1.png)
![CP1](../figures/V27_versus_aws-l3-dev/CP1_2.png)
![CP1](../figures/V27_versus_aws-l3-dev/CP1_3.png)
![CP1](../figures/V27_versus_aws-l3-dev/CP1_4.png)
![CP1](../figures/V27_versus_aws-l3-dev/CP1_5.png)
![CP1](../figures/V27_versus_aws-l3-dev/CP1_6.png)
![CP1](../figures/V27_versus_aws-l3-dev/CP1_7.png)
![CP1](../figures/V27_versus_aws-l3-dev/CP1_8.png)
![CP1](../figures/V27_versus_aws-l3-dev/CP1_9.png)
![CP1](../figures/V27_versus_aws-l3-dev/CP1_10.png)
![CP1](../figures/V27_versus_aws-l3-dev/CP1_11.png)
![CP1](../figures/V27_versus_aws-l3-dev/CP1_12.png)
![CP1](../figures/V27_versus_aws-l3-dev/CP1_13.png)
![CP1](../figures/V27_versus_aws-l3-dev/CP1_14.png)
![CP1](../figures/V27_versus_aws-l3-dev/CP1_15.png)
![CP1](../figures/V27_versus_aws-l3-dev/CP1_16.png)
 
## <a id='s1-3' />DY2
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![DY2](../figures/V27_versus_aws-l3-dev/DY2_0.png)
![DY2](../figures/V27_versus_aws-l3-dev/DY2_1.png)
![DY2](../figures/V27_versus_aws-l3-dev/DY2_2.png)
![DY2](../figures/V27_versus_aws-l3-dev/DY2_3.png)
![DY2](../figures/V27_versus_aws-l3-dev/DY2_4.png)
![DY2](../figures/V27_versus_aws-l3-dev/DY2_5.png)
![DY2](../figures/V27_versus_aws-l3-dev/DY2_6.png)
![DY2](../figures/V27_versus_aws-l3-dev/DY2_7.png)
![DY2](../figures/V27_versus_aws-l3-dev/DY2_8.png)
![DY2](../figures/V27_versus_aws-l3-dev/DY2_9.png)
![DY2](../figures/V27_versus_aws-l3-dev/DY2_10.png)
![DY2](../figures/V27_versus_aws-l3-dev/DY2_11.png)
![DY2](../figures/V27_versus_aws-l3-dev/DY2_12.png)
![DY2](../figures/V27_versus_aws-l3-dev/DY2_13.png)
![DY2](../figures/V27_versus_aws-l3-dev/DY2_14.png)
![DY2](../figures/V27_versus_aws-l3-dev/DY2_15.png)
![DY2](../figures/V27_versus_aws-l3-dev/DY2_16.png)
 
## <a id='s1-4' />EGP
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_stake, z_stake_cor, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
p_l, z_boom_cor_u, z_boom_cor_l, z_stake_cor, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![EGP](../figures/V27_versus_aws-l3-dev/EGP_0.png)
![EGP](../figures/V27_versus_aws-l3-dev/EGP_1.png)
![EGP](../figures/V27_versus_aws-l3-dev/EGP_2.png)
![EGP](../figures/V27_versus_aws-l3-dev/EGP_3.png)
![EGP](../figures/V27_versus_aws-l3-dev/EGP_4.png)
![EGP](../figures/V27_versus_aws-l3-dev/EGP_5.png)
![EGP](../figures/V27_versus_aws-l3-dev/EGP_6.png)
![EGP](../figures/V27_versus_aws-l3-dev/EGP_7.png)
![EGP](../figures/V27_versus_aws-l3-dev/EGP_8.png)
![EGP](../figures/V27_versus_aws-l3-dev/EGP_9.png)
![EGP](../figures/V27_versus_aws-l3-dev/EGP_10.png)
![EGP](../figures/V27_versus_aws-l3-dev/EGP_11.png)
![EGP](../figures/V27_versus_aws-l3-dev/EGP_12.png)
![EGP](../figures/V27_versus_aws-l3-dev/EGP_13.png)
![EGP](../figures/V27_versus_aws-l3-dev/EGP_14.png)
![EGP](../figures/V27_versus_aws-l3-dev/EGP_15.png)
![EGP](../figures/V27_versus_aws-l3-dev/EGP_16.png)
 
## <a id='s1-5' />FRE
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![FRE](../figures/V27_versus_aws-l3-dev/FRE_0.png)
![FRE](../figures/V27_versus_aws-l3-dev/FRE_1.png)
![FRE](../figures/V27_versus_aws-l3-dev/FRE_2.png)
![FRE](../figures/V27_versus_aws-l3-dev/FRE_3.png)
![FRE](../figures/V27_versus_aws-l3-dev/FRE_4.png)
![FRE](../figures/V27_versus_aws-l3-dev/FRE_5.png)
![FRE](../figures/V27_versus_aws-l3-dev/FRE_6.png)
![FRE](../figures/V27_versus_aws-l3-dev/FRE_7.png)
![FRE](../figures/V27_versus_aws-l3-dev/FRE_8.png)
![FRE](../figures/V27_versus_aws-l3-dev/FRE_9.png)
![FRE](../figures/V27_versus_aws-l3-dev/FRE_10.png)
![FRE](../figures/V27_versus_aws-l3-dev/FRE_11.png)
![FRE](../figures/V27_versus_aws-l3-dev/FRE_12.png)
 
## <a id='s1-6' />HUM
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![HUM](../figures/V27_versus_aws-l3-dev/HUM_0.png)
![HUM](../figures/V27_versus_aws-l3-dev/HUM_1.png)
![HUM](../figures/V27_versus_aws-l3-dev/HUM_2.png)
![HUM](../figures/V27_versus_aws-l3-dev/HUM_3.png)
![HUM](../figures/V27_versus_aws-l3-dev/HUM_4.png)
![HUM](../figures/V27_versus_aws-l3-dev/HUM_5.png)
![HUM](../figures/V27_versus_aws-l3-dev/HUM_6.png)
![HUM](../figures/V27_versus_aws-l3-dev/HUM_7.png)
![HUM](../figures/V27_versus_aws-l3-dev/HUM_8.png)
![HUM](../figures/V27_versus_aws-l3-dev/HUM_9.png)
![HUM](../figures/V27_versus_aws-l3-dev/HUM_10.png)
![HUM](../figures/V27_versus_aws-l3-dev/HUM_11.png)
![HUM](../figures/V27_versus_aws-l3-dev/HUM_12.png)
![HUM](../figures/V27_versus_aws-l3-dev/HUM_13.png)
![HUM](../figures/V27_versus_aws-l3-dev/HUM_14.png)
![HUM](../figures/V27_versus_aws-l3-dev/HUM_15.png)
![HUM](../figures/V27_versus_aws-l3-dev/HUM_16.png)
 
## <a id='s1-7' />JAR
Variables in new file:
p_u, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_boom_l, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![JAR](../figures/V27_versus_aws-l3-dev/JAR_0.png)
![JAR](../figures/V27_versus_aws-l3-dev/JAR_1.png)
![JAR](../figures/V27_versus_aws-l3-dev/JAR_2.png)
![JAR](../figures/V27_versus_aws-l3-dev/JAR_3.png)
![JAR](../figures/V27_versus_aws-l3-dev/JAR_4.png)
![JAR](../figures/V27_versus_aws-l3-dev/JAR_5.png)
![JAR](../figures/V27_versus_aws-l3-dev/JAR_6.png)
![JAR](../figures/V27_versus_aws-l3-dev/JAR_7.png)
![JAR](../figures/V27_versus_aws-l3-dev/JAR_8.png)
![JAR](../figures/V27_versus_aws-l3-dev/JAR_9.png)
![JAR](../figures/V27_versus_aws-l3-dev/JAR_10.png)
![JAR](../figures/V27_versus_aws-l3-dev/JAR_11.png)
![JAR](../figures/V27_versus_aws-l3-dev/JAR_12.png)
![JAR](../figures/V27_versus_aws-l3-dev/JAR_13.png)
![JAR](../figures/V27_versus_aws-l3-dev/JAR_14.png)
![JAR](../figures/V27_versus_aws-l3-dev/JAR_15.png)
 
## <a id='s1-8' />KAN_B
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, usr, albedo, dlr, ulr, t_surf, z_boom_u, z_boom_cor_u, z_stake_cor, z_surf_combined, snow_height, t_i_2, t_i_4, t_i_6, t_i_8, tilt_x, rot, gps_lon, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, t_i_2, t_i_4, t_i_6, t_i_8, rot, gps_lon

Old variables removed from new files:
dsr_cor, usr_cor, cc, z_stake, precip_u, t_i_1, t_i_3, t_i_5, t_i_7, tilt_y, gps_lat, gps_alt
 
![KAN_B](../figures/V27_versus_aws-l3-dev/KAN_B_0.png)
![KAN_B](../figures/V27_versus_aws-l3-dev/KAN_B_1.png)
![KAN_B](../figures/V27_versus_aws-l3-dev/KAN_B_2.png)
![KAN_B](../figures/V27_versus_aws-l3-dev/KAN_B_3.png)
![KAN_B](../figures/V27_versus_aws-l3-dev/KAN_B_4.png)
![KAN_B](../figures/V27_versus_aws-l3-dev/KAN_B_5.png)
![KAN_B](../figures/V27_versus_aws-l3-dev/KAN_B_6.png)
![KAN_B](../figures/V27_versus_aws-l3-dev/KAN_B_7.png)
 
## <a id='s1-9' />KAN_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![KAN_L](../figures/V27_versus_aws-l3-dev/KAN_L_0.png)
![KAN_L](../figures/V27_versus_aws-l3-dev/KAN_L_1.png)
![KAN_L](../figures/V27_versus_aws-l3-dev/KAN_L_2.png)
![KAN_L](../figures/V27_versus_aws-l3-dev/KAN_L_3.png)
![KAN_L](../figures/V27_versus_aws-l3-dev/KAN_L_4.png)
![KAN_L](../figures/V27_versus_aws-l3-dev/KAN_L_5.png)
![KAN_L](../figures/V27_versus_aws-l3-dev/KAN_L_6.png)
![KAN_L](../figures/V27_versus_aws-l3-dev/KAN_L_7.png)
![KAN_L](../figures/V27_versus_aws-l3-dev/KAN_L_8.png)
![KAN_L](../figures/V27_versus_aws-l3-dev/KAN_L_9.png)
![KAN_L](../figures/V27_versus_aws-l3-dev/KAN_L_10.png)
![KAN_L](../figures/V27_versus_aws-l3-dev/KAN_L_11.png)
![KAN_L](../figures/V27_versus_aws-l3-dev/KAN_L_12.png)
![KAN_L](../figures/V27_versus_aws-l3-dev/KAN_L_13.png)
 
## <a id='s1-10' />KAN_M
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![KAN_M](../figures/V27_versus_aws-l3-dev/KAN_M_0.png)
![KAN_M](../figures/V27_versus_aws-l3-dev/KAN_M_1.png)
![KAN_M](../figures/V27_versus_aws-l3-dev/KAN_M_2.png)
![KAN_M](../figures/V27_versus_aws-l3-dev/KAN_M_3.png)
![KAN_M](../figures/V27_versus_aws-l3-dev/KAN_M_4.png)
![KAN_M](../figures/V27_versus_aws-l3-dev/KAN_M_5.png)
![KAN_M](../figures/V27_versus_aws-l3-dev/KAN_M_6.png)
![KAN_M](../figures/V27_versus_aws-l3-dev/KAN_M_7.png)
![KAN_M](../figures/V27_versus_aws-l3-dev/KAN_M_8.png)
![KAN_M](../figures/V27_versus_aws-l3-dev/KAN_M_9.png)
![KAN_M](../figures/V27_versus_aws-l3-dev/KAN_M_10.png)
![KAN_M](../figures/V27_versus_aws-l3-dev/KAN_M_11.png)
![KAN_M](../figures/V27_versus_aws-l3-dev/KAN_M_12.png)
 
## <a id='s1-11' />KAN_T
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![KAN_T](../figures/V27_versus_aws-l3-dev/KAN_T_0.png)
![KAN_T](../figures/V27_versus_aws-l3-dev/KAN_T_1.png)
![KAN_T](../figures/V27_versus_aws-l3-dev/KAN_T_2.png)
![KAN_T](../figures/V27_versus_aws-l3-dev/KAN_T_3.png)
![KAN_T](../figures/V27_versus_aws-l3-dev/KAN_T_4.png)
![KAN_T](../figures/V27_versus_aws-l3-dev/KAN_T_5.png)
![KAN_T](../figures/V27_versus_aws-l3-dev/KAN_T_6.png)
![KAN_T](../figures/V27_versus_aws-l3-dev/KAN_T_7.png)
![KAN_T](../figures/V27_versus_aws-l3-dev/KAN_T_8.png)
![KAN_T](../figures/V27_versus_aws-l3-dev/KAN_T_9.png)
![KAN_T](../figures/V27_versus_aws-l3-dev/KAN_T_10.png)
![KAN_T](../figures/V27_versus_aws-l3-dev/KAN_T_11.png)
![KAN_T](../figures/V27_versus_aws-l3-dev/KAN_T_12.png)
![KAN_T](../figures/V27_versus_aws-l3-dev/KAN_T_13.png)
 
## <a id='s1-12' />KAN_U
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_stake, z_stake_cor, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
qh_l, dlhf_l, dshf_l, z_boom_cor_u, z_boom_cor_l, z_stake_cor, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![KAN_U](../figures/V27_versus_aws-l3-dev/KAN_U_0.png)
![KAN_U](../figures/V27_versus_aws-l3-dev/KAN_U_1.png)
![KAN_U](../figures/V27_versus_aws-l3-dev/KAN_U_2.png)
![KAN_U](../figures/V27_versus_aws-l3-dev/KAN_U_3.png)
![KAN_U](../figures/V27_versus_aws-l3-dev/KAN_U_4.png)
![KAN_U](../figures/V27_versus_aws-l3-dev/KAN_U_5.png)
![KAN_U](../figures/V27_versus_aws-l3-dev/KAN_U_6.png)
![KAN_U](../figures/V27_versus_aws-l3-dev/KAN_U_7.png)
![KAN_U](../figures/V27_versus_aws-l3-dev/KAN_U_8.png)
![KAN_U](../figures/V27_versus_aws-l3-dev/KAN_U_9.png)
![KAN_U](../figures/V27_versus_aws-l3-dev/KAN_U_10.png)
![KAN_U](../figures/V27_versus_aws-l3-dev/KAN_U_11.png)
![KAN_U](../figures/V27_versus_aws-l3-dev/KAN_U_12.png)
![KAN_U](../figures/V27_versus_aws-l3-dev/KAN_U_13.png)
![KAN_U](../figures/V27_versus_aws-l3-dev/KAN_U_14.png)
![KAN_U](../figures/V27_versus_aws-l3-dev/KAN_U_15.png)
![KAN_U](../figures/V27_versus_aws-l3-dev/KAN_U_16.png)
 
## <a id='s1-13' />KPC_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![KPC_L](../figures/V27_versus_aws-l3-dev/KPC_L_0.png)
![KPC_L](../figures/V27_versus_aws-l3-dev/KPC_L_1.png)
![KPC_L](../figures/V27_versus_aws-l3-dev/KPC_L_2.png)
![KPC_L](../figures/V27_versus_aws-l3-dev/KPC_L_3.png)
![KPC_L](../figures/V27_versus_aws-l3-dev/KPC_L_4.png)
![KPC_L](../figures/V27_versus_aws-l3-dev/KPC_L_5.png)
![KPC_L](../figures/V27_versus_aws-l3-dev/KPC_L_6.png)
![KPC_L](../figures/V27_versus_aws-l3-dev/KPC_L_7.png)
![KPC_L](../figures/V27_versus_aws-l3-dev/KPC_L_8.png)
![KPC_L](../figures/V27_versus_aws-l3-dev/KPC_L_9.png)
![KPC_L](../figures/V27_versus_aws-l3-dev/KPC_L_10.png)
![KPC_L](../figures/V27_versus_aws-l3-dev/KPC_L_11.png)
![KPC_L](../figures/V27_versus_aws-l3-dev/KPC_L_12.png)
 
## <a id='s1-14' />KPC_U
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![KPC_U](../figures/V27_versus_aws-l3-dev/KPC_U_0.png)
![KPC_U](../figures/V27_versus_aws-l3-dev/KPC_U_1.png)
![KPC_U](../figures/V27_versus_aws-l3-dev/KPC_U_2.png)
![KPC_U](../figures/V27_versus_aws-l3-dev/KPC_U_3.png)
![KPC_U](../figures/V27_versus_aws-l3-dev/KPC_U_4.png)
![KPC_U](../figures/V27_versus_aws-l3-dev/KPC_U_5.png)
![KPC_U](../figures/V27_versus_aws-l3-dev/KPC_U_6.png)
![KPC_U](../figures/V27_versus_aws-l3-dev/KPC_U_7.png)
![KPC_U](../figures/V27_versus_aws-l3-dev/KPC_U_8.png)
![KPC_U](../figures/V27_versus_aws-l3-dev/KPC_U_9.png)
![KPC_U](../figures/V27_versus_aws-l3-dev/KPC_U_10.png)
![KPC_U](../figures/V27_versus_aws-l3-dev/KPC_U_11.png)
![KPC_U](../figures/V27_versus_aws-l3-dev/KPC_U_12.png)
 
## <a id='s1-15' />LYN_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![LYN_L](../figures/V27_versus_aws-l3-dev/LYN_L_0.png)
![LYN_L](../figures/V27_versus_aws-l3-dev/LYN_L_1.png)
![LYN_L](../figures/V27_versus_aws-l3-dev/LYN_L_2.png)
![LYN_L](../figures/V27_versus_aws-l3-dev/LYN_L_3.png)
![LYN_L](../figures/V27_versus_aws-l3-dev/LYN_L_4.png)
![LYN_L](../figures/V27_versus_aws-l3-dev/LYN_L_5.png)
![LYN_L](../figures/V27_versus_aws-l3-dev/LYN_L_6.png)
![LYN_L](../figures/V27_versus_aws-l3-dev/LYN_L_7.png)
![LYN_L](../figures/V27_versus_aws-l3-dev/LYN_L_8.png)
![LYN_L](../figures/V27_versus_aws-l3-dev/LYN_L_9.png)
![LYN_L](../figures/V27_versus_aws-l3-dev/LYN_L_10.png)
![LYN_L](../figures/V27_versus_aws-l3-dev/LYN_L_11.png)
![LYN_L](../figures/V27_versus_aws-l3-dev/LYN_L_12.png)
 
## <a id='s1-16' />LYN_T
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![LYN_T](../figures/V27_versus_aws-l3-dev/LYN_T_0.png)
![LYN_T](../figures/V27_versus_aws-l3-dev/LYN_T_1.png)
![LYN_T](../figures/V27_versus_aws-l3-dev/LYN_T_2.png)
![LYN_T](../figures/V27_versus_aws-l3-dev/LYN_T_3.png)
![LYN_T](../figures/V27_versus_aws-l3-dev/LYN_T_4.png)
![LYN_T](../figures/V27_versus_aws-l3-dev/LYN_T_5.png)
![LYN_T](../figures/V27_versus_aws-l3-dev/LYN_T_6.png)
![LYN_T](../figures/V27_versus_aws-l3-dev/LYN_T_7.png)
![LYN_T](../figures/V27_versus_aws-l3-dev/LYN_T_8.png)
![LYN_T](../figures/V27_versus_aws-l3-dev/LYN_T_9.png)
![LYN_T](../figures/V27_versus_aws-l3-dev/LYN_T_10.png)
![LYN_T](../figures/V27_versus_aws-l3-dev/LYN_T_11.png)
![LYN_T](../figures/V27_versus_aws-l3-dev/LYN_T_12.png)
 
## <a id='s1-17' />MIT
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![MIT](../figures/V27_versus_aws-l3-dev/MIT_0.png)
![MIT](../figures/V27_versus_aws-l3-dev/MIT_1.png)
![MIT](../figures/V27_versus_aws-l3-dev/MIT_2.png)
![MIT](../figures/V27_versus_aws-l3-dev/MIT_3.png)
![MIT](../figures/V27_versus_aws-l3-dev/MIT_4.png)
![MIT](../figures/V27_versus_aws-l3-dev/MIT_5.png)
![MIT](../figures/V27_versus_aws-l3-dev/MIT_6.png)
![MIT](../figures/V27_versus_aws-l3-dev/MIT_7.png)
![MIT](../figures/V27_versus_aws-l3-dev/MIT_8.png)
![MIT](../figures/V27_versus_aws-l3-dev/MIT_9.png)
![MIT](../figures/V27_versus_aws-l3-dev/MIT_10.png)
![MIT](../figures/V27_versus_aws-l3-dev/MIT_11.png)
![MIT](../figures/V27_versus_aws-l3-dev/MIT_12.png)
 
## <a id='s1-18' />NAE
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![NAE](../figures/V27_versus_aws-l3-dev/NAE_0.png)
![NAE](../figures/V27_versus_aws-l3-dev/NAE_1.png)
![NAE](../figures/V27_versus_aws-l3-dev/NAE_2.png)
![NAE](../figures/V27_versus_aws-l3-dev/NAE_3.png)
![NAE](../figures/V27_versus_aws-l3-dev/NAE_4.png)
![NAE](../figures/V27_versus_aws-l3-dev/NAE_5.png)
![NAE](../figures/V27_versus_aws-l3-dev/NAE_6.png)
![NAE](../figures/V27_versus_aws-l3-dev/NAE_7.png)
![NAE](../figures/V27_versus_aws-l3-dev/NAE_8.png)
![NAE](../figures/V27_versus_aws-l3-dev/NAE_9.png)
![NAE](../figures/V27_versus_aws-l3-dev/NAE_10.png)
![NAE](../figures/V27_versus_aws-l3-dev/NAE_11.png)
![NAE](../figures/V27_versus_aws-l3-dev/NAE_12.png)
![NAE](../figures/V27_versus_aws-l3-dev/NAE_13.png)
![NAE](../figures/V27_versus_aws-l3-dev/NAE_14.png)
![NAE](../figures/V27_versus_aws-l3-dev/NAE_15.png)
![NAE](../figures/V27_versus_aws-l3-dev/NAE_16.png)
 
## <a id='s1-19' />NAU
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![NAU](../figures/V27_versus_aws-l3-dev/NAU_0.png)
![NAU](../figures/V27_versus_aws-l3-dev/NAU_1.png)
![NAU](../figures/V27_versus_aws-l3-dev/NAU_2.png)
![NAU](../figures/V27_versus_aws-l3-dev/NAU_3.png)
![NAU](../figures/V27_versus_aws-l3-dev/NAU_4.png)
![NAU](../figures/V27_versus_aws-l3-dev/NAU_5.png)
![NAU](../figures/V27_versus_aws-l3-dev/NAU_6.png)
![NAU](../figures/V27_versus_aws-l3-dev/NAU_7.png)
![NAU](../figures/V27_versus_aws-l3-dev/NAU_8.png)
![NAU](../figures/V27_versus_aws-l3-dev/NAU_9.png)
![NAU](../figures/V27_versus_aws-l3-dev/NAU_10.png)
![NAU](../figures/V27_versus_aws-l3-dev/NAU_11.png)
![NAU](../figures/V27_versus_aws-l3-dev/NAU_12.png)
![NAU](../figures/V27_versus_aws-l3-dev/NAU_13.png)
![NAU](../figures/V27_versus_aws-l3-dev/NAU_14.png)
![NAU](../figures/V27_versus_aws-l3-dev/NAU_15.png)
![NAU](../figures/V27_versus_aws-l3-dev/NAU_16.png)
 
## <a id='s1-20' />NEM
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![NEM](../figures/V27_versus_aws-l3-dev/NEM_0.png)
![NEM](../figures/V27_versus_aws-l3-dev/NEM_1.png)
![NEM](../figures/V27_versus_aws-l3-dev/NEM_2.png)
![NEM](../figures/V27_versus_aws-l3-dev/NEM_3.png)
![NEM](../figures/V27_versus_aws-l3-dev/NEM_4.png)
![NEM](../figures/V27_versus_aws-l3-dev/NEM_5.png)
![NEM](../figures/V27_versus_aws-l3-dev/NEM_6.png)
![NEM](../figures/V27_versus_aws-l3-dev/NEM_7.png)
![NEM](../figures/V27_versus_aws-l3-dev/NEM_8.png)
![NEM](../figures/V27_versus_aws-l3-dev/NEM_9.png)
![NEM](../figures/V27_versus_aws-l3-dev/NEM_10.png)
![NEM](../figures/V27_versus_aws-l3-dev/NEM_11.png)
![NEM](../figures/V27_versus_aws-l3-dev/NEM_12.png)
![NEM](../figures/V27_versus_aws-l3-dev/NEM_13.png)
![NEM](../figures/V27_versus_aws-l3-dev/NEM_14.png)
![NEM](../figures/V27_versus_aws-l3-dev/NEM_15.png)
![NEM](../figures/V27_versus_aws-l3-dev/NEM_16.png)
 
## <a id='s1-21' />NSE
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![NSE](../figures/V27_versus_aws-l3-dev/NSE_0.png)
![NSE](../figures/V27_versus_aws-l3-dev/NSE_1.png)
![NSE](../figures/V27_versus_aws-l3-dev/NSE_2.png)
![NSE](../figures/V27_versus_aws-l3-dev/NSE_3.png)
![NSE](../figures/V27_versus_aws-l3-dev/NSE_4.png)
![NSE](../figures/V27_versus_aws-l3-dev/NSE_5.png)
![NSE](../figures/V27_versus_aws-l3-dev/NSE_6.png)
![NSE](../figures/V27_versus_aws-l3-dev/NSE_7.png)
![NSE](../figures/V27_versus_aws-l3-dev/NSE_8.png)
![NSE](../figures/V27_versus_aws-l3-dev/NSE_9.png)
![NSE](../figures/V27_versus_aws-l3-dev/NSE_10.png)
![NSE](../figures/V27_versus_aws-l3-dev/NSE_11.png)
![NSE](../figures/V27_versus_aws-l3-dev/NSE_12.png)
![NSE](../figures/V27_versus_aws-l3-dev/NSE_13.png)
![NSE](../figures/V27_versus_aws-l3-dev/NSE_14.png)
![NSE](../figures/V27_versus_aws-l3-dev/NSE_15.png)
![NSE](../figures/V27_versus_aws-l3-dev/NSE_16.png)
 
## <a id='s1-22' />NUK_B
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, usr, albedo, dlr, ulr, t_surf, z_boom_u, z_boom_cor_u, z_stake_cor, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, t_i_2, t_i_4, t_i_6, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u, t_i_2, t_i_4, t_i_6, t_i_8

Old variables removed from new files:
z_stake, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_3, t_i_5, t_i_7
 
![NUK_B](../figures/V27_versus_aws-l3-dev/NUK_B_0.png)
![NUK_B](../figures/V27_versus_aws-l3-dev/NUK_B_1.png)
![NUK_B](../figures/V27_versus_aws-l3-dev/NUK_B_2.png)
![NUK_B](../figures/V27_versus_aws-l3-dev/NUK_B_3.png)
![NUK_B](../figures/V27_versus_aws-l3-dev/NUK_B_4.png)
![NUK_B](../figures/V27_versus_aws-l3-dev/NUK_B_5.png)
![NUK_B](../figures/V27_versus_aws-l3-dev/NUK_B_6.png)
![NUK_B](../figures/V27_versus_aws-l3-dev/NUK_B_7.png)
![NUK_B](../figures/V27_versus_aws-l3-dev/NUK_B_8.png)
 
## <a id='s1-23' />NUK_K
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![NUK_K](../figures/V27_versus_aws-l3-dev/NUK_K_0.png)
![NUK_K](../figures/V27_versus_aws-l3-dev/NUK_K_1.png)
![NUK_K](../figures/V27_versus_aws-l3-dev/NUK_K_2.png)
![NUK_K](../figures/V27_versus_aws-l3-dev/NUK_K_3.png)
![NUK_K](../figures/V27_versus_aws-l3-dev/NUK_K_4.png)
![NUK_K](../figures/V27_versus_aws-l3-dev/NUK_K_5.png)
![NUK_K](../figures/V27_versus_aws-l3-dev/NUK_K_6.png)
![NUK_K](../figures/V27_versus_aws-l3-dev/NUK_K_7.png)
![NUK_K](../figures/V27_versus_aws-l3-dev/NUK_K_8.png)
![NUK_K](../figures/V27_versus_aws-l3-dev/NUK_K_9.png)
![NUK_K](../figures/V27_versus_aws-l3-dev/NUK_K_10.png)
![NUK_K](../figures/V27_versus_aws-l3-dev/NUK_K_11.png)
![NUK_K](../figures/V27_versus_aws-l3-dev/NUK_K_12.png)
![NUK_K](../figures/V27_versus_aws-l3-dev/NUK_K_13.png)
 
## <a id='s1-24' />NUK_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![NUK_L](../figures/V27_versus_aws-l3-dev/NUK_L_0.png)
![NUK_L](../figures/V27_versus_aws-l3-dev/NUK_L_1.png)
![NUK_L](../figures/V27_versus_aws-l3-dev/NUK_L_2.png)
![NUK_L](../figures/V27_versus_aws-l3-dev/NUK_L_3.png)
![NUK_L](../figures/V27_versus_aws-l3-dev/NUK_L_4.png)
![NUK_L](../figures/V27_versus_aws-l3-dev/NUK_L_5.png)
![NUK_L](../figures/V27_versus_aws-l3-dev/NUK_L_6.png)
![NUK_L](../figures/V27_versus_aws-l3-dev/NUK_L_7.png)
![NUK_L](../figures/V27_versus_aws-l3-dev/NUK_L_8.png)
![NUK_L](../figures/V27_versus_aws-l3-dev/NUK_L_9.png)
![NUK_L](../figures/V27_versus_aws-l3-dev/NUK_L_10.png)
![NUK_L](../figures/V27_versus_aws-l3-dev/NUK_L_11.png)
![NUK_L](../figures/V27_versus_aws-l3-dev/NUK_L_12.png)
![NUK_L](../figures/V27_versus_aws-l3-dev/NUK_L_13.png)
 
## <a id='s1-25' />NUK_N
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![NUK_N](../figures/V27_versus_aws-l3-dev/NUK_N_0.png)
![NUK_N](../figures/V27_versus_aws-l3-dev/NUK_N_1.png)
![NUK_N](../figures/V27_versus_aws-l3-dev/NUK_N_2.png)
![NUK_N](../figures/V27_versus_aws-l3-dev/NUK_N_3.png)
![NUK_N](../figures/V27_versus_aws-l3-dev/NUK_N_4.png)
![NUK_N](../figures/V27_versus_aws-l3-dev/NUK_N_5.png)
![NUK_N](../figures/V27_versus_aws-l3-dev/NUK_N_6.png)
![NUK_N](../figures/V27_versus_aws-l3-dev/NUK_N_7.png)
![NUK_N](../figures/V27_versus_aws-l3-dev/NUK_N_8.png)
![NUK_N](../figures/V27_versus_aws-l3-dev/NUK_N_9.png)
![NUK_N](../figures/V27_versus_aws-l3-dev/NUK_N_10.png)
![NUK_N](../figures/V27_versus_aws-l3-dev/NUK_N_11.png)
![NUK_N](../figures/V27_versus_aws-l3-dev/NUK_N_12.png)
 
## <a id='s1-26' />NUK_P
## <a id='s1-27' />NUK_U
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![NUK_U](../figures/V27_versus_aws-l3-dev/NUK_U_0.png)
![NUK_U](../figures/V27_versus_aws-l3-dev/NUK_U_1.png)
![NUK_U](../figures/V27_versus_aws-l3-dev/NUK_U_2.png)
![NUK_U](../figures/V27_versus_aws-l3-dev/NUK_U_3.png)
![NUK_U](../figures/V27_versus_aws-l3-dev/NUK_U_4.png)
![NUK_U](../figures/V27_versus_aws-l3-dev/NUK_U_5.png)
![NUK_U](../figures/V27_versus_aws-l3-dev/NUK_U_6.png)
![NUK_U](../figures/V27_versus_aws-l3-dev/NUK_U_7.png)
![NUK_U](../figures/V27_versus_aws-l3-dev/NUK_U_8.png)
![NUK_U](../figures/V27_versus_aws-l3-dev/NUK_U_9.png)
![NUK_U](../figures/V27_versus_aws-l3-dev/NUK_U_10.png)
![NUK_U](../figures/V27_versus_aws-l3-dev/NUK_U_11.png)
![NUK_U](../figures/V27_versus_aws-l3-dev/NUK_U_12.png)
![NUK_U](../figures/V27_versus_aws-l3-dev/NUK_U_13.png)
 
## <a id='s1-28' />ORO
## <a id='s1-29' />QAS_A
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![QAS_A](../figures/V27_versus_aws-l3-dev/QAS_A_0.png)
![QAS_A](../figures/V27_versus_aws-l3-dev/QAS_A_1.png)
![QAS_A](../figures/V27_versus_aws-l3-dev/QAS_A_2.png)
![QAS_A](../figures/V27_versus_aws-l3-dev/QAS_A_3.png)
![QAS_A](../figures/V27_versus_aws-l3-dev/QAS_A_4.png)
![QAS_A](../figures/V27_versus_aws-l3-dev/QAS_A_5.png)
![QAS_A](../figures/V27_versus_aws-l3-dev/QAS_A_6.png)
![QAS_A](../figures/V27_versus_aws-l3-dev/QAS_A_7.png)
![QAS_A](../figures/V27_versus_aws-l3-dev/QAS_A_8.png)
![QAS_A](../figures/V27_versus_aws-l3-dev/QAS_A_9.png)
![QAS_A](../figures/V27_versus_aws-l3-dev/QAS_A_10.png)
![QAS_A](../figures/V27_versus_aws-l3-dev/QAS_A_11.png)
![QAS_A](../figures/V27_versus_aws-l3-dev/QAS_A_12.png)
 
## <a id='s1-30' />QAS_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![QAS_L](../figures/V27_versus_aws-l3-dev/QAS_L_0.png)
![QAS_L](../figures/V27_versus_aws-l3-dev/QAS_L_1.png)
![QAS_L](../figures/V27_versus_aws-l3-dev/QAS_L_2.png)
![QAS_L](../figures/V27_versus_aws-l3-dev/QAS_L_3.png)
![QAS_L](../figures/V27_versus_aws-l3-dev/QAS_L_4.png)
![QAS_L](../figures/V27_versus_aws-l3-dev/QAS_L_5.png)
![QAS_L](../figures/V27_versus_aws-l3-dev/QAS_L_6.png)
![QAS_L](../figures/V27_versus_aws-l3-dev/QAS_L_7.png)
![QAS_L](../figures/V27_versus_aws-l3-dev/QAS_L_8.png)
![QAS_L](../figures/V27_versus_aws-l3-dev/QAS_L_9.png)
![QAS_L](../figures/V27_versus_aws-l3-dev/QAS_L_10.png)
![QAS_L](../figures/V27_versus_aws-l3-dev/QAS_L_11.png)
![QAS_L](../figures/V27_versus_aws-l3-dev/QAS_L_12.png)
![QAS_L](../figures/V27_versus_aws-l3-dev/QAS_L_13.png)
 
## <a id='s1-31' />QAS_M
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![QAS_M](../figures/V27_versus_aws-l3-dev/QAS_M_0.png)
![QAS_M](../figures/V27_versus_aws-l3-dev/QAS_M_1.png)
![QAS_M](../figures/V27_versus_aws-l3-dev/QAS_M_2.png)
![QAS_M](../figures/V27_versus_aws-l3-dev/QAS_M_3.png)
![QAS_M](../figures/V27_versus_aws-l3-dev/QAS_M_4.png)
![QAS_M](../figures/V27_versus_aws-l3-dev/QAS_M_5.png)
![QAS_M](../figures/V27_versus_aws-l3-dev/QAS_M_6.png)
![QAS_M](../figures/V27_versus_aws-l3-dev/QAS_M_7.png)
![QAS_M](../figures/V27_versus_aws-l3-dev/QAS_M_8.png)
![QAS_M](../figures/V27_versus_aws-l3-dev/QAS_M_9.png)
![QAS_M](../figures/V27_versus_aws-l3-dev/QAS_M_10.png)
![QAS_M](../figures/V27_versus_aws-l3-dev/QAS_M_11.png)
![QAS_M](../figures/V27_versus_aws-l3-dev/QAS_M_12.png)
![QAS_M](../figures/V27_versus_aws-l3-dev/QAS_M_13.png)
 
## <a id='s1-32' />QAS_U
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![QAS_U](../figures/V27_versus_aws-l3-dev/QAS_U_0.png)
![QAS_U](../figures/V27_versus_aws-l3-dev/QAS_U_1.png)
![QAS_U](../figures/V27_versus_aws-l3-dev/QAS_U_2.png)
![QAS_U](../figures/V27_versus_aws-l3-dev/QAS_U_3.png)
![QAS_U](../figures/V27_versus_aws-l3-dev/QAS_U_4.png)
![QAS_U](../figures/V27_versus_aws-l3-dev/QAS_U_5.png)
![QAS_U](../figures/V27_versus_aws-l3-dev/QAS_U_6.png)
![QAS_U](../figures/V27_versus_aws-l3-dev/QAS_U_7.png)
![QAS_U](../figures/V27_versus_aws-l3-dev/QAS_U_8.png)
![QAS_U](../figures/V27_versus_aws-l3-dev/QAS_U_9.png)
![QAS_U](../figures/V27_versus_aws-l3-dev/QAS_U_10.png)
![QAS_U](../figures/V27_versus_aws-l3-dev/QAS_U_11.png)
![QAS_U](../figures/V27_versus_aws-l3-dev/QAS_U_12.png)
![QAS_U](../figures/V27_versus_aws-l3-dev/QAS_U_13.png)
 
## <a id='s1-33' />RED_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![RED_L](../figures/V27_versus_aws-l3-dev/RED_L_0.png)
![RED_L](../figures/V27_versus_aws-l3-dev/RED_L_1.png)
![RED_L](../figures/V27_versus_aws-l3-dev/RED_L_2.png)
![RED_L](../figures/V27_versus_aws-l3-dev/RED_L_3.png)
![RED_L](../figures/V27_versus_aws-l3-dev/RED_L_4.png)
![RED_L](../figures/V27_versus_aws-l3-dev/RED_L_5.png)
![RED_L](../figures/V27_versus_aws-l3-dev/RED_L_6.png)
![RED_L](../figures/V27_versus_aws-l3-dev/RED_L_7.png)
![RED_L](../figures/V27_versus_aws-l3-dev/RED_L_8.png)
![RED_L](../figures/V27_versus_aws-l3-dev/RED_L_9.png)
![RED_L](../figures/V27_versus_aws-l3-dev/RED_L_10.png)
![RED_L](../figures/V27_versus_aws-l3-dev/RED_L_11.png)
![RED_L](../figures/V27_versus_aws-l3-dev/RED_L_12.png)
![RED_L](../figures/V27_versus_aws-l3-dev/RED_L_13.png)
 
## <a id='s1-34' />SCO_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![SCO_L](../figures/V27_versus_aws-l3-dev/SCO_L_0.png)
![SCO_L](../figures/V27_versus_aws-l3-dev/SCO_L_1.png)
![SCO_L](../figures/V27_versus_aws-l3-dev/SCO_L_2.png)
![SCO_L](../figures/V27_versus_aws-l3-dev/SCO_L_3.png)
![SCO_L](../figures/V27_versus_aws-l3-dev/SCO_L_4.png)
![SCO_L](../figures/V27_versus_aws-l3-dev/SCO_L_5.png)
![SCO_L](../figures/V27_versus_aws-l3-dev/SCO_L_6.png)
![SCO_L](../figures/V27_versus_aws-l3-dev/SCO_L_7.png)
![SCO_L](../figures/V27_versus_aws-l3-dev/SCO_L_8.png)
![SCO_L](../figures/V27_versus_aws-l3-dev/SCO_L_9.png)
![SCO_L](../figures/V27_versus_aws-l3-dev/SCO_L_10.png)
![SCO_L](../figures/V27_versus_aws-l3-dev/SCO_L_11.png)
![SCO_L](../figures/V27_versus_aws-l3-dev/SCO_L_12.png)
![SCO_L](../figures/V27_versus_aws-l3-dev/SCO_L_13.png)
 
## <a id='s1-35' />SCO_U
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![SCO_U](../figures/V27_versus_aws-l3-dev/SCO_U_0.png)
![SCO_U](../figures/V27_versus_aws-l3-dev/SCO_U_1.png)
![SCO_U](../figures/V27_versus_aws-l3-dev/SCO_U_2.png)
![SCO_U](../figures/V27_versus_aws-l3-dev/SCO_U_3.png)
![SCO_U](../figures/V27_versus_aws-l3-dev/SCO_U_4.png)
![SCO_U](../figures/V27_versus_aws-l3-dev/SCO_U_5.png)
![SCO_U](../figures/V27_versus_aws-l3-dev/SCO_U_6.png)
![SCO_U](../figures/V27_versus_aws-l3-dev/SCO_U_7.png)
![SCO_U](../figures/V27_versus_aws-l3-dev/SCO_U_8.png)
![SCO_U](../figures/V27_versus_aws-l3-dev/SCO_U_9.png)
![SCO_U](../figures/V27_versus_aws-l3-dev/SCO_U_10.png)
![SCO_U](../figures/V27_versus_aws-l3-dev/SCO_U_11.png)
![SCO_U](../figures/V27_versus_aws-l3-dev/SCO_U_12.png)
![SCO_U](../figures/V27_versus_aws-l3-dev/SCO_U_13.png)
 
## <a id='s1-36' />SDL
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![SDL](../figures/V27_versus_aws-l3-dev/SDL_0.png)
![SDL](../figures/V27_versus_aws-l3-dev/SDL_1.png)
![SDL](../figures/V27_versus_aws-l3-dev/SDL_2.png)
![SDL](../figures/V27_versus_aws-l3-dev/SDL_3.png)
![SDL](../figures/V27_versus_aws-l3-dev/SDL_4.png)
![SDL](../figures/V27_versus_aws-l3-dev/SDL_5.png)
![SDL](../figures/V27_versus_aws-l3-dev/SDL_6.png)
![SDL](../figures/V27_versus_aws-l3-dev/SDL_7.png)
![SDL](../figures/V27_versus_aws-l3-dev/SDL_8.png)
![SDL](../figures/V27_versus_aws-l3-dev/SDL_9.png)
![SDL](../figures/V27_versus_aws-l3-dev/SDL_10.png)
![SDL](../figures/V27_versus_aws-l3-dev/SDL_11.png)
![SDL](../figures/V27_versus_aws-l3-dev/SDL_12.png)
![SDL](../figures/V27_versus_aws-l3-dev/SDL_13.png)
![SDL](../figures/V27_versus_aws-l3-dev/SDL_14.png)
![SDL](../figures/V27_versus_aws-l3-dev/SDL_15.png)
![SDL](../figures/V27_versus_aws-l3-dev/SDL_16.png)
 
## <a id='s1-37' />SDM
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![SDM](../figures/V27_versus_aws-l3-dev/SDM_0.png)
![SDM](../figures/V27_versus_aws-l3-dev/SDM_1.png)
![SDM](../figures/V27_versus_aws-l3-dev/SDM_2.png)
![SDM](../figures/V27_versus_aws-l3-dev/SDM_3.png)
![SDM](../figures/V27_versus_aws-l3-dev/SDM_4.png)
![SDM](../figures/V27_versus_aws-l3-dev/SDM_5.png)
![SDM](../figures/V27_versus_aws-l3-dev/SDM_6.png)
![SDM](../figures/V27_versus_aws-l3-dev/SDM_7.png)
![SDM](../figures/V27_versus_aws-l3-dev/SDM_8.png)
![SDM](../figures/V27_versus_aws-l3-dev/SDM_9.png)
![SDM](../figures/V27_versus_aws-l3-dev/SDM_10.png)
![SDM](../figures/V27_versus_aws-l3-dev/SDM_11.png)
![SDM](../figures/V27_versus_aws-l3-dev/SDM_12.png)
![SDM](../figures/V27_versus_aws-l3-dev/SDM_13.png)
![SDM](../figures/V27_versus_aws-l3-dev/SDM_14.png)
![SDM](../figures/V27_versus_aws-l3-dev/SDM_15.png)
![SDM](../figures/V27_versus_aws-l3-dev/SDM_16.png)
 
## <a id='s1-38' />SER_B
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, usr, albedo, dlr, ulr, t_surf, z_boom_u, z_boom_cor_u, z_stake_cor, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, t_i_2, t_i_4, t_i_6, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u, t_i_2, t_i_4, t_i_6, t_i_8

Old variables removed from new files:
z_stake, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_3, t_i_5, t_i_7
 
![SER_B](../figures/V27_versus_aws-l3-dev/SER_B_0.png)
![SER_B](../figures/V27_versus_aws-l3-dev/SER_B_1.png)
![SER_B](../figures/V27_versus_aws-l3-dev/SER_B_2.png)
![SER_B](../figures/V27_versus_aws-l3-dev/SER_B_3.png)
![SER_B](../figures/V27_versus_aws-l3-dev/SER_B_4.png)
![SER_B](../figures/V27_versus_aws-l3-dev/SER_B_5.png)
![SER_B](../figures/V27_versus_aws-l3-dev/SER_B_6.png)
![SER_B](../figures/V27_versus_aws-l3-dev/SER_B_7.png)
![SER_B](../figures/V27_versus_aws-l3-dev/SER_B_8.png)
 
## <a id='s1-39' />SWC
Variables in new file:
p_u, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_boom_l, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![SWC](../figures/V27_versus_aws-l3-dev/SWC_0.png)
![SWC](../figures/V27_versus_aws-l3-dev/SWC_1.png)
![SWC](../figures/V27_versus_aws-l3-dev/SWC_2.png)
![SWC](../figures/V27_versus_aws-l3-dev/SWC_3.png)
![SWC](../figures/V27_versus_aws-l3-dev/SWC_4.png)
![SWC](../figures/V27_versus_aws-l3-dev/SWC_5.png)
![SWC](../figures/V27_versus_aws-l3-dev/SWC_6.png)
![SWC](../figures/V27_versus_aws-l3-dev/SWC_7.png)
![SWC](../figures/V27_versus_aws-l3-dev/SWC_8.png)
![SWC](../figures/V27_versus_aws-l3-dev/SWC_9.png)
![SWC](../figures/V27_versus_aws-l3-dev/SWC_10.png)
![SWC](../figures/V27_versus_aws-l3-dev/SWC_11.png)
![SWC](../figures/V27_versus_aws-l3-dev/SWC_12.png)
![SWC](../figures/V27_versus_aws-l3-dev/SWC_13.png)
![SWC](../figures/V27_versus_aws-l3-dev/SWC_14.png)
![SWC](../figures/V27_versus_aws-l3-dev/SWC_15.png)
 
## <a id='s1-40' />TAS_A
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![TAS_A](../figures/V27_versus_aws-l3-dev/TAS_A_0.png)
![TAS_A](../figures/V27_versus_aws-l3-dev/TAS_A_1.png)
![TAS_A](../figures/V27_versus_aws-l3-dev/TAS_A_2.png)
![TAS_A](../figures/V27_versus_aws-l3-dev/TAS_A_3.png)
![TAS_A](../figures/V27_versus_aws-l3-dev/TAS_A_4.png)
![TAS_A](../figures/V27_versus_aws-l3-dev/TAS_A_5.png)
![TAS_A](../figures/V27_versus_aws-l3-dev/TAS_A_6.png)
![TAS_A](../figures/V27_versus_aws-l3-dev/TAS_A_7.png)
![TAS_A](../figures/V27_versus_aws-l3-dev/TAS_A_8.png)
![TAS_A](../figures/V27_versus_aws-l3-dev/TAS_A_9.png)
![TAS_A](../figures/V27_versus_aws-l3-dev/TAS_A_10.png)
![TAS_A](../figures/V27_versus_aws-l3-dev/TAS_A_11.png)
![TAS_A](../figures/V27_versus_aws-l3-dev/TAS_A_12.png)
![TAS_A](../figures/V27_versus_aws-l3-dev/TAS_A_13.png)
 
## <a id='s1-41' />TAS_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![TAS_L](../figures/V27_versus_aws-l3-dev/TAS_L_0.png)
![TAS_L](../figures/V27_versus_aws-l3-dev/TAS_L_1.png)
![TAS_L](../figures/V27_versus_aws-l3-dev/TAS_L_2.png)
![TAS_L](../figures/V27_versus_aws-l3-dev/TAS_L_3.png)
![TAS_L](../figures/V27_versus_aws-l3-dev/TAS_L_4.png)
![TAS_L](../figures/V27_versus_aws-l3-dev/TAS_L_5.png)
![TAS_L](../figures/V27_versus_aws-l3-dev/TAS_L_6.png)
![TAS_L](../figures/V27_versus_aws-l3-dev/TAS_L_7.png)
![TAS_L](../figures/V27_versus_aws-l3-dev/TAS_L_8.png)
![TAS_L](../figures/V27_versus_aws-l3-dev/TAS_L_9.png)
![TAS_L](../figures/V27_versus_aws-l3-dev/TAS_L_10.png)
![TAS_L](../figures/V27_versus_aws-l3-dev/TAS_L_11.png)
![TAS_L](../figures/V27_versus_aws-l3-dev/TAS_L_12.png)
 
## <a id='s1-42' />TAS_U
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![TAS_U](../figures/V27_versus_aws-l3-dev/TAS_U_0.png)
![TAS_U](../figures/V27_versus_aws-l3-dev/TAS_U_1.png)
![TAS_U](../figures/V27_versus_aws-l3-dev/TAS_U_2.png)
![TAS_U](../figures/V27_versus_aws-l3-dev/TAS_U_3.png)
![TAS_U](../figures/V27_versus_aws-l3-dev/TAS_U_4.png)
![TAS_U](../figures/V27_versus_aws-l3-dev/TAS_U_5.png)
![TAS_U](../figures/V27_versus_aws-l3-dev/TAS_U_6.png)
![TAS_U](../figures/V27_versus_aws-l3-dev/TAS_U_7.png)
![TAS_U](../figures/V27_versus_aws-l3-dev/TAS_U_8.png)
![TAS_U](../figures/V27_versus_aws-l3-dev/TAS_U_9.png)
![TAS_U](../figures/V27_versus_aws-l3-dev/TAS_U_10.png)
![TAS_U](../figures/V27_versus_aws-l3-dev/TAS_U_11.png)
![TAS_U](../figures/V27_versus_aws-l3-dev/TAS_U_12.png)
 
## <a id='s1-43' />THU_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![THU_L](../figures/V27_versus_aws-l3-dev/THU_L_0.png)
![THU_L](../figures/V27_versus_aws-l3-dev/THU_L_1.png)
![THU_L](../figures/V27_versus_aws-l3-dev/THU_L_2.png)
![THU_L](../figures/V27_versus_aws-l3-dev/THU_L_3.png)
![THU_L](../figures/V27_versus_aws-l3-dev/THU_L_4.png)
![THU_L](../figures/V27_versus_aws-l3-dev/THU_L_5.png)
![THU_L](../figures/V27_versus_aws-l3-dev/THU_L_6.png)
![THU_L](../figures/V27_versus_aws-l3-dev/THU_L_7.png)
![THU_L](../figures/V27_versus_aws-l3-dev/THU_L_8.png)
![THU_L](../figures/V27_versus_aws-l3-dev/THU_L_9.png)
![THU_L](../figures/V27_versus_aws-l3-dev/THU_L_10.png)
![THU_L](../figures/V27_versus_aws-l3-dev/THU_L_11.png)
![THU_L](../figures/V27_versus_aws-l3-dev/THU_L_12.png)
 
## <a id='s1-44' />THU_L2
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![THU_L2](../figures/V27_versus_aws-l3-dev/THU_L2_0.png)
![THU_L2](../figures/V27_versus_aws-l3-dev/THU_L2_1.png)
![THU_L2](../figures/V27_versus_aws-l3-dev/THU_L2_2.png)
![THU_L2](../figures/V27_versus_aws-l3-dev/THU_L2_3.png)
![THU_L2](../figures/V27_versus_aws-l3-dev/THU_L2_4.png)
![THU_L2](../figures/V27_versus_aws-l3-dev/THU_L2_5.png)
![THU_L2](../figures/V27_versus_aws-l3-dev/THU_L2_6.png)
![THU_L2](../figures/V27_versus_aws-l3-dev/THU_L2_7.png)
![THU_L2](../figures/V27_versus_aws-l3-dev/THU_L2_8.png)
![THU_L2](../figures/V27_versus_aws-l3-dev/THU_L2_9.png)
![THU_L2](../figures/V27_versus_aws-l3-dev/THU_L2_10.png)
![THU_L2](../figures/V27_versus_aws-l3-dev/THU_L2_11.png)
![THU_L2](../figures/V27_versus_aws-l3-dev/THU_L2_12.png)
 
## <a id='s1-45' />THU_U
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![THU_U](../figures/V27_versus_aws-l3-dev/THU_U_0.png)
![THU_U](../figures/V27_versus_aws-l3-dev/THU_U_1.png)
![THU_U](../figures/V27_versus_aws-l3-dev/THU_U_2.png)
![THU_U](../figures/V27_versus_aws-l3-dev/THU_U_3.png)
![THU_U](../figures/V27_versus_aws-l3-dev/THU_U_4.png)
![THU_U](../figures/V27_versus_aws-l3-dev/THU_U_5.png)
![THU_U](../figures/V27_versus_aws-l3-dev/THU_U_6.png)
![THU_U](../figures/V27_versus_aws-l3-dev/THU_U_7.png)
![THU_U](../figures/V27_versus_aws-l3-dev/THU_U_8.png)
![THU_U](../figures/V27_versus_aws-l3-dev/THU_U_9.png)
![THU_U](../figures/V27_versus_aws-l3-dev/THU_U_10.png)
![THU_U](../figures/V27_versus_aws-l3-dev/THU_U_11.png)
![THU_U](../figures/V27_versus_aws-l3-dev/THU_U_12.png)
![THU_U](../figures/V27_versus_aws-l3-dev/THU_U_13.png)
 
## <a id='s1-46' />TUN
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![TUN](../figures/V27_versus_aws-l3-dev/TUN_0.png)
![TUN](../figures/V27_versus_aws-l3-dev/TUN_1.png)
![TUN](../figures/V27_versus_aws-l3-dev/TUN_2.png)
![TUN](../figures/V27_versus_aws-l3-dev/TUN_3.png)
![TUN](../figures/V27_versus_aws-l3-dev/TUN_4.png)
![TUN](../figures/V27_versus_aws-l3-dev/TUN_5.png)
![TUN](../figures/V27_versus_aws-l3-dev/TUN_6.png)
![TUN](../figures/V27_versus_aws-l3-dev/TUN_7.png)
![TUN](../figures/V27_versus_aws-l3-dev/TUN_8.png)
![TUN](../figures/V27_versus_aws-l3-dev/TUN_9.png)
![TUN](../figures/V27_versus_aws-l3-dev/TUN_10.png)
![TUN](../figures/V27_versus_aws-l3-dev/TUN_11.png)
![TUN](../figures/V27_versus_aws-l3-dev/TUN_12.png)
![TUN](../figures/V27_versus_aws-l3-dev/TUN_13.png)
![TUN](../figures/V27_versus_aws-l3-dev/TUN_14.png)
![TUN](../figures/V27_versus_aws-l3-dev/TUN_15.png)
![TUN](../figures/V27_versus_aws-l3-dev/TUN_16.png)
 
## <a id='s1-47' />UPE_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![UPE_L](../figures/V27_versus_aws-l3-dev/UPE_L_0.png)
![UPE_L](../figures/V27_versus_aws-l3-dev/UPE_L_1.png)
![UPE_L](../figures/V27_versus_aws-l3-dev/UPE_L_2.png)
![UPE_L](../figures/V27_versus_aws-l3-dev/UPE_L_3.png)
![UPE_L](../figures/V27_versus_aws-l3-dev/UPE_L_4.png)
![UPE_L](../figures/V27_versus_aws-l3-dev/UPE_L_5.png)
![UPE_L](../figures/V27_versus_aws-l3-dev/UPE_L_6.png)
![UPE_L](../figures/V27_versus_aws-l3-dev/UPE_L_7.png)
![UPE_L](../figures/V27_versus_aws-l3-dev/UPE_L_8.png)
![UPE_L](../figures/V27_versus_aws-l3-dev/UPE_L_9.png)
![UPE_L](../figures/V27_versus_aws-l3-dev/UPE_L_10.png)
![UPE_L](../figures/V27_versus_aws-l3-dev/UPE_L_11.png)
![UPE_L](../figures/V27_versus_aws-l3-dev/UPE_L_12.png)
 
## <a id='s1-48' />UPE_U
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor

Old variables removed from new files:

 
![UPE_U](../figures/V27_versus_aws-l3-dev/UPE_U_0.png)
![UPE_U](../figures/V27_versus_aws-l3-dev/UPE_U_1.png)
![UPE_U](../figures/V27_versus_aws-l3-dev/UPE_U_2.png)
![UPE_U](../figures/V27_versus_aws-l3-dev/UPE_U_3.png)
![UPE_U](../figures/V27_versus_aws-l3-dev/UPE_U_4.png)
![UPE_U](../figures/V27_versus_aws-l3-dev/UPE_U_5.png)
![UPE_U](../figures/V27_versus_aws-l3-dev/UPE_U_6.png)
![UPE_U](../figures/V27_versus_aws-l3-dev/UPE_U_7.png)
![UPE_U](../figures/V27_versus_aws-l3-dev/UPE_U_8.png)
![UPE_U](../figures/V27_versus_aws-l3-dev/UPE_U_9.png)
![UPE_U](../figures/V27_versus_aws-l3-dev/UPE_U_10.png)
![UPE_U](../figures/V27_versus_aws-l3-dev/UPE_U_11.png)
![UPE_U](../figures/V27_versus_aws-l3-dev/UPE_U_12.png)
 
## <a id='s1-49' />UWN
## <a id='s1-50' />WEG_B
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, usr, albedo, dlr, ulr, t_surf, z_boom_u, z_boom_cor_u, z_stake_cor, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u, t_i_2, t_i_4, t_i_6, t_i_8

Old variables removed from new files:
z_stake, precip_u, precip_u_cor, precip_u_rate, t_i_1
 
![WEG_B](../figures/V27_versus_aws-l3-dev/WEG_B_0.png)
![WEG_B](../figures/V27_versus_aws-l3-dev/WEG_B_1.png)
![WEG_B](../figures/V27_versus_aws-l3-dev/WEG_B_2.png)
![WEG_B](../figures/V27_versus_aws-l3-dev/WEG_B_3.png)
![WEG_B](../figures/V27_versus_aws-l3-dev/WEG_B_4.png)
![WEG_B](../figures/V27_versus_aws-l3-dev/WEG_B_5.png)
![WEG_B](../figures/V27_versus_aws-l3-dev/WEG_B_6.png)
![WEG_B](../figures/V27_versus_aws-l3-dev/WEG_B_7.png)
![WEG_B](../figures/V27_versus_aws-l3-dev/WEG_B_8.png)
![WEG_B](../figures/V27_versus_aws-l3-dev/WEG_B_9.png)
 
## <a id='s1-51' />WEG_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![WEG_L](../figures/V27_versus_aws-l3-dev/WEG_L_0.png)
![WEG_L](../figures/V27_versus_aws-l3-dev/WEG_L_1.png)
![WEG_L](../figures/V27_versus_aws-l3-dev/WEG_L_2.png)
![WEG_L](../figures/V27_versus_aws-l3-dev/WEG_L_3.png)
![WEG_L](../figures/V27_versus_aws-l3-dev/WEG_L_4.png)
![WEG_L](../figures/V27_versus_aws-l3-dev/WEG_L_5.png)
![WEG_L](../figures/V27_versus_aws-l3-dev/WEG_L_6.png)
![WEG_L](../figures/V27_versus_aws-l3-dev/WEG_L_7.png)
![WEG_L](../figures/V27_versus_aws-l3-dev/WEG_L_8.png)
![WEG_L](../figures/V27_versus_aws-l3-dev/WEG_L_9.png)
![WEG_L](../figures/V27_versus_aws-l3-dev/WEG_L_10.png)
![WEG_L](../figures/V27_versus_aws-l3-dev/WEG_L_11.png)
![WEG_L](../figures/V27_versus_aws-l3-dev/WEG_L_12.png)
![WEG_L](../figures/V27_versus_aws-l3-dev/WEG_L_13.png)
 
## <a id='s1-52' />ZAC_A
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_wrt_ice_or_water, qh_u, rh_l, rh_l_wrt_ice_or_water, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_cor_u, z_boom_l, z_boom_cor_l, z_surf_combined, snow_height, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_boom_cor_l, rainfall_u, rainfall_cor_u, rainfall_l, rainfall_cor_l

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate
 
![ZAC_A](../figures/V27_versus_aws-l3-dev/ZAC_A_0.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev/ZAC_A_1.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev/ZAC_A_2.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev/ZAC_A_3.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev/ZAC_A_4.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev/ZAC_A_5.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev/ZAC_A_6.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev/ZAC_A_7.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev/ZAC_A_8.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev/ZAC_A_9.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev/ZAC_A_10.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev/ZAC_A_11.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev/ZAC_A_12.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev/ZAC_A_13.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev/ZAC_A_14.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev/ZAC_A_15.png)
![ZAC_A](../figures/V27_versus_aws-l3-dev/ZAC_A_16.png)
 
## <a id='s1-53' />ZAC_L
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![ZAC_L](../figures/V27_versus_aws-l3-dev/ZAC_L_0.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev/ZAC_L_1.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev/ZAC_L_2.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev/ZAC_L_3.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev/ZAC_L_4.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev/ZAC_L_5.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev/ZAC_L_6.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev/ZAC_L_7.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev/ZAC_L_8.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev/ZAC_L_9.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev/ZAC_L_10.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev/ZAC_L_11.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev/ZAC_L_12.png)
![ZAC_L](../figures/V27_versus_aws-l3-dev/ZAC_L_13.png)
 
## <a id='s1-54' />ZAC_U
Variables in new file:
p_u, t_u, rh_u, rh_u_wrt_ice_or_water, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_cor_u, z_stake, z_stake_cor, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, rainfall_u, rainfall_cor_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_wrt_ice_or_water, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_boom_cor_u, z_stake_cor, rainfall_u, rainfall_cor_u

Old variables removed from new files:
precip_u, precip_u_cor, precip_u_rate
 
![ZAC_U](../figures/V27_versus_aws-l3-dev/ZAC_U_0.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev/ZAC_U_1.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev/ZAC_U_2.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev/ZAC_U_3.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev/ZAC_U_4.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev/ZAC_U_5.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev/ZAC_U_6.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev/ZAC_U_7.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev/ZAC_U_8.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev/ZAC_U_9.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev/ZAC_U_10.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev/ZAC_U_11.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev/ZAC_U_12.png)
![ZAC_U](../figures/V27_versus_aws-l3-dev/ZAC_U_13.png)
 
