<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Peppol

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/account_peppol
- Dependencies: [[Odoo 19/Community Addons/account_edi_proxy_client/account_edi_proxy_client|account_edi_proxy_client]], [[Odoo 19/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]]

## Summary

This module is used to send/receive documents with PEPPOL

## XML Artifacts (detected)

- Views: 8
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `Account_Edi_Proxy_ClientUser`
- `AccountJournal`
- `AccountMove`
- `ResCompany`
- `ResPartner`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Peppol - Models and Relations
class Account_Edi_Proxy_ClientUser
class AccountJournal
class AccountMove
class ResCompany
class ResPartner
class "account_edi_proxy_client.user" as account_edi_proxy_client_user
ResCompany --> account_edi_proxy_client_user : many2one
class "account.journal" as account_journal
ResCompany --> account_journal : many2one
class "res.company" as res_company
ResCompany --> res_company : many2one
ResCompany --> account_journal : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


