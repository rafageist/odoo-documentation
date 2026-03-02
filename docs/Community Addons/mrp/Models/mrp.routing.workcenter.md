<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# mrp.routing.workcenter

- Module: [[docs/Community Addons/mrp/mrp|mrp]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/mrp_routing.py`
- Python classes: `MrpRoutingWorkcenter`
- Description: Work Center Usage
- Inherits: `mail.activity.mixin`, `mail.thread`

## Field footprint

- Detected fields: 23
- Field types: `Boolean` x 3, `Char` x 2, `Float` x 4, `Integer` x 4, `Many2many` x 4, `Many2one` x 3, `One2many` x 1, `Selection` x 2
- Relation fields: 8

## Sample fields

- `active`: `Boolean`
- `allow_operation_dependencies`: `Boolean` (related `bom_id.allow_operation_dependencies`)
- `blocked_by_operation_ids`: `Many2many` (comodel `mrp.routing.workcenter`)
- `bom_id`: `Many2one` (comodel `mrp.bom`)
- `bom_product_template_attribute_value_ids`: `Many2many` (comodel `product.template.attribute.value`)
- `company_id`: `Many2one` (comodel `res.company`, related `bom_id.company_id`)
- `cost`: `Float` (comodel `Cost`, compute `_compute_cost`)
- `cost_mode`: `Selection`
- `cycle_number`: `Integer` (comodel `Repetitions`, compute `_compute_time_cycle`)
- `name`: `Char` (comodel `Operation`)
- `needed_by_operation_ids`: `Many2many` (comodel `mrp.routing.workcenter`)
- `possible_bom_product_template_attribute_value_ids`: `Many2many` (related `bom_id.possible_product_template_attribute_value_ids`)
- `sequence`: `Integer` (comodel `Sequence`)
- `show_time_total`: `Boolean` (comodel `Show Total Duration?`, compute `_compute_time_cycle`)
- `time_computed_on`: `Char` (comodel `Computed on last`, compute `_compute_time_computed_on`)
- `time_cycle`: `Float` (comodel `Cycles`, compute `_compute_time_cycle`)
- `time_cycle_manual`: `Float` (comodel `Manual Duration`)
- `time_mode`: `Selection`
- `time_mode_batch`: `Integer` (comodel `Based on`)
- `time_total`: `Float` (comodel `Total Duration`, compute `_compute_time_cycle`)

## Method hints

- Detected methods: 13
- Action methods: `action_archive`, `action_open_operation_form`, `action_unarchive`
- Compute methods: `_compute_cost`, `_compute_time_computed_on`, `_compute_time_cycle`, `_compute_workorder_count`
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
title mrp.routing.workcenter - Direct Relations
class "mrp.routing.workcenter" as mrp_routing_workcenter
class "mrp.bom" as mrp_bom
class "mrp.routing.workcenter" as mrp_routing_workcenter
class "mrp.workcenter" as mrp_workcenter
class "mrp.workorder" as mrp_workorder
class "product.template.attribute.value" as product_template_attribute_value
class "res.company" as res_company
mrp_routing_workcenter --> mrp_workcenter : workcenter_id
mrp_routing_workcenter --> mrp_bom : bom_id
mrp_routing_workcenter --> res_company : company_id
mrp_routing_workcenter --|> mrp_workorder : workorder_ids
mrp_routing_workcenter .. product_template_attribute_value : bom_product_template_attribute_value_ids
mrp_routing_workcenter .. mrp_routing_workcenter : blocked_by_operation_ids
mrp_routing_workcenter .. mrp_routing_workcenter : needed_by_operation_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/mrp/Models]]

<!-- GENERATED:MODEL -->
