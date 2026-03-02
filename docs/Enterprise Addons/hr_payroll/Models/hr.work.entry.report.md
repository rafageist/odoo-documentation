<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.work.entry.report

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `report/hr_work_entry_report.py`
- Python classes: `HrWorkEntryReport`
- Description: Work Entries Analysis Report

## Field footprint

- Detected fields: 8
- Field types: `Date` x 1, `Float` x 1, `Many2one` x 4, `Selection` x 2
- Relation fields: 4

## Sample fields

- `company_id`: `Many2one` (comodel `res.company`)
- `date`: `Date` (comodel `Date`)
- `department_id`: `Many2one` (comodel `hr.department`)
- `employee_id`: `Many2one` (comodel `hr.employee`)
- `number_of_days`: `Float` (comodel `Days`)
- `state`: `Selection`
- `work_entry_source`: `Selection`
- `work_entry_type_id`: `Many2one` (comodel `hr.work.entry.type`)

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
title hr.work.entry.report - Direct Relations
class "hr.work.entry.report" as hr_work_entry_report
class "hr.department" as hr_department
class "hr.employee" as hr_employee
class "hr.work.entry.type" as hr_work_entry_type
class "res.company" as res_company
hr_work_entry_report --> res_company : company_id
hr_work_entry_report --> hr_department : department_id
hr_work_entry_report --> hr_employee : employee_id
hr_work_entry_report --> hr_work_entry_type : work_entry_type_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Models]]

<!-- GENERATED:MODEL -->
