<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# base.automation

- Module: [[docs/Enterprise Addons/ai_documents/ai_documents|ai_documents]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/base_automation.py`
- Python classes: `BaseAutomation`

## Field footprint

- Detected fields: 1
- Field types: `Many2one` x 1
- Relation fields: 1

## Sample fields

- `ai_autosort_folder_id`: `Many2one` (comodel `documents.document`)

## Method hints

- Detected methods: 1
- Action methods: none
- Compute methods: none
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
title base.automation - Direct Relations
class "base.automation" as base_automation
class "documents.document" as documents_document
base_automation --> documents_document : ai_autosort_folder_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/ai_documents/Models]]

<!-- GENERATED:MODEL -->
