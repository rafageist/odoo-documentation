<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# HR Org Chart

- Scope: Community Addons
- Source: odoo/addons/hr_org_chart
- Dependencies: [[docs/Community Addons/hr/hr|hr]], [[docs/Community Addons/web_hierarchy/web_hierarchy|web_hierarchy]]

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
!include ../../../templates/DiagramStyles.puml
title HR Org Chart - Models and Relations
class HrEmployee
class HrEmployeePublic
class "hr.employee" as hr_employee
HrEmployee --|> hr_employee : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





