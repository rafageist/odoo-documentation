<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Ecuadorian Accounting EDI

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_ec_edi
- Dependencies: [[Odoo 19/Community Addons/account_edi/account_edi|account_edi]], [[Odoo 19/Community Addons/certificate/certificate|certificate]], [[Odoo 19/Community Addons/l10n_ec/l10n_ec|l10n_ec]]

## XML Artifacts (detected)

- Views: 15
- Actions: 3
- Menus: 2
- Rules (ir.rule): 2
- Access CSV entries: 6

## Detected Models

- `AccountEdiFormat`
- `AccountJournal`
- `AccountMove`
- `AccountMoveLine`
- `AccountTax`
- `CertificateCertificate`
- `l10n_ec.reimbursement`
- `l10n_ec.taxpayer.type`
- `ProductTemplate`
- `ResCompany`
- `ResCountry`
- `ResPartner`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Ecuadorian Accounting EDI - Models and Relations
class AccountEdiFormat
class AccountJournal
class AccountMove
class AccountMoveLine
class AccountTax
class CertificateCertificate
class "l10n_ec.reimbursement" as l10n_ec_reimbursement
class "l10n_ec.taxpayer.type" as l10n_ec_taxpayer_type
class ProductTemplate
class ResCompany
class ResCountry
class ResPartner
class "account.move.line" as account_move_line
AccountMove .. account_move_line : many2many
AccountMove --|> account_move_line : one2many
class "account.move" as account_move
AccountMove .. account_move : many2many
AccountMove --|> l10n_ec_reimbursement : one2many
AccountMoveLine --> account_move : many2one
l10n_ec_reimbursement --> account_move : many2one
class "res.partner" as res_partner
l10n_ec_reimbursement --> res_partner : many2one
class "l10n_latam.identification.type" as l10n_latam_identification_type
l10n_ec_reimbursement --> l10n_latam_identification_type : many2one
class "res.country" as res_country
l10n_ec_reimbursement --> res_country : many2one
class "l10n_latam.document.type" as l10n_latam_document_type
l10n_ec_reimbursement --> l10n_latam_document_type : many2one
class "account.tax" as account_tax
l10n_ec_reimbursement --> account_tax : many2one
l10n_ec_taxpayer_type --> account_tax : many2one
l10n_ec_taxpayer_type --> account_tax : many2one
l10n_ec_taxpayer_type --> account_tax : many2one
ProductTemplate --> account_tax : many2one
class "certificate.certificate" as certificate_certificate
ResCompany --> certificate_certificate : many2one
ResCompany --> account_tax : many2one
ResCompany --> account_tax : many2one
ResCompany --> account_tax : many2one
class "account.account" as account_account
ResCompany --> account_account : many2one
ResCompany --> account_account : many2one
ResPartner --> l10n_ec_taxpayer_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

