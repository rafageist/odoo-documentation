<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Spreadsheet Test

- Version: v18
- Category: enterprise
- Source: enterprise18/test_spreadsheet_edition
- Dependencies: [[Odoo 18/Enterprise Addons/spreadsheet_edition/spreadsheet_edition|spreadsheet_edition]], [[Odoo 18/Community Addons/test_spreadsheet/test_spreadsheet|test_spreadsheet]]

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
- `SpreadsheetDummy`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Spreadsheet Test - Models and Relations
class SpreadsheetCellThread
class SpreadsheetDummy
class "spreadsheet.test" as spreadsheet_test
SpreadsheetCellThread --> spreadsheet_test : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
