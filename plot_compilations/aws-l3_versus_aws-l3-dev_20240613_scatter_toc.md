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

 
![CEN1](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CEN1_0.png)
![CEN1](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CEN1_1.png)
![CEN1](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CEN1_2.png)
![CEN1](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CEN1_3.png)
![CEN1](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CEN1_4.png)
![CEN1](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CEN1_5.png)
![CEN1](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CEN1_6.png)
 
## <a id='s1-2' />CEN2
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_numsat, gps_q, batt_v, fan_dc_u, fan_dc_l, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_geoid, gps_numsat, gps_q, t_log

Old variables removed from new files:

 
![CEN2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CEN2_0.png)
![CEN2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CEN2_1.png)
![CEN2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CEN2_2.png)
![CEN2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CEN2_3.png)
![CEN2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CEN2_4.png)
![CEN2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CEN2_5.png)
![CEN2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CEN2_6.png)
![CEN2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CEN2_7.png)
![CEN2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CEN2_8.png)
 
## <a id='s1-3' />CP1
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_numsat, gps_q, batt_v, fan_dc_u, fan_dc_l, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_geoid, gps_numsat, gps_q, t_log

Old variables removed from new files:

 
![CP1](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CP1_0.png)
![CP1](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CP1_1.png)
![CP1](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CP1_2.png)
![CP1](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CP1_3.png)
![CP1](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CP1_4.png)
![CP1](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CP1_5.png)
![CP1](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CP1_6.png)
![CP1](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CP1_7.png)
![CP1](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/CP1_8.png)
 
## <a id='s1-4' />DY2
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_numsat, gps_q, batt_v, fan_dc_u, fan_dc_l, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_geoid, gps_numsat, gps_q, t_log

Old variables removed from new files:

 
![DY2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/DY2_0.png)
![DY2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/DY2_1.png)
![DY2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/DY2_2.png)
![DY2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/DY2_3.png)
![DY2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/DY2_4.png)
![DY2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/DY2_5.png)
![DY2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/DY2_6.png)
![DY2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/DY2_7.png)
![DY2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/DY2_8.png)
 
## <a id='s1-5' />EGP
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![EGP](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/EGP_0.png)
![EGP](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/EGP_1.png)
![EGP](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/EGP_2.png)
![EGP](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/EGP_3.png)
![EGP](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/EGP_4.png)
![EGP](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/EGP_5.png)
![EGP](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/EGP_6.png)
 
## <a id='s1-6' />FRE
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![FRE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/FRE_0.png)
![FRE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/FRE_1.png)
![FRE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/FRE_2.png)
![FRE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/FRE_3.png)
![FRE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/FRE_4.png)
![FRE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/FRE_5.png)
![FRE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/FRE_6.png)
 
## <a id='s1-7' />HUM
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_numsat, gps_q, batt_v, fan_dc_u, fan_dc_l, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_geoid, gps_numsat, gps_q, t_log

Old variables removed from new files:

 
![HUM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/HUM_0.png)
![HUM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/HUM_1.png)
![HUM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/HUM_2.png)
![HUM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/HUM_3.png)
![HUM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/HUM_4.png)
![HUM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/HUM_5.png)
![HUM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/HUM_6.png)
![HUM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/HUM_7.png)
![HUM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/HUM_8.png)
 
## <a id='s1-8' />JAR
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![JAR](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/JAR_0.png)
![JAR](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/JAR_1.png)
![JAR](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/JAR_2.png)
![JAR](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/JAR_3.png)
![JAR](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/JAR_4.png)
![JAR](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/JAR_5.png)
![JAR](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/JAR_6.png)
 
## <a id='s1-9' />JAR_O
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![JAR_O](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/JAR_O_0.png)
![JAR_O](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/JAR_O_1.png)
![JAR_O](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/JAR_O_2.png)
![JAR_O](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/JAR_O_3.png)
![JAR_O](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/JAR_O_4.png)
![JAR_O](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/JAR_O_5.png)
![JAR_O](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/JAR_O_6.png)
 
## <a id='s1-10' />KAN_B
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, t_surf, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
batt_v_ss

Old variables removed from new files:

 
![KAN_B](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_B_0.png)
![KAN_B](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_B_1.png)
![KAN_B](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_B_2.png)
![KAN_B](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_B_3.png)
![KAN_B](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_B_4.png)
![KAN_B](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_B_5.png)
 
