# Bronze quality review

This is a self-assessment against the [Home Assistant Core quality scale](https://contributors.home-assistant.io/core/quality-scale/rules/), not an official rating. This custom integration depends on another custom integration; Core acceptance and exemptions have not been reviewed. Status: 2026-11-02.

| Bronze rule | Assessment |
| --- | --- |
| action-setup | Not applicable: no actions are registered. |
| appropriate-polling | Uses the source coordinator; no additional polling. The source determines the interval. |
| brands | The local `brand/` directory includes the 256 px MCZ icon and logo from the existing Maestro MCZ brand. Local branding is supported for custom integrations since Home Assistant 2026.3. For a formal Core assessment, the domain-specific Core brands requirement still needs review. |
| common-modules | Base entity is in `entity.py`; no coordinator is implemented here. |
| config-flow | UI selects an existing account; source availability is checked. |
| config-flow-test-coverage | Partial: account selection, absent/duplicate account, invalid input and unavailable source/retry are tested using Home Assistant API doubles. Full coverage with the actual Home Assistant test framework and reported coverage remain to be verified. |
| dependency-transparency | Pending review: Maestro MCZ is an independently distributed custom integration, not a PyPI client library; Core applicability/eligibility is unverified. |
| docs-actions | Not applicable: no actions. |
| docs-conditions | Not applicable: no integration-specific conditions. |
| docs-high-level-description | README describes MCZ and the source integration. |
| docs-installation-instructions | README covers prerequisites, manual and HACS installation, and configuration. |
| docs-removal-instructions | README covers removal. |
| docs-triggers | Not applicable: no integration-specific triggers. |
| entity-event-setup | Entities inherit CoordinatorEntity lifecycle; discovery listener is registered for the config entry and removed on unload. Review against Core rule remains necessary. |
| entity-unique-id | Entities derive a unique ID from the source stove identifier and field key. |
| has-entity-name | Base entity sets `has_entity_name`; known names use translation keys. |
| runtime-data | Source references are held in `ConfigEntry.runtime_data`. |
| test-before-configure | Checks that the selected source provides stove coordinators; it does not independently contact MCZ. Source integration manages authentication and connection. Core exemption/acceptance remains unverified. |
| test-before-setup | Checks for a source coordinator and retries with ConfigEntryNotReady if absent. It does not independently test the MCZ connection. |
| unique-config-entry | Source entry ID is used as the unique ID and already selected entries are filtered out. |

The assessment is not a claim that Bronze is achieved. In particular, a formal Core review, Core branding eligibility, full config-flow coverage in Home Assistant, and the custom dependency's eligibility are unresolved. The integration remains beta.
