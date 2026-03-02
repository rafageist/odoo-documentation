<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.appraisal.goal

- Module: [[docs/Enterprise Addons/hr_appraisal/hr_appraisal|hr_appraisal]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/hr_appraisal_goal.py`
- Python classes: `HrAppraisalGoal`
- Description: Appraisal Goal
- Inherits: `hr.mixin`, `mail.activity.mixin`, `mail.thread`

## Field footprint

- Detected fields: 22
- Field types: `Boolean` x 3, `Char` x 2, `Date` x 1, `Float` x 1, `Html` x 1, `Integer` x 3, `Many2many` x 6, `Many2one` x 3, `One2many` x 1, `Selection` x 1
- Relation fields: 10

## Sample fields

- `active`: `Boolean`
- `child_ids`: `One2many` (comodel `hr.appraisal.goal`)
- `company_id`: `Many2one` (comodel `res.company`, related `employee_ids.company_id`, store `True`)
- `deadline`: `Date`
- `department_ids`: `Many2many` (comodel `hr.department`, compute `_compute_department_ids`, store `True`)
- `description`: `Html`
- `employee_autocomplete_ids`: `Many2many` (comodel `hr.employee`, compute `_compute_employee_autocomplete`)
- `employee_ids`: `Many2many` (comodel `hr.employee`)
- `has_edit_right`: `Boolean` (compute `_compute_has_edit_right`)
- `is_manager`: `Boolean` (compute `_compute_is_manager`)
- `job_ids`: `Many2many` (comodel `hr.job`, compute `_compute_job_ids`, store `True`)
- `manager_ids`: `Many2many` (comodel `hr.employee`, compute `_compute_manager_ids`, store `True`)
- `name`: `Char`
- `number_of_completed_sibling_goals`: `Integer` (compute `compute_number_of_completed_sibling_goals`, store `True`)
- `number_of_sibling_goals`: `Integer` (compute `_compute_number_of_sibling_goals`, store `True`)
- `parent_id`: `Many2one` (comodel `hr.appraisal.goal`)
- `parent_path`: `Char`
- `progression`: `Selection` (compute `_compute_progression`, store `True`)
- `sibling_goals_ratio`: `Float` (compute `_compute_sibling_goals_ratio`, store `True`)
- `tag_ids`: `Many2many` (comodel `hr.appraisal.goal.tag`)

## Method hints

- Detected methods: 22
- Action methods: `action_archive`, `action_confirm`, `action_open_goal_template`, `action_save_as_template`, `action_select_employees`
- Compute methods: `_compute_department_ids`, `_compute_employee_autocomplete`, `_compute_has_edit_right`, `_compute_is_manager`, `_compute_job_ids`, `_compute_manager_ids`, `_compute_number_of_sibling_goals`, `_compute_progression`, and 1 more
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
title hr.appraisal.goal - Direct Relations
class "hr.appraisal.goal" as hr_appraisal_goal
class "hr.appraisal.goal" as hr_appraisal_goal
class "hr.appraisal.goal.tag" as hr_appraisal_goal_tag
class "hr.department" as hr_department
class "hr.employee" as hr_employee
class "hr.job" as hr_job
class "res.company" as res_company
hr_appraisal_goal .. hr_employee : employee_ids
hr_appraisal_goal .. hr_employee : employee_autocomplete_ids
hr_appraisal_goal --> res_company : company_id
hr_appraisal_goal .. hr_employee : manager_ids
hr_appraisal_goal .. hr_department : department_ids
hr_appraisal_goal .. hr_job : job_ids
hr_appraisal_goal .. hr_appraisal_goal_tag : tag_ids
hr_appraisal_goal --> hr_appraisal_goal : template_goal_id
hr_appraisal_goal --> hr_appraisal_goal : parent_id
hr_appraisal_goal --|> hr_appraisal_goal : child_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_appraisal/Models]]

<!-- GENERATED:MODEL -->
