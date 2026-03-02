<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Remote Work

- Scope: Community Addons
- Source: odoo/addons/hr_homeworking
- Dependencies: [[docs/Community Addons/hr/hr|hr]]

## XML Artifacts (detected)

- Views: 5
- Actions: 0
- Menus: 0
- Rules (ir.rule): 2
- Access CSV entries: 2

## Detected Models

- `HrEmployee`
- `HrEmployeePublic`
- `hr.employee.location`
- `HrWorkLocation`
- `ResPartner`
- `ResUsers`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Remote Work - Models and Relations
class HrEmployee
class HrEmployeePublic
class "hr.employee.location" as hr_employee_location
class HrWorkLocation
class ResPartner
class ResUsers
class "hr.work.location" as hr_work_location
HrEmployee --> hr_work_location : many2one
HrEmployee --> hr_work_location : many2one
HrEmployee --> hr_work_location : many2one
HrEmployee --> hr_work_location : many2one
HrEmployee --> hr_work_location : many2one
HrEmployee --> hr_work_location : many2one
HrEmployee --> hr_work_location : many2one
HrEmployee --> hr_work_location : many2one
HrEmployeePublic --> hr_work_location : many2one
HrEmployeePublic --> hr_work_location : many2one
HrEmployeePublic --> hr_work_location : many2one
HrEmployeePublic --> hr_work_location : many2one
HrEmployeePublic --> hr_work_location : many2one
HrEmployeePublic --> hr_work_location : many2one
HrEmployeePublic --> hr_work_location : many2one
hr_employee_location --> hr_work_location : many2one
class "hr.employee" as hr_employee
hr_employee_location --> hr_employee : many2one
ResUsers --> hr_work_location : many2one
ResUsers --> hr_work_location : many2one
ResUsers --> hr_work_location : many2one
ResUsers --> hr_work_location : many2one
ResUsers --> hr_work_location : many2one
ResUsers --> hr_work_location : many2one
ResUsers --> hr_work_location : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





