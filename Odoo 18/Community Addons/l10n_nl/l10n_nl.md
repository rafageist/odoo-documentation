<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Netherlands - Accounting

- Version: v18
- Category: community
- Source: odoo/addons/l10n_nl
- Dependencies: [[Odoo 18/Community Addons/base_iban/base_iban|base_iban]], [[Odoo 18/Community Addons/base_vat/base_vat|base_vat]], [[Odoo 18/Community Addons/account/account|account]]
## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountJournal`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Netherlands - Accounting - Models and Relations
class AccountJournal
class ResCompany
class "account.account" as account_account
ResCompany --> account_account : many2one
ResCompany --> account_account : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