## <a id='s1-11' />KAN_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![KAN_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_L_0.png)
![KAN_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_L_1.png)
![KAN_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_L_2.png)
![KAN_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_L_3.png)
![KAN_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_L_4.png)
![KAN_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_L_5.png)
![KAN_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_L_6.png)
 
## <a id='s1-12' />KAN_Lv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![KAN_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_Lv3_0.png)
![KAN_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_Lv3_1.png)
![KAN_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_Lv3_2.png)
![KAN_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_Lv3_3.png)
![KAN_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_Lv3_4.png)
![KAN_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_Lv3_5.png)
![KAN_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_Lv3_6.png)
 
## <a id='s1-13' />KAN_M
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![KAN_M](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_M_0.png)
![KAN_M](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_M_1.png)
![KAN_M](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_M_2.png)
![KAN_M](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_M_3.png)
![KAN_M](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_M_4.png)
![KAN_M](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_M_5.png)
![KAN_M](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_M_6.png)
 
## <a id='s1-14' />KAN_Tv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![KAN_Tv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_Tv3_0.png)
![KAN_Tv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_Tv3_1.png)
![KAN_Tv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_Tv3_2.png)
![KAN_Tv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_Tv3_3.png)
![KAN_Tv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_Tv3_4.png)
![KAN_Tv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_Tv3_5.png)
![KAN_Tv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_Tv3_6.png)
 
## <a id='s1-15' />KAN_U
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, fan_dc_l, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
z_stake, z_pt, z_pt_cor, gps_geoid, gps_q, batt_v_ss, t_log

Old variables removed from new files:

 
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_U_0.png)
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_U_1.png)
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_U_2.png)
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_U_3.png)
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_U_4.png)
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_U_5.png)
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_U_6.png)
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_U_7.png)
![KAN_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KAN_U_8.png)
 
## <a id='s1-16' />KPC_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![KPC_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_L_0.png)
![KPC_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_L_1.png)
![KPC_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_L_2.png)
![KPC_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_L_3.png)
![KPC_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_L_4.png)
![KPC_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_L_5.png)
![KPC_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_L_6.png)
 
## <a id='s1-17' />KPC_Lv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![KPC_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_Lv3_0.png)
![KPC_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_Lv3_1.png)
![KPC_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_Lv3_2.png)
![KPC_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_Lv3_3.png)
![KPC_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_Lv3_4.png)
![KPC_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_Lv3_5.png)
![KPC_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_Lv3_6.png)
 
## <a id='s1-18' />KPC_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![KPC_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_U_0.png)
![KPC_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_U_1.png)
![KPC_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_U_2.png)
![KPC_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_U_3.png)
![KPC_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_U_4.png)
![KPC_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_U_5.png)
![KPC_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_U_6.png)
 
## <a id='s1-19' />KPC_Uv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![KPC_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_Uv3_0.png)
![KPC_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_Uv3_1.png)
![KPC_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_Uv3_2.png)
![KPC_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_Uv3_3.png)
![KPC_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_Uv3_4.png)
![KPC_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_Uv3_5.png)
![KPC_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/KPC_Uv3_6.png)
 
## <a id='s1-20' />LYN_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![LYN_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/LYN_L_0.png)
![LYN_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/LYN_L_1.png)
![LYN_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/LYN_L_2.png)
![LYN_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/LYN_L_3.png)
![LYN_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/LYN_L_4.png)
![LYN_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/LYN_L_5.png)
![LYN_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/LYN_L_6.png)
 
## <a id='s1-21' />LYN_T
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![LYN_T](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/LYN_T_0.png)
![LYN_T](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/LYN_T_1.png)
![LYN_T](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/LYN_T_2.png)
![LYN_T](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/LYN_T_3.png)
![LYN_T](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/LYN_T_4.png)
![LYN_T](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/LYN_T_5.png)
![LYN_T](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/LYN_T_6.png)
 
## <a id='s1-22' />MIT
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![MIT](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/MIT_0.png)
![MIT](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/MIT_1.png)
![MIT](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/MIT_2.png)
![MIT](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/MIT_3.png)
![MIT](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/MIT_4.png)
![MIT](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/MIT_5.png)
![MIT](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/MIT_6.png)
 
