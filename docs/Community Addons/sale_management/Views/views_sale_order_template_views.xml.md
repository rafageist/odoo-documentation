---
tags: [odoo, community, generated, views]
---

# views/sale_order_template_views.xml

- Module: [[docs/Community Addons/sale_management/sale_management|sale_management]]
- Scope: Community Addons
- Source file: `views/sale_order_template_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `sale_order_template_view_tree`
- Name: sale.order.template.list
- Model: `sale.order.template`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `company_id`, `name`, `sequence`
- XPath or positional patches: 0

### `sale_order_template_view_form`
- Name: sale.order.template.form
- Model: `sale.order.template`
- Type: inferred from arch
- Root tag: `form`
- Field references: 17
- Sample fields: `active`, `company_id`, `display_type`, `is_optional`, `journal_id`, `mail_template_id`, `name`, `note`, `number_of_days`, `prepayment_percent`, and 7 more
- XPath or positional patches: 0

### `sale_order_template_view_search`
- Name: sale.order.template.search
- Model: `sale.order.template`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

## Actions

- `sale_order_template_action`: `act_window` Quotation Templates

## Navigation

- **Parent:** [[docs/Community Addons/sale_management/Views]]

