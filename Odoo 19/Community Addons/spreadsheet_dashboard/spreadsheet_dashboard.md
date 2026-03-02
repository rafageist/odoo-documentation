<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Spreadsheet dashboard

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/spreadsheet_dashboard
- Dependencies: [[Odoo 19/Community Addons/spreadsheet/spreadsheet|spreadsheet]]

## Summary

Spreadsheet

## XML Artifacts (detected)

- Views: 5
- Actions: 2
- Menus: 4
- Rules (ir.rule): 4
- Access CSV entries: 5

## Detected Models

- `spreadsheet.dashboard`
- `spreadsheet.dashboard.group`
- `spreadsheet.dashboard.share`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Spreadsheet dashboard - Models and Relations
class "spreadsheet.dashboard" as spreadsheet_dashboard
class "spreadsheet.dashboard.group" as spreadsheet_dashboard_group
class "spreadsheet.dashboard.share" as spreadsheet_dashboard_share
spreadsheet_dashboard --> spreadsheet_dashboard_group : many2one
class "res.company" as res_company
spreadsheet_dashboard .. res_company : many2many
class "res.groups" as res_groups
spreadsheet_dashboard .. res_groups : many2many
class "res.users" as res_users
spreadsheet_dashboard .. res_users : many2many
class "ir.model" as ir_model
spreadsheet_dashboard .. ir_model : many2many
spreadsheet_dashboard_group --|> spreadsheet_dashboard : one2many
spreadsheet_dashboard_group --|> spreadsheet_dashboard : one2many
spreadsheet_dashboard_share --> spreadsheet_dashboard : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

