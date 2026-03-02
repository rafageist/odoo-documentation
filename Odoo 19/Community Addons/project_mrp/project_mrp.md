<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# MRP Project

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/project_mrp
- Dependencies: [[Odoo 19/Community Addons/mrp/mrp|mrp]], [[Odoo 19/Community Addons/project/project|project]]

## Summary

Monitor MRP using project

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `MrpBom`
- `MrpProduction`
- `ProjectProject`
- `StockRule`
- `StockMove`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title MRP Project - Models and Relations
class MrpBom
class MrpProduction
class ProjectProject
class StockRule
class StockMove
class "project.project" as project_project
MrpBom --> project_project : many2one
MrpProduction --> project_project : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


