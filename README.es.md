# Maestro MCZ - Sensores adicionales

<img src="custom_components/maestro_rtinfo/brand/icon.png" alt="Maestro MCZ Extra Sensors" width="128">

[English](README.md)

Maestro MCZ Extra Sensors es una integración personalizada de solo lectura para [Home Assistant](https://www.home-assistant.io/) que muestra datos adicionales de estufas [MCZ Maestro](https://www.mcz.it/es/tecnologia-maestro). Utiliza la integración existente [Maestro MCZ](https://github.com/Robbe-B/maestro_mcz) para crear entidades con datos como la temperatura de humos, el estado de funcionamiento o la limpieza del brasero.


La integración sigue en fase beta. Consulta la [revisión de calidad de bronce](docs/bronze-review.md) para conocer lo realizado y lo pendiente; no es una clasificación oficial.

La integración incluye el icono y el logotipo de MCZ como marca local para Home Assistant 2026.3 o posterior.

## Dispositivos compatibles

La integración se ha instalado en Home Assistant 2026.10.4 con Maestro MCZ 0.6.7-beta y una estufa MCZ Ego Comfort Air con firmware M2S.AIR.24.20. No se han validado todas las entidades ni todos los estados. Otros modelos y versiones pueden ofrecer campos diferentes y aún no se han comprobado.

## Requisitos previos

1. Configura la estufa en la app Maestro+ MCZ y comprueba que esté conectada.
2. Instala y configura la [integración Maestro MCZ](https://github.com/Robbe-B/maestro_mcz) en Home Assistant. Comprueba que detecte la estufa.
3. Asegúrate de que Home Assistant pueda acceder a la nube de MCZ a través de la integración existente.

## Instalación

### Instalación manual

1. Copia la carpeta `custom_components/maestro_rtinfo` de este repositorio dentro de la carpeta `custom_components` de la configuración de Home Assistant. Si no existe, créala.
2. Reinicia Home Assistant.

### HACS

[![Open this integration in Home Assistant Marketplace](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=olerida&repository=maestro_rtinfo&category=integration)

1. En HACS, abre **Integraciones** y selecciona **Repositorios personalizados** en el menú.
2. Añade `https://github.com/olerida/maestro_rtinfo` con la categoría **Integración**.
3. Busca **Maestro MCZ Extra Sensors** en HACS y pulsa **Descargar**.
4. Reinicia Home Assistant.

Es un repositorio personalizado; no está incluido en el catálogo predeterminado de HACS. La versión actual es beta; selecciona **Mostrar versiones beta** en HACS si no aparece.

## Actualización

Instala la actualización disponible en HACS y reinicia Home Assistant. Si la versión beta no aparece, activa **Mostrar versiones beta** para este repositorio en HACS. Se conservan los ajustes de las entidades existentes.

## Configuración

1. En Home Assistant, abre **Ajustes** → **Dispositivos y servicios**.
2. Selecciona **Añadir integración** y busca **Maestro MCZ Extra Sensors**.
3. En **Integración Maestro MCZ**, selecciona la cuenta configurada en la integración original y confirma.

No necesitas introducir de nuevo tus credenciales de MCZ. Puedes repetir la configuración para otra cuenta Maestro MCZ.

## Funciones compatibles

La integración descubre los valores simples revisados disponibles en `State` y `Status` de la integración original. Según la estufa y los datos recibidos, puede ofrecer:

- **Sensores:** fase de funcionamiento y potencia activa, temperaturas de humos y placa, velocidades solicitadas y reales del extractor y del sinfín, datos de limpieza y valores de recetas.
- **Sensores binarios:** campos disponibles de tipo activado/desactivado, como el modo de adaptación y otras opciones de funcionamiento.

Las entidades identificadas tienen iconos acordes con su función; los campos no documentados usan un icono neutral. Puedes personalizar el icono de cada entidad en Home Assistant.

La integración no ofrece controles ni envía órdenes a la estufa. Procura no duplicar los campos que ya tiene registrados Maestro MCZ. Algunos campos revisados conservan su nombre técnico porque no se ha confirmado su significado. Consulta el [inventario de campos](docs/inventario-campos.md), basado en la investigación de una estufa.

### Habilitar entidades no confirmadas

Las entidades nuevas correspondientes a campos cuyo significado no se ha confirmado se crean deshabilitadas. Para habilitar una, abre **Ajustes** → **Dispositivos y servicios** → **Entidades**, muestra las entidades deshabilitadas, selecciónala y habilítala. Este valor predeterminado se aplica al registrar cada entidad; al actualizar se respetan las elecciones existentes. Las entidades disponibles dependen de los datos que envíe la estufa.

## Actualización de datos

La integración lee los datos del coordinador existente de Maestro MCZ y se actualiza cuando este lo hace. No realiza consultas adicionales a la nube. El intervalo depende de la integración original y puede ser más lento que la pantalla de datos en tiempo real de Maestro+.


Antes de configurarse, la integración comprueba que al menos un coordinador de origen informe de una última actualización correcta, sin forzar otra petición a la nube. Si todas han fallado, la configuración muestra un error y las entradas existentes reintentan el inicio.

## Limitaciones conocidas

- Es un proyecto comunitario independiente, no una integración oficial de MCZ.
- Solo puede mostrar datos que conserve la integración Maestro MCZ original; puede faltar información que sí aparece en la app.
- No se han comprobado todos los modelos ni el significado y las unidades de todos los campos. Algunos pueden conservar un valor con la estufa apagada; por ejemplo, la potencia activa por sí sola no demuestra que esté calentando.
- El componente utiliza interfaces internas de Maestro MCZ, que pueden cambiar en futuras versiones. El código contempla las estructuras de coordinador examinadas en 0.6.7-beta y 1.0.2; no se ha comprobado el funcionamiento completo con 1.0.2.
- Recarga esta integración después de recargar o actualizar la integración Maestro MCZ original.
- Los nombres identificados y el formulario están disponibles en español e inglés. Los campos no identificados conservan su nombre técnico.

## Solución de problemas

- **No aparece ninguna cuenta Maestro MCZ al configurar:** configura primero la integración original y comprueba que esté cargada. Cada cuenta solo se puede añadir una vez.
- **Falta una entidad:** revisa el diagnóstico del dispositivo y la lista de entidades deshabilitadas. Solo se crean entidades cuando la integración original proporciona un valor simple; los datos que tu modelo no ofrezca pueden no aparecer.
- **Los valores no están disponibles o no se actualizan:** comprueba la conexión de la estufa y la integración original. Esta integración utiliza su conexión y su intervalo de actualización.
- **Se ha recargado la integración original:** recarga Maestro MCZ Extra Sensors para que vuelva a conectarse al coordinador actual.

## Eliminar la integración

Abre **Ajustes** → **Dispositivos y servicios**, selecciona **Maestro MCZ Extra Sensors**, abre su menú y pulsa **Eliminar**. Para borrar también los archivos, elimina `custom_components/maestro_rtinfo` y reinicia Home Assistant. La integración Maestro MCZ original y su cuenta son independientes.

## Licencia

El código del proyecto se distribuye bajo la [licencia MIT](LICENSE). El icono Maestro+ y las marcas MCZ pertenecen a su titular y no están incluidos en la licencia MIT.


Seguridad: solo se exponen los campos de telemetría revisados explícitamente; se ignoran los campos desconocidos. Las entidades desconocidas ya registradas pueden quedar no disponibles.
