<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Subscriptions

- Version: v18
- Category: enterprise
- Source: enterprise18/sale_subscription
- Dependencies: [[Odoo 18/Enterprise Addons/account_accountant/account_accountant|account_accountant]], [[Odoo 18/Community Addons/sale_management/sale_management|sale_management]], [[Odoo 18/Community Addons/portal/portal|portal]], [[Odoo 18/Enterprise Addons/web_cohort/web_cohort|web_cohort]], [[Odoo 18/Community Addons/rating/rating|rating]], [[Odoo 18/Community Addons/base_automation/base_automation|base_automation]], [[Odoo 18/Community Addons/sms/sms|sms]]

## Summary

Generate recurring invoices and manage renewals

## XML Artifacts (detected)

- Views: 48
- Actions: 42
- Menus: 23
- Rules (ir.rule): 9
- Access CSV entries: 22

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `PaymentProvider`
- `payment.token`
- `PaymentTransaction`
- `product_template`
- `Pricelist`
- `ResPartner`
- `sale.order`
- `BaseAutomation`
- `sale.order.alert`
- `sale.order.close.reason`
- `SaleOrderLine`
- `sale.order.log`
- `SaleOrderOption`
- `sale.order.template`
- `sale.order.template.line`
- `sale.order.template.option`
- `sale.subscription.plan`
- `sale.subscription.pricing`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Subscriptions - Models and Relations
class AccountMove
class AccountMoveLine
class PaymentProvider
class "payment.token" as payment_token
class PaymentTransaction
class product_template
class Pricelist
class ResPartner
class "sale.order" as sale_order
class BaseAutomation
class "sale.order.alert" as sale_order_alert
class "sale.order.close.reason" as sale_order_close_reason
class SaleOrderLine
class "sale.order.log" as sale_order_log
class SaleOrderOption
class "sale.order.template" as sale_order_template
class "sale.order.template.line" as sale_order_template_line
class "sale.order.template.option" as sale_order_template_option
class "sale.subscription.plan" as sale_subscription_plan
class "sale.subscription.pricing" as sale_subscription_pricing
AccountMoveLine --> sale_order : many2one
product_template --|> sale_subscription_pricing : one2many
Pricelist --|> sale_subscription_pricing : one2many
sale_order --> sale_subscription_plan : many2one
sale_order --> sale_order : many2one
sale_order --> sale_order : many2one
sale_order --|> sale_order : one2many
sale_order --> sale_order_close_reason : many2one
sale_order --> payment_token : many2one
class "res.users" as res_users
sale_order --> res_users : many2one
class "res.partner" as res_partner
sale_order --> res_partner : many2one
sale_order --|> sale_order_log : one2many
sale_order --> sale_order : many2one
sale_order .. res_users : many2many
class "base.automation" as base_automation
sale_order_alert --> base_automation : many2one
class "ir.actions.server" as ir_actions_server
sale_order_alert --> ir_actions_server : many2one
class "res.currency" as res_currency
sale_order_alert --> res_currency : many2one
sale_order_alert .. sale_subscription_plan : many2many
sale_order_alert .. res_partner : many2many
class "res.company" as res_company
sale_order_alert --> res_company : many2one
class "crm.team" as crm_team
sale_order_alert .. crm_team : many2many
class "product.product" as product_product
sale_order_alert .. product_product : many2many
sale_order_alert .. res_users : many2many
class "sale.order.line" as sale_order_line
SaleOrderLine --> sale_order_line : many2one
sale_order_log --> sale_order : many2one
sale_order_log --> res_users : many2one
sale_order_log --> crm_team : many2one
sale_order_log --> sale_subscription_plan : many2one
sale_order_log --> res_company : many2one
sale_order_log --> res_currency : many2one
sale_order_log --> sale_order : many2one
sale_order_template --> sale_subscription_plan : many2one
sale_subscription_plan --> res_company : many2one
sale_subscription_plan .. sale_subscription_plan : many2many
class "mail.template" as mail_template
sale_subscription_plan --> mail_template : many2one
sale_subscription_plan --|> sale_subscription_pricing : one2many
class "product.template" as product_template
sale_subscription_pricing --> product_template : many2one
sale_subscription_pricing .. product_product : many2many
sale_subscription_pricing --> sale_subscription_plan : many2one
class "product.pricelist" as product_pricelist
sale_subscription_pricing --> product_pricelist : many2one
sale_subscription_pricing --> res_company : many2one
sale_subscription_pricing --> res_currency : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