## <a id='s1-23' />NAE
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_hdop, batt_v, fan_dc_u, fan_dc_l, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![NAE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NAE_0.png)
![NAE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NAE_1.png)
![NAE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NAE_2.png)
![NAE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NAE_3.png)
![NAE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NAE_4.png)
![NAE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NAE_5.png)
![NAE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NAE_6.png)
![NAE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NAE_7.png)
 
## <a id='s1-24' />NAU
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_numsat, gps_q, batt_v, fan_dc_u, fan_dc_l, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_geoid, gps_numsat, gps_q, t_log

Old variables removed from new files:

 
![NAU](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NAU_0.png)
![NAU](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NAU_1.png)
![NAU](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NAU_2.png)
![NAU](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NAU_3.png)
![NAU](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NAU_4.png)
![NAU](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NAU_5.png)
![NAU](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NAU_6.png)
![NAU](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NAU_7.png)
![NAU](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NAU_8.png)
 
## <a id='s1-25' />NEM
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_hdop, batt_v, fan_dc_u, fan_dc_l, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![NEM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NEM_0.png)
![NEM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NEM_1.png)
![NEM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NEM_2.png)
![NEM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NEM_3.png)
![NEM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NEM_4.png)
![NEM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NEM_5.png)
![NEM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NEM_6.png)
![NEM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NEM_7.png)
 
## <a id='s1-26' />NSE
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_numsat, gps_q, batt_v, fan_dc_u, fan_dc_l, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_geoid, gps_numsat, gps_q, t_log

Old variables removed from new files:

 
![NSE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NSE_0.png)
![NSE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NSE_1.png)
![NSE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NSE_2.png)
![NSE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NSE_3.png)
![NSE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NSE_4.png)
![NSE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NSE_5.png)
![NSE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NSE_6.png)
![NSE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NSE_7.png)
![NSE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NSE_8.png)
 
## <a id='s1-27' />NUK_B
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, t_surf, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![NUK_B](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_B_0.png)
![NUK_B](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_B_1.png)
![NUK_B](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_B_2.png)
![NUK_B](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_B_3.png)
![NUK_B](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_B_4.png)
![NUK_B](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_B_5.png)
 
## <a id='s1-28' />NUK_K
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![NUK_K](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_K_0.png)
![NUK_K](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_K_1.png)
![NUK_K](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_K_2.png)
![NUK_K](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_K_3.png)
![NUK_K](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_K_4.png)
![NUK_K](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_K_5.png)
![NUK_K](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_K_6.png)
 
## <a id='s1-29' />NUK_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![NUK_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_L_0.png)
![NUK_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_L_1.png)
![NUK_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_L_2.png)
![NUK_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_L_3.png)
![NUK_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_L_4.png)
![NUK_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_L_5.png)
![NUK_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_L_6.png)
 
## <a id='s1-30' />NUK_N
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![NUK_N](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_N_0.png)
![NUK_N](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_N_1.png)
![NUK_N](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_N_2.png)
![NUK_N](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_N_3.png)
![NUK_N](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_N_4.png)
![NUK_N](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_N_5.png)
![NUK_N](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_N_6.png)
 
## <a id='s1-31' />NUK_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![NUK_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_U_0.png)
![NUK_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_U_1.png)
![NUK_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_U_2.png)
![NUK_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_U_3.png)
![NUK_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_U_4.png)
![NUK_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_U_5.png)
![NUK_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_U_6.png)
 
## <a id='s1-32' />NUK_Uv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![NUK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_Uv3_0.png)
![NUK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_Uv3_1.png)
![NUK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_Uv3_2.png)
![NUK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_Uv3_3.png)
![NUK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_Uv3_4.png)
![NUK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_Uv3_5.png)
![NUK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/NUK_Uv3_6.png)
 
## <a id='s1-33' />QAS_A
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![QAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_A_0.png)
![QAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_A_1.png)
![QAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_A_2.png)
![QAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_A_3.png)
![QAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_A_4.png)
![QAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_A_5.png)
![QAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_A_6.png)
 
## <a id='s1-34' />QAS_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![QAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_L_0.png)
![QAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_L_1.png)
![QAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_L_2.png)
![QAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_L_3.png)
![QAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_L_4.png)
![QAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_L_5.png)
![QAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_L_6.png)
 
