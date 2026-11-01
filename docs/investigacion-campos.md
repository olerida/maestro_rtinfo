# Investigación de campos — Maestro+ 5.8.0

## Alcance y método

Se inspeccionó el APK `it.mcz.maestro` 5.8.0 suministrado por el usuario. SHA-256 del APK principal: `0aa7b6b623fe193e1dbb0844f85847fb9b70a5c4be41c0310a55526763fcba2b`. REA identificó la aplicación como Flutter; su código Dart está compilado en la biblioteca ARM `libapp.so` del APK adicional. Se inventariaron los recursos con REA y se revisaron el fichero original `assets/flutter_assets/assets/translations/es.json` y las cadenas de esa biblioteca. El análisis es estático: no se ha observado cómo se ejecuta la pantalla ni se ha probado la respuesta de la estufa encendida.

## Etiquetas originales

| Clave del recurso español | Texto de la app | Campo del diagnóstico coincidente | Alcance |
|---|---|---|---|
| `temp_fumi` | Temp. Humos | `temp_fumi` | Coincidencia exacta del nombre; aún no se ha trazado el enlace desde la pantalla. |
| `temp_scheda` | Temp. Tarjeta | `temp_scheda` | Coincidencia exacta del nombre; aún no se ha trazado el enlace desde la pantalla. |
| `silent` | Silencioso | `silent` | Coincidencia exacta del nombre; la relación con la pantalla concreta no está trazada. |
| `potenza_attiva` | Potencia activa | — | El campo `potenza_att` es un candidato por su nombre, pero no existe una relación demostrada entre ambos. |
| `ventola_fumi` | Ventilador de humos | — | Candidatos: `vel_imp_ventola_fumi`, `vel_real_ventola_fumi`; no se ha trazado la relación. |
| `coclea` | Tornillo alimentador | — | Candidatos: `vel_imp_coclea`, `vel_real_coclea`; no se ha trazado la relación. |
| `real` | Real | — | No se ha demostrado a qué campos se aplica. |
| `set` | Set | — | No se ha demostrado a qué campos se aplica. |
| `prossimo_clean_braciere` | Próxima limpieza del brasero | — | No se ha demostrado la relación con los contadores. |

## Otros campos

`set_pot_man` y `potenza_att` aparecen juntos en un ejemplo JSON integrado en la aplicación, con valores 2 y 3 respectivamente; esto confirma que son campos distintos, pero no su significado dinámico. En el diagnóstico del usuario, con la estufa apagada, valían 4 y 1. No se ha establecido cómo evoluciona `potenza_att` durante el funcionamiento ni si expresa energía en kW.

La integración comunitaria `maestro_mcz` interpreta `temp_fumi` como temperatura de humos, `temp_scheda` como temperatura de placa y `vel_real_ventola_fumi` y `vel_real_coclea` como velocidades en rpm. Esto es evidencia de una implementación comunitaria, no prueba de comportamiento de la app ni garantía para todos los modelos.

`pressione`, `pressione_imp`, `potenza_counter`, `t_dur_pul` y `t_int_pul` aparecen en los datos o cadenas, pero no se ha verificado su unidad o significado operativo. Conservar nombres técnicos cuando falte esa evidencia.

Ghidra 12.1.4 está configurado en REA y se ha analizado el binario ARM de 32 bits. La búsqueda encontró `potenza_att` en la dirección 0x366074 y `potenza_attiva` en 0x39ac74; al consultar referencias directas a `potenza_att`, Ghidra no reportó ninguna. Esto no demuestra que el campo no se use: Flutter AOT dificulta el mapeo de cadenas a widgets y pueden existir referencias indirectas. El paso más fiable para identificar los valores de la pantalla es compararla con una captura de la respuesta de datos de la misma estufa en el mismo momento; después repetir en otro estado para comprobar cambios y unidades. Evitar registrar contraseñas, tokens o identificadores personales en las capturas.

## Comparación con las capturas del usuario

Las capturas de la app se tomaron el 1 de noviembre de 2026 a las 23:07–23:08. El diagnóstico disponible es de esa mañana, por lo que las coincidencias son indicios y no una prueba simultánea.

| Pantalla | Valor en la pantalla | Campo candidato | Valor en el diagnóstico | Evaluación |
|---|---:|---|---:|---|
| Potencia activa | 1 | `potenza_att` | 1 | Coherente con el nombre y valor; no establece cómo cambia mientras trabaja. |
| Duración, bajo potencia activa | 233537 | `potenza_counter` | 233537 | Coincidencia muy distintiva; unidad y semántica exacta aún desconocidas. |
| Duración prevista de limpieza del brasero | 20 sec | `t_dur_pul` | 20 | Coincide con el nombre y valor; la app muestra segundos. |
| Fase | off | `state` / `fase_op` | off / off | Coinciden ambas fuentes. |
| Modo activo | overnight | `mode` / `mod_lav_att` | overnight / overnight | Coinciden ambas fuentes. |
| Tornillo alimentador, Set / Real | 0 / 0 RPM | `vel_imp_coclea` / `vel_real_coclea` | 0 / 0 | Coherente con los nombres; al ser ceros no permite distinguir las columnas. |
| Ventilador de humos, Set / Real | 0 / 0 RPM | `vel_imp_ventola_fumi` / `vel_real_ventola_fumi` | 0 / 0 | Coherente con los nombres; al ser ceros no permite distinguir las columnas. |
| Activo, Set / Real | 0 / 100 | `pressione_imp` / `pressione` | 0 / 101 | Posible relación, pero la diferencia temporal impide confirmarla y se desconoce la unidad. |
| Tiempo restante | 0 sec | `t_int_pul` | 0 | Posible relación; el cero también coincide con muchos otros campos. |

La estufa estaba apagada en las capturas aunque la app muestra potencia activa 1. No debe tratarse ese valor por sí solo como una indicación de que la estufa esté calentando. Para comprobar semántica y evolución, obtener otro diagnóstico simultáneo con la app, preferiblemente con la estufa en un estado diferente.
