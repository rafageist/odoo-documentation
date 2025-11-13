<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Project Planning

- Version: v18
- Category: enterprise
- Source: enterprise18/project_forecast
- Dependencies: [[Odoo 18/Community Addons/project/project|project]], [[Odoo 18/Enterprise Addons/planning/planning|planning]], [[Odoo 18/Enterprise Addons/web_grid/web_grid|web_grid]]

## Summary

Plan your resources on project tasks

## XML Artifacts (detected)

- Views: 16
- Actions: 23
- Menus: 2
- Rules (ir.rule): 3
- Access CSV entries: 0

## Detected Models

- `PlanningTemplate`
- `Project`
- `PlanningShift`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Project Planning - Models and Relations
class PlanningTemplate
class Project
class PlanningShift
class "project.project" as project_project
PlanningTemplate --> project_project : many2one
class "res.company" as res_company
PlanningTemplate --> res_company : many2one
PlanningShift --> project_project : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
