<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Türkiye - Accounting

- Scope: Community Addons
- Source: odoo/addons/l10n_tr
- Dependencies: [[docs/Community Addons/account/account|account]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





