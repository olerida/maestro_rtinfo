# Changelog

## 0.2.5

- Check the source coordinator’s most recent update before setup, without making extra cloud requests; retry when all updates failed.
- Add isolated Home Assistant 2026.10.4 tests for config flows, recovery, entity discovery and updates; enforce full config-flow line coverage in CI.
- Document dependency and connection-rule applicability in the Bronze assessment.

## 0.2.4

- Use the MCZ icon and logo from Home Assistant Brands as local custom integration branding.
- Clarify the branding requirement in the Bronze quality review.

## 0.2.3

- Store source coordinators in config entry runtime data and validate the selected source during setup.
- Add account selection and setup tests, and document a preliminary Bronze quality assessment.

## 0.2.2

- Add meaningful icons to identified entities and a neutral icon for undocumented fields.

## 0.2.1

- Add MIT license and correct manifest metadata for publication.

## 0.2.0

- Disable newly discovered, unconfirmed entities by default; users can enable them in Home Assistant.
- Translate known entity names and configuration screens into English and Spanish.
- Preserve existing entity registry choices and technical field names for undocumented fields.
