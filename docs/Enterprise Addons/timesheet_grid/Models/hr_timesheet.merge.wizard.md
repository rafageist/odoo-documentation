<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr_timesheet.merge.wizard

- Module: [[docs/Enterprise Addons/timesheet_grid/timesheet_grid|timesheet_grid]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/hr_timesheet_merge_wizard.py`
- Python classes: `Hr_TimesheetMergeWizard`
- Description: Merge Timesheets

## Field footprint

- Detected fields: 8
- Field types: `Char` x 1, `Date` x 1, `Float` x 1, `Many2many` x 1, `Many2one` x 4
- Relation fields: 5

## Sample fields

- `date`: `Date` (comodel `Date`)
- `employee_id`: `Many2one` (comodel `hr.employee`)
- `encoding_uom_id`: `Many2one` (comodel `uom.uom`)
- `name`: `Char` (comodel `Description`, compute `_compute_name`, store `True`)
- `project_id`: `Many2one` (comodel `project.project`)
- `task_id`: `Many2one` (comodel `project.task`, compute `_compute_task_id`, store `True`)
- `timesheet_ids`: `Many2many` (comodel `account.analytic.line`)
- `unit_amount`: `Float` (comodel `Quantity`, compute `_compute_unit_amount`, store `True`)

## Method hints

- Detected methods: 7
- Action methods: `action_merge`
- Compute methods: `_compute_name`, `_compute_task_id`, `_compute_unit_amount`
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
title hr_timesheet.merge.wizard - Direct Relations
class "hr_timesheet.merge.wizard" as hr_timesheet_merge_wizard
class "account.analytic.line" as account_analytic_line
class "hr.employee" as hr_employee
class "project.project" as project_project
class "project.task" as project_task
class "uom.uom" as uom_uom
hr_timesheet_merge_wizard .. account_analytic_line : timesheet_ids
hr_timesheet_merge_wizard --> uom_uom : encoding_uom_id
hr_timesheet_merge_wizard --> project_project : project_id
hr_timesheet_merge_wizard --> project_task : task_id
hr_timesheet_merge_wizard --> hr_employee : employee_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/timesheet_grid/Models]]

<!-- GENERATED:MODEL -->
