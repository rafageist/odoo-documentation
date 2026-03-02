<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.return

- Module: [[docs/Enterprise Addons/l10n_it_reports/l10n_it_reports|l10n_it_reports]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/account_return.py`
- Python classes: `AccountReturn`

## Field footprint

- Detected fields: 2
- Field types: `Boolean` x 1, `Char` x 1
- Relation fields: 0

## Sample fields

- `country_code`: `Char` (related `company_id.country_id.code`)
- `is_quarter_month`: `Boolean` (compute `_compute_is_quarter_month`)

## Method hints

- Detected methods: 5
- Action methods: `action_submit`
- Compute methods: `_compute_is_quarter_month`, `_compute_record_states_for_it`, `_compute_visible_states`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_it_reports/Models]]

<!-- GENERATED:MODEL -->
