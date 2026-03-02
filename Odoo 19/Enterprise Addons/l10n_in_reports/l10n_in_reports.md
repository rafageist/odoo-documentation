<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Indian - Accounting Reports

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_in_reports
- Dependencies: [[Odoo 19/Community Addons/l10n_in/l10n_in|l10n_in]], [[Odoo 19/Enterprise Addons/account_reports/account_reports|account_reports]], [[Odoo 19/Enterprise Addons/accountant/accountant|accountant]], [[Odoo 19/Enterprise Addons/account_batch_payment/account_batch_payment|account_batch_payment]], [[Odoo 19/Community Addons/barcodes/barcodes|barcodes]], [[Odoo 19/Enterprise Addons/account_invoice_extract/account_invoice_extract|account_invoice_extract]]

## XML Artifacts (detected)

- Views: 15
- Actions: 3
- Menus: 3
- Rules (ir.rule): 0
- Access CSV entries: 7

## Detected Models

- `AccountBatchPayment`
- `AccountJournal`
- `AccountMove`
- `AccountPayment`
- `AccountPaymentMethod`
- `AccountReturnType`
- `AccountReturn`
- `AccountReturnCheck`
- `enet.bank.template`
- `l10n_in.gstr.document.summary.line`
- `IrAttachment`
- `AccountReport`
- `ResCompany`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Indian - Accounting Reports - Models and Relations
class AccountBatchPayment
class AccountJournal
class AccountMove
class AccountPayment
class AccountPaymentMethod
class AccountReturnType
class AccountReturn
class AccountReturnCheck
class "enet.bank.template" as enet_bank_template
class "l10n_in.gstr.document.summary.line" as l10n_in_gstr_document_summary_line
class IrAttachment
class AccountReport
class ResCompany
class "ir.attachment" as ir_attachment
AccountBatchPayment .. ir_attachment : many2many
AccountJournal --> enet_bank_template : many2one
class "account.return" as account_return
AccountMove --> account_return : many2one
AccountReturn --|> l10n_in_gstr_document_summary_line : one2many
AccountReturn .. ir_attachment : many2many
AccountReturn .. ir_attachment : many2many
l10n_in_gstr_document_summary_line --> account_return : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

