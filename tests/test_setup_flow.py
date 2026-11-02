"""Exercise setup and account selection with Home Assistant API doubles."""
import asyncio
import importlib.util
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import AsyncMock, Mock, patch

ROOT = Path(__file__).parents[1] / "custom_components" / "maestro_rtinfo"


def load_modules():
    """Load integration modules without installing Home Assistant."""
    ha = types.ModuleType("homeassistant")
    entries = types.ModuleType("homeassistant.config_entries")
    core = types.ModuleType("homeassistant.core")
    const = types.ModuleType("homeassistant.const")
    exceptions = types.ModuleType("homeassistant.exceptions")
    vol = types.ModuleType("voluptuous")

    class Flow:
        def __init_subclass__(cls, **kwargs):
            super().__init_subclass__()
        def _async_current_entries(self):
            return self.current_entries
        async def async_set_unique_id(self, value):
            self.unique_id = value
        def _abort_if_unique_id_configured(self):
            pass
        def async_create_entry(self, **kwargs):
            return {"type": "create_entry", **kwargs}
        def async_abort(self, **kwargs):
            return {"type": "abort", **kwargs}
        def async_show_form(self, **kwargs):
            return {"type": "form", **kwargs}

    entries.ConfigEntry = type("ConfigEntry", (), {})
    entries.ConfigFlow = Flow
    core.HomeAssistant = type("HomeAssistant", (), {})
    core.callback = lambda fn: fn
    const.Platform = types.SimpleNamespace(SENSOR="sensor", BINARY_SENSOR="binary_sensor")
    exceptions.ConfigEntryNotReady = type("ConfigEntryNotReady", (Exception,), {})
    vol.Required = lambda key: key
    vol.In = lambda values: values
    vol.Schema = lambda value: value
    package = types.ModuleType("test_maestro_rtinfo")
    package.__path__ = [str(ROOT)]
    modules = {"homeassistant": ha, "homeassistant.config_entries": entries,
               "homeassistant.core": core, "homeassistant.const": const,
               "homeassistant.exceptions": exceptions, "voluptuous": vol,
               "test_maestro_rtinfo": package}
    with patch.dict(sys.modules, modules):
        spec = importlib.util.spec_from_file_location("test_maestro_rtinfo", ROOT / "__init__.py", submodule_search_locations=[str(ROOT)])
        integration = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = integration
        spec.loader.exec_module(integration)
        spec = importlib.util.spec_from_file_location("test_maestro_rtinfo.config_flow", ROOT / "config_flow.py")
        flow = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(flow)
    return integration, flow, exceptions.ConfigEntryNotReady


integration, flow_module, NotReady = load_modules()


class SetupTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.source = types.SimpleNamespace(domain="maestro_mcz", runtime_data=None)
        self.hass = types.SimpleNamespace(data={}, config_entries=types.SimpleNamespace(
            async_get_entry=Mock(return_value=self.source),
            async_forward_entry_setups=AsyncMock(), async_unload_platforms=AsyncMock(return_value=True)))
        self.entry = types.SimpleNamespace(data={"source_entry_id": "source"}, entry_id="extra")

    async def test_missing_source_retries(self):
        self.hass.config_entries.async_get_entry.return_value = None
        with self.assertRaises(NotReady):
            await integration.async_setup_entry(self.hass, self.entry)
        self.hass.config_entries.async_forward_entry_setups.assert_not_awaited()

    async def test_current_account_coordinator_and_unload(self):
        stove = object()
        coordinator = types.SimpleNamespace(stoves={"serial": stove})
        self.source.runtime_data = coordinator
        self.assertTrue(await integration.async_setup_entry(self.hass, self.entry))
        self.assertEqual(self.entry.runtime_data, [(coordinator, stove)])
        self.hass.config_entries.async_forward_entry_setups.assert_awaited_once()
        self.assertTrue(await integration.async_unload_entry(self.hass, self.entry))

    async def test_legacy_coordinator(self):
        coordinator = types.SimpleNamespace(maestroapi=object())
        self.hass.data = {"maestro_mcz": {"source": [coordinator]}}
        await integration.async_setup_entry(self.hass, self.entry)
        self.assertEqual(self.entry.runtime_data, [(coordinator, coordinator.maestroapi)])

    async def test_wrong_domain_is_not_accepted(self):
        self.source.domain = "other"
        with self.assertRaises(NotReady):
            await integration.async_setup_entry(self.hass, self.entry)


class FlowTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.flow = flow_module.MaestroRtinfoConfigFlow()
        self.flow.current_entries = []
        self.source = types.SimpleNamespace(entry_id="source", title="My stove")
        self.flow.hass = types.SimpleNamespace(config_entries=types.SimpleNamespace(
            async_entries=Mock(return_value=[self.source])))

    async def test_no_account_aborts(self):
        self.flow.hass.config_entries.async_entries.return_value = []
        self.assertEqual((await self.flow.async_step_user())["reason"], "no_source")

    async def test_existing_account_is_not_offered_twice(self):
        self.flow.current_entries = [types.SimpleNamespace(data={"source_entry_id": "source"})]
        self.assertEqual((await self.flow.async_step_user())["reason"], "no_source")

    async def test_account_can_be_selected(self):
        self.assertEqual((await self.flow.async_step_user())["type"], "form")
        with patch.object(flow_module, "get_sources", return_value=[object()]):
            result = await self.flow.async_step_user({"source_entry_id": "source"})
        self.assertEqual(result["data"], {"source_entry_id": "source"})
        self.assertEqual(self.flow.unique_id, "source")

    async def test_unavailable_source_can_be_retried(self):
        with patch.object(flow_module, "get_sources", side_effect=[[], [object()]]):
            result = await self.flow.async_step_user({"source_entry_id": "source"})
            self.assertEqual(result["errors"]["base"], "source_unavailable")
            result = await self.flow.async_step_user({"source_entry_id": "source"})
            self.assertEqual(result["type"], "create_entry")

    async def test_invalid_account_is_not_created(self):
        result = await self.flow.async_step_user({"source_entry_id": "invalid"})
        self.assertEqual(result["type"], "form")


if __name__ == "__main__":
    unittest.main()
