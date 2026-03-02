<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# crm.lost.reason

- Module: [[docs/Community Addons/crm/crm|crm]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/crm_lost_reason.py`
- Python classes: `CrmLostReason`
- Description: Opp. Lost Reason

## Field footprint

- Detected fields: 3
- Field types: `Boolean` x 1, `Char` x 1, `Integer` x 1
- Relation fields: 0

## Sample fields

- `active`: `Boolean` (comodel `Active`)
- `leads_count`: `Integer` (comodel `Leads Count`, compute `_compute_leads_count`)
- `name`: `Char` (comodel `Description`)

## Method hints

- Detected methods: 2
- Action methods: `action_lost_leads`
- Compute methods: `_compute_leads_count`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/crm/Models]]

<!-- GENERATED:MODEL -->
