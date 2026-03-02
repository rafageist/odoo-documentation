<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# l10n_be.hr.payroll.schedule.change.wizard

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/l10n_be_hr_payroll_schedule_change_wizard.py`
- Python classes: `L10n_BeHrPayrollScheduleChangeWizard`
- Description: Change contract working schedule

## Field footprint

- Detected fields: 22
- Field types: `Boolean` x 3, `Date` x 2, `Float` x 4, `Many2one` x 10, `Monetary` x 3
- Relation fields: 10

## Sample fields

- `company_id`: `Many2one` (related `version_id.company_id`)
- `currency_id`: `Many2one` (related `company_id.currency_id`)
- `current_resource_calendar_id`: `Many2one` (comodel `resource.calendar`, related `version_id.resource_calendar_id`)
- `current_wage`: `Monetary` (comodel `Wage`, compute `_compute_wages`, store `True`)
- `date_end`: `Date` (comodel `End Date`)
- `date_start`: `Date` (comodel `Start Date`)
- `employee_id`: `Many2one` (related `version_id.employee_id`)
- `found_leave_allocation`: `Boolean` (compute `_compute_leave_allocation_id`)
- `full_resource_calendar_id`: `Many2one` (comodel `resource.calendar`, related `structure_type_id.default_resource_calendar_id`)
- `full_time_off_allocation`: `Float` (compute `_compute_full_time_off_allocation`)
- `full_wage`: `Monetary` (comodel `Full Time Equivalent Wage`, compute `_compute_wages`, store `True`)
- `initial_time_off_allocation`: `Float` (compute `_compute_leave_allocation_id`)
- `leave_allocation_id`: `Many2one` (comodel `hr.leave.allocation`, compute `_compute_leave_allocation_id`)
- `leave_type_id`: `Many2one` (comodel `hr.leave.type`)
- `previous_contract_creation`: `Boolean` (comodel `Post Change Contract Creation`)
- `requires_new_contract`: `Boolean` (compute `_compute_requires_new_contract`)
- `resource_calendar_id`: `Many2one` (comodel `resource.calendar`)
- `structure_type_id`: `Many2one` (related `version_id.structure_type_id`)
- `time_off_allocation`: `Float` (compute `_compute_time_off_allocation`, store `True`)
- `version_id`: `Many2one` (comodel `hr.version`)

## Method hints

- Detected methods: 8
- Action methods: `action_validate`
- Compute methods: `_compute_full_time_off_allocation`, `_compute_leave_allocation_id`, `_compute_new_allocation`, `_compute_requires_new_contract`, `_compute_time_off_allocation`, `_compute_wages`
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
title l10n_be.hr.payroll.schedule.change.wizard - Direct Relations
class "l10n_be.hr.payroll.schedule.change.wizard" as l10n_be_hr_payroll_schedule_change_wizard
class "hr.leave.allocation" as hr_leave_allocation
class "hr.leave.type" as hr_leave_type
class "hr.version" as hr_version
class "resource.calendar" as resource_calendar
l10n_be_hr_payroll_schedule_change_wizard --> hr_version : version_id
l10n_be_hr_payroll_schedule_change_wizard --> resource_calendar : full_resource_calendar_id
l10n_be_hr_payroll_schedule_change_wizard --> resource_calendar : current_resource_calendar_id
l10n_be_hr_payroll_schedule_change_wizard --> resource_calendar : resource_calendar_id
l10n_be_hr_payroll_schedule_change_wizard --> hr_leave_type : leave_type_id
l10n_be_hr_payroll_schedule_change_wizard --> hr_leave_allocation : leave_allocation_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll/Models]]

<!-- GENERATED:MODEL -->
