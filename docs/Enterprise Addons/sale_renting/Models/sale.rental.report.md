<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# sale.rental.report

- Module: [[docs/Enterprise Addons/sale_renting/sale_renting|sale_renting]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `report/rental_report.py`
- Python classes: `SaleRentalReport`
- Description: Rental Analysis Report

## Field footprint

- Detected fields: 15
- Field types: `Date` x 1, `Float` x 4, `Many2one` x 9, `Selection` x 1
- Relation fields: 9

## Sample fields

- `categ_id`: `Many2one` (comodel `product.category`)
- `company_id`: `Many2one` (comodel `res.company`)
- `currency_id`: `Many2one` (comodel `res.currency`)
- `date`: `Date` (comodel `Date`)
- `order_id`: `Many2one` (comodel `sale.order`)
- `partner_id`: `Many2one` (comodel `res.partner`)
- `price`: `Float` (comodel `Daily Amount`)
- `product_id`: `Many2one` (comodel `product.product`)
- `product_tmpl_id`: `Many2one` (comodel `product.template`)
- `product_uom_id`: `Many2one` (comodel `uom.uom`)
- `qty_delivered`: `Float` (comodel `Daily Picked-Up Qty`)
- `qty_returned`: `Float` (comodel `Daily Returned Qty`)
- `quantity`: `Float` (comodel `Daily Ordered Qty`)
- `state`: `Selection`
- `user_id`: `Many2one` (comodel `res.users`)

## Method hints

- Detected methods: 6
- Action methods: none
- Compute methods: none
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
title sale.rental.report - Direct Relations
class "sale.rental.report" as sale_rental_report
class "product.category" as product_category
class "product.product" as product_product
class "product.template" as product_template
class "res.company" as res_company
class "res.currency" as res_currency
class "res.partner" as res_partner
class "res.users" as res_users
class "sale.order" as sale_order
class "uom.uom" as uom_uom
sale_rental_report --> sale_order : order_id
sale_rental_report --> product_product : product_id
sale_rental_report --> uom_uom : product_uom_id
sale_rental_report --> res_partner : partner_id
sale_rental_report --> res_users : user_id
sale_rental_report --> res_company : company_id
sale_rental_report --> product_template : product_tmpl_id
sale_rental_report --> product_category : categ_id
sale_rental_report --> res_currency : currency_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_renting/Models]]

<!-- GENERATED:MODEL -->
