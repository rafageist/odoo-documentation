<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Electronic invoicing for Colombia with DIAN

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_co_dian
- Dependencies: [[Odoo 18/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]], [[Odoo 18/Enterprise Addons/l10n_co_edi/l10n_co_edi|l10n_co_edi]], [[Odoo 18/Community Addons/certificate/certificate|certificate]]

## Summary

Colombian Localization for EDI documents

## XML Artifacts (detected)

- Views: 8
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `AccountJournal`
- `AccountMove`
- `AccountMoveLine`
- `Certificate`
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
class Certificate
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

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
