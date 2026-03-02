<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# purchase.bill.union

- Module: [[docs/Community Addons/purchase/purchase|purchase]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `report/purchase_bill.py`
- Python classes: `PurchaseBillUnion`
- Description: Purchases & Bills Union

## Field footprint

- Detected fields: 9
- Field types: `Char` x 2, `Date` x 1, `Float` x 1, `Many2one` x 5
- Relation fields: 5

## Sample fields

- `amount`: `Float`
- `company_id`: `Many2one` (comodel `res.company`)
- `currency_id`: `Many2one` (comodel `res.currency`)
- `date`: `Date`
- `name`: `Char`
- `partner_id`: `Many2one` (comodel `res.partner`)
- `purchase_order_id`: `Many2one` (comodel `purchase.order`)
- `reference`: `Char`
- `vendor_bill_id`: `Many2one` (comodel `account.move`)

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: `_compute_display_name`
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
title purchase.bill.union - Direct Relations
class "purchase.bill.union" as purchase_bill_union
class "account.move" as account_move
class "purchase.order" as purchase_order
class "res.company" as res_company
class "res.currency" as res_currency
class "res.partner" as res_partner
purchase_bill_union --> res_partner : partner_id
purchase_bill_union --> res_currency : currency_id
purchase_bill_union --> res_company : company_id
purchase_bill_union --> account_move : vendor_bill_id
purchase_bill_union --> purchase_order : purchase_order_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/purchase/Models]]

<!-- GENERATED:MODEL -->
