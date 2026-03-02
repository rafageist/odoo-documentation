<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# documents.account.folder.setting

- Module: [[docs/Enterprise Addons/documents_account/documents_account|documents_account]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/documents_account_folder_setting.py`
- Python classes: `DocumentsAccountFolderSetting`
- Description: Journal and Folder settings

## Field footprint

- Detected fields: 5
- Field types: `Many2many` x 1, `Many2one` x 4
- Relation fields: 5

## Sample fields

- `company_account_folder_id`: `Many2one` (related `company_id.account_folder_id`)
- `company_id`: `Many2one` (comodel `res.company`)
- `folder_id`: `Many2one` (comodel `documents.document`)
- `journal_id`: `Many2one` (comodel `account.journal`)
- `tag_ids`: `Many2many` (comodel `documents.tag`)

## Method hints

- Detected methods: 0
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
title documents.account.folder.setting - Direct Relations
class "documents.account.folder.setting" as documents_account_folder_setting
class "account.journal" as account_journal
class "documents.document" as documents_document
class "documents.tag" as documents_tag
class "res.company" as res_company
documents_account_folder_setting --> res_company : company_id
documents_account_folder_setting --> account_journal : journal_id
documents_account_folder_setting --> documents_document : folder_id
documents_account_folder_setting .. documents_tag : tag_ids
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/documents_account/Models]]

<!-- GENERATED:MODEL -->
