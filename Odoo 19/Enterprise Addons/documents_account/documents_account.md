<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Documents - Accounting

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/documents_account
- Dependencies: [[Odoo 19/Enterprise Addons/documents/documents|documents]], [[Odoo 19/Enterprise Addons/account_reports/account_reports|account_reports]]

## Summary

Invoices from Documents

## XML Artifacts (detected)

- Views: 10
- Actions: 20
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 2

## Detected Models

- `AccountJournal`
- `account.move`
- `AccountReport`
- `documents.account.folder.setting`
- `DocumentsDocument`
- `IrActionsServer`
- `IrAttachment`
- `ResCompany`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Documents - Accounting - Models and Relations
class AccountJournal
class "account.move" as account_move
class AccountReport
class "documents.account.folder.setting" as documents_account_folder_setting
class DocumentsDocument
class IrActionsServer
class IrAttachment
class ResCompany
class "account.bank.statement.line" as account_bank_statement_line
account_move --> account_bank_statement_line : many2one
class "res.company" as res_company
documents_account_folder_setting --> res_company : many2one
class "account.journal" as account_journal
documents_account_folder_setting --> account_journal : many2one
class "documents.document" as documents_document
documents_account_folder_setting --> documents_document : many2one
class "documents.tag" as documents_tag
documents_account_folder_setting .. documents_tag : many2many
IrActionsServer --> account_journal : many2one
IrActionsServer .. account_journal : many2many
ResCompany --> documents_document : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

