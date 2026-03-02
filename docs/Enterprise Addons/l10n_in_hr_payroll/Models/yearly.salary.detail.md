<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# yearly.salary.detail

- Module: [[docs/Enterprise Addons/l10n_in_hr_payroll/l10n_in_hr_payroll|l10n_in_hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/hr_yearly_salary_detail.py`
- Python classes: `YearlySalaryDetail`
- Description: Hr Salary Employee By Category Report

## Field footprint

- Detected fields: 5
- Field types: `Many2many` x 2, `Many2one` x 2, `Selection` x 1
- Relation fields: 4

## Sample fields

- `department_id`: `Many2one` (comodel `hr.department`)
- `employee_ids`: `Many2many` (comodel `hr.employee`, compute `_compute_employee_ids`, store `True`)
- `job_id`: `Many2one` (comodel `hr.job`)
- `related_employee_ids`: `Many2many` (comodel `hr.employee`, compute `_compute_related_employee_ids`)
- `year`: `Selection`

## Method hints

- Detected methods: 6
- Action methods: none
- Compute methods: `_compute_employee_ids`, `_compute_related_employee_ids`
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
title yearly.salary.detail - Direct Relations
class "yearly.salary.detail" as yearly_salary_detail
class "hr.department" as hr_department
class "hr.employee" as hr_employee
class "hr.job" as hr_job
yearly_salary_detail .. hr_employee : related_employee_ids
yearly_salary_detail .. hr_employee : employee_ids
yearly_salary_detail --> hr_department : department_id
yearly_salary_detail --> hr_job : job_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_in_hr_payroll/Models]]

<!-- GENERATED:MODEL -->
