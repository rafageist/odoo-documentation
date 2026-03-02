<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# report.stock.quantity

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `report/report_stock_quantity.py`
- Python classes: `ReportStockQuantity`
- Description: Stock Quantity Report

## Field footprint

- Detected fields: 7
- Field types: `Date` x 1, `Float` x 1, `Many2one` x 4, `Selection` x 1
- Relation fields: 4

## Sample fields

- `company_id`: `Many2one` (comodel `res.company`)
- `date`: `Date`
- `product_id`: `Many2one` (comodel `product.product`)
- `product_qty`: `Float`
- `product_tmpl_id`: `Many2one` (comodel `product.template`)
- `state`: `Selection`
- `warehouse_id`: `Many2one` (comodel `stock.warehouse`)

## Method hints

- Detected methods: 2
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
title report.stock.quantity - Direct Relations
class "report.stock.quantity" as report_stock_quantity
class "product.product" as product_product
class "product.template" as product_template
class "res.company" as res_company
class "stock.warehouse" as stock_warehouse
report_stock_quantity --> product_template : product_tmpl_id
report_stock_quantity --> product_product : product_id
report_stock_quantity --> res_company : company_id
report_stock_quantity --> stock_warehouse : warehouse_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/stock/Models]]

<!-- GENERATED:MODEL -->
