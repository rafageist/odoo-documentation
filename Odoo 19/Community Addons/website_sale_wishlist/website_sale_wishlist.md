<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Shopper's Wishlist

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/website_sale_wishlist
- Dependencies: [[Odoo 19/Community Addons/website_sale/website_sale|website_sale]]

## Summary

Allow shoppers to enlist products

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 2
- Access CSV entries: 4

## Detected Models

- `product.wishlist`
- `ResPartner`
- `ProductTemplate`
- `ProductProduct`
- `ResUsers`
- `Website`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Shopper's Wishlist - Models and Relations
class "product.wishlist" as product_wishlist
class ResPartner
class ProductTemplate
class ProductProduct
class ResUsers
class Website
class "res.partner" as res_partner
product_wishlist --> res_partner : many2one
class "product.product" as product_product
product_wishlist --> product_product : many2one
class "res.currency" as res_currency
product_wishlist --> res_currency : many2one
class "product.pricelist" as product_pricelist
product_wishlist --> product_pricelist : many2one
class website
product_wishlist --> website : many2one
ResPartner --|> product_wishlist : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

