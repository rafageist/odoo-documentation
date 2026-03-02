<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Point of Sale

- Scope: Community Addons
- Source: odoo/addons/point_of_sale
- Dependencies: [[docs/Community Addons/resource/resource|resource]], [[docs/Community Addons/stock_account/stock_account|stock_account]], [[docs/Community Addons/barcodes/barcodes|barcodes]], [[docs/Community Addons/html_editor/html_editor|html_editor]], [[docs/Community Addons/digest/digest|digest]], [[docs/Community Addons/phone_validation/phone_validation|phone_validation]], [[docs/Community Addons/partner_autocomplete/partner_autocomplete|partner_autocomplete]], [[docs/Community Addons/iot_base/iot_base|iot_base]], [[docs/Community Addons/google_address_autocomplete/google_address_autocomplete|google_address_autocomplete]]

## Summary

Handle checkouts and payments for shops and restaurants.

## XML Artifacts (detected)

- Views: 60
- Actions: 38
- Menus: 29
- Rules (ir.rule): 12
- Access CSV entries: 54

## Detected Models

- `AccountBankStatementLine`
- `AccountCashRounding`
- `account.fiscal.position`
- `AccountJournal`
- `account.move`
- `AccountMoveLine`
- `AccountPayment`
- `account.tax`
- `account.tax.group`
- `BarcodeRule`
- `decimal.precision`
- `DigestDigest`
- `ir.module.module`
- `IrSequence`
- `pos.bill`
- `pos.category`
- `pos.config`
- `pos.note`
- `pos.order`
- `pos.order.line`
- `pos.pack.operation.lot`
- `account.cash.rounding`
- `pos.payment`
- `pos.payment.method`
- `pos.preset`
- `pos.printer`
- `pos.session`
- `StockRule`
- `product.attribute`
- `product.attribute.custom.value`
- `product.template.attribute.line`
- `product.template.attribute.value`
- `product.template.attribute.exclusion`
- `product.category`
- `product.combo`
- `product.combo.item`
- `product.pricelist`
- `product.pricelist.item`
- `product.product`
- `product.tag`
- `product.template`
- `product.uom`
- `resource.calendar.attendance`
- `res.company`
- `res.country`
- `res.country.state`
- `res.currency`
- `res.lang`
- `res.partner`
- `res.users`
- `StockPicking`
- `stock.picking.type`
- `StockMove`
- `StockReference`
- `StockWarehouse`
- `uom.uom`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Point of Sale - Models and Relations
class AccountBankStatementLine
class AccountCashRounding
class "account.fiscal.position" as account_fiscal_position
class AccountJournal
class "account.move" as account_move
class AccountMoveLine
class AccountPayment
class "account.tax" as account_tax
class "account.tax.group" as account_tax_group
class BarcodeRule
class "decimal.precision" as decimal_precision
class DigestDigest
class "ir.module.module" as ir_module_module
class IrSequence
class "pos.bill" as pos_bill
class "pos.category" as pos_category
class "pos.config" as pos_config
class "pos.note" as pos_note
class "pos.order" as pos_order
class "pos.order.line" as pos_order_line
class "pos.pack.operation.lot" as pos_pack_operation_lot
class "account.cash.rounding" as account_cash_rounding
class "pos.payment" as pos_payment
class "pos.payment.method" as pos_payment_method
class "pos.preset" as pos_preset
class "pos.printer" as pos_printer
class "pos.session" as pos_session
class StockRule
class "product.attribute" as product_attribute
class "product.attribute.custom.value" as product_attribute_custom_value
class "product.template.attribute.line" as product_template_attribute_line
class "product.template.attribute.value" as product_template_attribute_value
class "product.template.attribute.exclusion" as product_template_attribute_exclusion
class "product.category" as product_category
class "product.combo" as product_combo
class "product.combo.item" as product_combo_item
class "product.pricelist" as product_pricelist
class "product.pricelist.item" as product_pricelist_item
class "product.product" as product_product
class "product.tag" as product_tag
class "product.template" as product_template
class "product.uom" as product_uom
class "resource.calendar.attendance" as resource_calendar_attendance
class "res.company" as res_company
class "res.country" as res_country
class "res.country.state" as res_country_state
class "res.currency" as res_currency
class "res.lang" as res_lang
class "res.partner" as res_partner
class "res.users" as res_users
class StockPicking
class "stock.picking.type" as stock_picking_type
class StockMove
class StockReference
class StockWarehouse
class "uom.uom" as uom_uom
AccountBankStatementLine --> pos_session : many2one
AccountJournal --|> pos_payment_method : one2many
account_move --|> pos_order : one2many
account_move --|> pos_payment : one2many
account_move .. account_move : many2many
account_move --> pos_order : many2one
account_move --|> pos_session : one2many
AccountPayment --> pos_payment_method : many2one
class "account.account" as account_account
AccountPayment --> account_account : many2one
AccountPayment --> pos_session : many2one
pos_bill .. pos_config : many2many
pos_category --> pos_category : many2one
pos_category --|> pos_category : one2many
pos_config .. pos_printer : many2many
pos_config --> stock_picking_type : many2one
class "account.journal" as account_journal
pos_config --> account_journal : many2one
pos_config --> account_journal : many2one
pos_config --> res_currency : many2one
class "ir.sequence" as ir_sequence
pos_config --> ir_sequence : many2one
pos_config --> ir_sequence : many2one
pos_config --> ir_sequence : many2one
pos_config --> ir_sequence : many2one
pos_config .. pos_category : many2many
pos_config --|> pos_session : one2many
pos_config --> pos_session : many2one
pos_config --> product_pricelist : many2one
pos_config .. product_pricelist : many2many
pos_config --> res_company : many2one
class "res.groups" as res_groups
pos_config --> res_groups : many2one
pos_config --> res_groups : many2one
pos_config --> product_product : many2one
pos_config .. account_fiscal_position : many2many
pos_config --> account_fiscal_position : many2one
pos_config .. pos_bill : many2many
pos_config --> pos_preset : many2one
pos_config .. pos_preset : many2many
pos_config .. pos_payment_method : many2many
pos_config --> res_users : many2one
pos_config --> account_cash_rounding : many2one
class "stock.warehouse" as stock_warehouse
pos_config --> stock_warehouse : many2one
class "stock.route" as stock_route
pos_config --> stock_route : many2one
pos_config .. pos_config : many2many
pos_config .. pos_note : many2many
class "barcode.nomenclature" as barcode_nomenclature
pos_config --> barcode_nomenclature : many2one
pos_config .. pos_payment_method : many2many
pos_order --> res_users : many2one
pos_order --|> pos_order_line : one2many
pos_order --> res_company : many2one
pos_order --> product_pricelist : many2one
pos_order --> res_partner : many2one
pos_order --> pos_session : many2one
pos_order --> pos_config : many2one
pos_order --> res_currency : many2one
pos_order --> account_move : many2one
class "stock.picking" as stock_picking
pos_order --|> stock_picking : one2many
pos_order --> stock_picking_type : many2one
class "stock.reference" as stock_reference
pos_order .. stock_reference : many2many
pos_order --> pos_preset : many2one
pos_order --> account_journal : many2one
pos_order --> account_fiscal_position : many2one
pos_order --|> pos_payment : one2many
pos_order --> account_move : many2one
pos_order --> pos_order : many2one
pos_order .. pos_payment_method : many2many
pos_order --|> account_move : one2many
pos_order_line --> res_company : many2one
pos_order_line --> product_product : many2one
pos_order_line .. product_template_attribute_value : many2many
pos_order_line --|> product_attribute_custom_value : one2many
pos_order_line --> pos_order : many2one
pos_order_line .. account_tax : many2many
pos_order_line .. account_tax : many2many
pos_order_line --|> pos_pack_operation_lot : one2many
pos_order_line --> uom_uom : many2one
pos_order_line --> res_currency : many2one
pos_order_line --|> pos_order_line : one2many
pos_order_line --> pos_order_line : many2one
pos_order_line --> pos_order_line : many2one
pos_order_line --|> pos_order_line : one2many
pos_order_line --> product_combo_item : many2one
pos_pack_operation_lot --> pos_order_line : many2one
pos_pack_operation_lot --> pos_order : many2one
pos_pack_operation_lot --> product_product : many2one
pos_payment --> pos_order : many2one
pos_payment --> pos_payment_method : many2one
pos_payment --> res_currency : many2one
pos_payment --> res_partner : many2one
pos_payment --> pos_session : many2one
pos_payment --> res_users : many2one
pos_payment --> res_company : many2one
pos_payment --> account_move : many2one
pos_payment_method --> account_account : many2one
pos_payment_method --> account_account : many2one
pos_payment_method --> account_journal : many2one
pos_payment_method .. pos_session : many2many
pos_payment_method .. pos_config : many2many
pos_payment_method --> res_company : many2one
pos_preset --> product_pricelist : many2one
pos_preset --> account_fiscal_position : many2one
class "resource.calendar" as resource_calendar
pos_preset --> resource_calendar : many2one
pos_printer .. pos_category : many2many
pos_printer --> res_company : many2one
pos_printer .. pos_config : many2many
pos_session --> res_company : many2one
pos_session --> pos_config : many2one
pos_session --> res_users : many2one
pos_session --> res_currency : many2one
pos_session --> account_journal : many2one
pos_session --|> pos_order : one2many
class "account.bank.statement.line" as account_bank_statement_line
pos_session --|> account_bank_statement_line : one2many
pos_session --|> stock_picking : one2many
pos_session --> account_move : many2one
pos_session .. pos_payment_method : many2many
class "account.payment" as account_payment
pos_session --|> account_payment : one2many
product_attribute_custom_value --> pos_order_line : many2one
product_template .. pos_category : many2many
product_template .. product_template : many2many
res_partner --|> pos_order : one2many
res_partner --> account_fiscal_position : many2one
StockPicking --> pos_session : many2one
StockPicking --> pos_order : many2one
StockReference .. pos_order : many2many
StockWarehouse --> stock_picking_type : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





