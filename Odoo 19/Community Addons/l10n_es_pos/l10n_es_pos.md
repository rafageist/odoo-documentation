<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Spain - Point of Sale

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/l10n_es_pos
- Dependencies: [[Odoo 19/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[Odoo 19/Community Addons/l10n_es/l10n_es|l10n_es]]

## Summary

Spanish localization for Point of Sale

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `PosConfig`
- `PosOrder`
- `ResCompany`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Spain - Point of Sale - Models and Relations
class AccountMove
class PosConfig
class PosOrder
class ResCompany
class "account.journal" as account_journal
PosConfig --> account_journal : many2one
class "res.partner" as res_partner
PosConfig --> res_partner : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


