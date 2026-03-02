<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Resource

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/resource
- Dependencies: base (not documented), [[Odoo 19/Community Addons/web/web|web]]

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
!include ../../../Templates/DiagramStyles.puml
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


