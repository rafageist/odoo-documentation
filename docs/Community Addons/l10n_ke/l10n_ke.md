<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Kenya - Accounting

- Scope: Community Addons
- Source: odoo/addons/l10n_ke
- Dependencies: [[docs/Community Addons/account/account|account]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





