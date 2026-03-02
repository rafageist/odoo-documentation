<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Electronic invoicing for Colombia with DIAN

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_co_dian
- Dependencies: [[Odoo 19/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]], [[Odoo 19/Enterprise Addons/l10n_co_edi/l10n_co_edi|l10n_co_edi]], [[Odoo 19/Community Addons/certificate/certificate|certificate]]

## Summary

Colombian Localization for EDI documents

## XML Artifacts (detected)

- Views: 11
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 5

## Detected Models

- `AccountJournal`
- `AccountMove`
- `AccountMoveLine`
- `CertificateCertificate`
- `l10n_co_dian.document`
- `l10n_co_dian.operation_mode`
- `MailTemplate`
- `ResCompany`
- `ResPartner`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Electronic invoicing for Colombia with DIAN - Models and Relations
class AccountJournal
class AccountMove
class AccountMoveLine
class CertificateCertificate
class "l10n_co_dian.document" as l10n_co_dian_document
class "l10n_co_dian.operation_mode" as l10n_co_dian_operation_mode
class MailTemplate
class ResCompany
class ResPartner
AccountMove --|> l10n_co_dian_document : one2many
class "ir.attachment" as ir_attachment
AccountMove --> ir_attachment : many2one
l10n_co_dian_document --> ir_attachment : many2one
class "account.move" as account_move
l10n_co_dian_document --> account_move : many2one
class "res.company" as res_company
l10n_co_dian_operation_mode --> res_company : many2one
ResCompany --|> l10n_co_dian_operation_mode : one2many
class "certificate.certificate" as certificate_certificate
ResCompany --|> certificate_certificate : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

