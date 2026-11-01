"""Additional numeric and text values."""
from homeassistant.components.sensor import SensorDeviceClass, SensorEntity, SensorStateClass
from .entities import ExtraEntity, setup_sensors
from .fields import LABELS, snapshot


class MaestroExtraSensor(ExtraEntity, SensorEntity):
    def __init__(self, coordinator, stove, key):
        super().__init__(coordinator, stove, key)
        _, unit, device_class = LABELS.get(key, (None, None, None))
        self._attr_native_unit_of_measurement = unit
        if device_class == "temperature":
            self._attr_device_class = SensorDeviceClass.TEMPERATURE
        if unit:
            self._attr_state_class = SensorStateClass.MEASUREMENT

    @property
    def native_value(self):
        value = snapshot(self._stove).get(self._key)
        return None if isinstance(value, bool) else value


async def async_setup_entry(hass, entry, async_add_entities):
    await setup_sensors(hass, entry, async_add_entities, MaestroExtraSensor, False)
