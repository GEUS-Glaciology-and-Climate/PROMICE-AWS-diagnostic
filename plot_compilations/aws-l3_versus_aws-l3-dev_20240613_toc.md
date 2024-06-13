* [Comparison of data aws-l3-dev to aws-l3 (old).](#s1)
  * [CEN1](#s1-1)
  * [CEN2](#s1-2)
  * [CP1](#s1-3)
  * [DY2](#s1-4)
  * [EGP](#s1-5)
  * [FRE](#s1-6)
  * [HUM](#s1-7)
  * [JAR](#s1-8)
  * [JAR_O](#s1-9)
  * [KAN_B](#s1-10)
  * [KAN_L](#s1-11)
  * [KAN_Lv3](#s1-12)
  * [KAN_M](#s1-13)
  * [KAN_Tv3](#s1-14)
  * [KAN_U](#s1-15)
  * [KPC_L](#s1-16)
  * [KPC_Lv3](#s1-17)
  * [KPC_U](#s1-18)
  * [KPC_Uv3](#s1-19)
  * [LYN_L](#s1-20)
  * [LYN_T](#s1-21)
  * [MIT](#s1-22)
  * [NAE](#s1-23)
  * [NAU](#s1-24)
  * [NEM](#s1-25)
  * [NSE](#s1-26)
  * [NUK_B](#s1-27)
  * [NUK_K](#s1-28)
  * [NUK_L](#s1-29)
  * [NUK_N](#s1-30)
  * [NUK_U](#s1-31)
  * [NUK_Uv3](#s1-32)
  * [QAS_A](#s1-33)
  * [QAS_L](#s1-34)
  * [QAS_Lv3](#s1-35)
  * [QAS_M](#s1-36)
  * [QAS_Mv3](#s1-37)
  * [QAS_U](#s1-38)
  * [QAS_Uv3](#s1-39)
  * [Roof_GEUS](#s1-40)
  * [Roof_PROMICE](#s1-41)
  * [SCO_L](#s1-42)
  * [SCO_U](#s1-43)
  * [SDL](#s1-44)
  * [SDM](#s1-45)
  * [SWC](#s1-46)
  * [SWC_O](#s1-47)
  * [TAS_A](#s1-48)
  * [TAS_L](#s1-49)
  * [TAS_U](#s1-50)
  * [THU_L](#s1-51)
  * [THU_L2](#s1-52)
  * [THU_U](#s1-53)
  * [THU_U2](#s1-54)
  * [THU_U2v3](#s1-55)
  * [TUN](#s1-56)
  * [UPE_L](#s1-57)
  * [UPE_U](#s1-58)
  * [UWN](#s1-59)
  * [WEG_B](#s1-60)
  * [WEG_L](#s1-61)
  * [XXX](#s1-62)
  * [ZAK_A](#s1-63)
  * [ZAK_L](#s1-64)
  * [ZAK_Lv3](#s1-65)
  * [ZAK_U](#s1-66)
  * [ZAK_Uv3](#s1-67)
# <a id='s1' />Comparison of data aws-l3-dev to aws-l3 (old).
## <a id='s1-1' />CEN1
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![CEN1](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN1_0.png)
![CEN1](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN1_1.png)
![CEN1](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN1_2.png)
![CEN1](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN1_3.png)
![CEN1](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN1_4.png)
![CEN1](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN1_5.png)
![CEN1](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN1_6.png)
![CEN1](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN1_7.png)
![CEN1](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN1_8.png)
![CEN1](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN1_9.png)
![CEN1](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN1_10.png)
![CEN1](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN1_11.png)
 
## <a id='s1-2' />CEN2
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_numsat, gps_q, batt_v, fan_dc_u, fan_dc_l, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_geoid, gps_numsat, gps_q, t_log

Old variables removed from new files:

 
![CEN2](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN2_0.png)
![CEN2](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN2_1.png)
![CEN2](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN2_2.png)
![CEN2](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN2_3.png)
![CEN2](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN2_4.png)
![CEN2](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN2_5.png)
![CEN2](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN2_6.png)
![CEN2](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN2_7.png)
![CEN2](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN2_8.png)
![CEN2](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN2_9.png)
![CEN2](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN2_10.png)
![CEN2](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN2_11.png)
![CEN2](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN2_12.png)
![CEN2](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN2_13.png)
![CEN2](../figures/aws-l3_versus_aws-l3-dev_20240613/CEN2_14.png)
 
## <a id='s1-3' />CP1
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_numsat, gps_q, batt_v, fan_dc_u, fan_dc_l, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_geoid, gps_numsat, gps_q, t_log

Old variables removed from new files:

 
![CP1](../figures/aws-l3_versus_aws-l3-dev_20240613/CP1_0.png)
![CP1](../figures/aws-l3_versus_aws-l3-dev_20240613/CP1_1.png)
![CP1](../figures/aws-l3_versus_aws-l3-dev_20240613/CP1_2.png)
![CP1](../figures/aws-l3_versus_aws-l3-dev_20240613/CP1_3.png)
![CP1](../figures/aws-l3_versus_aws-l3-dev_20240613/CP1_4.png)
![CP1](../figures/aws-l3_versus_aws-l3-dev_20240613/CP1_5.png)
![CP1](../figures/aws-l3_versus_aws-l3-dev_20240613/CP1_6.png)
![CP1](../figures/aws-l3_versus_aws-l3-dev_20240613/CP1_7.png)
![CP1](../figures/aws-l3_versus_aws-l3-dev_20240613/CP1_8.png)
![CP1](../figures/aws-l3_versus_aws-l3-dev_20240613/CP1_9.png)
![CP1](../figures/aws-l3_versus_aws-l3-dev_20240613/CP1_10.png)
![CP1](../figures/aws-l3_versus_aws-l3-dev_20240613/CP1_11.png)
![CP1](../figures/aws-l3_versus_aws-l3-dev_20240613/CP1_12.png)
![CP1](../figures/aws-l3_versus_aws-l3-dev_20240613/CP1_13.png)
![CP1](../figures/aws-l3_versus_aws-l3-dev_20240613/CP1_14.png)
 
## <a id='s1-4' />DY2
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_numsat, gps_q, batt_v, fan_dc_u, fan_dc_l, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_geoid, gps_numsat, gps_q, t_log

Old variables removed from new files:

 
![DY2](../figures/aws-l3_versus_aws-l3-dev_20240613/DY2_0.png)
![DY2](../figures/aws-l3_versus_aws-l3-dev_20240613/DY2_1.png)
![DY2](../figures/aws-l3_versus_aws-l3-dev_20240613/DY2_2.png)
![DY2](../figures/aws-l3_versus_aws-l3-dev_20240613/DY2_3.png)
![DY2](../figures/aws-l3_versus_aws-l3-dev_20240613/DY2_4.png)
![DY2](../figures/aws-l3_versus_aws-l3-dev_20240613/DY2_5.png)
![DY2](../figures/aws-l3_versus_aws-l3-dev_20240613/DY2_6.png)
![DY2](../figures/aws-l3_versus_aws-l3-dev_20240613/DY2_7.png)
![DY2](../figures/aws-l3_versus_aws-l3-dev_20240613/DY2_8.png)
![DY2](../figures/aws-l3_versus_aws-l3-dev_20240613/DY2_9.png)
![DY2](../figures/aws-l3_versus_aws-l3-dev_20240613/DY2_10.png)
![DY2](../figures/aws-l3_versus_aws-l3-dev_20240613/DY2_11.png)
![DY2](../figures/aws-l3_versus_aws-l3-dev_20240613/DY2_12.png)
![DY2](../figures/aws-l3_versus_aws-l3-dev_20240613/DY2_13.png)
![DY2](../figures/aws-l3_versus_aws-l3-dev_20240613/DY2_14.png)
 
## <a id='s1-5' />EGP
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![EGP](../figures/aws-l3_versus_aws-l3-dev_20240613/EGP_0.png)
![EGP](../figures/aws-l3_versus_aws-l3-dev_20240613/EGP_1.png)
![EGP](../figures/aws-l3_versus_aws-l3-dev_20240613/EGP_2.png)
![EGP](../figures/aws-l3_versus_aws-l3-dev_20240613/EGP_3.png)
![EGP](../figures/aws-l3_versus_aws-l3-dev_20240613/EGP_4.png)
![EGP](../figures/aws-l3_versus_aws-l3-dev_20240613/EGP_5.png)
![EGP](../figures/aws-l3_versus_aws-l3-dev_20240613/EGP_6.png)
![EGP](../figures/aws-l3_versus_aws-l3-dev_20240613/EGP_7.png)
![EGP](../figures/aws-l3_versus_aws-l3-dev_20240613/EGP_8.png)
![EGP](../figures/aws-l3_versus_aws-l3-dev_20240613/EGP_9.png)
![EGP](../figures/aws-l3_versus_aws-l3-dev_20240613/EGP_10.png)
![EGP](../figures/aws-l3_versus_aws-l3-dev_20240613/EGP_11.png)
 
## <a id='s1-6' />FRE
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![FRE](../figures/aws-l3_versus_aws-l3-dev_20240613/FRE_0.png)
![FRE](../figures/aws-l3_versus_aws-l3-dev_20240613/FRE_1.png)
![FRE](../figures/aws-l3_versus_aws-l3-dev_20240613/FRE_2.png)
![FRE](../figures/aws-l3_versus_aws-l3-dev_20240613/FRE_3.png)
![FRE](../figures/aws-l3_versus_aws-l3-dev_20240613/FRE_4.png)
![FRE](../figures/aws-l3_versus_aws-l3-dev_20240613/FRE_5.png)
![FRE](../figures/aws-l3_versus_aws-l3-dev_20240613/FRE_6.png)
![FRE](../figures/aws-l3_versus_aws-l3-dev_20240613/FRE_7.png)
![FRE](../figures/aws-l3_versus_aws-l3-dev_20240613/FRE_8.png)
![FRE](../figures/aws-l3_versus_aws-l3-dev_20240613/FRE_9.png)
![FRE](../figures/aws-l3_versus_aws-l3-dev_20240613/FRE_10.png)
![FRE](../figures/aws-l3_versus_aws-l3-dev_20240613/FRE_11.png)
 
## <a id='s1-7' />HUM
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_numsat, gps_q, batt_v, fan_dc_u, fan_dc_l, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_geoid, gps_numsat, gps_q, t_log

Old variables removed from new files:

 
![HUM](../figures/aws-l3_versus_aws-l3-dev_20240613/HUM_0.png)
![HUM](../figures/aws-l3_versus_aws-l3-dev_20240613/HUM_1.png)
![HUM](../figures/aws-l3_versus_aws-l3-dev_20240613/HUM_2.png)
![HUM](../figures/aws-l3_versus_aws-l3-dev_20240613/HUM_3.png)
![HUM](../figures/aws-l3_versus_aws-l3-dev_20240613/HUM_4.png)
![HUM](../figures/aws-l3_versus_aws-l3-dev_20240613/HUM_5.png)
![HUM](../figures/aws-l3_versus_aws-l3-dev_20240613/HUM_6.png)
![HUM](../figures/aws-l3_versus_aws-l3-dev_20240613/HUM_7.png)
![HUM](../figures/aws-l3_versus_aws-l3-dev_20240613/HUM_8.png)
![HUM](../figures/aws-l3_versus_aws-l3-dev_20240613/HUM_9.png)
![HUM](../figures/aws-l3_versus_aws-l3-dev_20240613/HUM_10.png)
![HUM](../figures/aws-l3_versus_aws-l3-dev_20240613/HUM_11.png)
![HUM](../figures/aws-l3_versus_aws-l3-dev_20240613/HUM_12.png)
![HUM](../figures/aws-l3_versus_aws-l3-dev_20240613/HUM_13.png)
![HUM](../figures/aws-l3_versus_aws-l3-dev_20240613/HUM_14.png)
 
## <a id='s1-8' />JAR
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![JAR](../figures/aws-l3_versus_aws-l3-dev_20240613/JAR_0.png)
![JAR](../figures/aws-l3_versus_aws-l3-dev_20240613/JAR_1.png)
![JAR](../figures/aws-l3_versus_aws-l3-dev_20240613/JAR_2.png)
![JAR](../figures/aws-l3_versus_aws-l3-dev_20240613/JAR_3.png)
![JAR](../figures/aws-l3_versus_aws-l3-dev_20240613/JAR_4.png)
![JAR](../figures/aws-l3_versus_aws-l3-dev_20240613/JAR_5.png)
![JAR](../figures/aws-l3_versus_aws-l3-dev_20240613/JAR_6.png)
![JAR](../figures/aws-l3_versus_aws-l3-dev_20240613/JAR_7.png)
![JAR](../figures/aws-l3_versus_aws-l3-dev_20240613/JAR_8.png)
![JAR](../figures/aws-l3_versus_aws-l3-dev_20240613/JAR_9.png)
![JAR](../figures/aws-l3_versus_aws-l3-dev_20240613/JAR_10.png)
![JAR](../figures/aws-l3_versus_aws-l3-dev_20240613/JAR_11.png)
 
## <a id='s1-9' />JAR_O
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![JAR_O](../figures/aws-l3_versus_aws-l3-dev_20240613/JAR_O_0.png)
![JAR_O](../figures/aws-l3_versus_aws-l3-dev_20240613/JAR_O_1.png)
![JAR_O](../figures/aws-l3_versus_aws-l3-dev_20240613/JAR_O_2.png)
![JAR_O](../figures/aws-l3_versus_aws-l3-dev_20240613/JAR_O_3.png)
![JAR_O](../figures/aws-l3_versus_aws-l3-dev_20240613/JAR_O_4.png)
![JAR_O](../figures/aws-l3_versus_aws-l3-dev_20240613/JAR_O_5.png)
![JAR_O](../figures/aws-l3_versus_aws-l3-dev_20240613/JAR_O_6.png)
![JAR_O](../figures/aws-l3_versus_aws-l3-dev_20240613/JAR_O_7.png)
![JAR_O](../figures/aws-l3_versus_aws-l3-dev_20240613/JAR_O_8.png)
![JAR_O](../figures/aws-l3_versus_aws-l3-dev_20240613/JAR_O_9.png)
![JAR_O](../figures/aws-l3_versus_aws-l3-dev_20240613/JAR_O_10.png)
![JAR_O](../figures/aws-l3_versus_aws-l3-dev_20240613/JAR_O_11.png)
 
## <a id='s1-10' />KAN_B
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, t_surf, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
batt_v_ss

Old variables removed from new files:

 
![KAN_B](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_B_0.png)
![KAN_B](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_B_1.png)
![KAN_B](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_B_2.png)
![KAN_B](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_B_3.png)
![KAN_B](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_B_4.png)
![KAN_B](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_B_5.png)
![KAN_B](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_B_6.png)
![KAN_B](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_B_7.png)
![KAN_B](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_B_8.png)
![KAN_B](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_B_9.png)
![KAN_B](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_B_10.png)
 
## <a id='s1-11' />KAN_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![KAN_L](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_L_0.png)
![KAN_L](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_L_1.png)
![KAN_L](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_L_2.png)
![KAN_L](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_L_3.png)
![KAN_L](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_L_4.png)
![KAN_L](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_L_5.png)
![KAN_L](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_L_6.png)
![KAN_L](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_L_7.png)
![KAN_L](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_L_8.png)
![KAN_L](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_L_9.png)
![KAN_L](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_L_10.png)
![KAN_L](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_L_11.png)
 
## <a id='s1-12' />KAN_Lv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![KAN_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_Lv3_0.png)
![KAN_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_Lv3_1.png)
![KAN_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_Lv3_2.png)
![KAN_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_Lv3_3.png)
![KAN_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_Lv3_4.png)
![KAN_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_Lv3_5.png)
![KAN_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_Lv3_6.png)
![KAN_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_Lv3_7.png)
![KAN_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_Lv3_8.png)
![KAN_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_Lv3_9.png)
![KAN_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_Lv3_10.png)
![KAN_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_Lv3_11.png)
 
## <a id='s1-13' />KAN_M
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![KAN_M](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_M_0.png)
![KAN_M](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_M_1.png)
![KAN_M](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_M_2.png)
![KAN_M](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_M_3.png)
![KAN_M](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_M_4.png)
![KAN_M](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_M_5.png)
![KAN_M](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_M_6.png)
![KAN_M](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_M_7.png)
![KAN_M](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_M_8.png)
![KAN_M](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_M_9.png)
![KAN_M](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_M_10.png)
![KAN_M](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_M_11.png)
 
## <a id='s1-14' />KAN_Tv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![KAN_Tv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_Tv3_0.png)
![KAN_Tv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_Tv3_1.png)
![KAN_Tv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_Tv3_2.png)
![KAN_Tv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_Tv3_3.png)
![KAN_Tv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_Tv3_4.png)
![KAN_Tv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_Tv3_5.png)
![KAN_Tv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_Tv3_6.png)
![KAN_Tv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_Tv3_7.png)
![KAN_Tv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_Tv3_8.png)
![KAN_Tv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_Tv3_9.png)
![KAN_Tv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_Tv3_10.png)
![KAN_Tv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_Tv3_11.png)
 
## <a id='s1-15' />KAN_U
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, fan_dc_l, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_stake, z_pt, z_pt_cor, gps_geoid, gps_q, batt_v_ss, t_log

Old variables removed from new files:

 
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_U_0.png)
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_U_1.png)
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_U_2.png)
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_U_3.png)
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_U_4.png)
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_U_5.png)
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_U_6.png)
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_U_7.png)
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_U_8.png)
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_U_9.png)
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_U_10.png)
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_U_11.png)
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_U_12.png)
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_U_13.png)
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_U_14.png)
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KAN_U_15.png)
 
## <a id='s1-16' />KPC_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![KPC_L](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_L_0.png)
![KPC_L](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_L_1.png)
![KPC_L](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_L_2.png)
![KPC_L](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_L_3.png)
![KPC_L](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_L_4.png)
![KPC_L](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_L_5.png)
![KPC_L](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_L_6.png)
![KPC_L](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_L_7.png)
![KPC_L](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_L_8.png)
![KPC_L](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_L_9.png)
![KPC_L](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_L_10.png)
![KPC_L](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_L_11.png)
 
## <a id='s1-17' />KPC_Lv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![KPC_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_Lv3_0.png)
![KPC_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_Lv3_1.png)
![KPC_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_Lv3_2.png)
![KPC_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_Lv3_3.png)
![KPC_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_Lv3_4.png)
![KPC_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_Lv3_5.png)
![KPC_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_Lv3_6.png)
![KPC_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_Lv3_7.png)
![KPC_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_Lv3_8.png)
![KPC_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_Lv3_9.png)
![KPC_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_Lv3_10.png)
![KPC_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_Lv3_11.png)
 
## <a id='s1-18' />KPC_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![KPC_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_U_0.png)
![KPC_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_U_1.png)
![KPC_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_U_2.png)
![KPC_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_U_3.png)
![KPC_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_U_4.png)
![KPC_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_U_5.png)
![KPC_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_U_6.png)
![KPC_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_U_7.png)
![KPC_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_U_8.png)
![KPC_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_U_9.png)
![KPC_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_U_10.png)
![KPC_U](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_U_11.png)
 
## <a id='s1-19' />KPC_Uv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![KPC_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_Uv3_0.png)
![KPC_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_Uv3_1.png)
![KPC_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_Uv3_2.png)
![KPC_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_Uv3_3.png)
![KPC_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_Uv3_4.png)
![KPC_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_Uv3_5.png)
![KPC_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_Uv3_6.png)
![KPC_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_Uv3_7.png)
![KPC_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_Uv3_8.png)
![KPC_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_Uv3_9.png)
![KPC_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_Uv3_10.png)
![KPC_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/KPC_Uv3_11.png)
 
## <a id='s1-20' />LYN_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![LYN_L](../figures/aws-l3_versus_aws-l3-dev_20240613/LYN_L_0.png)
![LYN_L](../figures/aws-l3_versus_aws-l3-dev_20240613/LYN_L_1.png)
![LYN_L](../figures/aws-l3_versus_aws-l3-dev_20240613/LYN_L_2.png)
![LYN_L](../figures/aws-l3_versus_aws-l3-dev_20240613/LYN_L_3.png)
![LYN_L](../figures/aws-l3_versus_aws-l3-dev_20240613/LYN_L_4.png)
![LYN_L](../figures/aws-l3_versus_aws-l3-dev_20240613/LYN_L_5.png)
![LYN_L](../figures/aws-l3_versus_aws-l3-dev_20240613/LYN_L_6.png)
![LYN_L](../figures/aws-l3_versus_aws-l3-dev_20240613/LYN_L_7.png)
![LYN_L](../figures/aws-l3_versus_aws-l3-dev_20240613/LYN_L_8.png)
![LYN_L](../figures/aws-l3_versus_aws-l3-dev_20240613/LYN_L_9.png)
![LYN_L](../figures/aws-l3_versus_aws-l3-dev_20240613/LYN_L_10.png)
![LYN_L](../figures/aws-l3_versus_aws-l3-dev_20240613/LYN_L_11.png)
 
## <a id='s1-21' />LYN_T
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![LYN_T](../figures/aws-l3_versus_aws-l3-dev_20240613/LYN_T_0.png)
![LYN_T](../figures/aws-l3_versus_aws-l3-dev_20240613/LYN_T_1.png)
![LYN_T](../figures/aws-l3_versus_aws-l3-dev_20240613/LYN_T_2.png)
![LYN_T](../figures/aws-l3_versus_aws-l3-dev_20240613/LYN_T_3.png)
![LYN_T](../figures/aws-l3_versus_aws-l3-dev_20240613/LYN_T_4.png)
![LYN_T](../figures/aws-l3_versus_aws-l3-dev_20240613/LYN_T_5.png)
![LYN_T](../figures/aws-l3_versus_aws-l3-dev_20240613/LYN_T_6.png)
![LYN_T](../figures/aws-l3_versus_aws-l3-dev_20240613/LYN_T_7.png)
![LYN_T](../figures/aws-l3_versus_aws-l3-dev_20240613/LYN_T_8.png)
![LYN_T](../figures/aws-l3_versus_aws-l3-dev_20240613/LYN_T_9.png)
![LYN_T](../figures/aws-l3_versus_aws-l3-dev_20240613/LYN_T_10.png)
![LYN_T](../figures/aws-l3_versus_aws-l3-dev_20240613/LYN_T_11.png)
 
## <a id='s1-22' />MIT
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![MIT](../figures/aws-l3_versus_aws-l3-dev_20240613/MIT_0.png)
![MIT](../figures/aws-l3_versus_aws-l3-dev_20240613/MIT_1.png)
![MIT](../figures/aws-l3_versus_aws-l3-dev_20240613/MIT_2.png)
![MIT](../figures/aws-l3_versus_aws-l3-dev_20240613/MIT_3.png)
![MIT](../figures/aws-l3_versus_aws-l3-dev_20240613/MIT_4.png)
![MIT](../figures/aws-l3_versus_aws-l3-dev_20240613/MIT_5.png)
![MIT](../figures/aws-l3_versus_aws-l3-dev_20240613/MIT_6.png)
![MIT](../figures/aws-l3_versus_aws-l3-dev_20240613/MIT_7.png)
![MIT](../figures/aws-l3_versus_aws-l3-dev_20240613/MIT_8.png)
![MIT](../figures/aws-l3_versus_aws-l3-dev_20240613/MIT_9.png)
![MIT](../figures/aws-l3_versus_aws-l3-dev_20240613/MIT_10.png)
![MIT](../figures/aws-l3_versus_aws-l3-dev_20240613/MIT_11.png)
 
## <a id='s1-23' />NAE
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_hdop, batt_v, fan_dc_u, fan_dc_l, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![NAE](../figures/aws-l3_versus_aws-l3-dev_20240613/NAE_0.png)
![NAE](../figures/aws-l3_versus_aws-l3-dev_20240613/NAE_1.png)
![NAE](../figures/aws-l3_versus_aws-l3-dev_20240613/NAE_2.png)
![NAE](../figures/aws-l3_versus_aws-l3-dev_20240613/NAE_3.png)
![NAE](../figures/aws-l3_versus_aws-l3-dev_20240613/NAE_4.png)
![NAE](../figures/aws-l3_versus_aws-l3-dev_20240613/NAE_5.png)
![NAE](../figures/aws-l3_versus_aws-l3-dev_20240613/NAE_6.png)
![NAE](../figures/aws-l3_versus_aws-l3-dev_20240613/NAE_7.png)
![NAE](../figures/aws-l3_versus_aws-l3-dev_20240613/NAE_8.png)
![NAE](../figures/aws-l3_versus_aws-l3-dev_20240613/NAE_9.png)
![NAE](../figures/aws-l3_versus_aws-l3-dev_20240613/NAE_10.png)
![NAE](../figures/aws-l3_versus_aws-l3-dev_20240613/NAE_11.png)
![NAE](../figures/aws-l3_versus_aws-l3-dev_20240613/NAE_12.png)
![NAE](../figures/aws-l3_versus_aws-l3-dev_20240613/NAE_13.png)
 
## <a id='s1-24' />NAU
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_numsat, gps_q, batt_v, fan_dc_u, fan_dc_l, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_geoid, gps_numsat, gps_q, t_log

Old variables removed from new files:

 
![NAU](../figures/aws-l3_versus_aws-l3-dev_20240613/NAU_0.png)
![NAU](../figures/aws-l3_versus_aws-l3-dev_20240613/NAU_1.png)
![NAU](../figures/aws-l3_versus_aws-l3-dev_20240613/NAU_2.png)
![NAU](../figures/aws-l3_versus_aws-l3-dev_20240613/NAU_3.png)
![NAU](../figures/aws-l3_versus_aws-l3-dev_20240613/NAU_4.png)
![NAU](../figures/aws-l3_versus_aws-l3-dev_20240613/NAU_5.png)
![NAU](../figures/aws-l3_versus_aws-l3-dev_20240613/NAU_6.png)
![NAU](../figures/aws-l3_versus_aws-l3-dev_20240613/NAU_7.png)
![NAU](../figures/aws-l3_versus_aws-l3-dev_20240613/NAU_8.png)
![NAU](../figures/aws-l3_versus_aws-l3-dev_20240613/NAU_9.png)
![NAU](../figures/aws-l3_versus_aws-l3-dev_20240613/NAU_10.png)
![NAU](../figures/aws-l3_versus_aws-l3-dev_20240613/NAU_11.png)
![NAU](../figures/aws-l3_versus_aws-l3-dev_20240613/NAU_12.png)
![NAU](../figures/aws-l3_versus_aws-l3-dev_20240613/NAU_13.png)
![NAU](../figures/aws-l3_versus_aws-l3-dev_20240613/NAU_14.png)
 
## <a id='s1-25' />NEM
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_hdop, batt_v, fan_dc_u, fan_dc_l, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![NEM](../figures/aws-l3_versus_aws-l3-dev_20240613/NEM_0.png)
![NEM](../figures/aws-l3_versus_aws-l3-dev_20240613/NEM_1.png)
![NEM](../figures/aws-l3_versus_aws-l3-dev_20240613/NEM_2.png)
![NEM](../figures/aws-l3_versus_aws-l3-dev_20240613/NEM_3.png)
![NEM](../figures/aws-l3_versus_aws-l3-dev_20240613/NEM_4.png)
![NEM](../figures/aws-l3_versus_aws-l3-dev_20240613/NEM_5.png)
![NEM](../figures/aws-l3_versus_aws-l3-dev_20240613/NEM_6.png)
![NEM](../figures/aws-l3_versus_aws-l3-dev_20240613/NEM_7.png)
![NEM](../figures/aws-l3_versus_aws-l3-dev_20240613/NEM_8.png)
![NEM](../figures/aws-l3_versus_aws-l3-dev_20240613/NEM_9.png)
![NEM](../figures/aws-l3_versus_aws-l3-dev_20240613/NEM_10.png)
![NEM](../figures/aws-l3_versus_aws-l3-dev_20240613/NEM_11.png)
![NEM](../figures/aws-l3_versus_aws-l3-dev_20240613/NEM_12.png)
![NEM](../figures/aws-l3_versus_aws-l3-dev_20240613/NEM_13.png)
 
## <a id='s1-26' />NSE
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_numsat, gps_q, batt_v, fan_dc_u, fan_dc_l, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_geoid, gps_numsat, gps_q, t_log

Old variables removed from new files:

 
![NSE](../figures/aws-l3_versus_aws-l3-dev_20240613/NSE_0.png)
![NSE](../figures/aws-l3_versus_aws-l3-dev_20240613/NSE_1.png)
![NSE](../figures/aws-l3_versus_aws-l3-dev_20240613/NSE_2.png)
![NSE](../figures/aws-l3_versus_aws-l3-dev_20240613/NSE_3.png)
![NSE](../figures/aws-l3_versus_aws-l3-dev_20240613/NSE_4.png)
![NSE](../figures/aws-l3_versus_aws-l3-dev_20240613/NSE_5.png)
![NSE](../figures/aws-l3_versus_aws-l3-dev_20240613/NSE_6.png)
![NSE](../figures/aws-l3_versus_aws-l3-dev_20240613/NSE_7.png)
![NSE](../figures/aws-l3_versus_aws-l3-dev_20240613/NSE_8.png)
![NSE](../figures/aws-l3_versus_aws-l3-dev_20240613/NSE_9.png)
![NSE](../figures/aws-l3_versus_aws-l3-dev_20240613/NSE_10.png)
![NSE](../figures/aws-l3_versus_aws-l3-dev_20240613/NSE_11.png)
![NSE](../figures/aws-l3_versus_aws-l3-dev_20240613/NSE_12.png)
![NSE](../figures/aws-l3_versus_aws-l3-dev_20240613/NSE_13.png)
![NSE](../figures/aws-l3_versus_aws-l3-dev_20240613/NSE_14.png)
 
## <a id='s1-27' />NUK_B
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, t_surf, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![NUK_B](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_B_0.png)
![NUK_B](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_B_1.png)
![NUK_B](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_B_2.png)
![NUK_B](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_B_3.png)
![NUK_B](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_B_4.png)
![NUK_B](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_B_5.png)
![NUK_B](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_B_6.png)
![NUK_B](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_B_7.png)
![NUK_B](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_B_8.png)
![NUK_B](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_B_9.png)
![NUK_B](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_B_10.png)
 
## <a id='s1-28' />NUK_K
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![NUK_K](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_K_0.png)
![NUK_K](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_K_1.png)
![NUK_K](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_K_2.png)
![NUK_K](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_K_3.png)
![NUK_K](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_K_4.png)
![NUK_K](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_K_5.png)
![NUK_K](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_K_6.png)
![NUK_K](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_K_7.png)
![NUK_K](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_K_8.png)
![NUK_K](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_K_9.png)
![NUK_K](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_K_10.png)
![NUK_K](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_K_11.png)
 
## <a id='s1-29' />NUK_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![NUK_L](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_L_0.png)
![NUK_L](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_L_1.png)
![NUK_L](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_L_2.png)
![NUK_L](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_L_3.png)
![NUK_L](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_L_4.png)
![NUK_L](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_L_5.png)
![NUK_L](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_L_6.png)
![NUK_L](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_L_7.png)
![NUK_L](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_L_8.png)
![NUK_L](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_L_9.png)
![NUK_L](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_L_10.png)
![NUK_L](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_L_11.png)
 
## <a id='s1-30' />NUK_N
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![NUK_N](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_N_0.png)
![NUK_N](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_N_1.png)
![NUK_N](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_N_2.png)
![NUK_N](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_N_3.png)
![NUK_N](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_N_4.png)
![NUK_N](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_N_5.png)
![NUK_N](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_N_6.png)
![NUK_N](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_N_7.png)
![NUK_N](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_N_8.png)
![NUK_N](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_N_9.png)
![NUK_N](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_N_10.png)
![NUK_N](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_N_11.png)
 
## <a id='s1-31' />NUK_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![NUK_U](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_U_0.png)
![NUK_U](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_U_1.png)
![NUK_U](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_U_2.png)
![NUK_U](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_U_3.png)
![NUK_U](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_U_4.png)
![NUK_U](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_U_5.png)
![NUK_U](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_U_6.png)
![NUK_U](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_U_7.png)
![NUK_U](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_U_8.png)
![NUK_U](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_U_9.png)
![NUK_U](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_U_10.png)
![NUK_U](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_U_11.png)
 
## <a id='s1-32' />NUK_Uv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![NUK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_Uv3_0.png)
![NUK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_Uv3_1.png)
![NUK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_Uv3_2.png)
![NUK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_Uv3_3.png)
![NUK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_Uv3_4.png)
![NUK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_Uv3_5.png)
![NUK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_Uv3_6.png)
![NUK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_Uv3_7.png)
![NUK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_Uv3_8.png)
![NUK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_Uv3_9.png)
![NUK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_Uv3_10.png)
![NUK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/NUK_Uv3_11.png)
 
## <a id='s1-33' />QAS_A
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![QAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_A_0.png)
![QAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_A_1.png)
![QAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_A_2.png)
![QAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_A_3.png)
![QAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_A_4.png)
![QAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_A_5.png)
![QAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_A_6.png)
![QAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_A_7.png)
![QAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_A_8.png)
![QAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_A_9.png)
![QAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_A_10.png)
![QAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_A_11.png)
 
## <a id='s1-34' />QAS_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![QAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_L_0.png)
![QAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_L_1.png)
![QAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_L_2.png)
![QAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_L_3.png)
![QAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_L_4.png)
![QAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_L_5.png)
![QAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_L_6.png)
![QAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_L_7.png)
![QAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_L_8.png)
![QAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_L_9.png)
![QAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_L_10.png)
![QAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_L_11.png)
 
## <a id='s1-35' />QAS_Lv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![QAS_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Lv3_0.png)
![QAS_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Lv3_1.png)
![QAS_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Lv3_2.png)
![QAS_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Lv3_3.png)
![QAS_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Lv3_4.png)
![QAS_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Lv3_5.png)
![QAS_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Lv3_6.png)
![QAS_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Lv3_7.png)
![QAS_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Lv3_8.png)
![QAS_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Lv3_9.png)
![QAS_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Lv3_10.png)
![QAS_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Lv3_11.png)
 
## <a id='s1-36' />QAS_M
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![QAS_M](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_M_0.png)
![QAS_M](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_M_1.png)
![QAS_M](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_M_2.png)
![QAS_M](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_M_3.png)
![QAS_M](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_M_4.png)
![QAS_M](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_M_5.png)
![QAS_M](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_M_6.png)
![QAS_M](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_M_7.png)
![QAS_M](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_M_8.png)
![QAS_M](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_M_9.png)
![QAS_M](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_M_10.png)
![QAS_M](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_M_11.png)
 
## <a id='s1-37' />QAS_Mv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![QAS_Mv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Mv3_0.png)
![QAS_Mv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Mv3_1.png)
![QAS_Mv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Mv3_2.png)
![QAS_Mv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Mv3_3.png)
![QAS_Mv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Mv3_4.png)
![QAS_Mv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Mv3_5.png)
![QAS_Mv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Mv3_6.png)
![QAS_Mv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Mv3_7.png)
![QAS_Mv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Mv3_8.png)
![QAS_Mv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Mv3_9.png)
![QAS_Mv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Mv3_10.png)
![QAS_Mv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Mv3_11.png)
 
## <a id='s1-38' />QAS_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![QAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_U_0.png)
![QAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_U_1.png)
![QAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_U_2.png)
![QAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_U_3.png)
![QAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_U_4.png)
![QAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_U_5.png)
![QAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_U_6.png)
![QAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_U_7.png)
![QAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_U_8.png)
![QAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_U_9.png)
![QAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_U_10.png)
![QAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_U_11.png)
 
## <a id='s1-39' />QAS_Uv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![QAS_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Uv3_0.png)
![QAS_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Uv3_1.png)
![QAS_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Uv3_2.png)
![QAS_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Uv3_3.png)
![QAS_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Uv3_4.png)
![QAS_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Uv3_5.png)
![QAS_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Uv3_6.png)
![QAS_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Uv3_7.png)
![QAS_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Uv3_8.png)
![QAS_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Uv3_9.png)
![QAS_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Uv3_10.png)
![QAS_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/QAS_Uv3_11.png)
 
## <a id='s1-40' />Roof_GEUS
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_hdop, batt_v, fan_dc_u, fan_dc_l, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![Roof_GEUS](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_GEUS_0.png)
![Roof_GEUS](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_GEUS_1.png)
![Roof_GEUS](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_GEUS_2.png)
![Roof_GEUS](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_GEUS_3.png)
![Roof_GEUS](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_GEUS_4.png)
![Roof_GEUS](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_GEUS_5.png)
![Roof_GEUS](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_GEUS_6.png)
![Roof_GEUS](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_GEUS_7.png)
![Roof_GEUS](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_GEUS_8.png)
![Roof_GEUS](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_GEUS_9.png)
![Roof_GEUS](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_GEUS_10.png)
![Roof_GEUS](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_GEUS_11.png)
![Roof_GEUS](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_GEUS_12.png)
![Roof_GEUS](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_GEUS_13.png)
 
## <a id='s1-41' />Roof_PROMICE
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![Roof_PROMICE](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_PROMICE_0.png)
![Roof_PROMICE](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_PROMICE_1.png)
![Roof_PROMICE](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_PROMICE_2.png)
![Roof_PROMICE](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_PROMICE_3.png)
![Roof_PROMICE](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_PROMICE_4.png)
![Roof_PROMICE](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_PROMICE_5.png)
![Roof_PROMICE](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_PROMICE_6.png)
![Roof_PROMICE](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_PROMICE_7.png)
![Roof_PROMICE](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_PROMICE_8.png)
![Roof_PROMICE](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_PROMICE_9.png)
![Roof_PROMICE](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_PROMICE_10.png)
![Roof_PROMICE](../figures/aws-l3_versus_aws-l3-dev_20240613/Roof_PROMICE_11.png)
 
## <a id='s1-42' />SCO_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![SCO_L](../figures/aws-l3_versus_aws-l3-dev_20240613/SCO_L_0.png)
![SCO_L](../figures/aws-l3_versus_aws-l3-dev_20240613/SCO_L_1.png)
![SCO_L](../figures/aws-l3_versus_aws-l3-dev_20240613/SCO_L_2.png)
![SCO_L](../figures/aws-l3_versus_aws-l3-dev_20240613/SCO_L_3.png)
![SCO_L](../figures/aws-l3_versus_aws-l3-dev_20240613/SCO_L_4.png)
![SCO_L](../figures/aws-l3_versus_aws-l3-dev_20240613/SCO_L_5.png)
![SCO_L](../figures/aws-l3_versus_aws-l3-dev_20240613/SCO_L_6.png)
![SCO_L](../figures/aws-l3_versus_aws-l3-dev_20240613/SCO_L_7.png)
![SCO_L](../figures/aws-l3_versus_aws-l3-dev_20240613/SCO_L_8.png)
![SCO_L](../figures/aws-l3_versus_aws-l3-dev_20240613/SCO_L_9.png)
![SCO_L](../figures/aws-l3_versus_aws-l3-dev_20240613/SCO_L_10.png)
![SCO_L](../figures/aws-l3_versus_aws-l3-dev_20240613/SCO_L_11.png)
 
## <a id='s1-43' />SCO_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![SCO_U](../figures/aws-l3_versus_aws-l3-dev_20240613/SCO_U_0.png)
![SCO_U](../figures/aws-l3_versus_aws-l3-dev_20240613/SCO_U_1.png)
![SCO_U](../figures/aws-l3_versus_aws-l3-dev_20240613/SCO_U_2.png)
![SCO_U](../figures/aws-l3_versus_aws-l3-dev_20240613/SCO_U_3.png)
![SCO_U](../figures/aws-l3_versus_aws-l3-dev_20240613/SCO_U_4.png)
![SCO_U](../figures/aws-l3_versus_aws-l3-dev_20240613/SCO_U_5.png)
![SCO_U](../figures/aws-l3_versus_aws-l3-dev_20240613/SCO_U_6.png)
![SCO_U](../figures/aws-l3_versus_aws-l3-dev_20240613/SCO_U_7.png)
![SCO_U](../figures/aws-l3_versus_aws-l3-dev_20240613/SCO_U_8.png)
![SCO_U](../figures/aws-l3_versus_aws-l3-dev_20240613/SCO_U_9.png)
![SCO_U](../figures/aws-l3_versus_aws-l3-dev_20240613/SCO_U_10.png)
![SCO_U](../figures/aws-l3_versus_aws-l3-dev_20240613/SCO_U_11.png)
 
## <a id='s1-44' />SDL
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_numsat, gps_q, batt_v, fan_dc_u, fan_dc_l, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_geoid, gps_numsat, gps_q, t_log

Old variables removed from new files:

 
![SDL](../figures/aws-l3_versus_aws-l3-dev_20240613/SDL_0.png)
![SDL](../figures/aws-l3_versus_aws-l3-dev_20240613/SDL_1.png)
![SDL](../figures/aws-l3_versus_aws-l3-dev_20240613/SDL_2.png)
![SDL](../figures/aws-l3_versus_aws-l3-dev_20240613/SDL_3.png)
![SDL](../figures/aws-l3_versus_aws-l3-dev_20240613/SDL_4.png)
![SDL](../figures/aws-l3_versus_aws-l3-dev_20240613/SDL_5.png)
![SDL](../figures/aws-l3_versus_aws-l3-dev_20240613/SDL_6.png)
![SDL](../figures/aws-l3_versus_aws-l3-dev_20240613/SDL_7.png)
![SDL](../figures/aws-l3_versus_aws-l3-dev_20240613/SDL_8.png)
![SDL](../figures/aws-l3_versus_aws-l3-dev_20240613/SDL_9.png)
![SDL](../figures/aws-l3_versus_aws-l3-dev_20240613/SDL_10.png)
![SDL](../figures/aws-l3_versus_aws-l3-dev_20240613/SDL_11.png)
![SDL](../figures/aws-l3_versus_aws-l3-dev_20240613/SDL_12.png)
![SDL](../figures/aws-l3_versus_aws-l3-dev_20240613/SDL_13.png)
![SDL](../figures/aws-l3_versus_aws-l3-dev_20240613/SDL_14.png)
 
## <a id='s1-45' />SDM
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_numsat, gps_q, batt_v, fan_dc_u, fan_dc_l, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_geoid, gps_numsat, gps_q, t_log

Old variables removed from new files:

 
![SDM](../figures/aws-l3_versus_aws-l3-dev_20240613/SDM_0.png)
![SDM](../figures/aws-l3_versus_aws-l3-dev_20240613/SDM_1.png)
![SDM](../figures/aws-l3_versus_aws-l3-dev_20240613/SDM_2.png)
![SDM](../figures/aws-l3_versus_aws-l3-dev_20240613/SDM_3.png)
![SDM](../figures/aws-l3_versus_aws-l3-dev_20240613/SDM_4.png)
![SDM](../figures/aws-l3_versus_aws-l3-dev_20240613/SDM_5.png)
![SDM](../figures/aws-l3_versus_aws-l3-dev_20240613/SDM_6.png)
![SDM](../figures/aws-l3_versus_aws-l3-dev_20240613/SDM_7.png)
![SDM](../figures/aws-l3_versus_aws-l3-dev_20240613/SDM_8.png)
![SDM](../figures/aws-l3_versus_aws-l3-dev_20240613/SDM_9.png)
![SDM](../figures/aws-l3_versus_aws-l3-dev_20240613/SDM_10.png)
![SDM](../figures/aws-l3_versus_aws-l3-dev_20240613/SDM_11.png)
![SDM](../figures/aws-l3_versus_aws-l3-dev_20240613/SDM_12.png)
![SDM](../figures/aws-l3_versus_aws-l3-dev_20240613/SDM_13.png)
![SDM](../figures/aws-l3_versus_aws-l3-dev_20240613/SDM_14.png)
 
## <a id='s1-46' />SWC
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![SWC](../figures/aws-l3_versus_aws-l3-dev_20240613/SWC_0.png)
![SWC](../figures/aws-l3_versus_aws-l3-dev_20240613/SWC_1.png)
![SWC](../figures/aws-l3_versus_aws-l3-dev_20240613/SWC_2.png)
![SWC](../figures/aws-l3_versus_aws-l3-dev_20240613/SWC_3.png)
![SWC](../figures/aws-l3_versus_aws-l3-dev_20240613/SWC_4.png)
![SWC](../figures/aws-l3_versus_aws-l3-dev_20240613/SWC_5.png)
![SWC](../figures/aws-l3_versus_aws-l3-dev_20240613/SWC_6.png)
![SWC](../figures/aws-l3_versus_aws-l3-dev_20240613/SWC_7.png)
![SWC](../figures/aws-l3_versus_aws-l3-dev_20240613/SWC_8.png)
![SWC](../figures/aws-l3_versus_aws-l3-dev_20240613/SWC_9.png)
![SWC](../figures/aws-l3_versus_aws-l3-dev_20240613/SWC_10.png)
![SWC](../figures/aws-l3_versus_aws-l3-dev_20240613/SWC_11.png)
 
## <a id='s1-47' />SWC_O
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![SWC_O](../figures/aws-l3_versus_aws-l3-dev_20240613/SWC_O_0.png)
![SWC_O](../figures/aws-l3_versus_aws-l3-dev_20240613/SWC_O_1.png)
![SWC_O](../figures/aws-l3_versus_aws-l3-dev_20240613/SWC_O_2.png)
![SWC_O](../figures/aws-l3_versus_aws-l3-dev_20240613/SWC_O_3.png)
![SWC_O](../figures/aws-l3_versus_aws-l3-dev_20240613/SWC_O_4.png)
![SWC_O](../figures/aws-l3_versus_aws-l3-dev_20240613/SWC_O_5.png)
![SWC_O](../figures/aws-l3_versus_aws-l3-dev_20240613/SWC_O_6.png)
![SWC_O](../figures/aws-l3_versus_aws-l3-dev_20240613/SWC_O_7.png)
![SWC_O](../figures/aws-l3_versus_aws-l3-dev_20240613/SWC_O_8.png)
![SWC_O](../figures/aws-l3_versus_aws-l3-dev_20240613/SWC_O_9.png)
![SWC_O](../figures/aws-l3_versus_aws-l3-dev_20240613/SWC_O_10.png)
![SWC_O](../figures/aws-l3_versus_aws-l3-dev_20240613/SWC_O_11.png)
 
## <a id='s1-48' />TAS_A
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![TAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_A_0.png)
![TAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_A_1.png)
![TAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_A_2.png)
![TAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_A_3.png)
![TAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_A_4.png)
![TAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_A_5.png)
![TAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_A_6.png)
![TAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_A_7.png)
![TAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_A_8.png)
![TAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_A_9.png)
![TAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_A_10.png)
![TAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_A_11.png)
 
## <a id='s1-49' />TAS_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![TAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_L_0.png)
![TAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_L_1.png)
![TAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_L_2.png)
![TAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_L_3.png)
![TAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_L_4.png)
![TAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_L_5.png)
![TAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_L_6.png)
![TAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_L_7.png)
![TAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_L_8.png)
![TAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_L_9.png)
![TAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_L_10.png)
![TAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_L_11.png)
 
## <a id='s1-50' />TAS_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![TAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_U_0.png)
![TAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_U_1.png)
![TAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_U_2.png)
![TAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_U_3.png)
![TAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_U_4.png)
![TAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_U_5.png)
![TAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_U_6.png)
![TAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_U_7.png)
![TAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_U_8.png)
![TAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_U_9.png)
![TAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_U_10.png)
![TAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613/TAS_U_11.png)
 
## <a id='s1-51' />THU_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![THU_L](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_L_0.png)
![THU_L](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_L_1.png)
![THU_L](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_L_2.png)
![THU_L](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_L_3.png)
![THU_L](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_L_4.png)
![THU_L](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_L_5.png)
![THU_L](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_L_6.png)
![THU_L](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_L_7.png)
![THU_L](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_L_8.png)
![THU_L](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_L_9.png)
![THU_L](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_L_10.png)
![THU_L](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_L_11.png)
 
## <a id='s1-52' />THU_L2
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![THU_L2](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_L2_0.png)
![THU_L2](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_L2_1.png)
![THU_L2](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_L2_2.png)
![THU_L2](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_L2_3.png)
![THU_L2](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_L2_4.png)
![THU_L2](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_L2_5.png)
![THU_L2](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_L2_6.png)
![THU_L2](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_L2_7.png)
![THU_L2](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_L2_8.png)
![THU_L2](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_L2_9.png)
![THU_L2](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_L2_10.png)
![THU_L2](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_L2_11.png)
 
## <a id='s1-53' />THU_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![THU_U](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U_0.png)
![THU_U](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U_1.png)
![THU_U](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U_2.png)
![THU_U](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U_3.png)
![THU_U](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U_4.png)
![THU_U](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U_5.png)
![THU_U](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U_6.png)
![THU_U](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U_7.png)
![THU_U](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U_8.png)
![THU_U](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U_9.png)
![THU_U](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U_10.png)
![THU_U](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U_11.png)
 
## <a id='s1-54' />THU_U2
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![THU_U2](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U2_0.png)
![THU_U2](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U2_1.png)
![THU_U2](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U2_2.png)
![THU_U2](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U2_3.png)
![THU_U2](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U2_4.png)
![THU_U2](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U2_5.png)
![THU_U2](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U2_6.png)
![THU_U2](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U2_7.png)
![THU_U2](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U2_8.png)
![THU_U2](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U2_9.png)
![THU_U2](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U2_10.png)
![THU_U2](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U2_11.png)
 
## <a id='s1-55' />THU_U2v3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![THU_U2v3](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U2v3_0.png)
![THU_U2v3](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U2v3_1.png)
![THU_U2v3](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U2v3_2.png)
![THU_U2v3](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U2v3_3.png)
![THU_U2v3](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U2v3_4.png)
![THU_U2v3](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U2v3_5.png)
![THU_U2v3](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U2v3_6.png)
![THU_U2v3](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U2v3_7.png)
![THU_U2v3](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U2v3_8.png)
![THU_U2v3](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U2v3_9.png)
![THU_U2v3](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U2v3_10.png)
![THU_U2v3](../figures/aws-l3_versus_aws-l3-dev_20240613/THU_U2v3_11.png)
 
## <a id='s1-56' />TUN
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_numsat, gps_q, batt_v, fan_dc_u, fan_dc_l, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_geoid, gps_numsat, gps_q, t_log

Old variables removed from new files:

 
![TUN](../figures/aws-l3_versus_aws-l3-dev_20240613/TUN_0.png)
![TUN](../figures/aws-l3_versus_aws-l3-dev_20240613/TUN_1.png)
![TUN](../figures/aws-l3_versus_aws-l3-dev_20240613/TUN_2.png)
![TUN](../figures/aws-l3_versus_aws-l3-dev_20240613/TUN_3.png)
![TUN](../figures/aws-l3_versus_aws-l3-dev_20240613/TUN_4.png)
![TUN](../figures/aws-l3_versus_aws-l3-dev_20240613/TUN_5.png)
![TUN](../figures/aws-l3_versus_aws-l3-dev_20240613/TUN_6.png)
![TUN](../figures/aws-l3_versus_aws-l3-dev_20240613/TUN_7.png)
![TUN](../figures/aws-l3_versus_aws-l3-dev_20240613/TUN_8.png)
![TUN](../figures/aws-l3_versus_aws-l3-dev_20240613/TUN_9.png)
![TUN](../figures/aws-l3_versus_aws-l3-dev_20240613/TUN_10.png)
![TUN](../figures/aws-l3_versus_aws-l3-dev_20240613/TUN_11.png)
![TUN](../figures/aws-l3_versus_aws-l3-dev_20240613/TUN_12.png)
![TUN](../figures/aws-l3_versus_aws-l3-dev_20240613/TUN_13.png)
![TUN](../figures/aws-l3_versus_aws-l3-dev_20240613/TUN_14.png)
 
## <a id='s1-57' />UPE_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![UPE_L](../figures/aws-l3_versus_aws-l3-dev_20240613/UPE_L_0.png)
![UPE_L](../figures/aws-l3_versus_aws-l3-dev_20240613/UPE_L_1.png)
![UPE_L](../figures/aws-l3_versus_aws-l3-dev_20240613/UPE_L_2.png)
![UPE_L](../figures/aws-l3_versus_aws-l3-dev_20240613/UPE_L_3.png)
![UPE_L](../figures/aws-l3_versus_aws-l3-dev_20240613/UPE_L_4.png)
![UPE_L](../figures/aws-l3_versus_aws-l3-dev_20240613/UPE_L_5.png)
![UPE_L](../figures/aws-l3_versus_aws-l3-dev_20240613/UPE_L_6.png)
![UPE_L](../figures/aws-l3_versus_aws-l3-dev_20240613/UPE_L_7.png)
![UPE_L](../figures/aws-l3_versus_aws-l3-dev_20240613/UPE_L_8.png)
![UPE_L](../figures/aws-l3_versus_aws-l3-dev_20240613/UPE_L_9.png)
![UPE_L](../figures/aws-l3_versus_aws-l3-dev_20240613/UPE_L_10.png)
![UPE_L](../figures/aws-l3_versus_aws-l3-dev_20240613/UPE_L_11.png)
 
## <a id='s1-58' />UPE_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![UPE_U](../figures/aws-l3_versus_aws-l3-dev_20240613/UPE_U_0.png)
![UPE_U](../figures/aws-l3_versus_aws-l3-dev_20240613/UPE_U_1.png)
![UPE_U](../figures/aws-l3_versus_aws-l3-dev_20240613/UPE_U_2.png)
![UPE_U](../figures/aws-l3_versus_aws-l3-dev_20240613/UPE_U_3.png)
![UPE_U](../figures/aws-l3_versus_aws-l3-dev_20240613/UPE_U_4.png)
![UPE_U](../figures/aws-l3_versus_aws-l3-dev_20240613/UPE_U_5.png)
![UPE_U](../figures/aws-l3_versus_aws-l3-dev_20240613/UPE_U_6.png)
![UPE_U](../figures/aws-l3_versus_aws-l3-dev_20240613/UPE_U_7.png)
![UPE_U](../figures/aws-l3_versus_aws-l3-dev_20240613/UPE_U_8.png)
![UPE_U](../figures/aws-l3_versus_aws-l3-dev_20240613/UPE_U_9.png)
![UPE_U](../figures/aws-l3_versus_aws-l3-dev_20240613/UPE_U_10.png)
![UPE_U](../figures/aws-l3_versus_aws-l3-dev_20240613/UPE_U_11.png)
 
## <a id='s1-59' />UWN
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![UWN](../figures/aws-l3_versus_aws-l3-dev_20240613/UWN_0.png)
![UWN](../figures/aws-l3_versus_aws-l3-dev_20240613/UWN_1.png)
![UWN](../figures/aws-l3_versus_aws-l3-dev_20240613/UWN_2.png)
![UWN](../figures/aws-l3_versus_aws-l3-dev_20240613/UWN_3.png)
![UWN](../figures/aws-l3_versus_aws-l3-dev_20240613/UWN_4.png)
![UWN](../figures/aws-l3_versus_aws-l3-dev_20240613/UWN_5.png)
![UWN](../figures/aws-l3_versus_aws-l3-dev_20240613/UWN_6.png)
![UWN](../figures/aws-l3_versus_aws-l3-dev_20240613/UWN_7.png)
![UWN](../figures/aws-l3_versus_aws-l3-dev_20240613/UWN_8.png)
![UWN](../figures/aws-l3_versus_aws-l3-dev_20240613/UWN_9.png)
![UWN](../figures/aws-l3_versus_aws-l3-dev_20240613/UWN_10.png)
![UWN](../figures/aws-l3_versus_aws-l3-dev_20240613/UWN_11.png)
 
## <a id='s1-60' />WEG_B
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, t_surf, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![WEG_B](../figures/aws-l3_versus_aws-l3-dev_20240613/WEG_B_0.png)
![WEG_B](../figures/aws-l3_versus_aws-l3-dev_20240613/WEG_B_1.png)
![WEG_B](../figures/aws-l3_versus_aws-l3-dev_20240613/WEG_B_2.png)
![WEG_B](../figures/aws-l3_versus_aws-l3-dev_20240613/WEG_B_3.png)
![WEG_B](../figures/aws-l3_versus_aws-l3-dev_20240613/WEG_B_4.png)
![WEG_B](../figures/aws-l3_versus_aws-l3-dev_20240613/WEG_B_5.png)
![WEG_B](../figures/aws-l3_versus_aws-l3-dev_20240613/WEG_B_6.png)
![WEG_B](../figures/aws-l3_versus_aws-l3-dev_20240613/WEG_B_7.png)
![WEG_B](../figures/aws-l3_versus_aws-l3-dev_20240613/WEG_B_8.png)
![WEG_B](../figures/aws-l3_versus_aws-l3-dev_20240613/WEG_B_9.png)
![WEG_B](../figures/aws-l3_versus_aws-l3-dev_20240613/WEG_B_10.png)
 
## <a id='s1-61' />WEG_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![WEG_L](../figures/aws-l3_versus_aws-l3-dev_20240613/WEG_L_0.png)
![WEG_L](../figures/aws-l3_versus_aws-l3-dev_20240613/WEG_L_1.png)
![WEG_L](../figures/aws-l3_versus_aws-l3-dev_20240613/WEG_L_2.png)
![WEG_L](../figures/aws-l3_versus_aws-l3-dev_20240613/WEG_L_3.png)
![WEG_L](../figures/aws-l3_versus_aws-l3-dev_20240613/WEG_L_4.png)
![WEG_L](../figures/aws-l3_versus_aws-l3-dev_20240613/WEG_L_5.png)
![WEG_L](../figures/aws-l3_versus_aws-l3-dev_20240613/WEG_L_6.png)
![WEG_L](../figures/aws-l3_versus_aws-l3-dev_20240613/WEG_L_7.png)
![WEG_L](../figures/aws-l3_versus_aws-l3-dev_20240613/WEG_L_8.png)
![WEG_L](../figures/aws-l3_versus_aws-l3-dev_20240613/WEG_L_9.png)
![WEG_L](../figures/aws-l3_versus_aws-l3-dev_20240613/WEG_L_10.png)
![WEG_L](../figures/aws-l3_versus_aws-l3-dev_20240613/WEG_L_11.png)
 
## <a id='s1-62' />XXX
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![XXX](../figures/aws-l3_versus_aws-l3-dev_20240613/XXX_0.png)
![XXX](../figures/aws-l3_versus_aws-l3-dev_20240613/XXX_1.png)
![XXX](../figures/aws-l3_versus_aws-l3-dev_20240613/XXX_2.png)
![XXX](../figures/aws-l3_versus_aws-l3-dev_20240613/XXX_3.png)
![XXX](../figures/aws-l3_versus_aws-l3-dev_20240613/XXX_4.png)
![XXX](../figures/aws-l3_versus_aws-l3-dev_20240613/XXX_5.png)
![XXX](../figures/aws-l3_versus_aws-l3-dev_20240613/XXX_6.png)
![XXX](../figures/aws-l3_versus_aws-l3-dev_20240613/XXX_7.png)
![XXX](../figures/aws-l3_versus_aws-l3-dev_20240613/XXX_8.png)
![XXX](../figures/aws-l3_versus_aws-l3-dev_20240613/XXX_9.png)
![XXX](../figures/aws-l3_versus_aws-l3-dev_20240613/XXX_10.png)
![XXX](../figures/aws-l3_versus_aws-l3-dev_20240613/XXX_11.png)
 
## <a id='s1-63' />ZAK_A
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_hdop, batt_v, fan_dc_u, fan_dc_l, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![ZAK_A](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_A_0.png)
![ZAK_A](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_A_1.png)
![ZAK_A](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_A_2.png)
![ZAK_A](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_A_3.png)
![ZAK_A](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_A_4.png)
![ZAK_A](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_A_5.png)
![ZAK_A](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_A_6.png)
![ZAK_A](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_A_7.png)
![ZAK_A](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_A_8.png)
![ZAK_A](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_A_9.png)
![ZAK_A](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_A_10.png)
![ZAK_A](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_A_11.png)
![ZAK_A](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_A_12.png)
![ZAK_A](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_A_13.png)
 
## <a id='s1-64' />ZAK_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_numsat, gps_q, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_numsat, gps_q

Old variables removed from new files:

 
![ZAK_L](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_L_0.png)
![ZAK_L](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_L_1.png)
![ZAK_L](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_L_2.png)
![ZAK_L](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_L_3.png)
![ZAK_L](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_L_4.png)
![ZAK_L](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_L_5.png)
![ZAK_L](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_L_6.png)
![ZAK_L](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_L_7.png)
![ZAK_L](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_L_8.png)
![ZAK_L](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_L_9.png)
![ZAK_L](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_L_10.png)
![ZAK_L](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_L_11.png)
 
## <a id='s1-65' />ZAK_Lv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![ZAK_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_Lv3_0.png)
![ZAK_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_Lv3_1.png)
![ZAK_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_Lv3_2.png)
![ZAK_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_Lv3_3.png)
![ZAK_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_Lv3_4.png)
![ZAK_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_Lv3_5.png)
![ZAK_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_Lv3_6.png)
![ZAK_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_Lv3_7.png)
![ZAK_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_Lv3_8.png)
![ZAK_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_Lv3_9.png)
![ZAK_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_Lv3_10.png)
![ZAK_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_Lv3_11.png)
 
## <a id='s1-66' />ZAK_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![ZAK_U](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_U_0.png)
![ZAK_U](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_U_1.png)
![ZAK_U](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_U_2.png)
![ZAK_U](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_U_3.png)
![ZAK_U](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_U_4.png)
![ZAK_U](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_U_5.png)
![ZAK_U](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_U_6.png)
![ZAK_U](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_U_7.png)
![ZAK_U](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_U_8.png)
![ZAK_U](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_U_9.png)
![ZAK_U](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_U_10.png)
![ZAK_U](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_U_11.png)
 
## <a id='s1-67' />ZAK_Uv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![ZAK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_Uv3_0.png)
![ZAK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_Uv3_1.png)
![ZAK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_Uv3_2.png)
![ZAK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_Uv3_3.png)
![ZAK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_Uv3_4.png)
![ZAK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_Uv3_5.png)
![ZAK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_Uv3_6.png)
![ZAK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_Uv3_7.png)
![ZAK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_Uv3_8.png)
![ZAK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_Uv3_9.png)
![ZAK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_Uv3_10.png)
![ZAK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613/ZAK_Uv3_11.png)
 
