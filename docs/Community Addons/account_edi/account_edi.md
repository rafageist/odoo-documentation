<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Import/Export Invoices From XML/PDF

- Scope: Community Addons
- Source: odoo/addons/account_edi
- Dependencies: [[docs/Community Addons/account/account|account]]

## Generated coverage

- Models: 8
- XML files with UI/data artifacts: 3
- Views: 8
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 4
- Controller units: 0
- Frontend asset files: 0

## Module map

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
title Import/Export Invoices From XML/PDF - Generated Coverage
component "Module Overview" as overview
component "Models\n8" as models
component "Views / XML\n8 views\n3 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n4 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/account_edi/Models|Models]] (8)
- Views and XML: [[docs/Community Addons/account_edi/Views|Views]] (3 files)

## Key models

- `account.edi.document`
- `account.edi.format`
- `account.journal`
- `account.move`
- `account.move.send`
- `account.resequence.wizard`
- `ir.actions.report`
- `ir.attachment`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





## Curated analysis

### Functional role
- Provides the generic EDI document lifecycle used by invoice export and vendor-bill import before country-specific addons plug in their own formats.
- `account.edi.document` tracks status, attachment linkage, and retries per move, while `account.edi.format` defines the pluggable contract used by downstream localization modules.

### Operational footprint
- Extends `account.move`, `account.journal`, `ir.attachment`, `ir.actions.report`, and `account.move.send`, so posting and sending invoices can create or refresh EDI artifacts automatically.
- `data/cron.xml` schedules network retries and asynchronous work for formats that should not finish inside the posting transaction.

### Evidence
- Source files: `odoo19/addons/account_edi/models/account_edi_document.py`, `odoo19/addons/account_edi/models/account_edi_format.py`, `odoo19/addons/account_edi/models/account_move.py`
- UI and automation: `odoo19/addons/account_edi/views/account_move_views.xml`, `odoo19/addons/account_edi/views/account_journal_views.xml`, `odoo19/addons/account_edi/data/cron.xml`
- Tests: `odoo19/addons/account_edi/tests/test_edi.py`, `odoo19/addons/account_edi/tests/test_import_vendor_bill.py`

### Related notes
- `[[docs/Community Addons/account/account|account]]`
- `[[docs/Core/Infrastructure/Files]]`

### Risks and follow-up
- Journal configuration and format-specific addons decide whether a document is emitted synchronously or stays pending for cron retry.
- Support teams need to inspect both the invoice and the related EDI documents because provider failures surface in the EDI state machine, not only in accounting UI messages.
- Legacy comparison backlog was retired on 2026-03-02; keep this note focused on the current codebase.


