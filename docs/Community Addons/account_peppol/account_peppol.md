<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Peppol

- Scope: Community Addons
- Source: odoo/addons/account_peppol
- Dependencies: [[docs/Community Addons/account_edi_proxy_client/account_edi_proxy_client|account_edi_proxy_client]], [[docs/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





