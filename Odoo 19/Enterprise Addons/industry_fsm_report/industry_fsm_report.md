<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Field Service Reports

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/industry_fsm_report
- Dependencies: [[Odoo 19/Enterprise Addons/worksheet/worksheet|worksheet]], [[Odoo 19/Enterprise Addons/industry_fsm/industry_fsm|industry_fsm]], [[Odoo 19/Enterprise Addons/web_studio/web_studio|web_studio]]

## Summary

Create Reports for Field service technicians

## XML Artifacts (detected)

- Views: 23
- Actions: 25
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 3

## Detected Models

- `IrModel`
- `ProjectProject`
- `ProjectTask`
- `ProjectTaskRecurrence`
- `WorksheetTemplate`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Field Service Reports - Models and Relations
class IrModel
class ProjectProject
class ProjectTask
class ProjectTaskRecurrence
class WorksheetTemplate
class "worksheet.template" as worksheet_template
ProjectProject --> worksheet_template : many2one
ProjectTask --> worksheet_template : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

