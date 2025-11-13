<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Belgium - Import SODA files

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_be_soda
- Dependencies: [[Odoo 18/Enterprise Addons/account_accountant/account_accountant|account_accountant]], [[Odoo 18/Community Addons/l10n_be/l10n_be|l10n_be]]
## XML Artifacts (detected)

- Views: 4
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountJournal`
- `AccountMove`
- `AccountMoveLine`
- `soda.account.mapping`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Belgium - Import SODA files - Models and Relations
class AccountJournal
class AccountMove
class AccountMoveLine
class "soda.account.mapping" as soda_account_mapping
class "res.company" as res_company
soda_account_mapping --> res_company : many2one
class "account.account" as account_account
soda_account_mapping --> account_account : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
