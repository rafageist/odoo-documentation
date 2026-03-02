<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Estonia - Accounting

- Scope: Community Addons
- Source: odoo/addons/l10n_ee
- Dependencies: [[docs/Community Addons/account/account|account]], [[docs/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]]

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountTax`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Estonia - Accounting - Models and Relations
class AccountTax
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





