<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Sales

- Scope: Community Addons
- Source: odoo/addons/sale
- Dependencies: [[docs/Community Addons/sales_team/sales_team|sales_team]], [[docs/Community Addons/account_payment/account_payment|account_payment]], [[docs/Community Addons/utm/utm|utm]]

## Summary

Sales internal machinery

## XML Artifacts (detected)

- Views: 57
- Actions: 50
- Menus: 37
- Rules (ir.rule): 27
- Access CSV entries: 46

## Detected Models

- `account.move`
- `AccountMoveLine`
- `AccountAnalyticLine`
- `AccountAnalyticApplicability`
- `CrmTeam`
- `IrActionsReport`
- `IrConfigParameter`
- `PaymentProvider`
- `PaymentTransaction`
- `ProductDocument`
- `ProductPricelistItem`
- `ProductProduct`
- `ProductAttributeCustomValue`
- `ProductTemplate`
- `ResCompany`
- `ResPartner`
- `sale.order`
- `sale.order.line`
- `UtmCampaign`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Sales - Models and Relations
class "account.move" as account_move
class AccountMoveLine
class AccountAnalyticLine
class AccountAnalyticApplicability
class CrmTeam
class IrActionsReport
class IrConfigParameter
class PaymentProvider
class PaymentTransaction
class ProductDocument
class ProductPricelistItem
class ProductProduct
class ProductAttributeCustomValue
class ProductTemplate
class ResCompany
class ResPartner
class "sale.order" as sale_order
class "sale.order.line" as sale_order_line
class UtmCampaign
class "crm.team" as crm_team
account_move --> crm_team : many2one
AccountMoveLine .. sale_order_line : many2many
AccountAnalyticLine --> sale_order_line : many2one
PaymentTransaction .. sale_order : many2many
ProductAttributeCustomValue --> sale_order_line : many2one
class "product.template" as product_template
ProductTemplate .. product_template : many2many
class "product.product" as product_product
ResCompany --> product_product : many2one
class "account.account" as account_account
ResCompany --> account_account : many2one
ResPartner --|> sale_order : one2many
class "res.company" as res_company
sale_order --> res_company : many2one
class "res.partner" as res_partner
sale_order --> res_partner : many2one
class "mail.template" as mail_template
sale_order --> mail_template : many2one
class "account.journal" as account_journal
sale_order --> account_journal : many2one
sale_order --> res_partner : many2one
sale_order --> res_partner : many2one
class "account.fiscal.position" as account_fiscal_position
sale_order --> account_fiscal_position : many2one
class "account.payment.term" as account_payment_term
sale_order --> account_payment_term : many2one
class "account.payment.method.line" as account_payment_method_line
sale_order --> account_payment_method_line : many2one
class "product.pricelist" as product_pricelist
sale_order --> product_pricelist : many2one
class "res.currency" as res_currency
sale_order --> res_currency : many2one
class "res.users" as res_users
sale_order --> res_users : many2one
sale_order --> crm_team : many2one
sale_order --|> sale_order_line : one2many
sale_order .. account_move : many2many
class "payment.transaction" as payment_transaction
sale_order .. payment_transaction : many2many
sale_order .. payment_transaction : many2many
class "crm.tag" as crm_tag
sale_order .. crm_tag : many2many
sale_order .. sale_order : many2many
class "res.country" as res_country
sale_order --> res_country : many2one
sale_order_line --> sale_order : many2one
sale_order_line --> product_product : many2one
sale_order_line --> product_template : many2one
class "product.attribute.custom.value" as product_attribute_custom_value
sale_order_line --|> product_attribute_custom_value : one2many
class "product.template.attribute.value" as product_template_attribute_value
sale_order_line .. product_template_attribute_value : many2many
class "uom.uom" as uom_uom
sale_order_line --> uom_uom : many2one
sale_order_line .. uom_uom : many2many
sale_order_line --> sale_order_line : many2one
sale_order_line --|> sale_order_line : one2many
class "product.combo.item" as product_combo_item
sale_order_line --> product_combo_item : many2one
class "account.tax" as account_tax
sale_order_line .. account_tax : many2many
class "product.pricelist.item" as product_pricelist_item
sale_order_line --> product_pricelist_item : many2one
class "account.analytic.line" as account_analytic_line
sale_order_line --|> account_analytic_line : one2many
class "account.move.line" as account_move_line
sale_order_line .. account_move_line : many2many
sale_order_line --> sale_order_line : many2one
UtmCampaign --> res_company : many2one
UtmCampaign --> res_currency : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





