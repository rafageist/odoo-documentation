---
tags: [odoo, community, generated, views]
---

# views/stock_rule_views.xml

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Source file: `views/stock_rule_views.xml`
- Views: 4
- Actions: 1
- Menus: 2
- Rules: 0

## View records

### `view_route_rule_form`
- Name: stock.rule.form
- Model: `stock.rule`
- Type: inferred from arch
- Inherits: `stock.view_stock_rule_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `route_company_id`
- XPath or positional patches: 3

### `view_stock_rule_form`
- Name: stock.rule.form
- Model: `stock.rule`
- Type: inferred from arch
- Root tag: `form`
- Field references: 20
- Sample fields: `action`, `active`, `auto`, `company_id`, `delay`, `location_dest_from_rule`, `location_dest_id`, `location_src_id`, `name`, `partner_address_id`, and 10 more
- XPath or positional patches: 0

### `view_stock_rule_tree`
- Name: stock.rule.list
- Model: `stock.rule`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `action`, `company_id`, `location_dest_id`, `location_src_id`, `name`, `route_id`
- XPath or positional patches: 0

### `view_stock_rule_filter`
- Name: stock.rule.select
- Model: `stock.rule`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

## Actions

- `action_rules_form`: `act_window` Rules

## Menus

- `stock.menu_procurement_compute`: unnamed
- `menu_action_rules_form`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/stock/Views]]

