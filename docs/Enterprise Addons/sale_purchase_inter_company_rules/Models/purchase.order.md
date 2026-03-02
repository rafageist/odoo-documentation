<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# purchase.order

- Module: [[docs/Enterprise Addons/sale_purchase_inter_company_rules/sale_purchase_inter_company_rules|sale_purchase_inter_company_rules]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/purchase_order.py`
- Python classes: `PurchaseOrder`

## Field footprint

- Detected fields: 2
- Field types: `Boolean` x 1, `Many2one` x 1
- Relation fields: 1

## Sample fields

- `auto_generated`: `Boolean`
- `auto_sale_order_id`: `Many2one` (comodel `sale.order`)

## Method hints

- Detected methods: 4
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
title purchase.order - Direct Relations
class "purchase.order" as purchase_order
class "sale.order" as sale_order
purchase_order --> sale_order : auto_sale_order_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_purchase_inter_company_rules/Models]]

<!-- GENERATED:MODEL -->
