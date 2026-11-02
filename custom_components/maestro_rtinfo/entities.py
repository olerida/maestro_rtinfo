"""Discover new values from the existing integration's updates."""
from homeassistant.core import callback
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN, SOURCE_DOMAIN
from .fields import CONFIRMED_FIELDS, LABELS, snapshot


async def setup_sensors(hass, entry, async_add_entities, entity_class, boolean):
    sources = hass.data[DOMAIN][entry.entry_id]
    for coordinator, stove in sources:
        known = set()
        serial = stove.UniqueCode

        @callback
        def discover(coordinator=coordinator, stove=stove, known=known, serial=serial):
            registry = er.async_get(hass)
            prefix = f"{serial}-"
            existing = {item.unique_id[len(prefix):] for item in registry.entities.values()
                        if item.platform == SOURCE_DOMAIN and item.unique_id.startswith(prefix)}
            new = []
            for key, value in snapshot(stove).items():
                if key in known or key in existing or isinstance(value, bool) != boolean:
                    continue
                known.add(key)
                new.append(entity_class(coordinator, stove, key))
            if new:
                async_add_entities(new)

        discover()
        entry.async_on_unload(coordinator.async_add_listener(discover))


class ExtraEntity(CoordinatorEntity):
    _attr_has_entity_name = True
    _attr_entity_category = EntityCategory.DIAGNOSTIC

    def __init__(self, coordinator, stove, key):
        super().__init__(coordinator)
        self._stove = stove
        self._key = key
        self._attr_unique_id = f"{stove.UniqueCode}-{key}"
        self._attr_entity_registry_enabled_default = key in CONFIRMED_FIELDS
        if key in LABELS:
            self._attr_translation_key = key
        else:
            self._attr_name = key
        if hasattr(coordinator, "get_device_info"):
            self._attr_device_info = coordinator.get_device_info()
        else:
            self._attr_device_info = stove.get_device_info()

    @property
    def available(self):
        connected = getattr(self._stove, "is_connected", None)
        if connected is None:
            connected = getattr(getattr(self._stove, "Status", None), "is_connected", True)
        return super().available and connected is not False and self._key in snapshot(self._stove)
