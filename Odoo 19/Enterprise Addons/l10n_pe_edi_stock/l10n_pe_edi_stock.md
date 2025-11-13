<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Peruvian - Electronic Delivery Note

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_pe_edi_stock
- Dependencies: [[Odoo 19/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[Odoo 19/Enterprise Addons/l10n_pe_edi/l10n_pe_edi|l10n_pe_edi]]

## Summary

Electronic Delivery Note for Peru (OSE method) and UBL 2.1

## XML Artifacts (detected)

- Views: 7
- Actions: 2
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 2

## Detected Models

- `l10n_pe_edi.vehicle`
- `ProductTemplate`
- `ResCompany`
- `ResPartner`
- `StockPicking`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Peruvian - Electronic Delivery Note - Models and Relations
class "l10n_pe_edi.vehicle" as l10n_pe_edi_vehicle
class ProductTemplate
class ResCompany
class ResPartner
class StockPicking
class "res.partner" as res_partner
l10n_pe_edi_vehicle --> res_partner : many2one
class "res.company" as res_company
l10n_pe_edi_vehicle --> res_company : many2one
StockPicking --> l10n_pe_edi_vehicle : many2one
StockPicking --> res_partner : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
