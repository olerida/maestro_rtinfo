# Maestro MCZ Extra Sensors

[Español](README.es.md)

Maestro MCZ Extra Sensors is a read-only custom integration for [Home Assistant](https://www.home-assistant.io/) that exposes additional data reported by compatible [MCZ Maestro](https://www.mcz.it/en/maestro-technology) stoves. It uses the existing [Maestro MCZ integration](https://github.com/Robbe-B/maestro_mcz) to show information such as exhaust temperature, operating state and brazier cleaning values as entities.

## Supported devices

The integration has been installed on Home Assistant 2026.10.4 with Maestro MCZ 0.6.7-beta and an MCZ Ego Comfort Air stove with M2S.AIR.24.20 firmware. Not every entity or operating state has been validated. Other models and firmware may expose different fields and have not been verified.

## Prerequisites

1. Configure your stove in the Maestro+ MCZ app and verify that it is connected.
2. Install and configure the [Maestro MCZ integration](https://github.com/Robbe-B/maestro_mcz) in Home Assistant. Confirm that it can see your stove.
3. Make sure your Home Assistant installation can reach the MCZ cloud through the existing integration.

## Installation

### Manual installation

1. Copy the `custom_components/maestro_rtinfo` directory from this repository to the `custom_components` directory in your Home Assistant configuration directory. Create `custom_components` if necessary.
2. Restart Home Assistant.

### HACS

1. In HACS, open **Integrations** and choose **Custom repositories** from the menu.
2. Add `https://github.com/olerida/maestro_rtinfo` with category **Integration**.
3. Find **Maestro MCZ Extra Sensors** in HACS and select **Download**.
4. Restart Home Assistant.

This is a custom repository; it is not included in the default HACS catalog.

## Configuration

1. In Home Assistant, open **Settings** → **Devices & services**.
2. Select **Add integration** and search for **Maestro MCZ Extra Sensors**.
3. Under **Maestro MCZ integration**, select the account already configured in the original integration and submit.

No additional MCZ credentials are required. Repeat the setup for another Maestro MCZ account if needed.

## Supported functionality

The integration discovers scalar values available in the original integration's `State` and `Status` data. Depending on the stove and data returned, it can provide:

- **Sensors:** operating phase and active power, exhaust and board temperatures, requested and actual exhaust fan and auger speeds, cleaning information, and recipe values.
- **Binary sensors:** available on/off status fields, such as the adaptive mode and other operating options.

The integration does not provide controls and does not send commands to the stove. Fields already registered by Maestro MCZ are not intentionally duplicated. Some fields use technical names because their meaning has not been verified. See the [field inventory](docs/inventario-campos.md) for the investigation based on one stove.

### Enable unconfirmed entities

New entities for fields whose meaning is unconfirmed are disabled by default. To enable one, open **Settings** → **Devices & services** → **Entities**, show disabled entities, select the entity and enable it. This default applies when an entity is first registered; existing enabled or disabled choices are preserved during updates. Field availability can vary with the data reported by the stove.

## Data updates

The integration reads data from the existing Maestro MCZ coordinator and updates when that coordinator updates. It does not make its own cloud requests. The polling interval is controlled by the original integration and may be slower than the Maestro+ app's real-time display.

## Known limitations

- This is an independent community project, not an official MCZ integration.
- Only data retained by the original Maestro MCZ integration is available; some app data may be missing.
- Model coverage and the meaning and units of some fields remain unverified. A field may retain its last value while the stove is off; for example, active power alone does not prove that the stove is heating.
- The component uses internal interfaces of Maestro MCZ. An upstream update may require changes here. The code supports the coordinator structures inspected in 0.6.7-beta and 1.0.2; end-to-end operation with 1.0.2 has not been tested.
- Reload this integration after reloading or updating the original Maestro MCZ integration.
- Identified entity names and the setup flow are available in English and Spanish. Unidentified fields retain their technical names.

## Troubleshooting

- **No Maestro MCZ account is available during setup:** configure the original integration first and check that it is loaded. Each account can be added only once.
- **An entity is missing:** check the device's diagnostics and the disabled-entity list. Entities are created only when the original integration supplies a scalar value; values unavailable for your model may never appear.
- **Values are unavailable or stale:** check the stove's connection and the original integration. This integration uses its connection and update schedule.
- **The original integration was reloaded:** reload Maestro MCZ Extra Sensors so it reconnects to the current coordinator.

## Remove the integration

Open **Settings** → **Devices & services**, select **Maestro MCZ Extra Sensors**, open its menu and select **Delete**. To remove the files as well, delete `custom_components/maestro_rtinfo` and restart Home Assistant. The original Maestro MCZ integration and its account are separate.

## License

The project code is available under the [MIT License](LICENSE). The Maestro+ icon and MCZ trademarks belong to their respective owner and are not covered by the MIT license.
