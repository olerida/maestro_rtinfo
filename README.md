# Maestro MCZ - Información adicional

Integración complementaria de solo lectura para Home Assistant. Reutiliza la integración `maestro_mcz` y su conexión a MCZ; no necesita otra contraseña ni consulta directamente la API. Descubre los valores escalares disponibles en `State` y `Status`, incluidos campos desconocidos conservados por la integración original, y crea entidades de diagnóstico para aquellos que no tenga ya registrados Maestro MCZ. No publica contraseñas, tokens ni identificadores de red.

Probada con la estructura del diagnóstico de Maestro MCZ 0.6.7-beta y compatible a nivel de código con la estructura 1.0.2. La disponibilidad y el significado de los campos dependen del modelo, firmware y versión de la integración. Esta integración solo ve lo que expone `maestro_mcz`; la app puede tener datos adicionales por otros canales. Campos sin interpretación confirmada conservan su nombre técnico y no tienen unidad asignada. No son lecturas en directo continuas: se actualizan con el intervalo de la integración original.

## Instalación manual

1. Copia `custom_components/maestro_rtinfo` al directorio `config/custom_components/` de Home Assistant.
2. Reinicia Home Assistant.
3. En Ajustes → Dispositivos y servicios → Añadir integración, busca **Maestro MCZ - Información adicional** y selecciona tu cuenta Maestro MCZ existente.
4. Las nuevas entidades aparecerán en la sección Diagnóstico del dispositivo de la estufa.

Para instalar desde HACS como repositorio personalizado se requiere publicar este directorio en un repositorio Git compatible con HACS y añadir su URL. El archivo `hacs.json` está incluido; no hay repositorio publicado todavía.

Si recargas o actualizas Maestro MCZ, recarga también esta integración para que vuelva a enlazarse a sus coordinadores. Al iniciar Home Assistant, si Maestro MCZ aún no está lista, la integración reintentará el inicio. Es compatible con sus estructuras antigua y nueva, pero futuras versiones podrían cambiar su API interna.

No se han validado todos los modelos ni todas las unidades. Entidades y datos dependen de lo que haya devuelto la API, y la integración original puede descartar campos. No se ha probado en una instancia Home Assistant real todavía.
