<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# mrp.consumption.warning.line

- Module: [[docs/Community Addons/mrp/mrp|mrp]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `wizard/mrp_consumption_warning.py`
- Python classes: `MrpConsumptionWarningLine`
- Description: Line of issue consumption

## Field footprint

- Detected fields: 7
- Field types: `Float` x 2, `Many2one` x 4, `Selection` x 1
- Relation fields: 4

## Sample fields

- `consumption`: `Selection` (related `mrp_production_id.consumption`)
- `mrp_consumption_warning_id`: `Many2one` (comodel `mrp.consumption.warning`)
- `mrp_production_id`: `Many2one` (comodel `mrp.production`)
- `product_consumed_qty_uom`: `Float` (comodel `Consumed`)
- `product_expected_qty_uom`: `Float` (comodel `To Consume`)
- `product_id`: `Many2one` (comodel `product.product`)
- `product_uom_id`: `Many2one` (comodel `uom.uom`, related `product_id.uom_id`)

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
title mrp.consumption.warning.line - Direct Relations
class "mrp.consumption.warning.line" as mrp_consumption_warning_line
class "mrp.consumption.warning" as mrp_consumption_warning
class "mrp.production" as mrp_production
class "product.product" as product_product
class "uom.uom" as uom_uom
mrp_consumption_warning_line --> mrp_consumption_warning : mrp_consumption_warning_id
mrp_consumption_warning_line --> mrp_production : mrp_production_id
mrp_consumption_warning_line --> product_product : product_id
mrp_consumption_warning_line --> uom_uom : product_uom_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/mrp/Models]]

<!-- GENERATED:MODEL -->
