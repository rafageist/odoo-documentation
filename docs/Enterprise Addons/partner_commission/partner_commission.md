<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Resellers Commissions For Subscription

- Scope: Enterprise Addons
- Source: enterprise/partner_commission
- Dependencies: [[docs/Community Addons/purchase/purchase|purchase]], [[docs/Enterprise Addons/sale_subscription_partnership/sale_subscription_partnership|sale_subscription_partnership]], [[docs/Community Addons/website_crm_partner_assign/website_crm_partner_assign|website_crm_partner_assign]]

## Summary

Configure resellers commissions on subscription sale

## XML Artifacts (detected)

- Views: 18
- Actions: 4
- Menus: 1
- Rules (ir.rule): 6
- Access CSV entries: 10

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `commission.plan`
- `commission.rule`
- `CrmLead`
- `PurchaseOrder`
- `ResCompany`
- `ResPartnerGrade`
- `ResPartner`
- `SaleOrder`
- `SaleOrderLine`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Resellers Commissions For Subscription - Models and Relations
class AccountMove
class AccountMoveLine
class "commission.plan" as commission_plan
class "commission.rule" as commission_rule
class CrmLead
class PurchaseOrder
class ResCompany
class ResPartnerGrade
class ResPartner
class SaleOrder
class SaleOrderLine
class "res.partner" as res_partner
AccountMove --> res_partner : many2one
class "purchase.order.line" as purchase_order_line
AccountMove --> purchase_order_line : many2one
class "product.product" as product_product
commission_plan --> product_product : many2one
commission_plan --|> commission_rule : one2many
class "res.company" as res_company
commission_plan --> res_company : many2one
commission_rule --> commission_plan : many2one
class "product.category" as product_category
commission_rule --> product_category : many2one
commission_rule --> product_product : many2one
class "sale.order.template" as sale_order_template
commission_rule --> sale_order_template : many2one
class "product.pricelist" as product_pricelist
commission_rule --> product_pricelist : many2one
ResPartnerGrade --> commission_plan : many2one
ResPartner --> commission_plan : many2one
SaleOrder --> res_partner : many2one
SaleOrder --> commission_plan : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



