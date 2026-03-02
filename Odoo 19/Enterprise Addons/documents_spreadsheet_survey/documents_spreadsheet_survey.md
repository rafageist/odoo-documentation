<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Spreadsheet Survey

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/documents_spreadsheet_survey
- Dependencies: [[Odoo 19/Enterprise Addons/documents_spreadsheet/documents_spreadsheet|documents_spreadsheet]], [[Odoo 19/Community Addons/survey/survey|survey]]

## Summary

Spreadsheet for Survey results

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `Survey`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Spreadsheet Survey - Models and Relations
class Survey
class "documents.document" as documents_document
Survey --> documents_document : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

