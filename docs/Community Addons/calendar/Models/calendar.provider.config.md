<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# calendar.provider.config

- Module: [[docs/Community Addons/calendar/calendar|calendar]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `wizard/calendar_provider_config.py`
- Python classes: `CalendarProviderConfig`
- Description: Calendar Provider Configuration Wizard

## Field footprint

- Detected fields: 7
- Field types: `Boolean` x 2, `Char` x 4, `Selection` x 1
- Relation fields: 0

## Sample fields

- `cal_client_id`: `Char` (comodel `Google Client_id`)
- `cal_client_secret`: `Char` (comodel `Google Client_key`)
- `cal_sync_paused`: `Boolean` (comodel `Google Synchronization Paused`)
- `external_calendar_provider`: `Selection`
- `microsoft_outlook_client_identifier`: `Char` (comodel `Outlook Client Id`)
- `microsoft_outlook_client_secret`: `Char` (comodel `Outlook Client Secret`)
- `microsoft_outlook_sync_paused`: `Boolean` (comodel `Outlook Synchronization Paused`)

## Method hints

- Detected methods: 1
- Action methods: `action_calendar_prepare_external_provider_sync`
- Compute methods: none
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/calendar/Models]]

<!-- GENERATED:MODEL -->
