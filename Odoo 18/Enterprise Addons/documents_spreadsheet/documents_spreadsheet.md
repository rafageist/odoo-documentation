<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Documents Spreadsheet

- Version: v18
- Category: enterprise
- Source: enterprise18/documents_spreadsheet
- Dependencies: [[Odoo 18/Enterprise Addons/documents/documents|documents]], [[Odoo 18/Enterprise Addons/spreadsheet_edition/spreadsheet_edition|spreadsheet_edition]]

## Summary

Documents Spreadsheet

## XML Artifacts (detected)

- Views: 9
- Actions: 3
- Menus: 2
- Rules (ir.rule): 7
- Access CSV entries: 3

## Detected Models

- `DocumentAccess`
- `documents.document`
- `ResCompany`
- `SpreadsheetCellThread`
- `spreadsheet.contributor`
- `spreadsheet.template`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Documents Spreadsheet - Models and Relations
class DocumentAccess
class "documents.document" as documents_document
class ResCompany
class SpreadsheetCellThread
class "spreadsheet.contributor" as spreadsheet_contributor
class "spreadsheet.template" as spreadsheet_template
ResCompany --> documents_document : many2one
SpreadsheetCellThread --> documents_document : many2one
SpreadsheetCellThread --> spreadsheet_template : many2one
spreadsheet_contributor --> documents_document : many2one
class "res.users" as res_users
spreadsheet_contributor --> res_users : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
