<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Spreadsheet dashboard edition

- Scope: Enterprise Addons
- Source: enterprise/spreadsheet_dashboard_edition
- Dependencies: [[docs/Community Addons/spreadsheet_dashboard/spreadsheet_dashboard|spreadsheet_dashboard]], [[docs/Enterprise Addons/spreadsheet_edition/spreadsheet_edition|spreadsheet_edition]]

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
!include ../../../templates/DiagramStyles.puml
title Spreadsheet dashboard edition - Models and Relations
class SpreadsheetCellThread
class "spreadsheet.dashboard" as spreadsheet_dashboard
SpreadsheetCellThread --> spreadsheet_dashboard : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



