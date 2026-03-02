<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Field Service Reports

- Scope: Enterprise Addons
- Source: enterprise/industry_fsm_report
- Dependencies: [[docs/Enterprise Addons/worksheet/worksheet|worksheet]], [[docs/Enterprise Addons/industry_fsm/industry_fsm|industry_fsm]], [[docs/Enterprise Addons/web_studio/web_studio|web_studio]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




