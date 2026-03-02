<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# mailing.mailing

- Module: [[docs/Community Addons/mass_mailing_crm/mass_mailing_crm|mass_mailing_crm]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/mailing_mailing.py`
- Python classes: `MailingMailing`

## Field footprint

- Detected fields: 2
- Field types: `Boolean` x 1, `Integer` x 1
- Relation fields: 0

## Sample fields

- `crm_lead_count`: `Integer` (comodel `Leads/Opportunities Count`, compute `_compute_crm_lead_count`)
- `use_leads`: `Boolean` (comodel `Use Leads`, compute `_compute_use_leads`)

## Method hints

- Detected methods: 4
- Action methods: `action_redirect_to_leads_and_opportunities`
- Compute methods: `_compute_crm_lead_count`, `_compute_use_leads`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing_crm/Models]]

<!-- GENERATED:MODEL -->
