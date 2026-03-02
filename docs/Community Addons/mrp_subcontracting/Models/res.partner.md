<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# res.partner

- Module: [[docs/Community Addons/mrp_subcontracting/mrp_subcontracting|mrp_subcontracting]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/res_partner.py`
- Python classes: `ResPartner`

## Field footprint

- Detected fields: 5
- Field types: `Boolean` x 1, `Many2many` x 3, `Many2one` x 1
- Relation fields: 4

## Sample fields

- `bom_ids`: `Many2many` (comodel `mrp.bom`, compute `_compute_bom_ids`)
- `is_subcontractor`: `Boolean` (compute `_compute_is_subcontractor`, store `False`)
- `picking_ids`: `Many2many` (comodel `stock.picking`, compute `_compute_picking_ids`)
- `production_ids`: `Many2many` (comodel `mrp.production`, compute `_compute_production_ids`)
- `property_stock_subcontractor`: `Many2one` (comodel `stock.location`)

## Method hints

- Detected methods: 5
- Action methods: none
- Compute methods: `_compute_bom_ids`, `_compute_is_subcontractor`, `_compute_picking_ids`, `_compute_production_ids`
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
title res.partner - Direct Relations
class "res.partner" as res_partner
class "mrp.bom" as mrp_bom
class "mrp.production" as mrp_production
class "stock.location" as stock_location
class "stock.picking" as stock_picking
res_partner --> stock_location : property_stock_subcontractor
res_partner .. mrp_bom : bom_ids
res_partner .. mrp_production : production_ids
res_partner .. stock_picking : picking_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/mrp_subcontracting/Models]]

<!-- GENERATED:MODEL -->
