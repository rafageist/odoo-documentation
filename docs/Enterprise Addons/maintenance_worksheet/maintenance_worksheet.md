<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Worksheet for Maintenance

- Scope: Enterprise Addons
- Source: enterprise/maintenance_worksheet
- Dependencies: [[docs/Community Addons/maintenance/maintenance|maintenance]], [[docs/Enterprise Addons/worksheet/worksheet|worksheet]]

## Summary

Create custom worksheets for Maintenance

## XML Artifacts (detected)

- Views: 1
- Actions: 3
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 2

## Detected Models

- `MaintenanceRequest`
- `WorksheetTemplate`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Worksheet for Maintenance - Models and Relations
class MaintenanceRequest
class WorksheetTemplate
class "worksheet.template" as worksheet_template
MaintenanceRequest --> worksheet_template : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



