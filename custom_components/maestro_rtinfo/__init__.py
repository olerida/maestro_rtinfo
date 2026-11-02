"""Additional read-only sensors backed by Maestro MCZ's coordinator."""
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady

from .const import SOURCE_DOMAIN

PLATFORMS = [Platform.SENSOR, Platform.BINARY_SENSOR]


def get_sources(hass: HomeAssistant, entry_id: str):
    """Support both legacy per-stove and current per-account coordinators."""
    source = hass.config_entries.async_get_entry(entry_id)
    if source is None or source.domain != SOURCE_DOMAIN:
        return []
    legacy = hass.data.get(SOURCE_DOMAIN, {}).get(entry_id)
    if isinstance(legacy, list):
        return [(coordinator, coordinator.maestroapi) for coordinator in legacy]
    coordinator = getattr(source, "runtime_data", None)
    if coordinator is not None and isinstance(getattr(coordinator, "stoves", None), dict):
        return [(coordinator, stove) for stove in coordinator.stoves.values()]
    return []


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    sources = get_sources(hass, entry.data["source_entry_id"])
    if not sources:
        raise ConfigEntryNotReady("La integración Maestro MCZ debe estar configurada y cargada")
    entry.runtime_data = sources
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    if await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        return True
    return False
