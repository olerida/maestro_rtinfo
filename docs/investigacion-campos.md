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

## Análisis ARM64 con Blutter — versión 5.6.9

Se analizó la variante Android ARM64 5.6.9 (distinta de la 5.8.0 anterior). REA identificó el snapshot Dart `1ce86630892e2dca9a8543fdb8ed8e22`; Blutter identificó Dart 3.10.1 y recuperó las instrucciones anotadas de `HowItWorksInfoPage.dart` y `StateInfoResponse.dart`. En la serialización del modelo se identifica cada campo por su nombre y desplazamiento; en la pantalla se observan las cargas de esos mismos desplazamientos junto a las etiquetas. Estas relaciones son evidencia estática de la versión 5.6.9, no una prueba dinámica de la 5.8.0.

| Etiqueta en la app | Campo de StateInfoResponse | Desplazamiento |
|---|---|---|
| Ventilador de humos, Set / Real (RPM) | `vel_imp_ventola_fumi` / `vel_real_ventola_fumi` | 0x07 / 0x0b |
| Tornillo alimentador, Set / Real (RPM) | `vel_imp_coclea` / `vel_real_coclea` | 0x0f / 0x13 |
| Activo, Set / Real | `pressione_imp` / `pressione` | 0x1b / 0x17 |
| Potencia activa | `potenza_att` | 0x2f |
| Duración | `potenza_counter` | 0x33 |
| Duración prevista de limpieza | `t_dur_pul` | 0x37 |
| Tiempo restante de limpieza | `t_int_pul` | 0x3b |

Las dos duraciones de limpieza se muestran con sufijo `sec` en la app. La unidad de `potenza_counter` no queda establecida por la etiqueta. La app llama «Activo» a `pressione` y `pressione_imp`, pero eso no determina qué magnitud física o unidad representan. `potenza_att` muestra 1 con la estufa apagada en la captura; no debe utilizarse por sí solo como indicador de calefacción activa.

## Pantalla Recetas — versión 5.6.9 ARM64

El método `RecipePage.refreshData` obtiene tres propiedades de `StoveManager` y `RecipePage.build` las presenta con las etiquetas de la captura. Se ha cotejado el desplazamiento de cada propiedad con la serialización `StateResponse`:

| Etiqueta | Campo del estado | Desplazamiento |
|---|---|---|
| Activo | `pos_ric_flu` | 0x123 |
| Pellet | `pos_ric_pel` | 0xa3 |
| Modo de adaptación | `mod_ada_on` | 0x113 |

La pantalla añade el signo `+` a los números positivos. La integración existente conserva los tres campos y la integración complementaria ya ha creado entidades de solo lectura para ellos en HAOS. La correspondencia se ha trazado estáticamente en la versión 5.6.9; los valores cero/off también concuerdan con el diagnóstico y la captura de la estufa, aunque se obtuvieron a horas distintas. No se han probado escrituras.

## Contraste con la estufa encendida — 2 de noviembre de 2026

Diagnóstico actualizado a las 08:55:32 (hora de Madrid) y capturas de la app a las 08:56:27–36. La estufa estaba en fase `on`, modo `auto`, potencia activa 5. El diagnóstico confirma `potenza_att=5`, `state=on`, `mode=auto`, `potenza_counter=59293`, `t_dur_pul=20`, `t_int_pul=1141`, `pressione_imp=160`, `pressione=158`, `vel_imp_coclea=980`, `vel_real_coclea=981`, `temp_fumi=170` y `temp_scheda=23.9`.

Las capturas muestran respectivamente potencia 5, duración 59294, limpieza prevista 20 s, restante 1086 s, activo establecido 160 y real 159, sinfín establecido 980 y real 979, humos 170 °C y placa 24.0 °C. Las diferencias son coherentes con el intervalo de aproximadamente un minuto y el redondeo; no constituyen una medición simultánea. En el caso de potencia activa, la coincidencia con la app confirma su correspondencia en modo automático, sin establecer que indique kW ni que sea cero cuando la estufa esté apagada. La unidad y el significado preciso de `potenza_counter` siguen sin estar demostrados.

## wifi_status

En la versión 5.6.9 la aplicación deserializa `wifi_status` en el objeto `StateResponse` (desplazamiento 0x67), y el gestor de estado también lo actualiza. La presencia del campo no determina qué significan sus códigos ni si representan nivel de señal. En el diagnóstico del 2 de noviembre la respuesta contiene `wifi_status=3` e `is_connected=true`; es una observación, no una tabla de equivalencias. En HAOS la entidad `sensor.calentito_wifi_status` está habilitada. Se necesitan referencias adicionales o capturas de estados distintos para interpretar los códigos con seguridad.

## Opciones activas y observación en emulador

Se contrastaron las lecturas de `HowItWorksInfoPage.dart` con la serialización `StateInfoResponse.dart` de Maestro+ 5.6.9 ARM64. La pantalla muestra `crono_enabled` como Crono; `pul_brac` como Matic; `att_eco` como Start/Stop; `ingr_amb` como T.EXT; `sens_liv_pellet` como sensor de nivel de pellet; y `adaptive_on` como modo de adaptación. Estas denominaciones indican lo que muestra esta versión de la app; no explican por sí solas los detalles físicos de cada función. En particular, `adaptive_on` (datos en tiempo real) y `mod_ada_on` (recetas) son campos distintos y no debe asumirse que tengan siempre el mismo valor.

En el emulador ARM64 con la app 5.6.9, Frida observó dos deserializaciones `StateResponse` con `wifi_status=3` durante la sesión. Otra carga registró 2; el APK incorpora un ejemplo fijo con 2 y no se ha atribuido esa carga a la estufa. Se desconoce la semántica de ambos códigos: una observación de valores no establece si son estados, categorías de señal o una escala. La instrumentación no registró credenciales ni otros campos de la cuenta.

## Periodicidad de la pantalla

En la versión 5.6.9 ARM64, `HowItWorksInfoPage.getPeriodicInfo` crea un temporizador con una duración de 5.000.000 microsegundos y llama periódicamente a `getInfoState`: la pantalla intenta actualizarse cada 5 segundos mientras el temporizador está activo. Esto describe la solicitud desde la app, no garantiza que la estufa genere una medición nueva cada 5 segundos ni que Home Assistant use ese intervalo.

La última investigación se ha limitado a lecturas y análisis del código. No se han cambiado ajustes ni el estado de la estufa. El inventario de campos presentes en el diagnóstico está en `inventario-campos.md` y distingue los que siguen sin interpretación confirmada.
