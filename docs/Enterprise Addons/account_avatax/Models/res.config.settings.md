<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.config.settings

- Module: [[docs/Enterprise Addons/account_avatax/account_avatax|account_avatax]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_company.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 8
- Field types: `Boolean` x 4, `Char` x 3, `Selection` x 1
- Relation fields: 0

## Sample fields

- `avalara_address_validation`: `Boolean` (related `company_id.avalara_address_validation`)
- `avalara_api_id`: `Char` (related `company_id.avalara_api_id`)
- `avalara_api_key`: `Char` (related `company_id.avalara_api_key`)
- `avalara_commit`: `Boolean` (related `company_id.avalara_commit`)
- `avalara_environment`: `Selection` (related `company_id.avalara_environment`)
- `avalara_partner_code`: `Char` (related `company_id.partner_id.avalara_partner_code`)
- `avalara_use_upc`: `Boolean` (related `company_id.avalara_use_upc`)
- `setting_account_avatax`: `Boolean` (related `company_id.setting_account_avatax`)

## Method hints

- Detected methods: 4
- Action methods: none
- Compute methods: none
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_avatax/Models]]

<!-- GENERATED:MODEL -->
