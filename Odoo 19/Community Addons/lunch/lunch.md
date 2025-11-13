<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Lunch

- Version: v19
- Category: community
- Source: odoo19/addons/lunch
- Dependencies: [[Odoo 19/Community Addons/mail/mail|mail]]

## Summary

Handle lunch orders of your employees

## XML Artifacts (detected)

- Views: 39
- Actions: 17
- Menus: 17
- Rules (ir.rule): 10
- Access CSV entries: 17

## Detected Models

- `lunch.alert`
- `lunch.cashmove`
- `lunch.location`
- `lunch.order`
- `lunch.product`
- `lunch.product.category`
- `lunch.supplier`
- `lunch.topping`
- `ResCompany`
- `ResUsers`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Lunch - Models and Relations
class "lunch.alert" as lunch_alert
class "lunch.cashmove" as lunch_cashmove
class "lunch.location" as lunch_location
class "lunch.order" as lunch_order
class "lunch.product" as lunch_product
class "lunch.product.category" as lunch_product_category
class "lunch.supplier" as lunch_supplier
class "lunch.topping" as lunch_topping
class ResCompany
class ResUsers
class "ir.cron" as ir_cron
lunch_alert --> ir_cron : many2one
lunch_alert .. lunch_location : many2many
class "res.currency" as res_currency
lunch_cashmove --> res_currency : many2one
class "res.users" as res_users
lunch_cashmove --> res_users : many2one
class "res.company" as res_company
lunch_location --> res_company : many2one
lunch_order .. lunch_topping : many2many
lunch_order .. lunch_topping : many2many
lunch_order .. lunch_topping : many2many
lunch_order --> lunch_product : many2one
lunch_order --> res_users : many2one
lunch_order --> lunch_location : many2one
lunch_order --> res_company : many2one
lunch_product --> lunch_product_category : many2one
lunch_product --> lunch_supplier : many2one
lunch_product --> res_company : many2one
lunch_product --> res_currency : many2one
lunch_product .. res_users : many2many
lunch_product --> lunch_location : many2one
lunch_product_category --> res_company : many2one
lunch_product_category --> res_currency : many2one
class "res.partner" as res_partner
lunch_supplier --> res_partner : many2one
class "res.country.state" as res_country_state
lunch_supplier --> res_country_state : many2one
class "res.country" as res_country
lunch_supplier --> res_country : many2one
lunch_supplier --> res_company : many2one
lunch_supplier --> res_users : many2one
lunch_supplier --> ir_cron : many2one
lunch_supplier .. lunch_location : many2many
lunch_supplier --|> lunch_topping : one2many
lunch_supplier --|> lunch_topping : one2many
lunch_supplier --|> lunch_topping : one2many
lunch_topping --> res_company : many2one
lunch_topping --> res_currency : many2one
lunch_topping --> lunch_supplier : many2one
ResUsers --> lunch_location : many2one
ResUsers .. lunch_product : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
