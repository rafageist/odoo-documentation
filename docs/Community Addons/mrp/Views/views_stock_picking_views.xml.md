<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/stock_picking_views.xml

- Module: [[docs/Community Addons/mrp/mrp|mrp]]
- Scope: Community Addons
- Source file: `views/stock_picking_views.xml`
- Views: 3
- Actions: 2
- Menus: 1
- Rules: 0

## View records

### `view_picking_type_form_inherit_mrp`
- Name: Operation Types
- Model: `stock.picking.type`
- Type: inferred from arch
- Inherits: `stock.view_picking_type_form`
- Root tag: `xpath`
- Field references: 11
- Sample fields: `auto_print_done_mrp_lot`, `auto_print_done_mrp_product_labels`, `auto_print_done_production_order`, `auto_print_generated_mrp_lot`, `auto_print_mrp_reception_report`, `auto_print_mrp_reception_report_labels`, `auto_show_reception_report`, `done_mrp_lot_label_to_print`, `generated_mrp_lot_label_to_print`, `mrp_product_label_to_print`, and 1 more
- XPath or positional patches: 2

### `view_picking_form_inherit_mrp`
- Name: view.picking.form.inherit.mrp
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `production_count`
- Buttons: `action_view_mrp_production`
- XPath or positional patches: 1

### `stock_production_type_kanban`
- Name: stock.picking.type.kanban
- Model: `stock.picking.type`
- Type: inferred from arch
- Inherits: `stock.stock_picking_type_kanban`
- Root tag: `xpath`
- Field references: 10
- Sample fields: `color`, `count_mo_in_progress`, `count_mo_late`, `count_mo_to_close`, `count_mo_todo`, `count_mo_waiting`, `is_favorite`, `kanban_dashboard_graph`, `name`, `warehouse_id`
- Buttons: `%(mrp_production_action_picking_deshboard)d`
- XPath or positional patches: 2

## Actions

- `action_picking_tree_mrp_operation_graph`: `act_window` Manufacturings
- `action_picking_tree_mrp_operation`: `act_window` Manufacturings

## Menus

- `mrp_operation_picking`: Manufacturings

## Navigation

- **Parent:** [[docs/Community Addons/mrp/Views]]

<!-- GENERATED:VIEWFILE -->
