<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Worksheet for Maintenance

- Version: v19
- Category: enterprise
- Source: enterprise19/maintenance_worksheet
- Dependencies: [[Odoo 19/Community Addons/maintenance/maintenance|maintenance]], [[Odoo 19/Enterprise Addons/worksheet/worksheet|worksheet]]

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
!include ../../../Templates/DiagramStyles.puml
title Worksheet for Maintenance - Models and Relations
class MaintenanceRequest
class WorksheetTemplate
class "worksheet.template" as worksheet_template
MaintenanceRequest --> worksheet_template : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
