<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Kenya - Accounting

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/l10n_ke
- Dependencies: [[Odoo 19/Community Addons/account/account|account]]

## XML Artifacts (detected)

- Views: 5
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountMove`
- `AccountTax`
- `l10n_ke.item.code`
- `ResCompany`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Kenya - Accounting - Models and Relations
class AccountMove
class AccountTax
class "l10n_ke.item.code" as l10n_ke_item_code
class ResCompany
AccountTax --> l10n_ke_item_code : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


