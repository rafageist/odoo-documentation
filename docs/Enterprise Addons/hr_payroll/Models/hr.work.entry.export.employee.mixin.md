<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.work.entry.export.employee.mixin

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/hr_work_entry_export_mixin.py`
- Python classes: `HrWorkEntryExportEmployeeMixin`
- Description: Work Entry Export Employee

## Field footprint

- Detected fields: 5
- Field types: `Many2many` x 2, `Many2one` x 3
- Relation fields: 5

## Sample fields

- `company_id`: `Many2one` (related `export_id.company_id`, store `True`)
- `employee_id`: `Many2one` (comodel `hr.employee`)
- `export_id`: `Many2one` (comodel `hr.work.entry.export.mixin`)
- `version_ids`: `Many2many` (comodel `hr.version`, compute `_compute_contract_ids`, store `True`)
- `work_entry_ids`: `Many2many` (comodel `hr.work.entry`, compute `_compute_work_entry_ids`)

## Method hints

- Detected methods: 7
- Action methods: `action_open_work_entries`
- Compute methods: `_compute_contract_ids`, `_compute_work_entry_ids`
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
title hr.work.entry.export.employee.mixin - Direct Relations
class "hr.work.entry.export.employee.mixin" as hr_work_entry_export_employee_mixin
class "hr.employee" as hr_employee
class "hr.version" as hr_version
class "hr.work.entry" as hr_work_entry
class "hr.work.entry.export.mixin" as hr_work_entry_export_mixin
hr_work_entry_export_employee_mixin --> hr_work_entry_export_mixin : export_id
hr_work_entry_export_employee_mixin --> hr_employee : employee_id
hr_work_entry_export_employee_mixin .. hr_version : version_ids
hr_work_entry_export_employee_mixin .. hr_work_entry : work_entry_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Models]]

<!-- GENERATED:MODEL -->
