<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Spreadsheet Test

- Scope: Enterprise Addons
- Source: enterprise/test_spreadsheet_edition
- Dependencies: [[docs/Enterprise Addons/spreadsheet_edition/spreadsheet_edition|spreadsheet_edition]], [[docs/Community Addons/test_spreadsheet/test_spreadsheet|test_spreadsheet]]

## Summary

Spreadsheet Test, mainly to test the mixin behavior

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `SpreadsheetCellThread`
- `SpreadsheetTest`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Spreadsheet Test - Models and Relations
class SpreadsheetCellThread
class SpreadsheetTest
class "spreadsheet.test" as spreadsheet_test
SpreadsheetCellThread --> spreadsheet_test : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




