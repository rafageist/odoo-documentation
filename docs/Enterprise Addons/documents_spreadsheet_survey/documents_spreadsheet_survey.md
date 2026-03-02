<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Spreadsheet Survey

- Scope: Enterprise Addons
- Source: enterprise/documents_spreadsheet_survey
- Dependencies: [[docs/Enterprise Addons/documents_spreadsheet/documents_spreadsheet|documents_spreadsheet]], [[docs/Community Addons/survey/survey|survey]]

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
!include ../../../templates/DiagramStyles.puml
title Spreadsheet Survey - Models and Relations
class Survey
class "documents.document" as documents_document
Survey --> documents_document : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




