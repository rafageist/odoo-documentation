<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Germany - Certification for Point of Sale

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_de_pos_cert
- Dependencies: [[Odoo 19/Community Addons/l10n_de/l10n_de|l10n_de]], [[Odoo 19/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[Odoo 19/Community Addons/iap/iap|iap]]

## Summary

Germany TSS Regulation

## XML Artifacts (detected)

- Views: 8
- Actions: 1
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 1

## Detected Models

- `AccountTax`
- `l10n_de_pos.dsfinvk_export`
- `PosConfig`
- `PosOrder`
- `PosOrderLine`
- `PosPaymentMethod`
- `PosSession`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Germany - Certification for Point of Sale - Models and Relations
class AccountTax
class "l10n_de_pos.dsfinvk_export" as l10n_de_pos_dsfinvk_export
class PosConfig
class PosOrder
class PosOrderLine
class PosPaymentMethod
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
