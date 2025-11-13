<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Spreadsheet dashboard edition

- Version: v18
- Category: enterprise
- Source: enterprise18/spreadsheet_dashboard_edition
- Dependencies: [[Odoo 18/Community Addons/spreadsheet_dashboard/spreadsheet_dashboard|spreadsheet_dashboard]], [[Odoo 18/Enterprise Addons/spreadsheet_edition/spreadsheet_edition|spreadsheet_edition]]

## Summary

Spreadsheet Dashboard edition

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 0

## Detected Models

- `SpreadsheetCellThread`
- `spreadsheet.dashboard`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Spreadsheet dashboard edition - Models and Relations
class SpreadsheetCellThread
class "spreadsheet.dashboard" as spreadsheet_dashboard
SpreadsheetCellThread --> spreadsheet_dashboard : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
