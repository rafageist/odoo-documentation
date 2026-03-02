<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Mexico - Accounting

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/l10n_mx
- Dependencies: [[Odoo 19/Community Addons/account/account|account]]

## XML Artifacts (detected)

- Views: 7
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountAccount`
- `AccountMoveLine`
- `AccountTax`
- `ResBank`
- `ResPartnerBank`
- `ResCompany`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Mexico - Accounting - Models and Relations
class AccountAccount
class AccountMoveLine
class AccountTax
class ResBank
class ResPartnerBank
class ResCompany
class "account.account" as account_account
ResCompany --> account_account : many2one
ResCompany --> account_account : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


