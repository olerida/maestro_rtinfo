"""Additional boolean values."""
from homeassistant.components.binary_sensor import BinarySensorEntity
from .entity import ExtraEntity, setup_sensors
from .fields import snapshot


class MaestroExtraBinarySensor(ExtraEntity, BinarySensorEntity):
    @property
    def is_on(self):
        value = snapshot(self._stove).get(self._key)
        return value if isinstance(value, bool) else None


async def async_setup_entry(hass, entry, async_add_entities):
    await setup_sensors(hass, entry, async_add_entities, MaestroExtraBinarySensor, True)
