<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Spreadsheet dashboard

- Version: v18
- Category: community
- Source: odoo/addons/spreadsheet_dashboard
- Dependencies: [[Odoo 18/Community Addons/spreadsheet/spreadsheet|spreadsheet]]

## Summary

Spreadsheet

## XML Artifacts (detected)

- Views: 4
- Actions: 2
- Menus: 4
- Rules (ir.rule): 3
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
spreadsheet_dashboard --> res_company : many2one
class "res.groups" as res_groups
spreadsheet_dashboard .. res_groups : many2many
class "ir.model" as ir_model
spreadsheet_dashboard .. ir_model : many2many
spreadsheet_dashboard_group --|> spreadsheet_dashboard : one2many
spreadsheet_dashboard_group --|> spreadsheet_dashboard : one2many
spreadsheet_dashboard_share --> spreadsheet_dashboard : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
