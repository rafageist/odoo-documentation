---
tags: [odoo, community, generated, views]
---

# views/purchase_views.xml

- Module: [[docs/Community Addons/purchase/purchase|purchase]]
- Scope: Community Addons
- Source file: `views/purchase_views.xml`
- Views: 18
- Actions: 11
- Menus: 15
- Rules: 0

## View records

### `purchase_history_graph`
- Name: purchase.history.graph
- Model: `purchase.order.line`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `date_order`, `product_uom_qty`
- XPath or positional patches: 0

### `purchase_history_pivot`
- Name: purchase.history.pivot
- Model: `purchase.order.line`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `price_total`, `product_uom_qty`
- XPath or positional patches: 0

### `purchase_history_tree`
- Name: purchase.history.list
- Model: `purchase.order.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `company_id`, `currency_id`, `date_approve`, `order_id`, `partner_id`, `price_subtotal`, `price_unit`, `product_uom_qty`, `state`
- XPath or positional patches: 0

### `purchase_order_line_search`
- Name: purchase.order.line.search
- Model: `purchase.order.line`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `order_id`, `partner_id`, `product_id`
- XPath or positional patches: 0

### `purchase_order_line_form2`
- Name: purchase.order.line.form2
- Model: `purchase.order.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `analytic_distribution`, `company_id`, `date_order`, `date_planned`, `invoice_lines`, `name`, `order_id`, `partner_id`, `price_unit`, `product_id`, and 3 more
- XPath or positional patches: 0

### `purchase_order_line_tree`
- Name: purchase.order.line.list
- Model: `purchase.order.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `currency_id`, `date_planned`, `name`, `order_id`, `partner_id`, `price_subtotal`, `price_unit`, `product_id`, `product_qty`, `product_uom_id`
- XPath or positional patches: 0

### `purchase_order_view_activity`
- Name: purchase.order.activity
- Model: `purchase.order`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 5
- Sample fields: `amount_total`, `currency_id`, `name`, `partner_id`, `state`
- XPath or positional patches: 0

### `purchase_order_view_tree`
- Name: purchase.order.view.list
- Model: `purchase.order`
- Type: inferred from arch
- Root tag: `list`
- Field references: 18
- Sample fields: `activity_ids`, `amount_total`, `amount_total_cc`, `amount_untaxed`, `company_currency_id`, `company_id`, `currency_id`, `date_approve`, `date_order`, `date_planned`, and 8 more
- Buttons: `action_create_invoice`, `button_cancel`
- XPath or positional patches: 0

### `purchase_order_kpis_tree`
- Name: purchase.order.inherit.purchase.order.list
- Model: `purchase.order`
- Type: inferred from arch
- Root tag: `list`
- Field references: 18
- Sample fields: `activity_ids`, `amount_total`, `amount_total_cc`, `amount_untaxed`, `company_currency_id`, `company_id`, `currency_id`, `date_approve`, `date_order`, `date_planned`, and 8 more
- Buttons: `button_cancel`
- XPath or positional patches: 0

### `purchase_order_tree`
- Name: purchase.order.list
- Model: `purchase.order`
- Type: inferred from arch
- Root tag: `list`
- Field references: 17
- Sample fields: `activity_exception_decoration`, `activity_ids`, `amount_total`, `amount_untaxed`, `company_id`, `currency_id`, `date_approve`, `date_order`, `date_planned`, `invoice_status`, and 7 more
- XPath or positional patches: 0

### `purchase_order_view_kanban_without_dashboard`
- Name: purchase.order.view.kanban.without.dashboard
- Model: `purchase.order`
- Type: inferred from arch
- Inherits: `purchase.view_purchase_order_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_purchase_order_kanban`
- Name: purchase.order.kanban
- Model: `purchase.order`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 8
- Sample fields: `activity_ids`, `amount_total`, `currency_id`, `date_order`, `name`, `partner_id`, `priority`, `state`
- XPath or positional patches: 0

### `purchase_order_view_search`
- Name: purchase.order.select
- Model: `purchase.order`
- Type: inferred from arch
- Root tag: `search`
- Field references: 6
- Sample fields: `activity_type_id`, `activity_user_id`, `name`, `partner_id`, `product_id`, `user_id`
- XPath or positional patches: 0

### `view_purchase_order_filter`
- Name: request.quotation.select
- Model: `purchase.order`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `name`, `origin`, `partner_id`, `product_id`, `user_id`
- XPath or positional patches: 0

### `purchase_order_form`
- Name: purchase.order.form
- Model: `purchase.order`
- Type: inferred from arch
- Root tag: `form`
- Field references: 48
- Sample fields: `analytic_distribution`, `company_id`, `currency_id`, `date_approve`, `date_order`, `date_planned`, `discount`, `display_type`, `duplicated_order_ids`, `fiscal_position_id`, and 38 more
- Buttons: `%(purchase.action_report_purchase_order)d`, `action_acknowledge`, `action_add_from_catalog`, `action_bill_matching`, `action_purchase_comparison`, `action_rfq_send`, `action_view_invoice`, `button_approve`, `button_cancel`, `button_confirm`, and 4 more
- XPath or positional patches: 0

### `purchase_order_graph`
- Name: purchase.order.graph
- Model: `purchase.order`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `amount_total`, `partner_id`
- XPath or positional patches: 0

### `purchase_order_pivot`
- Name: purchase.order.pivot
- Model: `purchase.order`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `amount_total`, `partner_id`
- XPath or positional patches: 0

### `purchase_order_calendar`
- Name: purchase.order.calendar
- Model: `purchase.order`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 4
- Sample fields: `amount_total`, `currency_id`, `partner_id`, `partner_ref`
- XPath or positional patches: 0

## Actions

- `mail_followers_edit_action_from_purchase`: `act_window` Add/Remove Followers
- `action_confirm_rfqs`: `server` Confirm RFQ
- `action_rfq_form`: `act_window` Requests for Quotation
- `action_merger`: `server` Merge RFQs
- `action_accrued_expense_entry`: `act_window` Accrued Expense Entry
- `action_purchase_send_reminder`: `server` Send Reminder
- `action_purchase_history`: `act_window`
- `purchase_form_action`: `act_window` Purchase Orders
- `purchase_rfq`: `act_window` Requests for Quotation
- `product_product_action`: `act_window` Product Variants
- `product_normal_action_puchased`: `act_window` Products

## Menus

- `menu_purchase_form_action`: unnamed
- `menu_purchase_rfq`: unnamed
- `product_product_menu`: Product Variants
- `menu_procurement_partner_contact_form`: Products
- `menu_purchase_products`: Products
- `menu_purchase_uom_form_action`: Units & Packagings
- `menu_product_category_config_purchase`: unnamed
- `menu_product_attribute_action`: Attributes
- `menu_product_in_config_purchase`: unnamed
- `menu_product_in_config_purchase`: Products
- `menu_product_pricelist_action2_purchase`: unnamed
- `menu_purchase_config`: Configuration
- `menu_procurement_management_supplier_name`: Vendors
- `menu_procurement_management`: Orders
- `menu_purchase_root`: Purchase

## Navigation

- **Parent:** [[docs/Community Addons/purchase/Views]]

