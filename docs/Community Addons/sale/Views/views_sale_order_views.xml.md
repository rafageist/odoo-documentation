<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/sale_order_views.xml

- Module: [[docs/Community Addons/sale/sale|sale]]
- Scope: Community Addons
- Source file: `views/sale_order_views.xml`
- Views: 16
- Actions: 23
- Menus: 0
- Rules: 0

## View records

### `sale_order_view_search_inherit_sale`
- Name: sale.order.search.inherit.sale
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_sales_order_filter`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `sale_order_view_search_inherit_quotation`
- Name: sale.order.search.inherit.quotation
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_sales_order_filter`
- Root tag: `filter`
- Field references: 1
- Sample fields: `campaign_id`
- XPath or positional patches: 1

### `view_sales_order_filter`
- Name: sale.order.list.select
- Model: `sale.order`
- Type: inferred from arch
- Root tag: `search`
- Field references: 7
- Sample fields: `activity_type_id`, `activity_user_id`, `name`, `order_line`, `partner_id`, `team_id`, `user_id`
- XPath or positional patches: 0

### `view_order_form`
- Name: sale.order.form
- Model: `sale.order`
- Type: inferred from arch
- Root tag: `form`
- Field references: 68
- Sample fields: `analytic_distribution`, `campaign_id`, `client_order_ref`, `collapse_composition`, `collapse_prices`, `combo_item_id`, `commitment_date`, `company_id`, `currency_id`, `custom_product_template_attribute_value_id`, and 58 more
- Buttons: `%(sale.action_view_sale_advance_payment_inv)d`, `action_add_from_catalog`, `action_cancel`, `action_confirm`, `action_draft`, `action_lock`, `action_open_discount_wizard`, `action_preview_sale_order`, `action_quotation_send`, `action_unlock`, and 6 more
- XPath or positional patches: 0

### `view_quotation_kanban_with_onboarding`
- Name: sale.order.kanban
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `view_sale_order_kanban`
- Root tag: `kanban`
- Field references: 0
- XPath or positional patches: 1

### `view_quotation_tree_with_onboarding`
- Name: sale.order.list
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `view_quotation_tree`
- Root tag: `list`
- Field references: 0
- XPath or positional patches: 1

### `view_quotation_tree`
- Name: sale.order.list (quotes)
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale_order_tree`
- Root tag: `list`
- Field references: 4
- Sample fields: `create_date`, `date_order`, `invoice_status`, `state`
- XPath or positional patches: 1

### `sale_order_list_upload`
- Name: sale.order.tree.upload (orders)
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `view_order_tree`
- Root tag: `list`
- Field references: 0
- XPath or positional patches: 1

### `view_order_tree`
- Name: sale.order.list (orders)
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale_order_tree`
- Root tag: `list`
- Field references: 0
- XPath or positional patches: 1

### `sale_order_tree`
- Name: sale.order.list
- Model: `sale.order`
- Type: inferred from arch
- Root tag: `list`
- Field references: 19
- Sample fields: `activity_ids`, `amount_tax`, `amount_total`, `amount_untaxed`, `client_order_ref`, `commitment_date`, `company_id`, `currency_id`, `date_order`, `expected_date`, and 9 more
- Buttons: `%(sale.action_view_sale_advance_payment_inv)d`
- XPath or positional patches: 0

### `sale_order_kanban_upload`
- Name: sale.order.kanban.upload (orders)
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `view_sale_order_kanban`
- Root tag: `kanban`
- Field references: 0
- XPath or positional patches: 1

### `view_sale_order_kanban`
- Name: sale.order.kanban
- Model: `sale.order`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 7
- Sample fields: `activity_ids`, `amount_total`, `currency_id`, `date_order`, `name`, `partner_id`, `state`
- XPath or positional patches: 0

### `view_sale_order_pivot`
- Name: sale.order.pivot
- Model: `sale.order`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `amount_total`, `date_order`
- XPath or positional patches: 0

### `view_sale_order_graph`
- Name: sale.order.graph
- Model: `sale.order`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `amount_total`, `partner_id`
- XPath or positional patches: 0

### `view_sale_order_calendar`
- Name: sale.order.calendar
- Model: `sale.order`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 6
- Sample fields: `activity_ids`, `amount_total`, `currency_id`, `partner_id`, `payment_term_id`, `state`
- XPath or positional patches: 0

### `sale_order_view_activity`
- Name: sale.order.activity
- Model: `sale.order`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 5
- Sample fields: `amount_total`, `currency_id`, `name`, `partner_id`, `state`
- XPath or positional patches: 0

## Actions

- `mail_followers_edit_action_from_sale`: `act_window` Add/Remove Followers
- `model_sale_order_send_mail`: `server` Send an email
- `model_sale_order_action_share`: `server` Share
- `model_sale_order_action_quotation_sent`: `server` Mark Quotation as Sent
- `action_orders_upselling`: `act_window` Orders to Upsell
- `action_orders_to_invoice`: `act_window` Orders to Invoice
- `sale_order_action_view_quotation_graph`: `view`
- `sale_order_action_view_quotation_pivot`: `view`
- `sale_order_action_view_quotation_calendar`: `view`
- `sale_order_action_view_quotation_form`: `view`
- `action_quotations_kanban`: `view`
- `action_quotations_tree`: `view`
- `action_quotations`: `act_window` Quotations
- `sale_order_action_view_quotation_kanban`: `view`
- `sale_order_action_view_quotation_tree`: `view`
- `action_quotations_with_onboarding`: `act_window` Quotations
- `sale_order_action_view_order_graph`: `view`
- `sale_order_action_view_order_pivot`: `view`
- `sale_order_action_view_order_calendar`: `view`
- `sale_order_action_view_order_form`: `view`

## Navigation

- **Parent:** [[docs/Community Addons/sale/Views]]

<!-- GENERATED:VIEWFILE -->
