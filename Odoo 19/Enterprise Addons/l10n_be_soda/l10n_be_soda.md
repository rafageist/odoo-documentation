<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Belgium - Import SODA files

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_be_soda
- Dependencies: [[Odoo 19/Enterprise Addons/accountant/accountant|accountant]], [[Odoo 19/Community Addons/l10n_be/l10n_be|l10n_be]]

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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

