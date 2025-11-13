<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Proxy features for account_edi

- Version: v18
- Category: community
- Source: odoo/addons/account_edi_proxy_client
- Dependencies: [[Odoo 18/Community Addons/account/account|account]], [[Odoo 18/Community Addons/certificate/certificate|certificate]]
## XML Artifacts (detected)

- Views: 2
- Actions: 1
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 2

## Detected Models

- `account_edi_proxy_client.user`
- `Key`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Proxy features for account_edi - Models and Relations
class "account_edi_proxy_client.user" as account_edi_proxy_client_user
class Key
class ResCompany
class "res.company" as res_company
account_edi_proxy_client_user --> res_company : many2one
class "certificate.key" as certificate_key
account_edi_proxy_client_user --> certificate_key : many2one
ResCompany --|> account_edi_proxy_client_user : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
