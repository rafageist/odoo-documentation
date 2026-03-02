<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# hr.leave.attendance.report

- Module: [[docs/Community Addons/hr_holidays_attendance/hr_holidays_attendance|hr_holidays_attendance]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `report/hr_leave_attendance_report.py`
- Python classes: `HrLeaveAttendanceReport`
- Description: Attendance and Leave Analysis Report

## Field footprint

- Detected fields: 13
- Field types: `Boolean` x 1, `Char` x 1, `Date` x 1, `Float` x 4, `Many2many` x 2, `Many2one` x 4
- Relation fields: 6

## Sample fields

- `active`: `Boolean` (related `employee_id.active`)
- `attendance_ids`: `Many2many` (comodel `hr.attendance`, compute `_compute_leave_attendance_fields`)
- `date`: `Date` (comodel `Date`)
- `department_id`: `Many2one` (related `employee_id.department_id`)
- `difference_hours`: `Float` (comodel `Difference`)
- `employee_id`: `Many2one` (comodel `hr.employee`)
- `expected_hours`: `Float` (comodel `Expected Hours`)
- `job_id`: `Many2one` (related `employee_id.job_id`)
- `leave_hours`: `Float` (comodel `Approved Time Off`)
- `leave_ids`: `Many2many` (comodel `hr.leave`, compute `_compute_leave_attendance_fields`)
- `leave_type_names`: `Char` (comodel `Time Off Types`, compute `_compute_leave_attendance_fields`)
- `schedule_id`: `Many2one` (comodel `resource.calendar`)
- `worked_hours`: `Float` (comodel `Worked Hours`)

## Method hints

- Detected methods: 13
- Action methods: none
- Compute methods: `_compute_display_name`, `_compute_leave_attendance_fields`
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
title hr.leave.attendance.report - Direct Relations
class "hr.leave.attendance.report" as hr_leave_attendance_report
class "hr.attendance" as hr_attendance
class "hr.employee" as hr_employee
class "hr.leave" as hr_leave
class "resource.calendar" as resource_calendar
hr_leave_attendance_report --> hr_employee : employee_id
hr_leave_attendance_report --> resource_calendar : schedule_id
hr_leave_attendance_report .. hr_leave : leave_ids
hr_leave_attendance_report .. hr_attendance : attendance_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/hr_holidays_attendance/Models]]

<!-- GENERATED:MODEL -->
