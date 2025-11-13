<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Malaysia - E-invoicing

- Version: v18
- Category: community
- Source: odoo/addons/l10n_my_edi
- Dependencies: [[Odoo 18/Community Addons/l10n_my/l10n_my|l10n_my]], [[Odoo 18/Community Addons/l10n_my_ubl_pint/l10n_my_ubl_pint|l10n_my_ubl_pint]], [[Odoo 18/Community Addons/account_edi_proxy_client/account_edi_proxy_client|account_edi_proxy_client]]

## Summary

E-invoicing using MyInvois

## XML Artifacts (detected)

- Views: 9
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 6

## Detected Models

- `AccountEdiProxyClientUser`
- `AccountMove`
- `AccountTax`
- `l10n_my_edi.industry_classification`
- `ProductTemplate`
- `ResCompany`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Malaysia - E-invoicing - Models and Relations
class AccountEdiProxyClientUser
class AccountMove
class AccountTax
class "l10n_my_edi.industry_classification" as l10n_my_edi_industry_classification
class ProductTemplate
class ResCompany
class ResPartner
class "ir.attachment" as ir_attachment
AccountMove --> ir_attachment : many2one
class "account_edi_proxy_client.user" as account_edi_proxy_client_user
ResCompany --> account_edi_proxy_client_user : many2one
ResCompany --> l10n_my_edi_industry_classification : many2one
class "account.journal" as account_journal
ResCompany --> account_journal : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
