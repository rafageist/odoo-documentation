<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Project Stock

- Version: v18
- Category: community
- Source: odoo/addons/project_stock
- Dependencies: [[Odoo 18/Community Addons/stock/stock|stock]], [[Odoo 18/Community Addons/project/project|project]]

## Summary

Link Stock pickings to Project

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ProjectProject`
- `StockPicking`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Project Stock - Models and Relations
class ProjectProject
class StockPicking
class "project.project" as project_project
StockPicking --> project_project : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
