<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# France - Accounting

- Version: v18
- Category: community
- Source: odoo/addons/l10n_fr_account
- Dependencies: [[Odoo 18/Community Addons/base_iban/base_iban|base_iban]], [[Odoo 18/Community Addons/base_vat/base_vat|base_vat]], [[Odoo 18/Community Addons/account/account|account]], [[Odoo 18/Community Addons/l10n_fr/l10n_fr|l10n_fr]]
## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountMove`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title France - Accounting - Models and Relations
class AccountMove
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
