<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# hr.department

- Module: [[docs/Community Addons/hr/hr|hr]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `models/hr_department.py`
- Python classes: `HrDepartment`
- Description: Department
- Inherits: `mail.activity.mixin`, `mail.thread`

## Field footprint

- Detected fields: 17
- Field types: `Boolean` x 2, `Char` x 3, `Integer` x 3, `Many2one` x 4, `One2many` x 4, `Text` x 1
- Relation fields: 8

## Sample fields

- `active`: `Boolean` (comodel `Active`)
- `child_ids`: `One2many` (comodel `hr.department`)
- `color`: `Integer` (comodel `Color Index`)
- `company_id`: `Many2one` (comodel `res.company`)
- `complete_name`: `Char` (comodel `Complete Name`, compute `_compute_complete_name`)
- `has_read_access`: `Boolean` (store `False`)
- `jobs_ids`: `One2many` (comodel `hr.job`)
- `manager_id`: `Many2one` (comodel `hr.employee`)
- `master_department_id`: `Many2one` (comodel `hr.department`, compute `_compute_master_department_id`, store `True`)
- `member_ids`: `One2many` (comodel `hr.employee`)
- `name`: `Char` (comodel `Department Name`)
- `note`: `Text` (comodel `Note`)
- `parent_id`: `Many2one` (comodel `hr.department`)
- `parent_path`: `Char`
- `plan_ids`: `One2many` (comodel `mail.activity.plan`)
- `plans_count`: `Integer` (compute `_compute_plan_count`)
- `total_employee`: `Integer` (compute `_compute_total_employee`)

## Method hints

- Detected methods: 18
- Action methods: `action_employee_from_department`, `action_open_view_child_departments`, `action_plan_from_department`
- Compute methods: `_compute_complete_name`, `_compute_display_name`, `_compute_master_department_id`, `_compute_plan_count`, `_compute_total_employee`
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
title hr.department - Direct Relations
class "hr.department" as hr_department
class "hr.department" as hr_department
class "hr.employee" as hr_employee
class "hr.job" as hr_job
class "mail.activity.plan" as mail_activity_plan
class "res.company" as res_company
hr_department --> res_company : company_id
hr_department --> hr_department : parent_id
hr_department --|> hr_department : child_ids
hr_department --> hr_employee : manager_id
hr_department --|> hr_employee : member_ids
hr_department --|> hr_job : jobs_ids
hr_department --|> mail_activity_plan : plan_ids
hr_department --> hr_department : master_department_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/hr/Models]]

<!-- GENERATED:MODEL -->
