<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Mexico - Accounting

- Scope: Community Addons
- Source: odoo/addons/l10n_mx
- Dependencies: [[docs/Community Addons/account/account|account]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





