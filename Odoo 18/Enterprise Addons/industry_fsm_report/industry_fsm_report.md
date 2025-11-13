<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Field Service Reports

- Version: v18
- Category: enterprise
- Source: enterprise18/industry_fsm_report
- Dependencies: [[Odoo 18/Enterprise Addons/worksheet/worksheet|worksheet]], [[Odoo 18/Enterprise Addons/industry_fsm/industry_fsm|industry_fsm]], [[Odoo 18/Enterprise Addons/web_studio/web_studio|web_studio]]

## Summary

Create Reports for Field service workers

## XML Artifacts (detected)

- Views: 24
- Actions: 23
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

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
