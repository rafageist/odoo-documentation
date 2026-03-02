<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# spreadsheet.document.to.dashboard

- Module: [[docs/Enterprise Addons/spreadsheet_dashboard_documents/spreadsheet_dashboard_documents|spreadsheet_dashboard_documents]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/documents_to_dashboard.py`
- Python classes: `SpreadsheetDocumentToDashboard`
- Description: Create a dashboard from a spreadsheet document

## Field footprint

- Detected fields: 4
- Field types: `Char` x 1, `Many2many` x 1, `Many2one` x 2
- Relation fields: 3

## Sample fields

- `dashboard_group_id`: `Many2one` (comodel `spreadsheet.dashboard.group`)
- `document_id`: `Many2one` (comodel `documents.document`)
- `group_ids`: `Many2many` (comodel `res.groups`)
- `name`: `Char` (comodel `Dashboard Name`, compute `_compute_name`, store `True`)

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: `_compute_name`
- Onchange methods: none

## Direct relation diagram

```plantuml
@startuml
!define ODOO_COLOR_PRIMARY #714B67
!define ODOO_COLOR_ACCENT #875A7B
!define ODOO_COLOR_BG #FAF7FA

skinparam backgroundColor ODOO_COLOR_BG
skinparam defaultTextAlignment left
skinparam ArrowColor ODOO_COLOR_ACCENT
skinparam ClassBackgroundColor white
skinparam ClassBorderColor ODOO_COLOR_PRIMARY
skinparam ComponentBackgroundColor white
skinparam ComponentBorderColor ODOO_COLOR_PRIMARY
skinparam NoteBackgroundColor #FFF8FF
skinparam NoteBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBackgroundColor #FFFFFF
skinparam SequenceParticipantBorderColor ODOO_COLOR_PRIMARY
skinparam SequenceParticipantBackgroundColor #FFFFFF
skinparam sequence {
  ArrowColor ODOO_COLOR_ACCENT
  ActorBorderColor ODOO_COLOR_PRIMARY
}
title spreadsheet.document.to.dashboard - Direct Relations
class "spreadsheet.document.to.dashboard" as spreadsheet_document_to_dashboard
class "documents.document" as documents_document
class "res.groups" as res_groups
class "spreadsheet.dashboard.group" as spreadsheet_dashboard_group
spreadsheet_document_to_dashboard --> documents_document : document_id
spreadsheet_document_to_dashboard --> spreadsheet_dashboard_group : dashboard_group_id
spreadsheet_document_to_dashboard .. res_groups : group_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/spreadsheet_dashboard_documents/Models]]

<!-- GENERATED:MODEL -->
