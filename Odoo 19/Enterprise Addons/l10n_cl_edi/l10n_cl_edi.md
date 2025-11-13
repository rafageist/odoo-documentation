<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Chile - E-invoicing

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_cl_edi
- Dependencies: [[Odoo 19/Community Addons/l10n_cl/l10n_cl|l10n_cl]], [[Odoo 19/Community Addons/account_edi/account_edi|account_edi]], [[Odoo 19/Community Addons/account_debit_note/account_debit_note|account_debit_note]], [[Odoo 19/Community Addons/certificate/certificate|certificate]]
## XML Artifacts (detected)

- Views: 17
- Actions: 3
- Menus: 3
- Rules (ir.rule): 1
- Access CSV entries: 7

## Detected Models

- `AccountJournal`
- `account.move`
- `CertificateCertificate`
- `FetchmailServer`
- `l10n_cl.company.activities`
- `l10n_cl.dte.caf`
- `l10n_cl.edi.reference`
- `L10n_LatamDocumentType`
- `AccountPaymentTerm`
- `ResCompany`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Chile - E-invoicing - Models and Relations
class AccountJournal
class "account.move" as account_move
class CertificateCertificate
class FetchmailServer
class "l10n_cl.company.activities" as l10n_cl_company_activities
class "l10n_cl.dte.caf" as l10n_cl_dte_caf
class "l10n_cl.edi.reference" as l10n_cl_edi_reference
class L10n_LatamDocumentType
class AccountPaymentTerm
class ResCompany
class ResPartner
class "ir.attachment" as ir_attachment
account_move --> ir_attachment : many2one
account_move --> ir_attachment : many2one
account_move --|> l10n_cl_edi_reference : one2many
class "res.users" as res_users
CertificateCertificate --> res_users : many2one
class "l10n_latam.document.type" as l10n_latam_document_type
l10n_cl_dte_caf --> l10n_latam_document_type : many2one
class "res.company" as res_company
l10n_cl_dte_caf --> res_company : many2one
l10n_cl_edi_reference --> l10n_latam_document_type : many2one
l10n_cl_edi_reference --> account_move : many2one
L10n_LatamDocumentType --|> l10n_cl_dte_caf : one2many
ResCompany .. l10n_cl_company_activities : many2many
class "certificate.certificate" as certificate_certificate
ResCompany --|> certificate_certificate : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
