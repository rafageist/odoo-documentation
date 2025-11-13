<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Subscriptions

- Version: v19
- Category: enterprise
- Source: enterprise19/sale_subscription
- Dependencies: [[Odoo 19/Enterprise Addons/account_accountant/account_accountant|account_accountant]], [[Odoo 19/Community Addons/sale_management/sale_management|sale_management]], [[Odoo 19/Community Addons/portal/portal|portal]], [[Odoo 19/Enterprise Addons/web_cohort/web_cohort|web_cohort]], [[Odoo 19/Community Addons/rating/rating|rating]], [[Odoo 19/Community Addons/sms/sms|sms]]

## Summary

Generate recurring invoices and manage renewals

## XML Artifacts (detected)

- Views: 53
- Actions: 45
- Menus: 22
- Rules (ir.rule): 9
- Access CSV entries: 19

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `PaymentProvider`
- `PaymentToken`
- `PaymentTransaction`
- `ProductPricelist`
- `ProductPricelistItem`
- `ProductProduct`
- `ProductTemplate`
- `ResPartner`
- `sale.order`
- `sale.order.close.reason`
- `SaleOrderLine`
- `sale.order.log`
- `SaleOrderTemplate`
- `SaleOrderTemplateLine`
- `sale.subscription.plan`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Subscriptions - Models and Relations
class AccountMove
class AccountMoveLine
class PaymentProvider
class PaymentToken
class PaymentTransaction
class ProductPricelist
class ProductPricelistItem
class ProductProduct
class ProductTemplate
class ResPartner
class "sale.order" as sale_order
class "sale.order.close.reason" as sale_order_close_reason
class SaleOrderLine
class "sale.order.log" as sale_order_log
class SaleOrderTemplate
class SaleOrderTemplateLine
class "sale.subscription.plan" as sale_subscription_plan
AccountMoveLine --> sale_order : many2one
class "product.pricelist.item" as product_pricelist_item
ProductPricelist --|> product_pricelist_item : one2many
ProductPricelistItem --> sale_subscription_plan : many2one
ProductProduct --|> product_pricelist_item : one2many
ProductTemplate --|> product_pricelist_item : one2many
ProductTemplate --|> product_pricelist_item : one2many
sale_order --> sale_subscription_plan : many2one
sale_order --> sale_order : many2one
sale_order --> sale_order : many2one
sale_order --|> sale_order : one2many
sale_order --> sale_order_close_reason : many2one
class "payment.token" as payment_token
sale_order --> payment_token : many2one
class "res.users" as res_users
sale_order --> res_users : many2one
class "res.partner" as res_partner
sale_order --> res_partner : many2one
sale_order --|> sale_order_log : one2many
sale_order --> sale_order : many2one
sale_order .. res_users : many2many
class "sale.order.line" as sale_order_line
SaleOrderLine --> sale_order_line : many2one
sale_order_log --> sale_order : many2one
sale_order_log --> res_users : many2one
class "crm.team" as crm_team
sale_order_log --> crm_team : many2one
sale_order_log --> sale_subscription_plan : many2one
class "res.company" as res_company
sale_order_log --> res_company : many2one
class "res.currency" as res_currency
sale_order_log --> res_currency : many2one
sale_order_log --> sale_order : many2one
SaleOrderTemplate --> sale_subscription_plan : many2one
sale_subscription_plan --> res_company : many2one
sale_subscription_plan .. sale_subscription_plan : many2many
class "mail.template" as mail_template
sale_subscription_plan --> mail_template : many2one
sale_subscription_plan --|> product_pricelist_item : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
