<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Italy - E-invoicing

- Version: v18
- Category: community
- Source: odoo/addons/l10n_it_edi
- Dependencies: [[Odoo 18/Community Addons/l10n_it/l10n_it|l10n_it]], [[Odoo 18/Community Addons/account_edi_proxy_client/account_edi_proxy_client|account_edi_proxy_client]]
## XML Artifacts (detected)

- Views: 9
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountEdiProxyClientUser`
- `AccountMove`
- `l10n_it.ddt`
- `IrAttachment`
- `res.company`
- `res.partner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Italy - E-invoicing - Models and Relations
class AccountEdiProxyClientUser
class AccountMove
class "l10n_it.ddt" as l10n_it_ddt
class IrAttachment
class "res.company" as res_company
class "res.partner" as res_partner
class "ir.attachment" as ir_attachment
AccountMove --> ir_attachment : many2one
AccountMove --> l10n_it_ddt : many2one
class "account.move" as account_move
l10n_it_ddt --|> account_move : one2many
class "account_edi_proxy_client.user" as account_edi_proxy_client_user
res_company --> account_edi_proxy_client_user : many2one
class "res.country.state" as res_country_state
res_company --> res_country_state : many2one
res_company --> res_partner : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
