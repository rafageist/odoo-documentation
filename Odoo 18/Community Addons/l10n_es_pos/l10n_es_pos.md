<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Spain - Point of Sale

- Version: v18
- Category: community
- Source: odoo/addons/l10n_es_pos
- Dependencies: [[Odoo 18/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[Odoo 18/Community Addons/l10n_es/l10n_es|l10n_es]]

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

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
