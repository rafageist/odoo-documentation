<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Project Stock

- Scope: Community Addons
- Source: odoo/addons/project_stock
- Dependencies: [[docs/Community Addons/stock/stock|stock]], [[docs/Community Addons/project/project|project]]

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
!include ../../../templates/DiagramStyles.puml
title Project Stock - Models and Relations
class ProjectProject
class StockPicking
class "project.project" as project_project
StockPicking --> project_project : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





