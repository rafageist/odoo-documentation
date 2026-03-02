<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# sale.order.template

- Module: [[docs/Community Addons/sale_management/sale_management|sale_management]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/sale_order_template.py`
- Python classes: `SaleOrderTemplate`
- Description: Quotation Template

## Field footprint

- Detected fields: 12
- Field types: `Boolean` x 3, `Char` x 1, `Float` x 1, `Html` x 1, `Integer` x 2, `Many2one` x 3, `One2many` x 1
- Relation fields: 4

## Sample fields

- `active`: `Boolean`
- `company_id`: `Many2one` (comodel `res.company`)
- `journal_id`: `Many2one` (comodel `account.journal`)
- `mail_template_id`: `Many2one` (comodel `mail.template`)
- `name`: `Char`
- `note`: `Html`
- `number_of_days`: `Integer`
- `prepayment_percent`: `Float` (compute `_compute_prepayment_percent`, store `True`)
- `require_payment`: `Boolean` (compute `_compute_require_payment`, store `True`)
- `require_signature`: `Boolean` (compute `_compute_require_signature`, store `True`)
- `sale_order_template_line_ids`: `One2many` (comodel `sale.order.template.line`)
- `sequence`: `Integer`

## Method hints

- Detected methods: 10
- Action methods: none
- Compute methods: `_compute_prepayment_percent`, `_compute_require_payment`, `_compute_require_signature`
- Onchange methods: `_onchange_prepayment_percent`

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
title sale.order.template - Direct Relations
class "sale.order.template" as sale_order_template
class "account.journal" as account_journal
class "mail.template" as mail_template
class "res.company" as res_company
class "sale.order.template.line" as sale_order_template_line
sale_order_template --> res_company : company_id
sale_order_template --> mail_template : mail_template_id
sale_order_template --|> sale_order_template_line : sale_order_template_line_ids
sale_order_template --> account_journal : journal_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/sale_management/Models]]

<!-- GENERATED:MODEL -->
