<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Spreadsheet dashboard edition

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/spreadsheet_dashboard_edition
- Dependencies: [[Odoo 19/Community Addons/spreadsheet_dashboard/spreadsheet_dashboard|spreadsheet_dashboard]], [[Odoo 19/Enterprise Addons/spreadsheet_edition/spreadsheet_edition|spreadsheet_edition]]

## Summary

Spreadsheet Dashboard edition

## XML Artifacts (detected)

- Views: 3
- Actions: 1
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

