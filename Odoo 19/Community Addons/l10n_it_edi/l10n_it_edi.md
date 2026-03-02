<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Italy - E-invoicing

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/l10n_it_edi
- Dependencies: [[Odoo 19/Community Addons/l10n_it/l10n_it|l10n_it]], [[Odoo 19/Community Addons/account_edi_proxy_client/account_edi_proxy_client|account_edi_proxy_client]], [[Odoo 19/Community Addons/account_debit_note/account_debit_note|account_debit_note]]

## XML Artifacts (detected)

- Views: 13
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `Account_Edi_Proxy_ClientUser`
- `AccountMove`
- `AccountPaymentMethodLine`
- `AccountTax`
- `l10n_it.ddt`
- `l10n_it.document.type`
- `ResCompany`
- `ResPartner`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Italy - E-invoicing - Models and Relations
class Account_Edi_Proxy_ClientUser
class AccountMove
class AccountPaymentMethodLine
class AccountTax
class "l10n_it.ddt" as l10n_it_ddt
class "l10n_it.document.type" as l10n_it_document_type
class ResCompany
class ResPartner
AccountMove --> l10n_it_ddt : many2one
AccountMove --> l10n_it_document_type : many2one
class "account.move" as account_move
l10n_it_ddt --|> account_move : one2many
class "account_edi_proxy_client.user" as account_edi_proxy_client_user
ResCompany --> account_edi_proxy_client_user : many2one
class "account.journal" as account_journal
ResCompany --> account_journal : many2one
class "res.country.state" as res_country_state
ResCompany --> res_country_state : many2one
class "res.partner" as res_partner
ResCompany --> res_partner : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