## <a id='s1-35' />QAS_Lv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![QAS_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_Lv3_0.png)
![QAS_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_Lv3_1.png)
![QAS_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_Lv3_2.png)
![QAS_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_Lv3_3.png)
![QAS_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_Lv3_4.png)
![QAS_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_Lv3_5.png)
![QAS_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_Lv3_6.png)
 
## <a id='s1-36' />QAS_M
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![QAS_M](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_M_0.png)
![QAS_M](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_M_1.png)
![QAS_M](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_M_2.png)
![QAS_M](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_M_3.png)
![QAS_M](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_M_4.png)
![QAS_M](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_M_5.png)
![QAS_M](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_M_6.png)
 
## <a id='s1-37' />QAS_Mv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![QAS_Mv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_Mv3_0.png)
![QAS_Mv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_Mv3_1.png)
![QAS_Mv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_Mv3_2.png)
![QAS_Mv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_Mv3_3.png)
![QAS_Mv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_Mv3_4.png)
![QAS_Mv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_Mv3_5.png)
![QAS_Mv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_Mv3_6.png)
 
## <a id='s1-38' />QAS_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![QAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_U_0.png)
![QAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_U_1.png)
![QAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_U_2.png)
![QAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_U_3.png)
![QAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_U_4.png)
![QAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_U_5.png)
![QAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_U_6.png)
 
## <a id='s1-39' />QAS_Uv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![QAS_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_Uv3_0.png)
![QAS_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_Uv3_1.png)
![QAS_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_Uv3_2.png)
![QAS_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_Uv3_3.png)
![QAS_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_Uv3_4.png)
![QAS_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_Uv3_5.png)
![QAS_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/QAS_Uv3_6.png)
 
## <a id='s1-40' />Roof_GEUS
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_hdop, batt_v, fan_dc_u, fan_dc_l, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![Roof_GEUS](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/Roof_GEUS_0.png)
![Roof_GEUS](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/Roof_GEUS_1.png)
![Roof_GEUS](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/Roof_GEUS_2.png)
![Roof_GEUS](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/Roof_GEUS_3.png)
![Roof_GEUS](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/Roof_GEUS_4.png)
![Roof_GEUS](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/Roof_GEUS_5.png)
![Roof_GEUS](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/Roof_GEUS_6.png)
![Roof_GEUS](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/Roof_GEUS_7.png)
 
## <a id='s1-41' />Roof_PROMICE
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![Roof_PROMICE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/Roof_PROMICE_0.png)
![Roof_PROMICE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/Roof_PROMICE_1.png)
![Roof_PROMICE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/Roof_PROMICE_2.png)
![Roof_PROMICE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/Roof_PROMICE_3.png)
![Roof_PROMICE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/Roof_PROMICE_4.png)
![Roof_PROMICE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/Roof_PROMICE_5.png)
![Roof_PROMICE](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/Roof_PROMICE_6.png)
 
## <a id='s1-42' />SCO_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![SCO_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SCO_L_0.png)
![SCO_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SCO_L_1.png)
![SCO_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SCO_L_2.png)
![SCO_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SCO_L_3.png)
![SCO_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SCO_L_4.png)
![SCO_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SCO_L_5.png)
![SCO_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SCO_L_6.png)
 
## <a id='s1-43' />SCO_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![SCO_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SCO_U_0.png)
![SCO_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SCO_U_1.png)
![SCO_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SCO_U_2.png)
![SCO_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SCO_U_3.png)
![SCO_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SCO_U_4.png)
![SCO_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SCO_U_5.png)
![SCO_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SCO_U_6.png)
 
## <a id='s1-44' />SDL
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_numsat, gps_q, batt_v, fan_dc_u, fan_dc_l, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_geoid, gps_numsat, gps_q, t_log

Old variables removed from new files:

 
![SDL](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SDL_0.png)
![SDL](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SDL_1.png)
![SDL](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SDL_2.png)
![SDL](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SDL_3.png)
![SDL](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SDL_4.png)
![SDL](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SDL_5.png)
![SDL](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SDL_6.png)
![SDL](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SDL_7.png)
![SDL](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SDL_8.png)
 
## <a id='s1-45' />SDM
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_numsat, gps_q, batt_v, fan_dc_u, fan_dc_l, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_geoid, gps_numsat, gps_q, t_log

