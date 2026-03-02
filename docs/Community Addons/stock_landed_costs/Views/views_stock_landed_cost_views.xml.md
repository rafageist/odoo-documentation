<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/stock_landed_cost_views.xml

- Module: [[docs/Community Addons/stock_landed_costs/stock_landed_costs|stock_landed_costs]]
- Scope: Community Addons
- Source file: `views/stock_landed_cost_views.xml`
- Views: 5
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_stock_landed_cost_search`
- Name: stock.landed.cost.search
- Model: `stock.landed.cost`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `name`, `picking_ids`
- XPath or positional patches: 0

### `stock_landed_cost_view_kanban`
- Name: stock.landed.cost.kanban
- Model: `stock.landed.cost`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `account_journal_id`, `date`, `name`, `state`
- XPath or positional patches: 0

### `view_stock_landed_cost_tree2`
- Name: stock.landed.cost.list
- Model: `stock.landed.cost`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `amount_total`, `company_id`, `currency_id`, `date`, `name`, `state`
- XPath or positional patches: 0

### `view_stock_landed_cost_tree`
- Name: stock.landed.cost.list
- Model: `stock.landed.cost`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `activity_exception_decoration`, `company_id`, `date`, `name`, `state`
- XPath or positional patches: 0

### `view_stock_landed_cost_form`
- Name: stock.landed.cost.form
- Model: `stock.landed.cost`
- Type: inferred from arch
- Root tag: `form`
- Field references: 24
- Sample fields: `account_id`, `account_journal_id`, `account_move_id`, `additional_landed_cost`, `amount_total`, `company_id`, `cost_line_id`, `cost_lines`, `currency_id`, `date`, and 14 more
- Buttons: `button_cancel`, `button_validate`, `compute_landed_cost`
- XPath or positional patches: 0

## Actions

- `action_stock_landed_cost`: `act_window` Landed Costs

## Menus

- `menu_stock_landed_cost`: Landed Costs

## Navigation

- **Parent:** [[docs/Community Addons/stock_landed_costs/Views]]

<!-- GENERATED:VIEWFILE -->
