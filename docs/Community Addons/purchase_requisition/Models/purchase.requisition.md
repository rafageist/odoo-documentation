<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# purchase.requisition

- Module: [[docs/Community Addons/purchase_requisition/purchase_requisition|purchase_requisition]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/purchase_requisition.py`
- Python classes: `PurchaseRequisition`
- Description: Purchase Requisition
- Inherits: `mail.activity.mixin`, `mail.thread`

## Field footprint

- Detected fields: 16
- Field types: `Boolean` x 1, `Char` x 2, `Date` x 2, `Html` x 1, `Integer` x 1, `Many2one` x 5, `One2many` x 2, `Selection` x 2
- Relation fields: 7

## Sample fields

- `active`: `Boolean` (comodel `Active`)
- `company_id`: `Many2one` (comodel `res.company`)
- `currency_id`: `Many2one` (comodel `res.currency`, compute `_compute_currency_id`, store `True`)
- `date_end`: `Date`
- `date_start`: `Date`
- `description`: `Html`
- `line_ids`: `One2many` (comodel `purchase.requisition.line`)
- `name`: `Char`
- `order_count`: `Integer` (compute `_compute_orders_number`)
- `product_id`: `Many2one` (comodel `product.product`, related `line_ids.product_id`)
- `purchase_ids`: `One2many` (comodel `purchase.order`)
- `reference`: `Char`
- `requisition_type`: `Selection`
- `state`: `Selection`
- `user_id`: `Many2one` (comodel `res.users`)
- `vendor_id`: `Many2one` (comodel `res.partner`)

## Method hints

- Detected methods: 12
- Action methods: `action_cancel`, `action_confirm`, `action_done`, `action_draft`
- Compute methods: `_compute_currency_id`, `_compute_orders_number`
- Onchange methods: `_onchange_vendor`

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
title purchase.requisition - Direct Relations
class "purchase.requisition" as purchase_requisition
class "product.product" as product_product
class "purchase.order" as purchase_order
class "purchase.requisition.line" as purchase_requisition_line
class "res.company" as res_company
class "res.currency" as res_currency
class "res.partner" as res_partner
class "res.users" as res_users
purchase_requisition --> res_partner : vendor_id
purchase_requisition --> res_users : user_id
purchase_requisition --> res_company : company_id
purchase_requisition --|> purchase_order : purchase_ids
purchase_requisition --|> purchase_requisition_line : line_ids
purchase_requisition --> product_product : product_id
purchase_requisition --> res_currency : currency_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/purchase_requisition/Models]]

<!-- GENERATED:MODEL -->
