<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# HR Org Chart

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/hr_org_chart
- Dependencies: [[Odoo 19/Community Addons/hr/hr|hr]], [[Odoo 19/Community Addons/web_hierarchy/web_hierarchy|web_hierarchy]]

## XML Artifacts (detected)

- Views: 7
- Actions: 6
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HrEmployee`
- `HrEmployeePublic`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title HR Org Chart - Models and Relations
class HrEmployee
class HrEmployeePublic
class "hr.employee" as hr_employee
HrEmployee --|> hr_employee : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


