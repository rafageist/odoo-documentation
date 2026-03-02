<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Malaysia - E-invoicing

- Scope: Community Addons
- Source: odoo/addons/l10n_my_edi
- Dependencies: [[docs/Community Addons/l10n_my/l10n_my|l10n_my]], [[docs/Community Addons/l10n_my_ubl_pint/l10n_my_ubl_pint|l10n_my_ubl_pint]], [[docs/Community Addons/account_edi_proxy_client/account_edi_proxy_client|account_edi_proxy_client]]

## Summary

E-invoicing using MyInvois

## XML Artifacts (detected)

- Views: 12
- Actions: 2
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 7

## Detected Models

- `AccountEdiProxyClientUser`
- `AccountMove`
- `AccountMoveLine`
- `AccountTax`
- `l10n_my_edi.industry_classification`
- `myinvois.document`
- `ProductTemplate`
- `ResCompany`
- `ResPartner`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Malaysia - E-invoicing - Models and Relations
class AccountEdiProxyClientUser
class AccountMove
class AccountMoveLine
class AccountTax
class "l10n_my_edi.industry_classification" as l10n_my_edi_industry_classification
class "myinvois.document" as myinvois_document
class ProductTemplate
class ResCompany
class ResPartner
AccountMove .. myinvois_document : many2many
class "res.company" as res_company
myinvois_document --> res_company : many2one
class "res.currency" as res_currency
myinvois_document --> res_currency : many2one
class "ir.attachment" as ir_attachment
myinvois_document --> ir_attachment : many2one
class "account.move" as account_move
myinvois_document .. account_move : many2many
class "account_edi_proxy_client.user" as account_edi_proxy_client_user
ResCompany --> account_edi_proxy_client_user : many2one
class "account.journal" as account_journal
ResCompany --> account_journal : many2one
ResPartner --> l10n_my_edi_industry_classification : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





