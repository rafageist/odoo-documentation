<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Peppol

- Version: v18
- Category: community
- Source: odoo/addons/account_peppol
- Dependencies: [[Odoo 18/Community Addons/account_edi_proxy_client/account_edi_proxy_client|account_edi_proxy_client]], [[Odoo 18/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]]

## Summary

This module is used to send/receive documents with PEPPOL

## XML Artifacts (detected)

- Views: 9
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `AccountEdiProxyClientUser`
- `AccountJournal`
- `AccountMove`
- `ResCompany`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Peppol - Models and Relations
class AccountEdiProxyClientUser
class AccountJournal
class AccountMove
class ResCompany
class ResPartner
class "account.journal" as account_journal
ResCompany --> account_journal : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
