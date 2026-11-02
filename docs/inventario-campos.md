# Inventario de campos de la estufa

Campos no privados con valor en el diagnóstico del 2 de noviembre. «Sin confirmar» significa que aún no se ha demostrado su correspondencia con una etiqueta o unidad. Las relaciones confirmadas por código corresponden a la app 5.6.9 ARM64; el diagnóstico usa `mode` para el modo activo.

| Campo | Origen | Interpretación |
|---|---|---|
| `absolute_battery_charge_level` | State / Status | Sin confirmar |
| `act` | Status | Sin confirmar |
| `act_acc` | Status | Sin confirmar |
| `adaptive_on` | State | Modo de adaptación en tiempo real |
| `am_pm` | Status | Sin confirmar |
| `anno` | Status | Año del reloj de la estufa (integración comunitaria) |
| `att_eco` | State / Status | Start/Stop |
| `auto_pellet` | Status | Sin confirmar |
| `battery_capacity` | State / Status | Sin confirmar |
| `clean_air_in_prog` | Status | Sin confirmar |
| `clean_in_prog` | Status | Sin confirmar |
| `com_es_car_coclea` | Status | Sin confirmar |
| `cont_fine_pul` | Status | Sin confirmar |
| `crono_enabled` | State / Status | Crono |
| `en_sav_m` | Status | Sin confirmar |
| `fase_op` | Status | Sin confirmar |
| `giorno` | Status | Día del reloj de la estufa (integración comunitaria) |
| `giorno_sett` | Status | Sin confirmar |
| `has_battery` | State / Status | Sin confirmar |
| `index_vel_v1` | State / Status | Nivel ventilador 1 |
| `index_vel_v2` | State / Status | Nivel ventilador 2 |
| `index_vel_v3` | State / Status | Nivel ventilador 3 |
| `ing_term_amb1` | Status | Sin confirmar |
| `ingr_amb` | State / Status | T.EXT |
| `is_ble_connected` | Status | Sin confirmar |
| `is_connected` | State / Status | Sin confirmar |
| `is_crono_empty` | Status | Sin confirmar |
| `is_in_error` | State / Status | Alarma o error (integración comunitaria) |
| `is_live_only` | State / Status | Sin confirmar |
| `ist_eco_neg_amb` | Status | Histéresis negativa Start/Stop (integración comunitaria) |
| `ist_eco_pos_amb` | Status | Histéresis positiva Start/Stop (integración comunitaria) |
| `ist_neg_amb` | Status | Histéresis negativa ambiente (integración comunitaria) |
| `ist_pos_amb` | Status | Histéresis positiva ambiente (integración comunitaria) |
| `last_alarm` | State | Último código de alarma (integración comunitaria) |
| `last_stdt` | State / Status | Sin confirmar |
| `mc_vs_app` | Status | Sin confirmar |
| `mese` | Status | Mes del reloj de la estufa (integración comunitaria) |
| `minuti` | Status | Minutos del reloj de la estufa (integración comunitaria) |
| `mod_ada_on` | Status | Recetas: modo de adaptación |
| `mod_lav_att` | Status | Modo activo en modelo de la app |
| `mode` | State | Modo activo (nombre usado por integración) |
| `nome_banca_dati_sel` | State / Status | Sin confirmar |
| `ore` | Status | Hora del reloj de la estufa (integración comunitaria) |
| `ore_prox_manut` | Status | Horas hasta mantenimiento (integración comunitaria) |
| `pos_ric_asp` | Status | Sin confirmar |
| `pos_ric_flu` | Status | Recetas: Activo |
| `pos_ric_pel` | Status | Recetas: Pellet |
| `potenza_att` | State / Status | Potencia activa |
| `potenza_counter` | State | Duración mostrada en pantalla; unidad sin confirmar |
| `power_enabled` | Status | Sin confirmar |
| `pren_acc` | Status | Sin confirmar |
| `pres_pul` | State / Status | Sin confirmar |
| `pres_rete_ele` | State / Status | Sin confirmar |
| `pressione` | State / Status | Activo: Real |
| `pressione_imp` | State / Status | Activo: Set |
| `pressione_pascal` | Status | Sin confirmar |
| `pul_brac` | State / Status | Matic |
| `rit_ing_standby` | Status | Retardo de apagado Start/Stop (integración comunitaria) |
| `rit_usc_standby` | Status | Retardo de encendido Start/Stop (integración comunitaria) |
| `sav_m` | Status | Sin confirmar |
| `scheduled_turn_off_timestamp` | Status | Sin confirmar |
| `secondi` | Status | Segundos del reloj de la estufa (integración comunitaria) |
| `sens_liv_pel` | Status | Sin confirmar |
| `sens_liv_pellet` | State / Status | Sensor del nivel de pellet |
| `set_amb1` | State / Status | Sonda ambiente: temperatura objetivo |
| `set_amb2` | Status | Temperatura objetivo ambiente 2 (integración comunitaria) |
| `set_amb3` | Status | Temperatura objetivo ambiente 3 (integración comunitaria) |
| `set_pot_man` | Status | Potencia manual seleccionada (integración comunitaria) |
| `set_vent_v1` | Status | Ajuste ventilador 1 (integración comunitaria) |
| `set_vent_v2` | Status | Ajuste ventilador 2 (integración comunitaria) |
| `set_vent_v3` | Status | Ajuste ventilador 3 (integración comunitaria) |
| `silent` | Status | Sin confirmar |
| `silent_enabled` | Status | Sin confirmar |
| `site_time_zone` | State / Status | Sin confirmar |
| `sleep_enabled` | Status | Sin confirmar |
| `sm_nome_app` | Status | Sin confirmar |
| `sm_vs_app` | Status | Sin confirmar |
| `state` | State | Fase |
| `state_duration` | State | Duración de la fase |
| `stato_stufa` | Status | Estado de encendido (integración comunitaria) |
| `status` | Status | Sin confirmar |
| `status_timestamp` | State / Status | Sin confirmar |
| `t_car_pel_man` | Status | Sin confirmar |
| `t_dur_pul` | State | Limpieza: duración prevista (s) |
| `t_int_pul` | State | Limpieza: tiempo restante (s) |
| `t_power` | Status | Sin confirmar |
| `temp_NTC3` | State / Status | Sin confirmar |
| `temp_amb_can1` | Status | Sin confirmar |
| `temp_amb_can2` | Status | Sin confirmar |
| `temp_amb_can3` | Status | Sin confirmar |
| `temp_amb_install` | State / Status | Temperatura ambiente (integración comunitaria) |
| `temp_fumi` | State | Temperatura de humos (°C) |
| `temp_scheda` | State | Temperatura de tarjeta (°C) |
| `toni_buzz` | Status | Tonos (integración comunitaria) |
| `turbo_activation_timestamp` | Status | Sin confirmar |
| `umid_rel` | Status | Sin confirmar |
| `v_ven1_v0` | Status | Sin confirmar |
| `v_ven2_v0` | Status | Sin confirmar |
| `v_ven3_v0` | Status | Sin confirmar |
| `vel_imp_coclea` | State | Tornillo alimentador: Set (rpm) |
| `vel_imp_ventola_fumi` | State | Ventilador de humos: Set (rpm) |
| `vel_real_coclea` | State | Tornillo alimentador: Real (rpm) |
| `vel_real_ventola_fumi` | State | Ventilador de humos: Real (rpm) |
| `wifi_status` | Status | Código Wi-Fi; significado no confirmado |
