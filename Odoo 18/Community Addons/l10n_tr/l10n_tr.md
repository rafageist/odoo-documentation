<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Türkiye - Accounting

- Version: v18
- Category: community
- Source: odoo/addons/l10n_tr
- Dependencies: [[Odoo 18/Community Addons/account/account|account]]
## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountJournal`
- `AccountMoveLine`
- `ProductTemplate`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Türkiye - Accounting - Models and Relations
class AccountJournal
class AccountMoveLine
class ProductTemplate
class "account.account" as account_account
AccountJournal --> account_account : many2one
ProductTemplate --> account_account : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
