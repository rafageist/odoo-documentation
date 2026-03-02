<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Web

- Scope: Community Addons
- Source: odoo/addons/web
- Dependencies: base (not documented)

## XML Artifacts (detected)

- Views: 2
- Actions: 5
- Menus: 0
- Rules (ir.rule): 2
- Access CSV entries: 2

## Detected Models

- `IrModel`
- `IrUiMenu`
- `IrUiView`
- `ResCompany`
- `PropertiesBaseDefinition`
- `ResPartner`
- `ResUsers`
- `ResUsersSettings`
- `res.users.settings.embedded.action`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Web - Models and Relations
class IrModel
class IrUiMenu
class IrUiView
class ResCompany
class PropertiesBaseDefinition
class ResPartner
class ResUsers
class ResUsersSettings
class "res.users.settings.embedded.action" as res_users_settings_embedded_action
ResUsersSettings --|> res_users_settings_embedded_action : one2many
class "res.users.settings" as res_users_settings
res_users_settings_embedded_action --> res_users_settings : many2one
class "ir.actions.act_window" as ir_actions_act_window
res_users_settings_embedded_action --> ir_actions_act_window : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



