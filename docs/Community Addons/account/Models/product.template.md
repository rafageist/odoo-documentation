<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# product.template

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/product.py`
- Python classes: `ProductTemplate`

## Field footprint

- Detected fields: 7
- Field types: `Char` x 2, `Many2many` x 3, `Many2one` x 2
- Relation fields: 5

## Sample fields

- `account_tag_ids`: `Many2many` (comodel `account.account.tag`)
- `fiscal_country_codes`: `Char` (compute `_compute_fiscal_country_codes`)
- `property_account_expense_id`: `Many2one` (comodel `account.account`)
- `property_account_income_id`: `Many2one` (comodel `account.account`)
- `supplier_taxes_id`: `Many2many` (comodel `account.tax`)
- `tax_string`: `Char` (compute `_compute_tax_string`)
- `taxes_id`: `Many2many` (comodel `account.tax`)

## Method hints

- Detected methods: 12
- Action methods: none
- Compute methods: `_compute_fiscal_country_codes`, `_compute_tax_string`
- Onchange methods: `_onchange_type`

## Direct relation diagram

```plantuml
@startuml
!define ODOO_COLOR_PRIMARY #714B67
!define ODOO_COLOR_ACCENT #875A7B
!define ODOO_COLOR_BG #FAF7FA

skinparam backgroundColor ODOO_COLOR_BG
skinparam defaultTextAlignment left
skinparam ArrowColor ODOO_COLOR_ACCENT
skinparam ClassBackgroundColor white
skinparam ClassBorderColor ODOO_COLOR_PRIMARY
skinparam ComponentBackgroundColor white
skinparam ComponentBorderColor ODOO_COLOR_PRIMARY
skinparam NoteBackgroundColor #FFF8FF
skinparam NoteBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBackgroundColor #FFFFFF
skinparam SequenceParticipantBorderColor ODOO_COLOR_PRIMARY
skinparam SequenceParticipantBackgroundColor #FFFFFF
skinparam sequence {
  ArrowColor ODOO_COLOR_ACCENT
  ActorBorderColor ODOO_COLOR_PRIMARY
}
title product.template - Direct Relations
class "product.template" as product_template
class "account.account" as account_account
class "account.account.tag" as account_account_tag
class "account.tax" as account_tax
product_template .. account_tax : taxes_id
product_template .. account_tax : supplier_taxes_id
product_template --> account_account : property_account_income_id
product_template --> account_account : property_account_expense_id
product_template .. account_account_tag : account_tag_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/account/Models]]

<!-- GENERATED:MODEL -->
