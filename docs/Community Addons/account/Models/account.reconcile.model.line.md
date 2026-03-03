<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# account.reconcile.model.line

- Module: [[docs/Community Addons/account/account|account]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/account_reconcile_model.py`
- Python classes: `AccountReconcileModelLine`
- Description: Rules for the reconciliation model
- Inherits: `analytic.mixin`

## Field footprint

- Detected fields: 10
- Field types: `Char` x 2, `Float` x 1, `Integer` x 1, `Many2many` x 1, `Many2one` x 4, `Selection` x 1
- Relation fields: 5

## Sample fields

- `account_id`: `Many2one` (comodel `account.account`)
- `amount`: `Float` (compute `_compute_float_amount`, store `True`)
- `amount_string`: `Char`
- `amount_type`: `Selection`
- `company_id`: `Many2one` (related `model_id.company_id`, store `True`)
- `label`: `Char`
- `model_id`: `Many2one` (comodel `account.reconcile.model`)
- `partner_id`: `Many2one` (comodel `res.partner`)
- `sequence`: `Integer`
- `tax_ids`: `Many2many` (comodel `account.tax`)

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: `_compute_float_amount`
- Onchange methods: `_onchange_amount_type`

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
title account.reconcile.model.line - Direct Relations
class "account.reconcile.model.line" as account_reconcile_model_line
class "account.account" as account_account
class "account.reconcile.model" as account_reconcile_model
class "account.tax" as account_tax
class "res.partner" as res_partner
account_reconcile_model_line --> account_reconcile_model : model_id
account_reconcile_model_line --> account_account : account_id
account_reconcile_model_line --> res_partner : partner_id
account_reconcile_model_line .. account_tax : tax_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/account/Models]]

<!-- GENERATED:MODEL -->
