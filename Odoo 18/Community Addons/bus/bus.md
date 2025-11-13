<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# IM Bus

- Version: v18
- Category: community
- Source: odoo/addons/bus
- Dependencies: base (not documented), [[Odoo 18/Community Addons/web/web|web]]
## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `bus.bus`
- `bus.presence`
- `ir.attachment`
- `IrModel`
- `res.groups`
- `res.partner`
- `res.users`
- `res.users.settings`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title IM Bus - Models and Relations
class "bus.bus" as bus_bus
class "bus.presence" as bus_presence
class "ir.attachment" as ir_attachment
class IrModel
class "res.groups" as res_groups
class "res.partner" as res_partner
class "res.users" as res_users
class "res.users.settings" as res_users_settings
bus_presence --> res_users : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
