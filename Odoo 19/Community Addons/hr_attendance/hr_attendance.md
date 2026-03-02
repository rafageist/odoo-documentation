<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Attendances

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/hr_attendance
- Dependencies: [[Odoo 19/Community Addons/hr/hr|hr]], [[Odoo 19/Community Addons/barcodes/barcodes|barcodes]], [[Odoo 19/Community Addons/base_geolocalize/base_geolocalize|base_geolocalize]]

## Summary

Track employee attendance

## XML Artifacts (detected)

- Views: 22
- Actions: 11
- Menus: 12
- Rules (ir.rule): 4
- Access CSV entries: 8

## Detected Models

- `hr.attendance`
- `hr.attendance.overtime.line`
- `hr.attendance.overtime.rule`
- `hr.attendance.overtime.ruleset`
- `HrEmployee`
- `HrEmployeePublic`
- `hr.version`
- `ResCompany`
- `ResUsers`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Attendances - Models and Relations
class "hr.attendance" as hr_attendance
class "hr.attendance.overtime.line" as hr_attendance_overtime_line
class "hr.attendance.overtime.rule" as hr_attendance_overtime_rule
class "hr.attendance.overtime.ruleset" as hr_attendance_overtime_ruleset
class HrEmployee
class HrEmployeePublic
class "hr.version" as hr_version
class ResCompany
class ResUsers
class "hr.employee" as hr_employee
hr_attendance --> hr_employee : many2one
class "hr.department" as hr_department
hr_attendance --> hr_department : many2one
hr_attendance --> hr_employee : many2one
class "res.users" as res_users
hr_attendance --> res_users : many2one
hr_attendance .. hr_attendance_overtime_line : many2many
hr_attendance_overtime_line --> hr_employee : many2one
hr_attendance_overtime_line .. hr_attendance_overtime_rule : many2many
class "resource.calendar" as resource_calendar
hr_attendance_overtime_rule --> resource_calendar : many2one
hr_attendance_overtime_rule --> hr_attendance_overtime_ruleset : many2one
hr_attendance_overtime_ruleset --|> hr_attendance_overtime_rule : one2many
class "res.company" as res_company
hr_attendance_overtime_ruleset --> res_company : many2one
class "res.country" as res_country
hr_attendance_overtime_ruleset --> res_country : many2one
HrEmployee --> res_users : many2one
HrEmployee --|> hr_attendance : one2many
HrEmployee --> hr_attendance : many2one
HrEmployee --|> hr_attendance_overtime_line : one2many
hr_version --> hr_attendance_overtime_ruleset : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

## Curated analysis

### Functional role
- `hr_attendance` covers employee check-in and check-out, but in practice it is also the kiosk entry point, a barcode-enabled device flow, and the base for overtime computation.
- The overtime models and rulesets turn raw punches into policy-aware attendance outcomes that HR managers can audit and correct.

### Operational footprint
- `hr_attendance.py` and the overtime model files drive employee state, worked hours, extra-hours logic, and auto-check-out behavior.
- The public kiosk flow is exposed through `controllers/main.py`, while `data/hr_attendance_data.xml` schedules automatic check-out and absence handling.

### Evidence
- Source files: `odoo19/addons/hr_attendance/models/hr_attendance.py`, `odoo19/addons/hr_attendance/models/hr_attendance_overtime_rule.py`, `odoo19/addons/hr_attendance/models/hr_attendance_overtime_ruleset.py`
- UI, security, and automation: `odoo19/addons/hr_attendance/views/hr_attendance_view.xml`, `odoo19/addons/hr_attendance/security/hr_attendance_security.xml`, `odoo19/addons/hr_attendance/data/hr_attendance_data.xml`
- Tests: `odoo19/addons/hr_attendance/tests/test_hr_attendance_process.py`, `odoo19/addons/hr_attendance/tests/test_hr_attendance_overtime.py`, `odoo19/addons/hr_attendance/tests/test_hr_attendance_kiosk.py`

### Related notes
- `[[Odoo 19/Community Addons/hr/hr|hr]]`
- `[[Odoo 19/Core/Infrastructure/Security]]`

### Risks and follow-up
- Timezone handling, kiosk devices, and overtime thresholds are the failure hotspots; they need to be validated together, not in isolation.
- Shared or public kiosks require extra care around user identification, barcode devices, and access groups because the module exposes both HR and operational data.
- Odoo 18 comparison backlog was retired on 2026-03-02; keep this note focused on Odoo 19 behavior.


