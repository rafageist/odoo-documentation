<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Gelato

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/sale_gelato
- Dependencies: [[Odoo 19/Community Addons/sale/sale|sale]], [[Odoo 19/Community Addons/delivery/delivery|delivery]]

## Summary

Place orders through Gelato's print-on-demand service

## XML Artifacts (detected)

- Views: 6
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ProviderGelato`
- `ProductDocument`
- `ProductProduct`
- `ProductTemplate`
- `ResCompany`
- `ResPartner`
- `SaleOrder`
- `SaleOrderLine`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Gelato - Models and Relations
class ProviderGelato
class ProductDocument
class ProductProduct
class ProductTemplate
class ResCompany
class ResPartner
class SaleOrder
class SaleOrderLine
class "product.document" as product_document
ProductTemplate --|> product_document : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


