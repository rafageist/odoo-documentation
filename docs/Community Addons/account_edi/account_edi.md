<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Import/Export Invoices From XML/PDF

- Scope: Community Addons
- Source: odoo/addons/account_edi
- Dependencies: [[docs/Community Addons/account/account|account]]

## XML Artifacts (detected)

- Views: 8
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `account.edi.document`
- `account.edi.format`
- `AccountJournal`
- `AccountMove`
- `IrActionsReport`
- `IrAttachment`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Import/Export Invoices From XML/PDF - Models and Relations
class "account.edi.document" as account_edi_document
class "account.edi.format" as account_edi_format
class AccountJournal
class AccountMove
class IrActionsReport
class IrAttachment
class "account.move" as account_move
account_edi_document --> account_move : many2one
account_edi_document --> account_edi_format : many2one
class "ir.attachment" as ir_attachment
account_edi_document --> ir_attachment : many2one
AccountJournal .. account_edi_format : many2many
AccountJournal .. account_edi_format : many2many
AccountMove --|> account_edi_document : one2many
@enduml
```

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


