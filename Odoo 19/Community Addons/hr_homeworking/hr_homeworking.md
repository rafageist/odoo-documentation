<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Remote Work

- Version: v19
- Category: community
- Source: odoo19/addons/hr_homeworking
- Dependencies: [[Odoo 19/Community Addons/hr/hr|hr]]
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
!include ../../../Templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
