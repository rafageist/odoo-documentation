<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Resource

- Scope: Community Addons
- Source: odoo/addons/resource
- Dependencies: base (not documented), [[docs/Community Addons/web/web|web]]

## XML Artifacts (detected)

- Views: 12
- Actions: 7
- Menus: 4
- Rules (ir.rule): 5
- Access CSV entries: 8

## Detected Models

- `resource.calendar`
- `resource.calendar.attendance`
- `resource.calendar.leaves`
- `resource.resource`
- `ResCompany`
- `ResUsers`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Resource - Models and Relations
class "resource.calendar" as resource_calendar
class "resource.calendar.attendance" as resource_calendar_attendance
class "resource.calendar.leaves" as resource_calendar_leaves
class "resource.resource" as resource_resource
class ResCompany
class ResUsers
resource_calendar --|> resource_calendar_attendance : one2many
resource_calendar --|> resource_calendar_attendance : one2many
resource_calendar --|> resource_calendar_attendance : one2many
class "res.company" as res_company
resource_calendar --> res_company : many2one
resource_calendar --|> resource_calendar_leaves : one2many
resource_calendar --|> resource_calendar_leaves : one2many
resource_calendar_attendance --> resource_calendar : many2one
resource_calendar_leaves --> res_company : many2one
resource_calendar_leaves --> resource_calendar : many2one
resource_calendar_leaves --> resource_resource : many2one
resource_resource --> res_company : many2one
class "res.users" as res_users
resource_resource --> res_users : many2one
resource_resource --> resource_calendar : many2one
ResCompany --|> resource_calendar : one2many
ResCompany --> resource_calendar : many2one
ResUsers --|> resource_resource : one2many
ResUsers --> resource_calendar : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





