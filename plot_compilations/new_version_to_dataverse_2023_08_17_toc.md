* [Comparison of data v9 (new) to v8 (old).](#s1)
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
  * [KAN_M](#s1-12)
  * [KAN_U](#s1-13)
  * [KPC_L](#s1-14)
  * [KPC_Lv3](#s1-15)
  * [KPC_U](#s1-16)
  * [KPC_Uv3](#s1-17)
  * [LYN_L](#s1-18)
  * [LYN_T](#s1-19)
  * [MIT](#s1-20)
  * [NAE](#s1-21)
  * [NAU](#s1-22)
  * [NEM](#s1-23)
  * [NSE](#s1-24)
  * [NUK_K](#s1-25)
  * [NUK_L](#s1-26)
  * [NUK_N](#s1-27)
  * [NUK_U](#s1-28)
  * [NUK_Uv3](#s1-29)
  * [QAS_A](#s1-30)
  * [QAS_L](#s1-31)
  * [QAS_Lv3](#s1-32)
  * [QAS_M](#s1-33)
  * [QAS_U](#s1-34)
  * [QAS_Uv3](#s1-35)
  * [Roof_GEUS](#s1-36)
  * [Roof_PROMICE](#s1-37)
  * [SCO_L](#s1-38)
  * [SCO_U](#s1-39)
  * [SDL](#s1-40)
  * [SDM](#s1-41)
  * [SWC](#s1-42)
  * [SWC_O](#s1-43)
  * [TAS_A](#s1-44)
  * [TAS_L](#s1-45)
  * [TAS_U](#s1-46)
  * [THU_L](#s1-47)
  * [THU_L2](#s1-48)
  * [THU_U](#s1-49)
  * [THU_U2](#s1-50)
  * [TUN](#s1-51)
  * [UPE_L](#s1-52)
  * [UPE_U](#s1-53)
  * [UWN](#s1-54)
  * [WEG_B](#s1-55)
  * [WEG_L](#s1-56)
  * [ZAK_A](#s1-57)
  * [ZAK_L](#s1-58)
  * [ZAK_Lv3](#s1-59)
  * [ZAK_U](#s1-60)
  * [ZAK_Uv3](#s1-61)
# <a id='s1' />Comparison of data v9 (new) to v8 (old).
~version name is as defined in AWS_changelog.txt~
## <a id='s1-1' />CEN1
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![CEN1](../figures/flags/CEN1_0.png)
![CEN1](../figures/flags/CEN1_1.png)
![CEN1](../figures/flags/CEN1_2.png)
![CEN1](../figures/flags/CEN1_3.png)
![CEN1](../figures/flags/CEN1_4.png)
![CEN1](../figures/flags/CEN1_5.png)
![CEN1](../figures/flags/CEN1_6.png)
![CEN1](../figures/flags/CEN1_7.png)
![CEN1](../figures/flags/CEN1_8.png)
![CEN1](../figures/flags/CEN1_9.png)
 
## <a id='s1-2' />CEN2
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_hdop, batt_v, fan_dc_u, fan_dc_l, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, precip_u_rate, precip_l_rate

Old variables removed from new files:
gps_geounit
 
![CEN2](../figures/flags/CEN2_0.png)
![CEN2](../figures/flags/CEN2_1.png)
![CEN2](../figures/flags/CEN2_2.png)
![CEN2](../figures/flags/CEN2_3.png)
![CEN2](../figures/flags/CEN2_4.png)
![CEN2](../figures/flags/CEN2_5.png)
![CEN2](../figures/flags/CEN2_6.png)
![CEN2](../figures/flags/CEN2_7.png)
![CEN2](../figures/flags/CEN2_8.png)
![CEN2](../figures/flags/CEN2_9.png)
![CEN2](../figures/flags/CEN2_10.png)
![CEN2](../figures/flags/CEN2_11.png)
![CEN2](../figures/flags/CEN2_12.png)
 
## <a id='s1-3' />CP1
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_hdop, batt_v, fan_dc_u, fan_dc_l, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, precip_u_rate, precip_l_rate

Old variables removed from new files:
gps_geounit
 
![CP1](../figures/flags/CP1_0.png)
![CP1](../figures/flags/CP1_1.png)
![CP1](../figures/flags/CP1_2.png)
![CP1](../figures/flags/CP1_3.png)
![CP1](../figures/flags/CP1_4.png)
![CP1](../figures/flags/CP1_5.png)
![CP1](../figures/flags/CP1_6.png)
![CP1](../figures/flags/CP1_7.png)
![CP1](../figures/flags/CP1_8.png)
![CP1](../figures/flags/CP1_9.png)
![CP1](../figures/flags/CP1_10.png)
![CP1](../figures/flags/CP1_11.png)
![CP1](../figures/flags/CP1_12.png)
 
## <a id='s1-4' />DY2
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_hdop, batt_v, fan_dc_u, fan_dc_l, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, precip_u_rate, precip_l_rate

Old variables removed from new files:

 
![DY2](../figures/flags/DY2_0.png)
![DY2](../figures/flags/DY2_1.png)
![DY2](../figures/flags/DY2_2.png)
![DY2](../figures/flags/DY2_3.png)
![DY2](../figures/flags/DY2_4.png)
![DY2](../figures/flags/DY2_5.png)
![DY2](../figures/flags/DY2_6.png)
![DY2](../figures/flags/DY2_7.png)
![DY2](../figures/flags/DY2_8.png)
![DY2](../figures/flags/DY2_9.png)
![DY2](../figures/flags/DY2_10.png)
![DY2](../figures/flags/DY2_11.png)
![DY2](../figures/flags/DY2_12.png)
 
## <a id='s1-5' />EGP
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![EGP](../figures/flags/EGP_0.png)
![EGP](../figures/flags/EGP_1.png)
![EGP](../figures/flags/EGP_2.png)
![EGP](../figures/flags/EGP_3.png)
![EGP](../figures/flags/EGP_4.png)
![EGP](../figures/flags/EGP_5.png)
![EGP](../figures/flags/EGP_6.png)
![EGP](../figures/flags/EGP_7.png)
![EGP](../figures/flags/EGP_8.png)
![EGP](../figures/flags/EGP_9.png)
 
## <a id='s1-6' />FRE
C:/Users/bav/Downloads/dataverse_files/day/FRE_day.csv cannot be found in old data
## <a id='s1-7' />HUM
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_hdop, batt_v, fan_dc_u, fan_dc_l, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, precip_u_rate, precip_l_rate

Old variables removed from new files:

 
![HUM](../figures/flags/HUM_0.png)
![HUM](../figures/flags/HUM_1.png)
![HUM](../figures/flags/HUM_2.png)
![HUM](../figures/flags/HUM_3.png)
![HUM](../figures/flags/HUM_4.png)
![HUM](../figures/flags/HUM_5.png)
![HUM](../figures/flags/HUM_6.png)
![HUM](../figures/flags/HUM_7.png)
![HUM](../figures/flags/HUM_8.png)
![HUM](../figures/flags/HUM_9.png)
![HUM](../figures/flags/HUM_10.png)
![HUM](../figures/flags/HUM_11.png)
![HUM](../figures/flags/HUM_12.png)
 
## <a id='s1-8' />JAR
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![JAR](../figures/flags/JAR_0.png)
![JAR](../figures/flags/JAR_1.png)
![JAR](../figures/flags/JAR_2.png)
![JAR](../figures/flags/JAR_3.png)
![JAR](../figures/flags/JAR_4.png)
![JAR](../figures/flags/JAR_5.png)
![JAR](../figures/flags/JAR_6.png)
![JAR](../figures/flags/JAR_7.png)
![JAR](../figures/flags/JAR_8.png)
![JAR](../figures/flags/JAR_9.png)
 
## <a id='s1-9' />JAR_O
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![JAR_O](../figures/flags/JAR_O_0.png)
![JAR_O](../figures/flags/JAR_O_1.png)
![JAR_O](../figures/flags/JAR_O_2.png)
![JAR_O](../figures/flags/JAR_O_3.png)
![JAR_O](../figures/flags/JAR_O_4.png)
![JAR_O](../figures/flags/JAR_O_5.png)
![JAR_O](../figures/flags/JAR_O_6.png)
![JAR_O](../figures/flags/JAR_O_7.png)
![JAR_O](../figures/flags/JAR_O_8.png)
![JAR_O](../figures/flags/JAR_O_9.png)
 
## <a id='s1-10' />KAN_B
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, t_surf, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
cc, dlhf_u, dshf_u, gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![KAN_B](../figures/flags/KAN_B_0.png)
![KAN_B](../figures/flags/KAN_B_1.png)
![KAN_B](../figures/flags/KAN_B_2.png)
![KAN_B](../figures/flags/KAN_B_3.png)
![KAN_B](../figures/flags/KAN_B_4.png)
![KAN_B](../figures/flags/KAN_B_5.png)
![KAN_B](../figures/flags/KAN_B_6.png)
![KAN_B](../figures/flags/KAN_B_7.png)
![KAN_B](../figures/flags/KAN_B_8.png)
![KAN_B](../figures/flags/KAN_B_9.png)
 
## <a id='s1-11' />KAN_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![KAN_L](../figures/flags/KAN_L_0.png)
![KAN_L](../figures/flags/KAN_L_1.png)
![KAN_L](../figures/flags/KAN_L_2.png)
![KAN_L](../figures/flags/KAN_L_3.png)
![KAN_L](../figures/flags/KAN_L_4.png)
![KAN_L](../figures/flags/KAN_L_5.png)
![KAN_L](../figures/flags/KAN_L_6.png)
![KAN_L](../figures/flags/KAN_L_7.png)
![KAN_L](../figures/flags/KAN_L_8.png)
![KAN_L](../figures/flags/KAN_L_9.png)
 
## <a id='s1-12' />KAN_M
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![KAN_M](../figures/flags/KAN_M_0.png)
![KAN_M](../figures/flags/KAN_M_1.png)
![KAN_M](../figures/flags/KAN_M_2.png)
![KAN_M](../figures/flags/KAN_M_3.png)
![KAN_M](../figures/flags/KAN_M_4.png)
![KAN_M](../figures/flags/KAN_M_5.png)
![KAN_M](../figures/flags/KAN_M_6.png)
![KAN_M](../figures/flags/KAN_M_7.png)
![KAN_M](../figures/flags/KAN_M_8.png)
![KAN_M](../figures/flags/KAN_M_9.png)
 
## <a id='s1-13' />KAN_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![KAN_U](../figures/flags/KAN_U_0.png)
![KAN_U](../figures/flags/KAN_U_1.png)
![KAN_U](../figures/flags/KAN_U_2.png)
![KAN_U](../figures/flags/KAN_U_3.png)
![KAN_U](../figures/flags/KAN_U_4.png)
![KAN_U](../figures/flags/KAN_U_5.png)
![KAN_U](../figures/flags/KAN_U_6.png)
![KAN_U](../figures/flags/KAN_U_7.png)
![KAN_U](../figures/flags/KAN_U_8.png)
![KAN_U](../figures/flags/KAN_U_9.png)
 
## <a id='s1-14' />KPC_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![KPC_L](../figures/flags/KPC_L_0.png)
![KPC_L](../figures/flags/KPC_L_1.png)
![KPC_L](../figures/flags/KPC_L_2.png)
![KPC_L](../figures/flags/KPC_L_3.png)
![KPC_L](../figures/flags/KPC_L_4.png)
![KPC_L](../figures/flags/KPC_L_5.png)
![KPC_L](../figures/flags/KPC_L_6.png)
![KPC_L](../figures/flags/KPC_L_7.png)
![KPC_L](../figures/flags/KPC_L_8.png)
![KPC_L](../figures/flags/KPC_L_9.png)
 
## <a id='s1-15' />KPC_Lv3
C:/Users/bav/Downloads/dataverse_files/day/KPC_Lv3_day.csv cannot be found in old data
## <a id='s1-16' />KPC_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![KPC_U](../figures/flags/KPC_U_0.png)
![KPC_U](../figures/flags/KPC_U_1.png)
![KPC_U](../figures/flags/KPC_U_2.png)
![KPC_U](../figures/flags/KPC_U_3.png)
![KPC_U](../figures/flags/KPC_U_4.png)
![KPC_U](../figures/flags/KPC_U_5.png)
![KPC_U](../figures/flags/KPC_U_6.png)
![KPC_U](../figures/flags/KPC_U_7.png)
![KPC_U](../figures/flags/KPC_U_8.png)
![KPC_U](../figures/flags/KPC_U_9.png)
 
## <a id='s1-17' />KPC_Uv3
C:/Users/bav/Downloads/dataverse_files/day/KPC_Uv3_day.csv cannot be found in old data
## <a id='s1-18' />LYN_L
C:/Users/bav/Downloads/dataverse_files/day/LYN_L_day.csv cannot be found in old data
## <a id='s1-19' />LYN_T
C:/Users/bav/Downloads/dataverse_files/day/LYN_T_day.csv cannot be found in old data
## <a id='s1-20' />MIT
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![MIT](../figures/flags/MIT_0.png)
![MIT](../figures/flags/MIT_1.png)
![MIT](../figures/flags/MIT_2.png)
![MIT](../figures/flags/MIT_3.png)
![MIT](../figures/flags/MIT_4.png)
![MIT](../figures/flags/MIT_5.png)
![MIT](../figures/flags/MIT_6.png)
![MIT](../figures/flags/MIT_7.png)
![MIT](../figures/flags/MIT_8.png)
![MIT](../figures/flags/MIT_9.png)
 
## <a id='s1-21' />NAE
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_hdop, batt_v, fan_dc_u, fan_dc_l, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, precip_u_rate, precip_l_rate

Old variables removed from new files:

 
![NAE](../figures/flags/NAE_0.png)
![NAE](../figures/flags/NAE_1.png)
![NAE](../figures/flags/NAE_2.png)
![NAE](../figures/flags/NAE_3.png)
![NAE](../figures/flags/NAE_4.png)
![NAE](../figures/flags/NAE_5.png)
![NAE](../figures/flags/NAE_6.png)
![NAE](../figures/flags/NAE_7.png)
![NAE](../figures/flags/NAE_8.png)
![NAE](../figures/flags/NAE_9.png)
![NAE](../figures/flags/NAE_10.png)
![NAE](../figures/flags/NAE_11.png)
![NAE](../figures/flags/NAE_12.png)
 
## <a id='s1-22' />NAU
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_hdop, batt_v, fan_dc_u, fan_dc_l, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, precip_u_rate, precip_l_rate

Old variables removed from new files:

 
![NAU](../figures/flags/NAU_0.png)
![NAU](../figures/flags/NAU_1.png)
![NAU](../figures/flags/NAU_2.png)
![NAU](../figures/flags/NAU_3.png)
![NAU](../figures/flags/NAU_4.png)
![NAU](../figures/flags/NAU_5.png)
![NAU](../figures/flags/NAU_6.png)
![NAU](../figures/flags/NAU_7.png)
![NAU](../figures/flags/NAU_8.png)
![NAU](../figures/flags/NAU_9.png)
![NAU](../figures/flags/NAU_10.png)
![NAU](../figures/flags/NAU_11.png)
![NAU](../figures/flags/NAU_12.png)
 
## <a id='s1-23' />NEM
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_hdop, batt_v, fan_dc_u, fan_dc_l, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, precip_u_rate, precip_l_rate

Old variables removed from new files:

 
![NEM](../figures/flags/NEM_0.png)
![NEM](../figures/flags/NEM_1.png)
![NEM](../figures/flags/NEM_2.png)
![NEM](../figures/flags/NEM_3.png)
![NEM](../figures/flags/NEM_4.png)
![NEM](../figures/flags/NEM_5.png)
![NEM](../figures/flags/NEM_6.png)
![NEM](../figures/flags/NEM_7.png)
![NEM](../figures/flags/NEM_8.png)
![NEM](../figures/flags/NEM_9.png)
![NEM](../figures/flags/NEM_10.png)
![NEM](../figures/flags/NEM_11.png)
![NEM](../figures/flags/NEM_12.png)
 
## <a id='s1-24' />NSE
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_hdop, batt_v, fan_dc_u, fan_dc_l, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, precip_u_rate, precip_l_rate

Old variables removed from new files:
gps_geounit
 
![NSE](../figures/flags/NSE_0.png)
![NSE](../figures/flags/NSE_1.png)
![NSE](../figures/flags/NSE_2.png)
![NSE](../figures/flags/NSE_3.png)
![NSE](../figures/flags/NSE_4.png)
![NSE](../figures/flags/NSE_5.png)
![NSE](../figures/flags/NSE_6.png)
![NSE](../figures/flags/NSE_7.png)
![NSE](../figures/flags/NSE_8.png)
![NSE](../figures/flags/NSE_9.png)
![NSE](../figures/flags/NSE_10.png)
![NSE](../figures/flags/NSE_11.png)
![NSE](../figures/flags/NSE_12.png)
 
## <a id='s1-25' />NUK_K
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![NUK_K](../figures/flags/NUK_K_0.png)
![NUK_K](../figures/flags/NUK_K_1.png)
![NUK_K](../figures/flags/NUK_K_2.png)
![NUK_K](../figures/flags/NUK_K_3.png)
![NUK_K](../figures/flags/NUK_K_4.png)
![NUK_K](../figures/flags/NUK_K_5.png)
![NUK_K](../figures/flags/NUK_K_6.png)
![NUK_K](../figures/flags/NUK_K_7.png)
![NUK_K](../figures/flags/NUK_K_8.png)
![NUK_K](../figures/flags/NUK_K_9.png)
 
## <a id='s1-26' />NUK_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![NUK_L](../figures/flags/NUK_L_0.png)
![NUK_L](../figures/flags/NUK_L_1.png)
![NUK_L](../figures/flags/NUK_L_2.png)
![NUK_L](../figures/flags/NUK_L_3.png)
![NUK_L](../figures/flags/NUK_L_4.png)
![NUK_L](../figures/flags/NUK_L_5.png)
![NUK_L](../figures/flags/NUK_L_6.png)
![NUK_L](../figures/flags/NUK_L_7.png)
![NUK_L](../figures/flags/NUK_L_8.png)
![NUK_L](../figures/flags/NUK_L_9.png)
 
## <a id='s1-27' />NUK_N
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![NUK_N](../figures/flags/NUK_N_0.png)
![NUK_N](../figures/flags/NUK_N_1.png)
![NUK_N](../figures/flags/NUK_N_2.png)
![NUK_N](../figures/flags/NUK_N_3.png)
![NUK_N](../figures/flags/NUK_N_4.png)
![NUK_N](../figures/flags/NUK_N_5.png)
![NUK_N](../figures/flags/NUK_N_6.png)
![NUK_N](../figures/flags/NUK_N_7.png)
![NUK_N](../figures/flags/NUK_N_8.png)
![NUK_N](../figures/flags/NUK_N_9.png)
 
## <a id='s1-28' />NUK_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![NUK_U](../figures/flags/NUK_U_0.png)
![NUK_U](../figures/flags/NUK_U_1.png)
![NUK_U](../figures/flags/NUK_U_2.png)
![NUK_U](../figures/flags/NUK_U_3.png)
![NUK_U](../figures/flags/NUK_U_4.png)
![NUK_U](../figures/flags/NUK_U_5.png)
![NUK_U](../figures/flags/NUK_U_6.png)
![NUK_U](../figures/flags/NUK_U_7.png)
![NUK_U](../figures/flags/NUK_U_8.png)
![NUK_U](../figures/flags/NUK_U_9.png)
 
## <a id='s1-29' />NUK_Uv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![NUK_Uv3](../figures/flags/NUK_Uv3_0.png)
![NUK_Uv3](../figures/flags/NUK_Uv3_1.png)
![NUK_Uv3](../figures/flags/NUK_Uv3_2.png)
![NUK_Uv3](../figures/flags/NUK_Uv3_3.png)
![NUK_Uv3](../figures/flags/NUK_Uv3_4.png)
![NUK_Uv3](../figures/flags/NUK_Uv3_5.png)
![NUK_Uv3](../figures/flags/NUK_Uv3_6.png)
![NUK_Uv3](../figures/flags/NUK_Uv3_7.png)
![NUK_Uv3](../figures/flags/NUK_Uv3_8.png)
![NUK_Uv3](../figures/flags/NUK_Uv3_9.png)
 
## <a id='s1-30' />QAS_A
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![QAS_A](../figures/flags/QAS_A_0.png)
![QAS_A](../figures/flags/QAS_A_1.png)
![QAS_A](../figures/flags/QAS_A_2.png)
![QAS_A](../figures/flags/QAS_A_3.png)
![QAS_A](../figures/flags/QAS_A_4.png)
![QAS_A](../figures/flags/QAS_A_5.png)
![QAS_A](../figures/flags/QAS_A_6.png)
![QAS_A](../figures/flags/QAS_A_7.png)
![QAS_A](../figures/flags/QAS_A_8.png)
![QAS_A](../figures/flags/QAS_A_9.png)
 
## <a id='s1-31' />QAS_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![QAS_L](../figures/flags/QAS_L_0.png)
![QAS_L](../figures/flags/QAS_L_1.png)
![QAS_L](../figures/flags/QAS_L_2.png)
![QAS_L](../figures/flags/QAS_L_3.png)
![QAS_L](../figures/flags/QAS_L_4.png)
![QAS_L](../figures/flags/QAS_L_5.png)
![QAS_L](../figures/flags/QAS_L_6.png)
![QAS_L](../figures/flags/QAS_L_7.png)
![QAS_L](../figures/flags/QAS_L_8.png)
![QAS_L](../figures/flags/QAS_L_9.png)
 
## <a id='s1-32' />QAS_Lv3
C:/Users/bav/Downloads/dataverse_files/day/QAS_Lv3_day.csv cannot be found in old data
## <a id='s1-33' />QAS_M
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![QAS_M](../figures/flags/QAS_M_0.png)
![QAS_M](../figures/flags/QAS_M_1.png)
![QAS_M](../figures/flags/QAS_M_2.png)
![QAS_M](../figures/flags/QAS_M_3.png)
![QAS_M](../figures/flags/QAS_M_4.png)
![QAS_M](../figures/flags/QAS_M_5.png)
![QAS_M](../figures/flags/QAS_M_6.png)
![QAS_M](../figures/flags/QAS_M_7.png)
![QAS_M](../figures/flags/QAS_M_8.png)
![QAS_M](../figures/flags/QAS_M_9.png)
 
## <a id='s1-34' />QAS_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![QAS_U](../figures/flags/QAS_U_0.png)
![QAS_U](../figures/flags/QAS_U_1.png)
![QAS_U](../figures/flags/QAS_U_2.png)
![QAS_U](../figures/flags/QAS_U_3.png)
![QAS_U](../figures/flags/QAS_U_4.png)
![QAS_U](../figures/flags/QAS_U_5.png)
![QAS_U](../figures/flags/QAS_U_6.png)
![QAS_U](../figures/flags/QAS_U_7.png)
![QAS_U](../figures/flags/QAS_U_8.png)
![QAS_U](../figures/flags/QAS_U_9.png)
 
## <a id='s1-35' />QAS_Uv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![QAS_Uv3](../figures/flags/QAS_Uv3_0.png)
![QAS_Uv3](../figures/flags/QAS_Uv3_1.png)
![QAS_Uv3](../figures/flags/QAS_Uv3_2.png)
![QAS_Uv3](../figures/flags/QAS_Uv3_3.png)
![QAS_Uv3](../figures/flags/QAS_Uv3_4.png)
![QAS_Uv3](../figures/flags/QAS_Uv3_5.png)
![QAS_Uv3](../figures/flags/QAS_Uv3_6.png)
![QAS_Uv3](../figures/flags/QAS_Uv3_7.png)
![QAS_Uv3](../figures/flags/QAS_Uv3_8.png)
![QAS_Uv3](../figures/flags/QAS_Uv3_9.png)
 
## <a id='s1-36' />Roof_GEUS
C:/Users/bav/Downloads/dataverse_files/day/Roof_GEUS_day.csv cannot be found in old data
## <a id='s1-37' />Roof_PROMICE
C:/Users/bav/Downloads/dataverse_files/day/Roof_PROMICE_day.csv cannot be found in old data
## <a id='s1-38' />SCO_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![SCO_L](../figures/flags/SCO_L_0.png)
![SCO_L](../figures/flags/SCO_L_1.png)
![SCO_L](../figures/flags/SCO_L_2.png)
![SCO_L](../figures/flags/SCO_L_3.png)
![SCO_L](../figures/flags/SCO_L_4.png)
![SCO_L](../figures/flags/SCO_L_5.png)
![SCO_L](../figures/flags/SCO_L_6.png)
![SCO_L](../figures/flags/SCO_L_7.png)
![SCO_L](../figures/flags/SCO_L_8.png)
![SCO_L](../figures/flags/SCO_L_9.png)
 
## <a id='s1-39' />SCO_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![SCO_U](../figures/flags/SCO_U_0.png)
![SCO_U](../figures/flags/SCO_U_1.png)
![SCO_U](../figures/flags/SCO_U_2.png)
![SCO_U](../figures/flags/SCO_U_3.png)
![SCO_U](../figures/flags/SCO_U_4.png)
![SCO_U](../figures/flags/SCO_U_5.png)
![SCO_U](../figures/flags/SCO_U_6.png)
![SCO_U](../figures/flags/SCO_U_7.png)
![SCO_U](../figures/flags/SCO_U_8.png)
![SCO_U](../figures/flags/SCO_U_9.png)
 
## <a id='s1-40' />SDL
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_hdop, batt_v, fan_dc_u, fan_dc_l, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, precip_u_rate, precip_l_rate

Old variables removed from new files:
gps_geounit
 
![SDL](../figures/flags/SDL_0.png)
![SDL](../figures/flags/SDL_1.png)
![SDL](../figures/flags/SDL_2.png)
![SDL](../figures/flags/SDL_3.png)
![SDL](../figures/flags/SDL_4.png)
![SDL](../figures/flags/SDL_5.png)
![SDL](../figures/flags/SDL_6.png)
![SDL](../figures/flags/SDL_7.png)
![SDL](../figures/flags/SDL_8.png)
![SDL](../figures/flags/SDL_9.png)
![SDL](../figures/flags/SDL_10.png)
![SDL](../figures/flags/SDL_11.png)
![SDL](../figures/flags/SDL_12.png)
 
## <a id='s1-41' />SDM
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_hdop, batt_v, fan_dc_u, fan_dc_l, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, precip_u_rate, precip_l_rate

Old variables removed from new files:

 
![SDM](../figures/flags/SDM_0.png)
![SDM](../figures/flags/SDM_1.png)
![SDM](../figures/flags/SDM_2.png)
![SDM](../figures/flags/SDM_3.png)
![SDM](../figures/flags/SDM_4.png)
![SDM](../figures/flags/SDM_5.png)
![SDM](../figures/flags/SDM_6.png)
![SDM](../figures/flags/SDM_7.png)
![SDM](../figures/flags/SDM_8.png)
![SDM](../figures/flags/SDM_9.png)
![SDM](../figures/flags/SDM_10.png)
![SDM](../figures/flags/SDM_11.png)
![SDM](../figures/flags/SDM_12.png)
 
## <a id='s1-42' />SWC
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![SWC](../figures/flags/SWC_0.png)
![SWC](../figures/flags/SWC_1.png)
![SWC](../figures/flags/SWC_2.png)
![SWC](../figures/flags/SWC_3.png)
![SWC](../figures/flags/SWC_4.png)
![SWC](../figures/flags/SWC_5.png)
![SWC](../figures/flags/SWC_6.png)
![SWC](../figures/flags/SWC_7.png)
![SWC](../figures/flags/SWC_8.png)
![SWC](../figures/flags/SWC_9.png)
 
## <a id='s1-43' />SWC_O
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![SWC_O](../figures/flags/SWC_O_0.png)
![SWC_O](../figures/flags/SWC_O_1.png)
![SWC_O](../figures/flags/SWC_O_2.png)
![SWC_O](../figures/flags/SWC_O_3.png)
![SWC_O](../figures/flags/SWC_O_4.png)
![SWC_O](../figures/flags/SWC_O_5.png)
![SWC_O](../figures/flags/SWC_O_6.png)
![SWC_O](../figures/flags/SWC_O_7.png)
![SWC_O](../figures/flags/SWC_O_8.png)
![SWC_O](../figures/flags/SWC_O_9.png)
 
## <a id='s1-44' />TAS_A
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![TAS_A](../figures/flags/TAS_A_0.png)
![TAS_A](../figures/flags/TAS_A_1.png)
![TAS_A](../figures/flags/TAS_A_2.png)
![TAS_A](../figures/flags/TAS_A_3.png)
![TAS_A](../figures/flags/TAS_A_4.png)
![TAS_A](../figures/flags/TAS_A_5.png)
![TAS_A](../figures/flags/TAS_A_6.png)
![TAS_A](../figures/flags/TAS_A_7.png)
![TAS_A](../figures/flags/TAS_A_8.png)
![TAS_A](../figures/flags/TAS_A_9.png)
 
## <a id='s1-45' />TAS_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![TAS_L](../figures/flags/TAS_L_0.png)
![TAS_L](../figures/flags/TAS_L_1.png)
![TAS_L](../figures/flags/TAS_L_2.png)
![TAS_L](../figures/flags/TAS_L_3.png)
![TAS_L](../figures/flags/TAS_L_4.png)
![TAS_L](../figures/flags/TAS_L_5.png)
![TAS_L](../figures/flags/TAS_L_6.png)
![TAS_L](../figures/flags/TAS_L_7.png)
![TAS_L](../figures/flags/TAS_L_8.png)
![TAS_L](../figures/flags/TAS_L_9.png)
 
## <a id='s1-46' />TAS_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![TAS_U](../figures/flags/TAS_U_0.png)
![TAS_U](../figures/flags/TAS_U_1.png)
![TAS_U](../figures/flags/TAS_U_2.png)
![TAS_U](../figures/flags/TAS_U_3.png)
![TAS_U](../figures/flags/TAS_U_4.png)
![TAS_U](../figures/flags/TAS_U_5.png)
![TAS_U](../figures/flags/TAS_U_6.png)
![TAS_U](../figures/flags/TAS_U_7.png)
![TAS_U](../figures/flags/TAS_U_8.png)
![TAS_U](../figures/flags/TAS_U_9.png)
 
## <a id='s1-47' />THU_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![THU_L](../figures/flags/THU_L_0.png)
![THU_L](../figures/flags/THU_L_1.png)
![THU_L](../figures/flags/THU_L_2.png)
![THU_L](../figures/flags/THU_L_3.png)
![THU_L](../figures/flags/THU_L_4.png)
![THU_L](../figures/flags/THU_L_5.png)
![THU_L](../figures/flags/THU_L_6.png)
![THU_L](../figures/flags/THU_L_7.png)
![THU_L](../figures/flags/THU_L_8.png)
![THU_L](../figures/flags/THU_L_9.png)
 
## <a id='s1-48' />THU_L2
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![THU_L2](../figures/flags/THU_L2_0.png)
![THU_L2](../figures/flags/THU_L2_1.png)
![THU_L2](../figures/flags/THU_L2_2.png)
![THU_L2](../figures/flags/THU_L2_3.png)
![THU_L2](../figures/flags/THU_L2_4.png)
![THU_L2](../figures/flags/THU_L2_5.png)
![THU_L2](../figures/flags/THU_L2_6.png)
![THU_L2](../figures/flags/THU_L2_7.png)
![THU_L2](../figures/flags/THU_L2_8.png)
![THU_L2](../figures/flags/THU_L2_9.png)
 
## <a id='s1-49' />THU_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![THU_U](../figures/flags/THU_U_0.png)
![THU_U](../figures/flags/THU_U_1.png)
![THU_U](../figures/flags/THU_U_2.png)
![THU_U](../figures/flags/THU_U_3.png)
![THU_U](../figures/flags/THU_U_4.png)
![THU_U](../figures/flags/THU_U_5.png)
![THU_U](../figures/flags/THU_U_6.png)
![THU_U](../figures/flags/THU_U_7.png)
![THU_U](../figures/flags/THU_U_8.png)
![THU_U](../figures/flags/THU_U_9.png)
 
## <a id='s1-50' />THU_U2
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![THU_U2](../figures/flags/THU_U2_0.png)
![THU_U2](../figures/flags/THU_U2_1.png)
![THU_U2](../figures/flags/THU_U2_2.png)
![THU_U2](../figures/flags/THU_U2_3.png)
![THU_U2](../figures/flags/THU_U2_4.png)
![THU_U2](../figures/flags/THU_U2_5.png)
![THU_U2](../figures/flags/THU_U2_6.png)
![THU_U2](../figures/flags/THU_U2_7.png)
![THU_U2](../figures/flags/THU_U2_8.png)
![THU_U2](../figures/flags/THU_U2_9.png)
 
## <a id='s1-51' />TUN
Variables in new file:
p_u, p_l, t_u, t_l, rh_u, rh_u_cor, qh_u, rh_l, rh_l_cor, qh_l, wspd_u, wspd_l, wdir_u, wdir_l, wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dlhf_l, dshf_u, dshf_l, z_boom_u, z_boom_l, precip_u, precip_u_cor, precip_u_rate, precip_l, precip_l_cor, precip_l_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, t_i_9, t_i_10, t_i_11, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_hdop, batt_v, fan_dc_u, fan_dc_l, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, wspd_x_l, wspd_y_l, precip_u_rate, precip_l_rate

Old variables removed from new files:

 
![TUN](../figures/flags/TUN_0.png)
![TUN](../figures/flags/TUN_1.png)
![TUN](../figures/flags/TUN_2.png)
![TUN](../figures/flags/TUN_3.png)
![TUN](../figures/flags/TUN_4.png)
![TUN](../figures/flags/TUN_5.png)
![TUN](../figures/flags/TUN_6.png)
![TUN](../figures/flags/TUN_7.png)
![TUN](../figures/flags/TUN_8.png)
![TUN](../figures/flags/TUN_9.png)
![TUN](../figures/flags/TUN_10.png)
![TUN](../figures/flags/TUN_11.png)
![TUN](../figures/flags/TUN_12.png)
 
## <a id='s1-52' />UPE_L
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![UPE_L](../figures/flags/UPE_L_0.png)
![UPE_L](../figures/flags/UPE_L_1.png)
![UPE_L](../figures/flags/UPE_L_2.png)
![UPE_L](../figures/flags/UPE_L_3.png)
![UPE_L](../figures/flags/UPE_L_4.png)
![UPE_L](../figures/flags/UPE_L_5.png)
![UPE_L](../figures/flags/UPE_L_6.png)
![UPE_L](../figures/flags/UPE_L_7.png)
![UPE_L](../figures/flags/UPE_L_8.png)
![UPE_L](../figures/flags/UPE_L_9.png)
 
## <a id='s1-53' />UPE_U
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_geounit, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![UPE_U](../figures/flags/UPE_U_0.png)
![UPE_U](../figures/flags/UPE_U_1.png)
![UPE_U](../figures/flags/UPE_U_2.png)
![UPE_U](../figures/flags/UPE_U_3.png)
![UPE_U](../figures/flags/UPE_U_4.png)
![UPE_U](../figures/flags/UPE_U_5.png)
![UPE_U](../figures/flags/UPE_U_6.png)
![UPE_U](../figures/flags/UPE_U_7.png)
![UPE_U](../figures/flags/UPE_U_8.png)
![UPE_U](../figures/flags/UPE_U_9.png)
 
## <a id='s1-54' />UWN
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![UWN](../figures/flags/UWN_0.png)
![UWN](../figures/flags/UWN_1.png)
![UWN](../figures/flags/UWN_2.png)
![UWN](../figures/flags/UWN_3.png)
![UWN](../figures/flags/UWN_4.png)
![UWN](../figures/flags/UWN_5.png)
![UWN](../figures/flags/UWN_6.png)
![UWN](../figures/flags/UWN_7.png)
![UWN](../figures/flags/UWN_8.png)
![UWN](../figures/flags/UWN_9.png)
 
## <a id='s1-55' />WEG_B
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, t_surf, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
cc, dlhf_u, dshf_u, gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![WEG_B](../figures/flags/WEG_B_0.png)
![WEG_B](../figures/flags/WEG_B_1.png)
![WEG_B](../figures/flags/WEG_B_2.png)
![WEG_B](../figures/flags/WEG_B_3.png)
![WEG_B](../figures/flags/WEG_B_4.png)
![WEG_B](../figures/flags/WEG_B_5.png)
![WEG_B](../figures/flags/WEG_B_6.png)
![WEG_B](../figures/flags/WEG_B_7.png)
![WEG_B](../figures/flags/WEG_B_8.png)
![WEG_B](../figures/flags/WEG_B_9.png)
 
## <a id='s1-56' />WEG_L
C:/Users/bav/Downloads/dataverse_files/day/WEG_L_day.csv cannot be found in old data
## <a id='s1-57' />ZAK_A
C:/Users/bav/Downloads/dataverse_files/day/ZAK_A_day.csv cannot be found in old data
## <a id='s1-58' />ZAK_L
C:/Users/bav/Downloads/dataverse_files/day/ZAK_L_day.csv cannot be found in old data
## <a id='s1-59' />ZAK_Lv3
C:/Users/bav/Downloads/dataverse_files/day/ZAK_Lv3_day.csv cannot be found in old data
## <a id='s1-60' />ZAK_U
C:/Users/bav/Downloads/dataverse_files/day/ZAK_U_day.csv cannot be found in old data
## <a id='s1-61' />ZAK_Uv3
Variables in new file:
p_u, t_u, rh_u, rh_u_cor, qh_u, wspd_u, wdir_u, wspd_x_u, wspd_y_u, dsr, dsr_cor, usr, usr_cor, albedo, dlr, ulr, cc, t_surf, dlhf_u, dshf_u, z_boom_u, z_stake, z_pt, z_pt_cor, precip_u, precip_u_cor, precip_u_rate, t_i_1, t_i_2, t_i_3, t_i_4, t_i_5, t_i_6, t_i_7, t_i_8, tilt_x, tilt_y, rot, gps_lat, gps_lon, gps_alt, gps_time, gps_geoid, gps_hdop, batt_v, fan_dc_u, t_log, t_rad, msg_lat, msg_lon

New variables not in old files:
wspd_x_u, wspd_y_u, precip_u_rate

Old variables removed from new files:
gps_numsat, gps_q, batt_v_ini, batt_v_ss, freq_vw
 
![ZAK_Uv3](../figures/flags/ZAK_Uv3_0.png)
![ZAK_Uv3](../figures/flags/ZAK_Uv3_1.png)
![ZAK_Uv3](../figures/flags/ZAK_Uv3_2.png)
![ZAK_Uv3](../figures/flags/ZAK_Uv3_3.png)
![ZAK_Uv3](../figures/flags/ZAK_Uv3_4.png)
![ZAK_Uv3](../figures/flags/ZAK_Uv3_5.png)
![ZAK_Uv3](../figures/flags/ZAK_Uv3_6.png)
![ZAK_Uv3](../figures/flags/ZAK_Uv3_7.png)
![ZAK_Uv3](../figures/flags/ZAK_Uv3_8.png)
![ZAK_Uv3](../figures/flags/ZAK_Uv3_9.png)
 
