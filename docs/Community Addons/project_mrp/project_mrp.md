<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# MRP Project

- Scope: Community Addons
- Source: odoo/addons/project_mrp
- Dependencies: [[docs/Community Addons/mrp/mrp|mrp]], [[docs/Community Addons/project/project|project]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





