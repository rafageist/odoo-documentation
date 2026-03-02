<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.storage.category.capacity

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/stock_storage_category.py`
- Python classes: `StockStorageCategoryCapacity`
- Description: Storage Category Capacity

## Field footprint

- Detected fields: 6
- Field types: `Float` x 1, `Many2one` x 5
- Relation fields: 5

## Sample fields

- `company_id`: `Many2one` (comodel `res.company`, related `storage_category_id.company_id`)
- `package_type_id`: `Many2one` (comodel `stock.package.type`)
- `product_id`: `Many2one` (comodel `product.product`)
- `product_uom_id`: `Many2one` (related `product_id.uom_id`)
- `quantity`: `Float` (comodel `Quantity`)
- `storage_category_id`: `Many2one` (comodel `stock.storage.category`)

## Method hints

- Detected methods: 0
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
title stock.storage.category.capacity - Direct Relations
class "stock.storage.category.capacity" as stock_storage_category_capacity
class "product.product" as product_product
class "res.company" as res_company
class "stock.package.type" as stock_package_type
class "stock.storage.category" as stock_storage_category
stock_storage_category_capacity --> stock_storage_category : storage_category_id
stock_storage_category_capacity --> product_product : product_id
stock_storage_category_capacity --> stock_package_type : package_type_id
stock_storage_category_capacity --> res_company : company_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/stock/Models]]

<!-- GENERATED:MODEL -->
