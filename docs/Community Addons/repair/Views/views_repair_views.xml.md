---
tags: [odoo, community, generated, views]
---

# views/repair_views.xml

- Module: [[docs/Community Addons/repair/repair|repair]]
- Scope: Community Addons
- Source file: `views/repair_views.xml`
- Views: 9
- Actions: 6
- Menus: 8
- Rules: 0

## View records

### `view_repair_tag_search`
- Name: repair.tag.search
- Model: `repair.tags`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `view_repair_tag_tree`
- Name: repair.tag.list
- Model: `repair.tags`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `color`, `name`
- XPath or positional patches: 0

### `view_repair_pivot`
- Name: repair.pivot
- Model: `repair.order`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `create_date`, `product_id`
- XPath or positional patches: 0

### `view_repair_graph`
- Name: repair.graph
- Model: `repair.order`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `create_date`, `product_id`
- XPath or positional patches: 0

### `view_repair_order_form_filter`
- Name: repair.select
- Model: `repair.order`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `name`, `partner_id`, `product_id`, `sale_order_id`
- XPath or positional patches: 0

### `view_repair_kanban`
- Name: repair.kanban
- Model: `repair.order`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `name`, `partner_id`, `product_id`, `state`, `tag_ids`
- XPath or positional patches: 0

### `view_repair_order_form`
- Name: repair.form
- Model: `repair.order`
- Type: inferred from arch
- Root tag: `form`
- Field references: 46
- Sample fields: `additional`, `allowed_lot_ids`, `company_id`, `date`, `date_deadline`, `description_picking`, `display_assign_serial`, `forecast_availability`, `forecast_expected_date`, `has_tracking`, and 36 more
- Buttons: `%(action_repair_move_lines)d`, `action_add_from_catalog_repair`, `action_assign`, `action_create_sale_order`, `action_generate_serial`, `action_repair_cancel`, `action_repair_cancel_draft`, `action_repair_end`, `action_repair_start`, `action_show_details`, and 3 more
- XPath or positional patches: 0

### `view_repair_order_tree`
- Name: repair.list
- Model: `repair.order`
- Type: inferred from arch
- Root tag: `list`
- Field references: 16
- Sample fields: `activity_exception_decoration`, `company_id`, `location_id`, `name`, `partner_id`, `parts_availability`, `parts_availability_state`, `picking_id`, `priority`, `product_id`, and 6 more
- XPath or positional patches: 0

### `repair_order_view_activity`
- Name: repair.order.view.activity
- Model: `repair.order`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 4
- Sample fields: `name`, `product_id`, `schedule_date`, `user_id`
- XPath or positional patches: 0

## Actions

- `action_repair_order_tag`: `act_window` Tags
- `action_picking_repair_graph`: `act_window` Repair Orders
- `action_picking_repair`: `act_window` Repair Orders
- `action_repair_order_graph`: `act_window` Repair Orders Analysis
- `action_repair_order_tree`: `act_window` Repair Orders
- `action_repair_order_form`: `act_window` Repair Orders

## Menus

- `repair_menu_tag`: Repair Orders Tags
- `repair_menu_product_product`: Product Variants
- `repair_menu_product_template`: Products
- `repair_menu_config`: Configuration
- `repair_menu`: Repairs
- `repair_menu_reporting`: Reporting
- `repair_order_menu`: Orders
- `menu_repair_order`: Repairs

## Navigation

- **Parent:** [[docs/Community Addons/repair/Views]]

