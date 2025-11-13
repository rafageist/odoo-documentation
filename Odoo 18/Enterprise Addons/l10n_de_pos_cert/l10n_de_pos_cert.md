<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Germany - Certification for Point of Sale

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_de_pos_cert
- Dependencies: [[Odoo 18/Community Addons/l10n_de/l10n_de|l10n_de]], [[Odoo 18/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[Odoo 18/Community Addons/iap/iap|iap]]

## Summary

Germany TSS Regulation

## XML Artifacts (detected)

- Views: 7
- Actions: 1
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 1

## Detected Models

- `l10n_de_pos.dsfinvk_export`
- `PosConfig`
- `PosOrder`
- `PosSession`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Germany - Certification for Point of Sale - Models and Relations
class "l10n_de_pos.dsfinvk_export" as l10n_de_pos_dsfinvk_export
class PosConfig
class PosOrder
class PosSession
class ResCompany
class "pos.config" as pos_config
l10n_de_pos_dsfinvk_export --> pos_config : many2one
class "res.company" as res_company
l10n_de_pos_dsfinvk_export --> res_company : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
