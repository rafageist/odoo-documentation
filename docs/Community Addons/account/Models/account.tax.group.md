<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# account.tax.group

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/account_tax.py`
- Python classes: `AccountTaxGroup`
- Description: Tax Group

## Field footprint

- Detected fields: 10
- Field types: `Char` x 4, `Integer` x 1, `Many2one` x 5
- Relation fields: 5

## Sample fields

- `advance_tax_payment_account_id`: `Many2one` (comodel `account.account`)
- `company_id`: `Many2one` (comodel `res.company`)
- `country_code`: `Char` (related `country_id.code`)
- `country_id`: `Many2one` (comodel `res.country`, compute `_compute_country_id`, store `True`)
- `name`: `Char`
- `pos_receipt_label`: `Char`
- `preceding_subtotal`: `Char`
- `sequence`: `Integer`
- `tax_payable_account_id`: `Many2one` (comodel `account.account`)
- `tax_receivable_account_id`: `Many2one` (comodel `account.account`)

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: `_compute_country_id`
- Onchange methods: none

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
title account.tax.group - Direct Relations
class "account.tax.group" as account_tax_group
class "account.account" as account_account
class "res.company" as res_company
class "res.country" as res_country
account_tax_group --> res_company : company_id
account_tax_group --> account_account : tax_payable_account_id
account_tax_group --> account_account : tax_receivable_account_id
account_tax_group --> account_account : advance_tax_payment_account_id
account_tax_group --> res_country : country_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/account/Models]]

<!-- GENERATED:MODEL -->
