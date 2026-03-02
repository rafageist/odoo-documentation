<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Project Planning

- Scope: Enterprise Addons
- Source: enterprise/project_forecast
- Dependencies: [[docs/Community Addons/project/project|project]], [[docs/Enterprise Addons/planning/planning|planning]], [[docs/Enterprise Addons/web_grid/web_grid|web_grid]]

## Summary

Plan your resources on project tasks

## XML Artifacts (detected)

- Views: 16
- Actions: 23
- Menus: 2
- Rules (ir.rule): 3
- Access CSV entries: 0

## Detected Models

- `PlanningSlot`
- `PlanningSlotTemplate`
- `ProjectProject`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Project Planning - Models and Relations
class PlanningSlot
class PlanningSlotTemplate
class ProjectProject
class "project.project" as project_project
PlanningSlot --> project_project : many2one
PlanningSlotTemplate --> project_project : many2one
class "res.company" as res_company
PlanningSlotTemplate --> res_company : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



