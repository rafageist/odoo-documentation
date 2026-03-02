<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# esg.employee.report

- Module: [[docs/Enterprise Addons/esg_hr/esg_hr|esg_hr]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `report/esg_employee_report.py`
- Python classes: `EsgEmployeeReport`
- Description: ESG Employee Report

## Field footprint

- Detected fields: 11
- Field types: `Boolean` x 2, `Float` x 1, `Integer` x 2, `Many2one` x 5, `Selection` x 1
- Relation fields: 5

## Sample fields

- `company_id`: `Many2one` (comodel `res.company`)
- `contract_type_id`: `Many2one` (comodel `hr.contract.type`)
- `count`: `Integer`
- `country_id`: `Many2one` (comodel `res.country`)
- `department_id`: `Many2one` (comodel `hr.department`)
- `is_full_time`: `Boolean`
- `is_team_leader`: `Boolean`
- `job_id`: `Many2one` (comodel `hr.job`)
- `leadership_level`: `Integer`
- `sex`: `Selection`
- `wage`: `Float` (comodel `Wage`)

## Method hints

- Detected methods: 8
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
title esg.employee.report - Direct Relations
class "esg.employee.report" as esg_employee_report
class "hr.contract.type" as hr_contract_type
class "hr.department" as hr_department
class "hr.job" as hr_job
class "res.company" as res_company
class "res.country" as res_country
esg_employee_report --> res_company : company_id
esg_employee_report --> hr_department : department_id
esg_employee_report --> res_country : country_id
esg_employee_report --> hr_job : job_id
esg_employee_report --> hr_contract_type : contract_type_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/esg_hr/Models]]

<!-- GENERATED:MODEL -->
