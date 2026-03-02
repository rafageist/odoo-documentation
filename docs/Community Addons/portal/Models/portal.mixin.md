<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# portal.mixin

- Module: [[docs/Community Addons/portal/portal|portal]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/portal_mixin.py`
- Python classes: `PortalMixin`
- Description: Portal Mixin

## Field footprint

- Detected fields: 3
- Field types: `Char` x 2, `Text` x 1
- Relation fields: 0

## Sample fields

- `access_token`: `Char` (comodel `Security Token`)
- `access_url`: `Char` (comodel `Portal Access URL`, compute `_compute_access_url`)
- `access_warning`: `Text` (comodel `Access warning`, compute `_compute_access_warning`)

## Method hints

- Detected methods: 7
- Action methods: `action_share`
- Compute methods: `_compute_access_url`, `_compute_access_warning`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/portal/Models]]

<!-- GENERATED:MODEL -->
