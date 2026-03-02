<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# l10n_be.schedule.change.allocation

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll/l10n_be_hr_payroll|l10n_be_hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/l10n_be_schedule_change_allocation.py`
- Python classes: `L10n_BeScheduleChangeAllocation`
- Description: Update allocation on schedule change

## Field footprint

- Detected fields: 6
- Field types: `Date` x 1, `Float` x 1, `Many2one` x 4
- Relation fields: 4

## Sample fields

- `current_resource_calendar_id`: `Many2one` (comodel `resource.calendar`)
- `effective_date`: `Date`
- `leave_allocation_id`: `Many2one` (comodel `hr.leave.allocation`)
- `maximum_days`: `Float`
- `new_resource_calendar_id`: `Many2one` (comodel `resource.calendar`)
- `version_id`: `Many2one` (comodel `hr.version`)

## Method hints

- Detected methods: 2
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
title l10n_be.schedule.change.allocation - Direct Relations
class "l10n_be.schedule.change.allocation" as l10n_be_schedule_change_allocation
class "hr.leave.allocation" as hr_leave_allocation
class "hr.version" as hr_version
class "resource.calendar" as resource_calendar
l10n_be_schedule_change_allocation --> hr_version : version_id
l10n_be_schedule_change_allocation --> hr_leave_allocation : leave_allocation_id
l10n_be_schedule_change_allocation --> resource_calendar : current_resource_calendar_id
l10n_be_schedule_change_allocation --> resource_calendar : new_resource_calendar_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll/Models]]

<!-- GENERATED:MODEL -->
