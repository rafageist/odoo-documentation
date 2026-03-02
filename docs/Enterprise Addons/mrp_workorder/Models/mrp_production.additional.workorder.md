<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# mrp_production.additional.workorder

- Module: [[docs/Enterprise Addons/mrp_workorder/mrp_workorder|mrp_workorder]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/additional_workorder.py`
- Python classes: `Mrp_ProductionAdditionalWorkorder`
- Description: Additional Workorder

## Field footprint

- Detected fields: 8
- Field types: `Char` x 1, `Datetime` x 1, `Float` x 1, `Many2many` x 1, `Many2one` x 4
- Relation fields: 5

## Sample fields

- `blocked_by_workorder_id`: `Many2one` (comodel `mrp.workorder`)
- `company_id`: `Many2one` (related `production_id.company_id`)
- `date_start`: `Datetime` (comodel `Date Start`)
- `duration_expected`: `Float` (comodel `Expected Duration`)
- `employee_assigned_ids`: `Many2many` (comodel `hr.employee`)
- `name`: `Char` (comodel `Title`)
- `production_id`: `Many2one` (comodel `mrp.production`)
- `workcenter_id`: `Many2one` (comodel `mrp.workcenter`)

## Method hints

- Detected methods: 1
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
title mrp_production.additional.workorder - Direct Relations
class "mrp_production.additional.workorder" as mrp_production_additional_workorder
class "hr.employee" as hr_employee
class "mrp.production" as mrp_production
class "mrp.workcenter" as mrp_workcenter
class "mrp.workorder" as mrp_workorder
mrp_production_additional_workorder --> mrp_production : production_id
mrp_production_additional_workorder --> mrp_workorder : blocked_by_workorder_id
mrp_production_additional_workorder --> mrp_workcenter : workcenter_id
mrp_production_additional_workorder .. hr_employee : employee_assigned_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/mrp_workorder/Models]]

<!-- GENERATED:MODEL -->
