<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# purchase.requisition.line

- Module: [[docs/Community Addons/purchase_requisition/purchase_requisition|purchase_requisition]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/purchase_requisition.py`
- Python classes: `PurchaseRequisitionLine`
- Description: Purchase Requisition Line
- Inherits: `analytic.mixin`

## Field footprint

- Detected fields: 9
- Field types: `Char` x 1, `Float` x 3, `Many2one` x 4, `One2many` x 1
- Relation fields: 5

## Sample fields

- `company_id`: `Many2one` (comodel `res.company`, related `requisition_id.company_id`, store `True`)
- `price_unit`: `Float` (compute `_compute_price_unit`, store `True`)
- `product_description_variants`: `Char` (comodel `Description`)
- `product_id`: `Many2one` (comodel `product.product`)
- `product_qty`: `Float`
- `product_uom_id`: `Many2one` (comodel `uom.uom`, compute `_compute_product_uom_id`, store `True`)
- `qty_ordered`: `Float` (compute `_compute_ordered_qty`)
- `requisition_id`: `Many2one` (comodel `purchase.requisition`)
- `supplier_info_ids`: `One2many` (comodel `product.supplierinfo`)

## Method hints

- Detected methods: 8
- Action methods: none
- Compute methods: `_compute_ordered_qty`, `_compute_price_unit`, `_compute_product_uom_id`
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
title purchase.requisition.line - Direct Relations
class "purchase.requisition.line" as purchase_requisition_line
class "product.product" as product_product
class "product.supplierinfo" as product_supplierinfo
class "purchase.requisition" as purchase_requisition
class "res.company" as res_company
class "uom.uom" as uom_uom
purchase_requisition_line --> product_product : product_id
purchase_requisition_line --> uom_uom : product_uom_id
purchase_requisition_line --> purchase_requisition : requisition_id
purchase_requisition_line --> res_company : company_id
purchase_requisition_line --|> product_supplierinfo : supplier_info_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/purchase_requisition/Models]]

<!-- GENERATED:MODEL -->
