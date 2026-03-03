<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# account.tax.repartition.line

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/account_tax.py`
- Python classes: `AccountTaxRepartitionLine`
- Description: Tax Repartition Line

## Field footprint

- Detected fields: 11
- Field types: `Binary` x 1, `Boolean` x 1, `Float` x 2, `Integer` x 1, `Many2many` x 1, `Many2one` x 3, `Selection` x 2
- Relation fields: 4

## Sample fields

- `account_id`: `Many2one` (comodel `account.account`)
- `company_id`: `Many2one` (comodel `res.company`, related `tax_id.company_id`, store `True`)
- `document_type`: `Selection`
- `factor`: `Float` (compute `_compute_factor`)
- `factor_percent`: `Float`
- `repartition_type`: `Selection`
- `sequence`: `Integer`
- `tag_ids`: `Many2many` (comodel `account.account.tag`)
- `tag_ids_domain`: `Binary` (compute `_compute_tag_ids_domain`)
- `tax_id`: `Many2one` (comodel `account.tax`)
- `use_in_tax_closing`: `Boolean` (compute `_compute_use_in_tax_closing`, store `True`)

## Method hints

- Detected methods: 5
- Action methods: none
- Compute methods: `_compute_factor`, `_compute_tag_ids_domain`, `_compute_use_in_tax_closing`
- Onchange methods: `_onchange_repartition_type`

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
title account.tax.repartition.line - Direct Relations
class "account.tax.repartition.line" as account_tax_repartition_line
class "account.account" as account_account
class "account.account.tag" as account_account_tag
class "account.tax" as account_tax
class "res.company" as res_company
account_tax_repartition_line --> account_account : account_id
account_tax_repartition_line .. account_account_tag : tag_ids
account_tax_repartition_line --> account_tax : tax_id
account_tax_repartition_line --> res_company : company_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/account/Models]]

<!-- GENERATED:MODEL -->
