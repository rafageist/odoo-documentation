<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# report/event_sale_report_views.xml

- Module: [[docs/Community Addons/event_sale/event_sale|event_sale]]
- Scope: Community Addons
- Source file: `report/event_sale_report_views.xml`
- Views: 5
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `event_sale_report_view_search`
- Name: event.sale.report.view.search
- Model: `event.sale.report`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `company_id`, `event_id`, `event_registration_name`, `sale_order_partner_id`
- XPath or positional patches: 0

### `event_sale_report_view_tree`
- Name: event.sale.report.view.list
- Model: `event.sale.report`
- Type: inferred from arch
- Root tag: `list`
- Field references: 12
- Sample fields: `event_id`, `event_registration_name`, `event_registration_state`, `event_slot_id`, `event_ticket_id`, `event_ticket_price`, `invoice_partner_id`, `product_id`, `sale_order_partner_id`, `sale_order_state`, and 2 more
- XPath or positional patches: 0

### `event_sale_report_view_pivot`
- Name: event.sale.report.view.pivot
- Model: `event.sale.report`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 5
- Sample fields: `event_id`, `event_ticket_price`, `product_id`, `sale_price`, `sale_price_untaxed`
- XPath or positional patches: 0

### `event_sale_report_view_form`
- Name: event.sale.report.view.form
- Model: `event.sale.report`
- Type: inferred from arch
- Root tag: `form`
- Field references: 15
- Sample fields: `event_date_begin`, `event_id`, `event_registration_create_date`, `event_registration_id`, `event_registration_name`, `event_registration_state`, `event_slot_id`, `event_ticket_id`, `event_ticket_price`, `event_type_id`, and 5 more
- XPath or positional patches: 0

### `event_sale_report_view_graph`
- Name: event.sale.report.view.graph
- Model: `event.sale.report`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `event_registration_create_date`, `event_ticket_price`, `sale_price`
- XPath or positional patches: 0

## Actions

- `event_sale_report_action`: `act_window` Revenues

## Menus

- `menu_action_show_revenues`: Revenues

## Navigation

- **Parent:** [[docs/Community Addons/event_sale/Views]]

<!-- GENERATED:VIEWFILE -->
