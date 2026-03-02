<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Spreadsheet

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/spreadsheet_edition
- Dependencies: [[Odoo 19/Community Addons/spreadsheet/spreadsheet|spreadsheet]], [[Odoo 19/Community Addons/mail/mail|mail]], [[Odoo 19/Enterprise Addons/web_enterprise/web_enterprise|web_enterprise]]

## Summary

Spreadsheet

## XML Artifacts (detected)

- Views: 2
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `spreadsheet.cell.thread`
- `spreadsheet.revision`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Spreadsheet - Models and Relations
class "spreadsheet.cell.thread" as spreadsheet_cell_thread
class "spreadsheet.revision" as spreadsheet_revision
spreadsheet_revision --> spreadsheet_revision : many2one
class "res.users" as res_users
spreadsheet_revision --> res_users : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

