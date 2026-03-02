<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Documents Spreadsheet

- Scope: Enterprise Addons
- Source: enterprise/documents_spreadsheet
- Dependencies: [[docs/Enterprise Addons/documents/documents|documents]], [[docs/Enterprise Addons/spreadsheet_edition/spreadsheet_edition|spreadsheet_edition]], [[docs/Community Addons/base_import/base_import|base_import]]

## Summary

Documents Spreadsheet

## XML Artifacts (detected)

- Views: 10
- Actions: 3
- Menus: 2
- Rules (ir.rule): 7
- Access CSV entries: 3

## Detected Models

- `DocumentsAccess`
- `documents.document`
- `SpreadsheetCellThread`
- `spreadsheet.contributor`
- `spreadsheet.template`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Documents Spreadsheet - Models and Relations
class DocumentsAccess
class "documents.document" as documents_document
class SpreadsheetCellThread
class "spreadsheet.contributor" as spreadsheet_contributor
class "spreadsheet.template" as spreadsheet_template
SpreadsheetCellThread --> documents_document : many2one
SpreadsheetCellThread --> spreadsheet_template : many2one
spreadsheet_contributor --> documents_document : many2one
class "res.users" as res_users
spreadsheet_contributor --> res_users : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



