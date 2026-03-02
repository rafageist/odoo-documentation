<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/mrp_production_views.xml

- Module: [[docs/Enterprise Addons/mrp_workorder/mrp_workorder|mrp_workorder]]
- Scope: Enterprise Addons
- Source file: `views/mrp_production_views.xml`
- Views: 7
- Actions: 4
- Menus: 3
- Rules: 0

## View records

### `mrp_production_view_form_log_note`
- Name: mrp.production.view.form.log.note
- Model: `mrp.production`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `log_note`
- XPath or positional patches: 0

### `mrp_production_form_view`
- Name: mrp.production.form.inherit.mrp_workorder
- Model: `mrp.production`
- Type: inferred from arch
- Inherits: `mrp.mrp_production_form_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `log_note`
- Buttons: `action_open_shop_floor`
- XPath or positional patches: 2

### `view_mrp_production_filter_shop_floor`
- Name: mrp.production.select.shop.floor
- Model: `mrp.production`
- Type: inferred from arch
- Root tag: `search`
- Field references: 7
- Sample fields: `move_raw_ids`, `name`, `origin`, `picking_type_id`, `product_id`, `product_variant_attributes`, `workcenter_id`
- XPath or positional patches: 0

### `mrp_production_view_search_inherit_planning`
- Name: mrp.production.search.view.inherit.planning
- Model: `mrp.production`
- Type: inferred from arch
- Inherits: `mrp.view_mrp_production_filter`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `mrp_production_tree_view_planning`
- Name: mrp.production.list.inherit.planning
- Model: `mrp.production`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `date_start`, `message_needaction`, `name`, `origin`, `product_id`, `product_qty`, `product_uom_id`, `reservation_state`, `state`
- XPath or positional patches: 0

### `mrp_production_gantt_view`
- Name: mrp.production.gantt
- Model: `mrp.production`
- Type: inferred from arch
- Root tag: `gantt`
- Field references: 0
- XPath or positional patches: 0

### `mrp_production_kanban_view_inherit`
- Name: mrp.production.kanban
- Model: `mrp.production`
- Type: inferred from arch
- Inherits: `mrp.mrp_production_kanban_view`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `date_deadline`, `is_delayed`
- XPath or positional patches: 1

## Actions

- `production_order_unplan_server_action`: `server` Unplan orders
- `mrp.mrp_production_action`: `act_window`
- `action_mrp_display`: `client` Shop Floor
- `action_view_mrp_overview`: `server` Overview

## Menus

- `menu_mrp_workorder_workcenter`: Planning by Workcenter
- `menu_mrp_workorder_production`: Planning by Production
- `mrp_workorder_menu_planning`: Work Orders

## Navigation

- **Parent:** [[docs/Enterprise Addons/mrp_workorder/Views]]

<!-- GENERATED:VIEWFILE -->
