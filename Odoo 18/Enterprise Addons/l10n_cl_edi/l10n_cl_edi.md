<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Chile - E-invoicing

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_cl_edi
- Dependencies: [[Odoo 18/Community Addons/l10n_cl/l10n_cl|l10n_cl]], [[Odoo 18/Community Addons/account_edi/account_edi|account_edi]], [[Odoo 18/Community Addons/account_debit_note/account_debit_note|account_debit_note]], [[Odoo 18/Community Addons/certificate/certificate|certificate]]
## XML Artifacts (detected)

- Views: 17
- Actions: 2
- Menus: 3
- Rules (ir.rule): 1
- Access CSV entries: 7

## Detected Models

- `AccountJournal`
- `account.move`
- `Certificate`
- `fetchmail.server`
- `l10n_cl.account.invoice.reference`
- `l10n_cl.company.activities`
- `l10n_cl.dte.caf`
- `L10nLatamDocumentType`
- `PaymentTerm`
- `ResCompany`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Chile - E-invoicing - Models and Relations
class AccountJournal
class "account.move" as account_move
class Certificate
class "fetchmail.server" as fetchmail_server
class "l10n_cl.account.invoice.reference" as l10n_cl_account_invoice_reference
class "l10n_cl.company.activities" as l10n_cl_company_activities
class "l10n_cl.dte.caf" as l10n_cl_dte_caf
class L10nLatamDocumentType
class PaymentTerm
class ResCompany
class ResPartner
class "ir.attachment" as ir_attachment
account_move --> ir_attachment : many2one
account_move --> ir_attachment : many2one
account_move --|> l10n_cl_account_invoice_reference : one2many
class "res.users" as res_users
Certificate --> res_users : many2one
class "l10n_latam.document.type" as l10n_latam_document_type
l10n_cl_account_invoice_reference --> l10n_latam_document_type : many2one
l10n_cl_account_invoice_reference --> account_move : many2one
l10n_cl_dte_caf --> l10n_latam_document_type : many2one
class "res.company" as res_company
l10n_cl_dte_caf --> res_company : many2one
L10nLatamDocumentType --|> l10n_cl_dte_caf : one2many
ResCompany .. l10n_cl_company_activities : many2many
class "certificate.certificate" as certificate_certificate
ResCompany --|> certificate_certificate : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
