<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Germany - Certification for Point of Sale

- Scope: Enterprise Addons
- Source: enterprise/l10n_de_pos_cert
- Dependencies: [[docs/Community Addons/l10n_de/l10n_de|l10n_de]], [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[docs/Community Addons/iap/iap|iap]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



