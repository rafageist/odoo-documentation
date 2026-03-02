<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# mrp.workcenter.productivity

- Module: [[docs/Community Addons/mrp/mrp|mrp]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/mrp_workcenter.py`
- Python classes: `MrpWorkcenterProductivity`
- Description: Workcenter Productivity Log

## Field footprint

- Detected fields: 11
- Field types: `Datetime` x 2, `Float` x 1, `Many2one` x 6, `Selection` x 1, `Text` x 1
- Relation fields: 6

## Sample fields

- `company_id`: `Many2one` (comodel `res.company`)
- `date_end`: `Datetime` (comodel `End Date`)
- `date_start`: `Datetime` (comodel `Start Date`)
- `description`: `Text` (comodel `Description`)
- `duration`: `Float` (comodel `Duration`, compute `_compute_duration`, store `True`)
- `loss_id`: `Many2one` (comodel `mrp.workcenter.productivity.loss`)
- `loss_type`: `Selection` (related `loss_id.loss_type`)
- `production_id`: `Many2one` (comodel `mrp.production`, related `workorder_id.production_id`)
- `user_id`: `Many2one` (comodel `res.users`)
- `workcenter_id`: `Many2one` (comodel `mrp.workcenter`)
- `workorder_id`: `Many2one` (comodel `mrp.workorder`)

## Method hints

- Detected methods: 9
- Action methods: none
- Compute methods: `_compute_duration`
- Onchange methods: `_date_end_changed`, `_date_start_changed`, `_duration_changed`

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
title mrp.workcenter.productivity - Direct Relations
class "mrp.workcenter.productivity" as mrp_workcenter_productivity
class "mrp.production" as mrp_production
class "mrp.workcenter" as mrp_workcenter
class "mrp.workcenter.productivity.loss" as mrp_workcenter_productivity_loss
class "mrp.workorder" as mrp_workorder
class "res.company" as res_company
class "res.users" as res_users
mrp_workcenter_productivity --> mrp_production : production_id
mrp_workcenter_productivity --> mrp_workcenter : workcenter_id
mrp_workcenter_productivity --> res_company : company_id
mrp_workcenter_productivity --> mrp_workorder : workorder_id
mrp_workcenter_productivity --> res_users : user_id
mrp_workcenter_productivity --> mrp_workcenter_productivity_loss : loss_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/mrp/Models]]

<!-- GENERATED:MODEL -->
