# Bronze quality review

This is a self-assessment against the [Home Assistant Core quality scale](https://contributors.home-assistant.io/core/quality-scale/rules/), not an official rating. This custom integration depends on another custom integration; Core acceptance and exemptions have not been reviewed. Status: 2026-11-02.

| Bronze rule | Assessment |
| --- | --- |
| action-setup | Not applicable: no actions are registered. |
| appropriate-polling | Uses the source coordinator; no additional polling. The source determines the interval. |
| brands | The local `brand/` directory includes the 256 px MCZ icon and logo from the existing Maestro MCZ brand. Local branding is supported for custom integrations since Home Assistant 2026.3. For a formal Core assessment, the domain-specific Core brands requirement still needs review. |
| common-modules | Base entity is in `entity.py`; no coordinator is implemented here. |
| config-flow | UI selects an existing account; source availability is checked. |
| config-flow-test-coverage | Verified: isolated Home Assistant 2026.10.4 tests exercise the actual flow manager, including source failure/recovery and duplicate accounts; config_flow.py has 100% line coverage. Maestro MCZ is simulated. CI enforces the flow coverage. |
| dependency-transparency | The rule covers external Python requirements; this manifest declares none. The separately installed Maestro MCZ integration is an Apache-2.0, open-source custom integration, not a requirement on PyPI. It remains a separate integration dependency and a Core eligibility issue, not resolved by this exception. |
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
| test-before-configure | Proposed exemption: no independent connection or credentials; the source integration manages authentication and updates. The flow checks that a source coordinator is present and at least one coordinator reports a successful last update, without making a network request. A successful previous update is not proof of present connectivity; Core review is required. |
| test-before-setup | Checks that source coordinators exist and at least one reports a successful last update; otherwise raises ConfigEntryNotReady for retry. No extra network requests are made. Source authentication and current connectivity are handled upstream; formal Core applicability is unverified. |
| unique-config-entry | Source entry ID is used as the unique ID and already selected entries are filtered out. |

The assessment is not a claim that Bronze is achieved. In particular, a formal Core review, Core branding eligibility, and the custom dependency's eligibility are unresolved. The integration remains beta.
