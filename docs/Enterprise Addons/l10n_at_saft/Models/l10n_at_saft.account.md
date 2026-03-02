<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# l10n_at_saft.account

- Module: [[docs/Enterprise Addons/l10n_at_saft/l10n_at_saft|l10n_at_saft]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/saft_account.py`
- Python classes: `L10n_At_SaftAccount`
- Description: Information for the SAF-T export about a virtual account from the chart of accounts given in the Austrian SAF-T specification; each (accounting) account has to be mapped to such a virtual account for the SAF-T export

## Field footprint

- Detected fields: 4
- Field types: `Char` x 4
- Relation fields: 0

## Sample fields

- `account_class`: `Char`
- `account_type`: `Char`
- `code`: `Char`
- `name`: `Char`

## Method hints

- Detected methods: 1
- Action methods: none
- Compute methods: `_compute_display_name`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_at_saft/Models]]

<!-- GENERATED:MODEL -->
