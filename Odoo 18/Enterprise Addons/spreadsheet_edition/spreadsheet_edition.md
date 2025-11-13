<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Spreadsheet

- Version: v18
- Category: enterprise
- Source: enterprise18/spreadsheet_edition
- Dependencies: [[Odoo 18/Community Addons/spreadsheet/spreadsheet|spreadsheet]], [[Odoo 18/Community Addons/mail/mail|mail]], [[Odoo 18/Enterprise Addons/web_enterprise/web_enterprise|web_enterprise]]

## Summary

Spreadsheet

## XML Artifacts (detected)

- Views: 2
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `IrModel`
- `spreadsheet.cell.thread`
- `spreadsheet.revision`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Spreadsheet - Models and Relations
class IrModel
class "spreadsheet.cell.thread" as spreadsheet_cell_thread
class "spreadsheet.revision" as spreadsheet_revision
spreadsheet_revision --> spreadsheet_revision : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
