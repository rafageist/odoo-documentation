<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# crm.team.member

- Module: [[docs/Community Addons/crm/crm|crm]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/crm_team_member.py`
- Python classes: `CrmTeamMember`

## Field footprint

- Detected fields: 7
- Field types: `Boolean` x 2, `Char` x 2, `Integer` x 3
- Relation fields: 0

## Sample fields

- `assignment_domain`: `Char` (comodel `Assignment Domain`)
- `assignment_domain_preferred`: `Char` (comodel `Preference assignment Domain`)
- `assignment_enabled`: `Boolean` (related `crm_team_id.assignment_enabled`)
- `assignment_max`: `Integer` (comodel `Average Leads Capacity (on 30 days)`)
- `assignment_optout`: `Boolean` (comodel `Pause assignment`)
- `lead_day_count`: `Integer` (comodel `Leads (last 24h)`, compute `_compute_lead_day_count`)
- `lead_month_count`: `Integer` (comodel `Leads (30 days)`, compute `_compute_lead_month_count`)

## Method hints

- Detected methods: 6
- Action methods: none
- Compute methods: `_compute_lead_day_count`, `_compute_lead_month_count`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/crm/Models]]

<!-- GENERATED:MODEL -->
