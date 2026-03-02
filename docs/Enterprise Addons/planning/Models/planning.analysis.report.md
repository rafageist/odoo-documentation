<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# planning.analysis.report

- Module: [[docs/Enterprise Addons/planning/planning|planning]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `report/planning_analysis_report.py`
- Python classes: `PlanningAnalysisReport`
- Description: Planning Analysis Report

## Field footprint

- Detected fields: 19
- Field types: `Boolean` x 2, `Char` x 1, `Datetime` x 2, `Float` x 2, `Many2one` x 9, `Selection` x 2, `Text` x 1
- Relation fields: 9

## Sample fields

- `allocated_hours`: `Float` (comodel `Allocated Time`)
- `allocated_percentage`: `Float` (comodel `Allocated Time (%)`)
- `company_id`: `Many2one` (comodel `res.company`)
- `department_id`: `Many2one` (comodel `hr.department`)
- `employee_id`: `Many2one` (comodel `hr.employee`)
- `end_datetime`: `Datetime` (comodel `End Date`)
- `job_title`: `Char` (comodel `Job Title`)
- `manager_id`: `Many2one` (comodel `hr.employee`)
- `name`: `Text` (comodel `Note`)
- `publication_warning`: `Boolean` (comodel `Modified Since Last Publication`)
- `recurrency_id`: `Many2one` (comodel `planning.recurrency`)
- `request_to_switch`: `Boolean` (comodel `Has there been a request to switch on this shift slot?`)
- `resource_id`: `Many2one` (comodel `resource.resource`)
- `resource_type`: `Selection`
- `role_id`: `Many2one` (comodel `planning.role`)
- `slot_id`: `Many2one` (comodel `planning.slot`)
- `start_datetime`: `Datetime` (comodel `Start Date`)
- `state`: `Selection`
- `user_id`: `Many2one` (comodel `res.users`)

## Method hints

- Detected methods: 6
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
title planning.analysis.report - Direct Relations
class "planning.analysis.report" as planning_analysis_report
class "hr.department" as hr_department
class "hr.employee" as hr_employee
class "planning.recurrency" as planning_recurrency
class "planning.role" as planning_role
class "planning.slot" as planning_slot
class "res.company" as res_company
class "res.users" as res_users
class "resource.resource" as resource_resource
planning_analysis_report --> res_company : company_id
planning_analysis_report --> hr_department : department_id
planning_analysis_report --> hr_employee : employee_id
planning_analysis_report --> hr_employee : manager_id
planning_analysis_report --> planning_recurrency : recurrency_id
planning_analysis_report --> resource_resource : resource_id
planning_analysis_report --> planning_role : role_id
planning_analysis_report --> res_users : user_id
planning_analysis_report --> planning_slot : slot_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/planning/Models]]

<!-- GENERATED:MODEL -->