Old variables removed from new files:

 
![SDM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SDM_0.png)
![SDM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SDM_1.png)
![SDM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SDM_2.png)
![SDM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SDM_3.png)
![SDM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SDM_4.png)
![SDM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SDM_5.png)
![SDM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SDM_6.png)
![SDM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SDM_7.png)
![SDM](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SDM_8.png)
 
## <a id='s1-46' />SWC
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![SWC](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SWC_0.png)
![SWC](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SWC_1.png)
![SWC](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SWC_2.png)
![SWC](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SWC_3.png)
![SWC](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SWC_4.png)
![SWC](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SWC_5.png)
![SWC](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SWC_6.png)
 
## <a id='s1-47' />SWC_O
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![SWC_O](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SWC_O_0.png)
![SWC_O](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SWC_O_1.png)
![SWC_O](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SWC_O_2.png)
![SWC_O](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SWC_O_3.png)
![SWC_O](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SWC_O_4.png)
![SWC_O](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SWC_O_5.png)
![SWC_O](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/SWC_O_6.png)
 
## <a id='s1-48' />TAS_A
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![TAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TAS_A_0.png)
![TAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TAS_A_1.png)
![TAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TAS_A_2.png)
![TAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TAS_A_3.png)
![TAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TAS_A_4.png)
![TAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TAS_A_5.png)
![TAS_A](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TAS_A_6.png)
 
## <a id='s1-49' />TAS_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![TAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TAS_L_0.png)
![TAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TAS_L_1.png)
![TAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TAS_L_2.png)
![TAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TAS_L_3.png)
![TAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TAS_L_4.png)
![TAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TAS_L_5.png)
![TAS_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TAS_L_6.png)
 
## <a id='s1-50' />TAS_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![TAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TAS_U_0.png)
![TAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TAS_U_1.png)
![TAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TAS_U_2.png)
![TAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TAS_U_3.png)
![TAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TAS_U_4.png)
![TAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TAS_U_5.png)
![TAS_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TAS_U_6.png)
 
## <a id='s1-51' />THU_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![THU_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_L_0.png)
![THU_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_L_1.png)
![THU_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_L_2.png)
![THU_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_L_3.png)
![THU_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_L_4.png)
![THU_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_L_5.png)
![THU_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_L_6.png)
 
## <a id='s1-52' />THU_L2
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![THU_L2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_L2_0.png)
![THU_L2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_L2_1.png)
![THU_L2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_L2_2.png)
![THU_L2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_L2_3.png)
![THU_L2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_L2_4.png)
![THU_L2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_L2_5.png)
![THU_L2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_L2_6.png)
 
## <a id='s1-53' />THU_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![THU_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_U_0.png)
![THU_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_U_1.png)
![THU_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_U_2.png)
![THU_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_U_3.png)
![THU_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_U_4.png)
![THU_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_U_5.png)
![THU_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_U_6.png)
 
## <a id='s1-54' />THU_U2
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![THU_U2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_U2_0.png)
![THU_U2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_U2_1.png)
![THU_U2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_U2_2.png)
![THU_U2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_U2_3.png)
![THU_U2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_U2_4.png)
![THU_U2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_U2_5.png)
![THU_U2](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_U2_6.png)
 
## <a id='s1-55' />THU_U2v3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![THU_U2v3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_U2v3_0.png)
![THU_U2v3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_U2v3_1.png)
![THU_U2v3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_U2v3_2.png)
![THU_U2v3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_U2v3_3.png)
![THU_U2v3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_U2v3_4.png)
![THU_U2v3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_U2v3_5.png)
![THU_U2v3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/THU_U2v3_6.png)
 
## <a id='s1-56' />TUN
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_numsat, gps_q, batt_v, fan_dc_u, fan_dc_l, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_geoid, gps_numsat, gps_q, t_log

Old variables removed from new files:

 
![TUN](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TUN_0.png)
![TUN](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TUN_1.png)
![TUN](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TUN_2.png)
![TUN](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TUN_3.png)
![TUN](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TUN_4.png)
![TUN](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TUN_5.png)
![TUN](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TUN_6.png)
![TUN](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TUN_7.png)
![TUN](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/TUN_8.png)
 
