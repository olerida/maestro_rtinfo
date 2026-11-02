"""Test startup against actual Home Assistant objects."""
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

import pytest
from homeassistant.exceptions import ConfigEntryNotReady
from pytest_homeassistant_custom_component.common import MockConfigEntry

from importlib import import_module


async def test_unavailable_then_ready(hass):
    integration = import_module("custom_components.maestro_rtinfo")
    source = MockConfigEntry(domain="maestro_mcz", entry_id="source1", data={})
    source.add_to_hass(hass)
    entry = MockConfigEntry(domain="maestro_rtinfo", data={"source_entry_id": source.entry_id})
    entry.add_to_hass(hass)
    coordinator = SimpleNamespace(maestroapi=object(), last_update_success=False)
    hass.data["maestro_mcz"] = {source.entry_id: [coordinator]}
    with pytest.raises(ConfigEntryNotReady):
        await integration.async_setup_entry(hass, entry)
    coordinator.last_update_success = True
    with patch.object(hass.config_entries, "async_forward_entry_setups", new=AsyncMock()) as forward:
        assert await integration.async_setup_entry(hass, entry)
        forward.assert_awaited_once()
    assert entry.runtime_data == [(coordinator, coordinator.maestroapi)]
    with patch.object(hass.config_entries, "async_unload_platforms", new=AsyncMock(return_value=True)):
        assert await integration.async_unload_entry(hass, entry)


async def test_current_source_account(hass):
    integration = import_module("custom_components.maestro_rtinfo")
    stove = object()
    coordinator = SimpleNamespace(stoves={"serial": stove}, last_update_success=True)
    source = MockConfigEntry(domain="maestro_mcz", entry_id="source2", data={})
    source.runtime_data = coordinator
    source.add_to_hass(hass)
    entry = MockConfigEntry(domain="maestro_rtinfo", data={"source_entry_id": source.entry_id})
    entry.add_to_hass(hass)
    with patch.object(hass.config_entries, "async_forward_entry_setups", new=AsyncMock()):
        assert await integration.async_setup_entry(hass, entry)
    assert entry.runtime_data == [(coordinator, stove)]
