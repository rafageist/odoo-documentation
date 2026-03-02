<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Spreadsheet Test

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/test_spreadsheet_edition
- Dependencies: [[Odoo 19/Enterprise Addons/spreadsheet_edition/spreadsheet_edition|spreadsheet_edition]], [[Odoo 19/Community Addons/test_spreadsheet/test_spreadsheet|test_spreadsheet]]

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
!include ../../../Templates/DiagramStyles.puml
title Spreadsheet Test - Models and Relations
class SpreadsheetCellThread
class SpreadsheetTest
class "spreadsheet.test" as spreadsheet_test
SpreadsheetCellThread --> spreadsheet_test : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

