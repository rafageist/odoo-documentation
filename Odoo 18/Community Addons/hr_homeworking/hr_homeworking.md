<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Remote Work

- Version: v18
- Category: community
- Source: odoo/addons/hr_homeworking
- Dependencies: [[Odoo 18/Community Addons/hr/hr|hr]]
## XML Artifacts (detected)

- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 2
- Access CSV entries: 2

## Detected Models

- `hr.employee.location`
- `WorkLocation`
- `ResPartner`
- `User`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Remote Work - Models and Relations
class "hr.employee.location" as hr_employee_location
class WorkLocation
class ResPartner
class User
class "hr.work.location" as hr_work_location
hr_employee_location --> hr_work_location : many2one
class "hr.employee" as hr_employee
hr_employee_location --> hr_employee : many2one
User --> hr_work_location : many2one
User --> hr_work_location : many2one
User --> hr_work_location : many2one
User --> hr_work_location : many2one
User --> hr_work_location : many2one
User --> hr_work_location : many2one
User --> hr_work_location : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
