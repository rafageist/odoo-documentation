<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# HR Org Chart

- Version: v18
- Category: community
- Source: odoo/addons/hr_org_chart
- Dependencies: [[Odoo 18/Community Addons/hr/hr|hr]], [[Odoo 18/Community Addons/web_hierarchy/web_hierarchy|web_hierarchy]]
## XML Artifacts (detected)

- Views: 8
- Actions: 5
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `Employee`
- `HrEmployeePublic`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title HR Org Chart - Models and Relations
class Employee
class HrEmployeePublic
class "hr.employee" as hr_employee
Employee --|> hr_employee : one2many
class "hr.employee.public" as hr_employee_public
HrEmployeePublic --|> hr_employee_public : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
