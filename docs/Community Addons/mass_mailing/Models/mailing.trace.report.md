<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# mailing.trace.report

- Module: [[docs/Community Addons/mass_mailing/mass_mailing|mass_mailing]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `report/mailing_trace_report.py`
- Python classes: `MailingTraceReport`
- Description: Mass Mailing Statistics

## Field footprint

- Detected fields: 17
- Field types: `Char` x 3, `Datetime` x 1, `Integer` x 11, `Selection` x 2
- Relation fields: 0

## Sample fields

- `bounced`: `Integer`
- `campaign`: `Char`
- `canceled`: `Integer`
- `clicked`: `Integer`
- `delivered`: `Integer`
- `email_from`: `Char` (comodel `From`)
- `error`: `Integer`
- `mailing_type`: `Selection`
- `name`: `Char`
- `opened`: `Integer`
- `pending`: `Integer`
- `processing`: `Integer`
- `replied`: `Integer`
- `scheduled`: `Integer`
- `scheduled_date`: `Datetime`
- `sent`: `Integer`
- `state`: `Selection`

## Method hints

- Detected methods: 6
- Action methods: none
- Compute methods: none
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing/Models]]

<!-- GENERATED:MODEL -->