## <a id='s1-57' />UPE_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![UPE_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/UPE_L_0.png)
![UPE_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/UPE_L_1.png)
![UPE_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/UPE_L_2.png)
![UPE_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/UPE_L_3.png)
![UPE_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/UPE_L_4.png)
![UPE_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/UPE_L_5.png)
![UPE_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/UPE_L_6.png)
 
## <a id='s1-58' />UPE_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_q, batt_v, batt_v_ss, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_q, batt_v_ss

Old variables removed from new files:

 
![UPE_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/UPE_U_0.png)
![UPE_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/UPE_U_1.png)
![UPE_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/UPE_U_2.png)
![UPE_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/UPE_U_3.png)
![UPE_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/UPE_U_4.png)
![UPE_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/UPE_U_5.png)
![UPE_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/UPE_U_6.png)
 
## <a id='s1-59' />UWN
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![UWN](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/UWN_0.png)
![UWN](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/UWN_1.png)
![UWN](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/UWN_2.png)
![UWN](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/UWN_3.png)
![UWN](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/UWN_4.png)
![UWN](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/UWN_5.png)
![UWN](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/UWN_6.png)
 
## <a id='s1-60' />WEG_B
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, t_surf, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![WEG_B](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/WEG_B_0.png)
![WEG_B](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/WEG_B_1.png)
![WEG_B](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/WEG_B_2.png)
![WEG_B](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/WEG_B_3.png)
![WEG_B](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/WEG_B_4.png)
![WEG_B](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/WEG_B_5.png)
 
## <a id='s1-61' />WEG_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![WEG_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/WEG_L_0.png)
![WEG_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/WEG_L_1.png)
![WEG_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/WEG_L_2.png)
![WEG_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/WEG_L_3.png)
![WEG_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/WEG_L_4.png)
![WEG_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/WEG_L_5.png)
![WEG_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/WEG_L_6.png)
 
## <a id='s1-62' />XXX
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![XXX](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/XXX_0.png)
![XXX](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/XXX_1.png)
![XXX](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/XXX_2.png)
![XXX](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/XXX_3.png)
![XXX](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/XXX_4.png)
![XXX](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/XXX_5.png)
![XXX](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/XXX_6.png)
 
## <a id='s1-63' />ZAK_A
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_hdop, batt_v, fan_dc_u, fan_dc_l, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![ZAK_A](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_A_0.png)
![ZAK_A](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_A_1.png)
![ZAK_A](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_A_2.png)
![ZAK_A](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_A_3.png)
![ZAK_A](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_A_4.png)
![ZAK_A](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_A_5.png)
![ZAK_A](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_A_6.png)
![ZAK_A](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_A_7.png)
 
## <a id='s1-64' />ZAK_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, gps_numsat, gps_q, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:
gps_numsat, gps_q

Old variables removed from new files:

 
![ZAK_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_L_0.png)
![ZAK_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_L_1.png)
![ZAK_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_L_2.png)
![ZAK_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_L_3.png)
![ZAK_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_L_4.png)
![ZAK_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_L_5.png)
![ZAK_L](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_L_6.png)
 
## <a id='s1-65' />ZAK_Lv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![ZAK_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_Lv3_0.png)
![ZAK_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_Lv3_1.png)
![ZAK_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_Lv3_2.png)
![ZAK_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_Lv3_3.png)
![ZAK_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_Lv3_4.png)
![ZAK_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_Lv3_5.png)
![ZAK_Lv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_Lv3_6.png)
 
## <a id='s1-66' />ZAK_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![ZAK_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_U_0.png)
![ZAK_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_U_1.png)
![ZAK_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_U_2.png)
![ZAK_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_U_3.png)
![ZAK_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_U_4.png)
![ZAK_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_U_5.png)
![ZAK_U](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_U_6.png)
 
## <a id='s1-67' />ZAK_Uv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, p_i, t_i, rh_i, rh_i_cor, wspd_i, wdir_i, wspd_x_i, wspd_y_i

New variables not in old files:


Old variables removed from new files:

 
![ZAK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_Uv3_0.png)
![ZAK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_Uv3_1.png)
![ZAK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_Uv3_2.png)
![ZAK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_Uv3_3.png)
![ZAK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_Uv3_4.png)
![ZAK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_Uv3_5.png)
![ZAK_Uv3](../figures/aws-l3_versus_aws-l3-dev_20240613_scatter/ZAK_Uv3_6.png)
 
