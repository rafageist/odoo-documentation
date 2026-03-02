<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.work.entry.export.mixin

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/hr_work_entry_export_mixin.py`
- Python classes: `HrWorkEntryExportMixin`
- Description: Work Entry Export Mixin

## Field footprint

- Detected fields: 10
- Field types: `Binary` x 1, `Char` x 1, `Date` x 2, `Integer` x 2, `Many2one` x 2, `One2many` x 1, `Selection` x 1
- Relation fields: 3

## Sample fields

- `company_id`: `Many2one` (comodel `res.company`)
- `create_uid`: `Many2one` (comodel `res.users`)
- `eligible_employee_count`: `Integer` (comodel `Eligible Employees Count`, compute `_compute_eligible_employee_count`)
- `eligible_employee_line_ids`: `One2many` (comodel `hr.work.entry.export.employee.mixin`)
- `export_file`: `Binary` (comodel `Export File`)
- `export_filename`: `Char` (comodel `Export Filename`)
- `period_start`: `Date` (comodel `Period Start`, compute `_compute_period_dates`, store `True`)
- `period_stop`: `Date` (comodel `Period Stop`, compute `_compute_period_dates`, store `True`)
- `reference_month`: `Selection`
- `reference_year`: `Integer` (comodel `Reference Year`)

## Method hints

- Detected methods: 17
- Action methods: `action_export_file`, `action_open_employees`, `action_populate`
- Compute methods: `_compute_display_name`, `_compute_eligible_employee_count`, `_compute_period_dates`
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
title hr.work.entry.export.mixin - Direct Relations
class "hr.work.entry.export.mixin" as hr_work_entry_export_mixin
class "hr.work.entry.export.employee.mixin" as hr_work_entry_export_employee_mixin
class "res.company" as res_company
class "res.users" as res_users
hr_work_entry_export_mixin --> res_users : create_uid
hr_work_entry_export_mixin --|> hr_work_entry_export_employee_mixin : eligible_employee_line_ids
hr_work_entry_export_mixin --> res_company : company_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Models]]

<!-- GENERATED:MODEL -->
