<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# account.analytic.line

- Module: [[docs/Community Addons/hr_timesheet/hr_timesheet|hr_timesheet]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/hr_timesheet.py`
- Python classes: `AccountAnalyticLine`

## Field footprint

- Detected fields: 14
- Field types: `Boolean` x 1, `Char` x 2, `Many2many` x 1, `Many2one` x 10
- Relation fields: 11

## Sample fields

- `calendar_display_name`: `Char` (compute `_compute_calendar_display_name`)
- `department_id`: `Many2one` (comodel `hr.department`, compute `_compute_department_id`, store `True`)
- `employee_id`: `Many2one` (comodel `hr.employee`)
- `encoding_uom_id`: `Many2one` (comodel `uom.uom`, compute `_compute_encoding_uom_id`)
- `job_title`: `Char` (related `employee_id.job_title`)
- `manager_id`: `Many2one` (comodel `hr.employee`, related `employee_id.parent_id`, store `True`)
- `message_partner_ids`: `Many2many` (comodel `res.partner`, compute `_compute_message_partner_ids`)
- `milestone_id`: `Many2one` (comodel `project.milestone`, related `task_id.milestone_id`)
- `parent_task_id`: `Many2one` (comodel `project.task`, related `task_id.parent_id`, store `True`)
- `partner_id`: `Many2one` (compute `_compute_partner_id`, store `True`)
- `project_id`: `Many2one` (comodel `project.project`, compute `_compute_project_id`, store `True`)
- `readonly_timesheet`: `Boolean` (compute `_compute_readonly_timesheet`)
- `task_id`: `Many2one` (comodel `project.task`, compute `_compute_task_id`, store `True`)
- `user_id`: `Many2one` (compute `_compute_user_id`, store `True`)

## Method hints

- Detected methods: 40
- Action methods: `action_open_timesheet_view_portal`
- Compute methods: `_compute_calendar_display_name`, `_compute_department_id`, `_compute_display_name`, `_compute_encoding_uom_id`, `_compute_message_partner_ids`, `_compute_partner_id`, `_compute_project_id`, `_compute_readonly_timesheet`, and 2 more
- Onchange methods: `_onchange_project_id`

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
title account.analytic.line - Direct Relations
class "account.analytic.line" as account_analytic_line
class "hr.department" as hr_department
class "hr.employee" as hr_employee
class "project.milestone" as project_milestone
class "project.project" as project_project
class "project.task" as project_task
class "res.partner" as res_partner
class "uom.uom" as uom_uom
account_analytic_line --> project_task : task_id
account_analytic_line --> project_task : parent_task_id
account_analytic_line --> project_project : project_id
account_analytic_line --> hr_employee : employee_id
account_analytic_line --> hr_department : department_id
account_analytic_line --> hr_employee : manager_id
account_analytic_line --> uom_uom : encoding_uom_id
account_analytic_line --> project_milestone : milestone_id
account_analytic_line .. res_partner : message_partner_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/hr_timesheet/Models]]

<!-- GENERATED:MODEL -->
