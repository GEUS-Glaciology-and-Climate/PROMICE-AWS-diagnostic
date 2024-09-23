  * [CEN1](#s0-1)
  * [CEN2](#s0-2)
  * [CP1](#s0-3)
  * [DY2](#s0-4)
  * [EGP](#s0-5)
  * [FRE](#s0-6)
  * [HUM](#s0-7)
  * [JAR](#s0-8)
  * [JAR_O](#s0-9)
  * [KAN_B](#s0-10)
  * [KAN_L](#s0-11)
  * [KAN_Lv3](#s0-12)
  * [KAN_M](#s0-13)
  * [KAN_Tv3](#s0-14)
  * [KAN_U](#s0-15)
  * [KPC_L](#s0-16)
  * [KPC_Lv3](#s0-17)
  * [KPC_U](#s0-18)
  * [KPC_Uv3](#s0-19)
  * [LYN_L](#s0-20)
  * [LYN_T](#s0-21)
  * [MIT](#s0-22)
  * [NAE](#s0-23)
  * [NAU](#s0-24)
  * [NEM](#s0-25)
  * [NSE](#s0-26)
  * [NUK_B](#s0-27)
  * [NUK_K](#s0-28)
  * [NUK_L](#s0-29)
  * [NUK_N](#s0-30)
  * [NUK_U](#s0-31)
  * [NUK_Uv3](#s0-32)
  * [QAS_A](#s0-33)
  * [QAS_L](#s0-34)
  * [QAS_Lv3](#s0-35)
  * [QAS_M](#s0-36)
  * [QAS_Mv3](#s0-37)
  * [QAS_U](#s0-38)
  * [QAS_Uv3](#s0-39)
  * [RED_Lv3](#s0-40)
  * [Roof_GEUS](#s0-41)
  * [SCO_L](#s0-42)
  * [SCO_Lv3](#s0-43)
  * [SCO_U](#s0-44)
  * [SCO_Uv3](#s0-45)
  * [SDL](#s0-46)
  * [SDM](#s0-47)
  * [SER_B](#s0-48)
  * [SWC](#s0-49)
  * [SWC_O](#s0-50)
  * [TAS_A](#s0-51)
  * [TAS_Av3](#s0-52)
  * [TAS_L](#s0-53)
  * [TAS_U](#s0-54)
  * [THU_L](#s0-55)
  * [THU_L2](#s0-56)
  * [THU_U](#s0-57)
  * [THU_U2](#s0-58)
  * [THU_U2v3](#s0-59)
  * [TUN](#s0-60)
  * [UPE_L](#s0-61)
  * [UPE_U](#s0-62)
  * [UWN](#s0-63)
  * [WEG_B](#s0-64)
  * [WEG_L](#s0-65)
  * [XXX](#s0-66)
  * [ZAC_A](#s0-67)
  * [ZAC_Lv3](#s0-68)
  * [ZAC_Uv3](#s0-69)
  * [ZAK_A](#s0-70)
  * [ZAK_Lv3](#s0-71)
  * [ZAK_Uv3](#s0-72)
## <a id='s0-1' />CEN1
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
z_pt_cor, precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![CEN1](../figures/V19_versus_aws-l3-dev_scatter/CEN1_0.png)
![CEN1](../figures/V19_versus_aws-l3-dev_scatter/CEN1_1.png)
![CEN1](../figures/V19_versus_aws-l3-dev_scatter/CEN1_2.png)
![CEN1](../figures/V19_versus_aws-l3-dev_scatter/CEN1_3.png)
![CEN1](../figures/V19_versus_aws-l3-dev_scatter/CEN1_4.png)
 
## <a id='s0-2' />CEN2
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt

Old variables removed from new files:
gps_time, gps_hdop, fan_dc_u, fan_dc_l
 
![CEN2](../figures/V19_versus_aws-l3-dev_scatter/CEN2_0.png)
![CEN2](../figures/V19_versus_aws-l3-dev_scatter/CEN2_1.png)
![CEN2](../figures/V19_versus_aws-l3-dev_scatter/CEN2_2.png)
![CEN2](../figures/V19_versus_aws-l3-dev_scatter/CEN2_3.png)
![CEN2](../figures/V19_versus_aws-l3-dev_scatter/CEN2_4.png)
![CEN2](../figures/V19_versus_aws-l3-dev_scatter/CEN2_5.png)
![CEN2](../figures/V19_versus_aws-l3-dev_scatter/CEN2_6.png)
![CEN2](../figures/V19_versus_aws-l3-dev_scatter/CEN2_7.png)
 
## <a id='s0-3' />CP1
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt

Old variables removed from new files:
gps_time, gps_hdop, fan_dc_u, fan_dc_l
 
![CP1](../figures/V19_versus_aws-l3-dev_scatter/CP1_0.png)
![CP1](../figures/V19_versus_aws-l3-dev_scatter/CP1_1.png)
![CP1](../figures/V19_versus_aws-l3-dev_scatter/CP1_2.png)
![CP1](../figures/V19_versus_aws-l3-dev_scatter/CP1_3.png)
![CP1](../figures/V19_versus_aws-l3-dev_scatter/CP1_4.png)
![CP1](../figures/V19_versus_aws-l3-dev_scatter/CP1_5.png)
![CP1](../figures/V19_versus_aws-l3-dev_scatter/CP1_6.png)
![CP1](../figures/V19_versus_aws-l3-dev_scatter/CP1_7.png)
 
## <a id='s0-4' />DY2
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt

Old variables removed from new files:
gps_time, gps_hdop, fan_dc_u, fan_dc_l
 
![DY2](../figures/V19_versus_aws-l3-dev_scatter/DY2_0.png)
![DY2](../figures/V19_versus_aws-l3-dev_scatter/DY2_1.png)
![DY2](../figures/V19_versus_aws-l3-dev_scatter/DY2_2.png)
![DY2](../figures/V19_versus_aws-l3-dev_scatter/DY2_3.png)
![DY2](../figures/V19_versus_aws-l3-dev_scatter/DY2_4.png)
![DY2](../figures/V19_versus_aws-l3-dev_scatter/DY2_5.png)
![DY2](../figures/V19_versus_aws-l3-dev_scatter/DY2_6.png)
![DY2](../figures/V19_versus_aws-l3-dev_scatter/DY2_7.png)
 
## <a id='s0-5' />EGP
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_l, z_stake, z_pt, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
p_l, t_l, rh_l, rh_l_cor, wspd_l, wdir_l, wspd_x_l, wspd_y_l, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_l, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt

Old variables removed from new files:
z_pt_cor, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![EGP](../figures/V19_versus_aws-l3-dev_scatter/EGP_0.png)
![EGP](../figures/V19_versus_aws-l3-dev_scatter/EGP_1.png)
![EGP](../figures/V19_versus_aws-l3-dev_scatter/EGP_2.png)
![EGP](../figures/V19_versus_aws-l3-dev_scatter/EGP_3.png)
![EGP](../figures/V19_versus_aws-l3-dev_scatter/EGP_4.png)
 
## <a id='s0-6' />FRE
No old file for this station
## <a id='s0-7' />HUM
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt

Old variables removed from new files:
gps_time, gps_hdop, fan_dc_u, fan_dc_l
 
![HUM](../figures/V19_versus_aws-l3-dev_scatter/HUM_0.png)
![HUM](../figures/V19_versus_aws-l3-dev_scatter/HUM_1.png)
![HUM](../figures/V19_versus_aws-l3-dev_scatter/HUM_2.png)
![HUM](../figures/V19_versus_aws-l3-dev_scatter/HUM_3.png)
![HUM](../figures/V19_versus_aws-l3-dev_scatter/HUM_4.png)
![HUM](../figures/V19_versus_aws-l3-dev_scatter/HUM_5.png)
![HUM](../figures/V19_versus_aws-l3-dev_scatter/HUM_6.png)
![HUM](../figures/V19_versus_aws-l3-dev_scatter/HUM_7.png)
 
## <a id='s0-8' />JAR
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![JAR](../figures/V19_versus_aws-l3-dev_scatter/JAR_0.png)
![JAR](../figures/V19_versus_aws-l3-dev_scatter/JAR_1.png)
![JAR](../figures/V19_versus_aws-l3-dev_scatter/JAR_2.png)
![JAR](../figures/V19_versus_aws-l3-dev_scatter/JAR_3.png)
![JAR](../figures/V19_versus_aws-l3-dev_scatter/JAR_4.png)
 
## <a id='s0-9' />JAR_O
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![JAR_O](../figures/V19_versus_aws-l3-dev_scatter/JAR_O_0.png)
![JAR_O](../figures/V19_versus_aws-l3-dev_scatter/JAR_O_1.png)
![JAR_O](../figures/V19_versus_aws-l3-dev_scatter/JAR_O_2.png)
![JAR_O](../figures/V19_versus_aws-l3-dev_scatter/JAR_O_3.png)
![JAR_O](../figures/V19_versus_aws-l3-dev_scatter/JAR_O_4.png)
![JAR_O](../figures/V19_versus_aws-l3-dev_scatter/JAR_O_5.png)
 
## <a id='s0-10' />KAN_B
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, z_boom_u, z_stake, z_pt, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
cc, z_surf_combined, z_ice_surf, snow_height, lat, lon, alt

Old variables removed from new files:
z_pt_cor, precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![KAN_B](../figures/V19_versus_aws-l3-dev_scatter/KAN_B_0.png)
![KAN_B](../figures/V19_versus_aws-l3-dev_scatter/KAN_B_1.png)
![KAN_B](../figures/V19_versus_aws-l3-dev_scatter/KAN_B_2.png)
 
## <a id='s0-11' />KAN_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![KAN_L](../figures/V19_versus_aws-l3-dev_scatter/KAN_L_0.png)
![KAN_L](../figures/V19_versus_aws-l3-dev_scatter/KAN_L_1.png)
![KAN_L](../figures/V19_versus_aws-l3-dev_scatter/KAN_L_2.png)
![KAN_L](../figures/V19_versus_aws-l3-dev_scatter/KAN_L_3.png)
![KAN_L](../figures/V19_versus_aws-l3-dev_scatter/KAN_L_4.png)
![KAN_L](../figures/V19_versus_aws-l3-dev_scatter/KAN_L_5.png)
 
## <a id='s0-12' />KAN_Lv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![KAN_Lv3](../figures/V19_versus_aws-l3-dev_scatter/KAN_Lv3_0.png)
![KAN_Lv3](../figures/V19_versus_aws-l3-dev_scatter/KAN_Lv3_1.png)
![KAN_Lv3](../figures/V19_versus_aws-l3-dev_scatter/KAN_Lv3_2.png)
![KAN_Lv3](../figures/V19_versus_aws-l3-dev_scatter/KAN_Lv3_3.png)
![KAN_Lv3](../figures/V19_versus_aws-l3-dev_scatter/KAN_Lv3_4.png)
![KAN_Lv3](../figures/V19_versus_aws-l3-dev_scatter/KAN_Lv3_5.png)
 
## <a id='s0-13' />KAN_M
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![KAN_M](../figures/V19_versus_aws-l3-dev_scatter/KAN_M_0.png)
![KAN_M](../figures/V19_versus_aws-l3-dev_scatter/KAN_M_1.png)
![KAN_M](../figures/V19_versus_aws-l3-dev_scatter/KAN_M_2.png)
![KAN_M](../figures/V19_versus_aws-l3-dev_scatter/KAN_M_3.png)
![KAN_M](../figures/V19_versus_aws-l3-dev_scatter/KAN_M_4.png)
![KAN_M](../figures/V19_versus_aws-l3-dev_scatter/KAN_M_5.png)
 
## <a id='s0-14' />KAN_Tv3
No old file for this station
## <a id='s0-15' />KAN_U
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_boom_l, z_stake, z_pt, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
p_l, t_l, rh_l, rh_l_cor, wspd_l, wdir_l, wspd_x_l, wspd_y_l, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_l, precip_l_cor, precip_l_rate, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt

Old variables removed from new files:
z_pt_cor, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![KAN_U](../figures/V19_versus_aws-l3-dev_scatter/KAN_U_0.png)
![KAN_U](../figures/V19_versus_aws-l3-dev_scatter/KAN_U_1.png)
![KAN_U](../figures/V19_versus_aws-l3-dev_scatter/KAN_U_2.png)
![KAN_U](../figures/V19_versus_aws-l3-dev_scatter/KAN_U_3.png)
![KAN_U](../figures/V19_versus_aws-l3-dev_scatter/KAN_U_4.png)
 
## <a id='s0-16' />KPC_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![KPC_L](../figures/V19_versus_aws-l3-dev_scatter/KPC_L_0.png)
![KPC_L](../figures/V19_versus_aws-l3-dev_scatter/KPC_L_1.png)
![KPC_L](../figures/V19_versus_aws-l3-dev_scatter/KPC_L_2.png)
![KPC_L](../figures/V19_versus_aws-l3-dev_scatter/KPC_L_3.png)
![KPC_L](../figures/V19_versus_aws-l3-dev_scatter/KPC_L_4.png)
![KPC_L](../figures/V19_versus_aws-l3-dev_scatter/KPC_L_5.png)
 
## <a id='s0-17' />KPC_Lv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![KPC_Lv3](../figures/V19_versus_aws-l3-dev_scatter/KPC_Lv3_0.png)
![KPC_Lv3](../figures/V19_versus_aws-l3-dev_scatter/KPC_Lv3_1.png)
![KPC_Lv3](../figures/V19_versus_aws-l3-dev_scatter/KPC_Lv3_2.png)
![KPC_Lv3](../figures/V19_versus_aws-l3-dev_scatter/KPC_Lv3_3.png)
![KPC_Lv3](../figures/V19_versus_aws-l3-dev_scatter/KPC_Lv3_4.png)
 
## <a id='s0-18' />KPC_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![KPC_U](../figures/V19_versus_aws-l3-dev_scatter/KPC_U_0.png)
![KPC_U](../figures/V19_versus_aws-l3-dev_scatter/KPC_U_1.png)
![KPC_U](../figures/V19_versus_aws-l3-dev_scatter/KPC_U_2.png)
![KPC_U](../figures/V19_versus_aws-l3-dev_scatter/KPC_U_3.png)
![KPC_U](../figures/V19_versus_aws-l3-dev_scatter/KPC_U_4.png)
![KPC_U](../figures/V19_versus_aws-l3-dev_scatter/KPC_U_5.png)
 
## <a id='s0-19' />KPC_Uv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log, wspd_x_i, wspd_y_i
 
![KPC_Uv3](../figures/V19_versus_aws-l3-dev_scatter/KPC_Uv3_0.png)
![KPC_Uv3](../figures/V19_versus_aws-l3-dev_scatter/KPC_Uv3_1.png)
![KPC_Uv3](../figures/V19_versus_aws-l3-dev_scatter/KPC_Uv3_2.png)
![KPC_Uv3](../figures/V19_versus_aws-l3-dev_scatter/KPC_Uv3_3.png)
![KPC_Uv3](../figures/V19_versus_aws-l3-dev_scatter/KPC_Uv3_4.png)
 
## <a id='s0-20' />LYN_L
No old file for this station
## <a id='s0-21' />LYN_T
No old file for this station
## <a id='s0-22' />MIT
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![MIT](../figures/V19_versus_aws-l3-dev_scatter/MIT_0.png)
![MIT](../figures/V19_versus_aws-l3-dev_scatter/MIT_1.png)
![MIT](../figures/V19_versus_aws-l3-dev_scatter/MIT_2.png)
![MIT](../figures/V19_versus_aws-l3-dev_scatter/MIT_3.png)
![MIT](../figures/V19_versus_aws-l3-dev_scatter/MIT_4.png)
 
## <a id='s0-23' />NAE
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt

Old variables removed from new files:
gps_time, gps_hdop, fan_dc_u, fan_dc_l
 
![NAE](../figures/V19_versus_aws-l3-dev_scatter/NAE_0.png)
![NAE](../figures/V19_versus_aws-l3-dev_scatter/NAE_1.png)
![NAE](../figures/V19_versus_aws-l3-dev_scatter/NAE_2.png)
![NAE](../figures/V19_versus_aws-l3-dev_scatter/NAE_3.png)
![NAE](../figures/V19_versus_aws-l3-dev_scatter/NAE_4.png)
![NAE](../figures/V19_versus_aws-l3-dev_scatter/NAE_5.png)
![NAE](../figures/V19_versus_aws-l3-dev_scatter/NAE_6.png)
![NAE](../figures/V19_versus_aws-l3-dev_scatter/NAE_7.png)
 
## <a id='s0-24' />NAU
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt

Old variables removed from new files:
gps_time, gps_hdop, fan_dc_u, fan_dc_l
 
![NAU](../figures/V19_versus_aws-l3-dev_scatter/NAU_0.png)
![NAU](../figures/V19_versus_aws-l3-dev_scatter/NAU_1.png)
![NAU](../figures/V19_versus_aws-l3-dev_scatter/NAU_2.png)
![NAU](../figures/V19_versus_aws-l3-dev_scatter/NAU_3.png)
![NAU](../figures/V19_versus_aws-l3-dev_scatter/NAU_4.png)
![NAU](../figures/V19_versus_aws-l3-dev_scatter/NAU_5.png)
![NAU](../figures/V19_versus_aws-l3-dev_scatter/NAU_6.png)
![NAU](../figures/V19_versus_aws-l3-dev_scatter/NAU_7.png)
 
## <a id='s0-25' />NEM
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt

Old variables removed from new files:
gps_time, gps_hdop, fan_dc_u, fan_dc_l
 
![NEM](../figures/V19_versus_aws-l3-dev_scatter/NEM_0.png)
![NEM](../figures/V19_versus_aws-l3-dev_scatter/NEM_1.png)
![NEM](../figures/V19_versus_aws-l3-dev_scatter/NEM_2.png)
![NEM](../figures/V19_versus_aws-l3-dev_scatter/NEM_3.png)
![NEM](../figures/V19_versus_aws-l3-dev_scatter/NEM_4.png)
![NEM](../figures/V19_versus_aws-l3-dev_scatter/NEM_5.png)
![NEM](../figures/V19_versus_aws-l3-dev_scatter/NEM_6.png)
![NEM](../figures/V19_versus_aws-l3-dev_scatter/NEM_7.png)
 
## <a id='s0-26' />NSE
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt

Old variables removed from new files:
gps_time, gps_hdop, fan_dc_u, fan_dc_l
 
![NSE](../figures/V19_versus_aws-l3-dev_scatter/NSE_0.png)
![NSE](../figures/V19_versus_aws-l3-dev_scatter/NSE_1.png)
![NSE](../figures/V19_versus_aws-l3-dev_scatter/NSE_2.png)
![NSE](../figures/V19_versus_aws-l3-dev_scatter/NSE_3.png)
![NSE](../figures/V19_versus_aws-l3-dev_scatter/NSE_4.png)
![NSE](../figures/V19_versus_aws-l3-dev_scatter/NSE_5.png)
![NSE](../figures/V19_versus_aws-l3-dev_scatter/NSE_6.png)
![NSE](../figures/V19_versus_aws-l3-dev_scatter/NSE_7.png)
 
## <a id='s0-27' />NUK_B
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, z_boom_u, z_stake, z_pt, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
cc, z_surf_combined, z_ice_surf, snow_height, lat, lon, alt

Old variables removed from new files:
z_pt_cor, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![NUK_B](../figures/V19_versus_aws-l3-dev_scatter/NUK_B_0.png)
![NUK_B](../figures/V19_versus_aws-l3-dev_scatter/NUK_B_1.png)
![NUK_B](../figures/V19_versus_aws-l3-dev_scatter/NUK_B_2.png)
![NUK_B](../figures/V19_versus_aws-l3-dev_scatter/NUK_B_3.png)
 
## <a id='s0-28' />NUK_K
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![NUK_K](../figures/V19_versus_aws-l3-dev_scatter/NUK_K_0.png)
![NUK_K](../figures/V19_versus_aws-l3-dev_scatter/NUK_K_1.png)
![NUK_K](../figures/V19_versus_aws-l3-dev_scatter/NUK_K_2.png)
![NUK_K](../figures/V19_versus_aws-l3-dev_scatter/NUK_K_3.png)
![NUK_K](../figures/V19_versus_aws-l3-dev_scatter/NUK_K_4.png)
![NUK_K](../figures/V19_versus_aws-l3-dev_scatter/NUK_K_5.png)
 
## <a id='s0-29' />NUK_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![NUK_L](../figures/V19_versus_aws-l3-dev_scatter/NUK_L_0.png)
![NUK_L](../figures/V19_versus_aws-l3-dev_scatter/NUK_L_1.png)
![NUK_L](../figures/V19_versus_aws-l3-dev_scatter/NUK_L_2.png)
![NUK_L](../figures/V19_versus_aws-l3-dev_scatter/NUK_L_3.png)
![NUK_L](../figures/V19_versus_aws-l3-dev_scatter/NUK_L_4.png)
![NUK_L](../figures/V19_versus_aws-l3-dev_scatter/NUK_L_5.png)
 
## <a id='s0-30' />NUK_N
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![NUK_N](../figures/V19_versus_aws-l3-dev_scatter/NUK_N_0.png)
![NUK_N](../figures/V19_versus_aws-l3-dev_scatter/NUK_N_1.png)
![NUK_N](../figures/V19_versus_aws-l3-dev_scatter/NUK_N_2.png)
![NUK_N](../figures/V19_versus_aws-l3-dev_scatter/NUK_N_3.png)
![NUK_N](../figures/V19_versus_aws-l3-dev_scatter/NUK_N_4.png)
 
## <a id='s0-31' />NUK_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![NUK_U](../figures/V19_versus_aws-l3-dev_scatter/NUK_U_0.png)
![NUK_U](../figures/V19_versus_aws-l3-dev_scatter/NUK_U_1.png)
![NUK_U](../figures/V19_versus_aws-l3-dev_scatter/NUK_U_2.png)
![NUK_U](../figures/V19_versus_aws-l3-dev_scatter/NUK_U_3.png)
![NUK_U](../figures/V19_versus_aws-l3-dev_scatter/NUK_U_4.png)
![NUK_U](../figures/V19_versus_aws-l3-dev_scatter/NUK_U_5.png)
 
## <a id='s0-32' />NUK_Uv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![NUK_Uv3](../figures/V19_versus_aws-l3-dev_scatter/NUK_Uv3_0.png)
![NUK_Uv3](../figures/V19_versus_aws-l3-dev_scatter/NUK_Uv3_1.png)
![NUK_Uv3](../figures/V19_versus_aws-l3-dev_scatter/NUK_Uv3_2.png)
![NUK_Uv3](../figures/V19_versus_aws-l3-dev_scatter/NUK_Uv3_3.png)
![NUK_Uv3](../figures/V19_versus_aws-l3-dev_scatter/NUK_Uv3_4.png)
![NUK_Uv3](../figures/V19_versus_aws-l3-dev_scatter/NUK_Uv3_5.png)
 
## <a id='s0-33' />QAS_A
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![QAS_A](../figures/V19_versus_aws-l3-dev_scatter/QAS_A_0.png)
![QAS_A](../figures/V19_versus_aws-l3-dev_scatter/QAS_A_1.png)
![QAS_A](../figures/V19_versus_aws-l3-dev_scatter/QAS_A_2.png)
![QAS_A](../figures/V19_versus_aws-l3-dev_scatter/QAS_A_3.png)
![QAS_A](../figures/V19_versus_aws-l3-dev_scatter/QAS_A_4.png)
 
## <a id='s0-34' />QAS_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![QAS_L](../figures/V19_versus_aws-l3-dev_scatter/QAS_L_0.png)
![QAS_L](../figures/V19_versus_aws-l3-dev_scatter/QAS_L_1.png)
![QAS_L](../figures/V19_versus_aws-l3-dev_scatter/QAS_L_2.png)
![QAS_L](../figures/V19_versus_aws-l3-dev_scatter/QAS_L_3.png)
![QAS_L](../figures/V19_versus_aws-l3-dev_scatter/QAS_L_4.png)
![QAS_L](../figures/V19_versus_aws-l3-dev_scatter/QAS_L_5.png)
 
## <a id='s0-35' />QAS_Lv3
No old file for this station
## <a id='s0-36' />QAS_M
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![QAS_M](../figures/V19_versus_aws-l3-dev_scatter/QAS_M_0.png)
![QAS_M](../figures/V19_versus_aws-l3-dev_scatter/QAS_M_1.png)
![QAS_M](../figures/V19_versus_aws-l3-dev_scatter/QAS_M_2.png)
![QAS_M](../figures/V19_versus_aws-l3-dev_scatter/QAS_M_3.png)
![QAS_M](../figures/V19_versus_aws-l3-dev_scatter/QAS_M_4.png)
![QAS_M](../figures/V19_versus_aws-l3-dev_scatter/QAS_M_5.png)
 
## <a id='s0-37' />QAS_Mv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![QAS_Mv3](../figures/V19_versus_aws-l3-dev_scatter/QAS_Mv3_0.png)
![QAS_Mv3](../figures/V19_versus_aws-l3-dev_scatter/QAS_Mv3_1.png)
![QAS_Mv3](../figures/V19_versus_aws-l3-dev_scatter/QAS_Mv3_2.png)
![QAS_Mv3](../figures/V19_versus_aws-l3-dev_scatter/QAS_Mv3_3.png)
![QAS_Mv3](../figures/V19_versus_aws-l3-dev_scatter/QAS_Mv3_4.png)
![QAS_Mv3](../figures/V19_versus_aws-l3-dev_scatter/QAS_Mv3_5.png)
 
## <a id='s0-38' />QAS_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![QAS_U](../figures/V19_versus_aws-l3-dev_scatter/QAS_U_0.png)
![QAS_U](../figures/V19_versus_aws-l3-dev_scatter/QAS_U_1.png)
![QAS_U](../figures/V19_versus_aws-l3-dev_scatter/QAS_U_2.png)
![QAS_U](../figures/V19_versus_aws-l3-dev_scatter/QAS_U_3.png)
![QAS_U](../figures/V19_versus_aws-l3-dev_scatter/QAS_U_4.png)
![QAS_U](../figures/V19_versus_aws-l3-dev_scatter/QAS_U_5.png)
 
## <a id='s0-39' />QAS_Uv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![QAS_Uv3](../figures/V19_versus_aws-l3-dev_scatter/QAS_Uv3_0.png)
![QAS_Uv3](../figures/V19_versus_aws-l3-dev_scatter/QAS_Uv3_1.png)
![QAS_Uv3](../figures/V19_versus_aws-l3-dev_scatter/QAS_Uv3_2.png)
![QAS_Uv3](../figures/V19_versus_aws-l3-dev_scatter/QAS_Uv3_3.png)
![QAS_Uv3](../figures/V19_versus_aws-l3-dev_scatter/QAS_Uv3_4.png)
![QAS_Uv3](../figures/V19_versus_aws-l3-dev_scatter/QAS_Uv3_5.png)
 
## <a id='s0-40' />RED_Lv3
No old file for this station
## <a id='s0-41' />Roof_GEUS
No old file for this station
## <a id='s0-42' />SCO_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![SCO_L](../figures/V19_versus_aws-l3-dev_scatter/SCO_L_0.png)
![SCO_L](../figures/V19_versus_aws-l3-dev_scatter/SCO_L_1.png)
![SCO_L](../figures/V19_versus_aws-l3-dev_scatter/SCO_L_2.png)
![SCO_L](../figures/V19_versus_aws-l3-dev_scatter/SCO_L_3.png)
![SCO_L](../figures/V19_versus_aws-l3-dev_scatter/SCO_L_4.png)
![SCO_L](../figures/V19_versus_aws-l3-dev_scatter/SCO_L_5.png)
 
## <a id='s0-43' />SCO_Lv3
No old file for this station
## <a id='s0-44' />SCO_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![SCO_U](../figures/V19_versus_aws-l3-dev_scatter/SCO_U_0.png)
![SCO_U](../figures/V19_versus_aws-l3-dev_scatter/SCO_U_1.png)
![SCO_U](../figures/V19_versus_aws-l3-dev_scatter/SCO_U_2.png)
![SCO_U](../figures/V19_versus_aws-l3-dev_scatter/SCO_U_3.png)
![SCO_U](../figures/V19_versus_aws-l3-dev_scatter/SCO_U_4.png)
![SCO_U](../figures/V19_versus_aws-l3-dev_scatter/SCO_U_5.png)
 
## <a id='s0-45' />SCO_Uv3
No old file for this station
## <a id='s0-46' />SDL
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt

Old variables removed from new files:
gps_time, gps_hdop, fan_dc_u, fan_dc_l
 
![SDL](../figures/V19_versus_aws-l3-dev_scatter/SDL_0.png)
![SDL](../figures/V19_versus_aws-l3-dev_scatter/SDL_1.png)
![SDL](../figures/V19_versus_aws-l3-dev_scatter/SDL_2.png)
![SDL](../figures/V19_versus_aws-l3-dev_scatter/SDL_3.png)
![SDL](../figures/V19_versus_aws-l3-dev_scatter/SDL_4.png)
![SDL](../figures/V19_versus_aws-l3-dev_scatter/SDL_5.png)
![SDL](../figures/V19_versus_aws-l3-dev_scatter/SDL_6.png)
![SDL](../figures/V19_versus_aws-l3-dev_scatter/SDL_7.png)
 
## <a id='s0-47' />SDM
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt

Old variables removed from new files:
gps_time, gps_hdop, fan_dc_u, fan_dc_l
 
![SDM](../figures/V19_versus_aws-l3-dev_scatter/SDM_0.png)
![SDM](../figures/V19_versus_aws-l3-dev_scatter/SDM_1.png)
![SDM](../figures/V19_versus_aws-l3-dev_scatter/SDM_2.png)
![SDM](../figures/V19_versus_aws-l3-dev_scatter/SDM_3.png)
![SDM](../figures/V19_versus_aws-l3-dev_scatter/SDM_4.png)
![SDM](../figures/V19_versus_aws-l3-dev_scatter/SDM_5.png)
![SDM](../figures/V19_versus_aws-l3-dev_scatter/SDM_6.png)
![SDM](../figures/V19_versus_aws-l3-dev_scatter/SDM_7.png)
 
## <a id='s0-48' />SER_B
No old file for this station
## <a id='s0-49' />SWC
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![SWC](../figures/V19_versus_aws-l3-dev_scatter/SWC_0.png)
![SWC](../figures/V19_versus_aws-l3-dev_scatter/SWC_1.png)
![SWC](../figures/V19_versus_aws-l3-dev_scatter/SWC_2.png)
![SWC](../figures/V19_versus_aws-l3-dev_scatter/SWC_3.png)
![SWC](../figures/V19_versus_aws-l3-dev_scatter/SWC_4.png)
![SWC](../figures/V19_versus_aws-l3-dev_scatter/SWC_5.png)
 
## <a id='s0-50' />SWC_O
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![SWC_O](../figures/V19_versus_aws-l3-dev_scatter/SWC_O_0.png)
![SWC_O](../figures/V19_versus_aws-l3-dev_scatter/SWC_O_1.png)
![SWC_O](../figures/V19_versus_aws-l3-dev_scatter/SWC_O_2.png)
![SWC_O](../figures/V19_versus_aws-l3-dev_scatter/SWC_O_3.png)
![SWC_O](../figures/V19_versus_aws-l3-dev_scatter/SWC_O_4.png)
![SWC_O](../figures/V19_versus_aws-l3-dev_scatter/SWC_O_5.png)
 
## <a id='s0-51' />TAS_A
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![TAS_A](../figures/V19_versus_aws-l3-dev_scatter/TAS_A_0.png)
![TAS_A](../figures/V19_versus_aws-l3-dev_scatter/TAS_A_1.png)
![TAS_A](../figures/V19_versus_aws-l3-dev_scatter/TAS_A_2.png)
![TAS_A](../figures/V19_versus_aws-l3-dev_scatter/TAS_A_3.png)
![TAS_A](../figures/V19_versus_aws-l3-dev_scatter/TAS_A_4.png)
![TAS_A](../figures/V19_versus_aws-l3-dev_scatter/TAS_A_5.png)
 
## <a id='s0-52' />TAS_Av3
No old file for this station
## <a id='s0-53' />TAS_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![TAS_L](../figures/V19_versus_aws-l3-dev_scatter/TAS_L_0.png)
![TAS_L](../figures/V19_versus_aws-l3-dev_scatter/TAS_L_1.png)
![TAS_L](../figures/V19_versus_aws-l3-dev_scatter/TAS_L_2.png)
![TAS_L](../figures/V19_versus_aws-l3-dev_scatter/TAS_L_3.png)
![TAS_L](../figures/V19_versus_aws-l3-dev_scatter/TAS_L_4.png)
![TAS_L](../figures/V19_versus_aws-l3-dev_scatter/TAS_L_5.png)
 
## <a id='s0-54' />TAS_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![TAS_U](../figures/V19_versus_aws-l3-dev_scatter/TAS_U_0.png)
![TAS_U](../figures/V19_versus_aws-l3-dev_scatter/TAS_U_1.png)
![TAS_U](../figures/V19_versus_aws-l3-dev_scatter/TAS_U_2.png)
![TAS_U](../figures/V19_versus_aws-l3-dev_scatter/TAS_U_3.png)
![TAS_U](../figures/V19_versus_aws-l3-dev_scatter/TAS_U_4.png)
 
## <a id='s0-55' />THU_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![THU_L](../figures/V19_versus_aws-l3-dev_scatter/THU_L_0.png)
![THU_L](../figures/V19_versus_aws-l3-dev_scatter/THU_L_1.png)
![THU_L](../figures/V19_versus_aws-l3-dev_scatter/THU_L_2.png)
![THU_L](../figures/V19_versus_aws-l3-dev_scatter/THU_L_3.png)
![THU_L](../figures/V19_versus_aws-l3-dev_scatter/THU_L_4.png)
![THU_L](../figures/V19_versus_aws-l3-dev_scatter/THU_L_5.png)
 
## <a id='s0-56' />THU_L2
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![THU_L2](../figures/V19_versus_aws-l3-dev_scatter/THU_L2_0.png)
![THU_L2](../figures/V19_versus_aws-l3-dev_scatter/THU_L2_1.png)
![THU_L2](../figures/V19_versus_aws-l3-dev_scatter/THU_L2_2.png)
![THU_L2](../figures/V19_versus_aws-l3-dev_scatter/THU_L2_3.png)
![THU_L2](../figures/V19_versus_aws-l3-dev_scatter/THU_L2_4.png)
![THU_L2](../figures/V19_versus_aws-l3-dev_scatter/THU_L2_5.png)
 
## <a id='s0-57' />THU_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![THU_U](../figures/V19_versus_aws-l3-dev_scatter/THU_U_0.png)
![THU_U](../figures/V19_versus_aws-l3-dev_scatter/THU_U_1.png)
![THU_U](../figures/V19_versus_aws-l3-dev_scatter/THU_U_2.png)
![THU_U](../figures/V19_versus_aws-l3-dev_scatter/THU_U_3.png)
![THU_U](../figures/V19_versus_aws-l3-dev_scatter/THU_U_4.png)
 
## <a id='s0-58' />THU_U2
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![THU_U2](../figures/V19_versus_aws-l3-dev_scatter/THU_U2_0.png)
![THU_U2](../figures/V19_versus_aws-l3-dev_scatter/THU_U2_1.png)
![THU_U2](../figures/V19_versus_aws-l3-dev_scatter/THU_U2_2.png)
![THU_U2](../figures/V19_versus_aws-l3-dev_scatter/THU_U2_3.png)
![THU_U2](../figures/V19_versus_aws-l3-dev_scatter/THU_U2_4.png)
![THU_U2](../figures/V19_versus_aws-l3-dev_scatter/THU_U2_5.png)
 
## <a id='s0-59' />THU_U2v3
No old file for this station
## <a id='s0-60' />TUN
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, d_t_i_9, d_t_i_10, d_t_i_11, t_i_10m, lat, lon, alt

Old variables removed from new files:
gps_time, gps_hdop, fan_dc_u, fan_dc_l
 
![TUN](../figures/V19_versus_aws-l3-dev_scatter/TUN_0.png)
![TUN](../figures/V19_versus_aws-l3-dev_scatter/TUN_1.png)
![TUN](../figures/V19_versus_aws-l3-dev_scatter/TUN_2.png)
![TUN](../figures/V19_versus_aws-l3-dev_scatter/TUN_3.png)
![TUN](../figures/V19_versus_aws-l3-dev_scatter/TUN_4.png)
![TUN](../figures/V19_versus_aws-l3-dev_scatter/TUN_5.png)
![TUN](../figures/V19_versus_aws-l3-dev_scatter/TUN_6.png)
![TUN](../figures/V19_versus_aws-l3-dev_scatter/TUN_7.png)
 
## <a id='s0-61' />UPE_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![UPE_L](../figures/V19_versus_aws-l3-dev_scatter/UPE_L_0.png)
![UPE_L](../figures/V19_versus_aws-l3-dev_scatter/UPE_L_1.png)
![UPE_L](../figures/V19_versus_aws-l3-dev_scatter/UPE_L_2.png)
![UPE_L](../figures/V19_versus_aws-l3-dev_scatter/UPE_L_3.png)
![UPE_L](../figures/V19_versus_aws-l3-dev_scatter/UPE_L_4.png)
![UPE_L](../figures/V19_versus_aws-l3-dev_scatter/UPE_L_5.png)
 
## <a id='s0-62' />UPE_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![UPE_U](../figures/V19_versus_aws-l3-dev_scatter/UPE_U_0.png)
![UPE_U](../figures/V19_versus_aws-l3-dev_scatter/UPE_U_1.png)
![UPE_U](../figures/V19_versus_aws-l3-dev_scatter/UPE_U_2.png)
![UPE_U](../figures/V19_versus_aws-l3-dev_scatter/UPE_U_3.png)
![UPE_U](../figures/V19_versus_aws-l3-dev_scatter/UPE_U_4.png)
![UPE_U](../figures/V19_versus_aws-l3-dev_scatter/UPE_U_5.png)
 
## <a id='s0-63' />UWN
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, z_surf_combined, z_ice_surf, snow_height, precip_u, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_surf_combined, z_ice_surf, snow_height, d_t_i_1, d_t_i_2, d_t_i_3, d_t_i_4, d_t_i_5, d_t_i_6, d_t_i_7, d_t_i_8, t_i_10m, lat, lon, alt

Old variables removed from new files:
precip_u_cor, precip_u_rate, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![UWN](../figures/V19_versus_aws-l3-dev_scatter/UWN_0.png)
![UWN](../figures/V19_versus_aws-l3-dev_scatter/UWN_1.png)
![UWN](../figures/V19_versus_aws-l3-dev_scatter/UWN_2.png)
![UWN](../figures/V19_versus_aws-l3-dev_scatter/UWN_3.png)
![UWN](../figures/V19_versus_aws-l3-dev_scatter/UWN_4.png)
![UWN](../figures/V19_versus_aws-l3-dev_scatter/UWN_5.png)
 
## <a id='s0-64' />WEG_B
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, z_boom_u, z_stake, z_pt, z_surf_combined, z_ice_surf, snow_height, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, lat, lon, alt, batt_v, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
cc, z_surf_combined, z_ice_surf, snow_height, lat, lon, alt

Old variables removed from new files:
z_pt_cor, gps_time, gps_geoid, gps_hdop, fan_dc_u, t_log
 
![WEG_B](../figures/V19_versus_aws-l3-dev_scatter/WEG_B_0.png)
![WEG_B](../figures/V19_versus_aws-l3-dev_scatter/WEG_B_1.png)
![WEG_B](../figures/V19_versus_aws-l3-dev_scatter/WEG_B_2.png)
![WEG_B](../figures/V19_versus_aws-l3-dev_scatter/WEG_B_3.png)
![WEG_B](../figures/V19_versus_aws-l3-dev_scatter/WEG_B_4.png)
 
## <a id='s0-65' />WEG_L
No old file for this station
## <a id='s0-66' />XXX
No old file for this station
## <a id='s0-67' />ZAC_A
No old file for this station
## <a id='s0-68' />ZAC_Lv3
No old file for this station
## <a id='s0-69' />ZAC_Uv3
No old file for this station
## <a id='s0-70' />ZAK_A
No new file for this station
## <a id='s0-71' />ZAK_Lv3
No new file for this station
## <a id='s0-72' />ZAK_Uv3
No new file for this station
