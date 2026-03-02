<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# stock.inventory.conflict

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `wizard/stock_inventory_conflict.py`
- Python classes: `StockInventoryConflict`
- Description: Conflict in Inventory

## Field footprint

- Detected fields: 2
- Field types: `Many2many` x 2
- Relation fields: 2

## Sample fields

- `quant_ids`: `Many2many` (comodel `stock.quant`)
- `quant_to_fix_ids`: `Many2many` (comodel `stock.quant`)

## Method hints

- Detected methods: 2
- Action methods: `action_keep_counted_quantity`, `action_keep_difference`
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
title stock.inventory.conflict - Direct Relations
class "stock.inventory.conflict" as stock_inventory_conflict
class "stock.quant" as stock_quant
stock_inventory_conflict .. stock_quant : quant_ids
stock_inventory_conflict .. stock_quant : quant_to_fix_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/stock/Models]]

<!-- GENERATED:MODEL -->
