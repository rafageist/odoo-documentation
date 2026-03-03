---
tags: [odoo, enterprise, generated, views]
---

# views/quality_views.xml

- Module: [[docs/Enterprise Addons/quality_mrp_workorder/quality_mrp_workorder|quality_mrp_workorder]]
- Scope: Enterprise Addons
- Source file: `views/quality_views.xml`
- Views: 10
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `quality_point_routing_view_form_inherit_quality_mrp_workorder`
- Name: quality.point.routing.view.form.inherit.quality.mrp
- Model: `quality.point`
- Type: inferred from arch
- Inherits: `mrp_workorder.quality_point_routing_view_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `quality_check_view_graph_inherit_mrp_workorder`
- Name: quality.check.view.graph.inherit.mrp.workorder
- Model: `quality.check`
- Type: inferred from arch
- Inherits: `quality_control.quality_check_view_graph`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `finished_product_sequence`
- XPath or positional patches: 1

### `quality_check_view_pivot_inherit_mrp_workorder`
- Name: quality.check.view.pivot.inherit.mrp.workorder
- Model: `quality.check`
- Type: inferred from arch
- Inherits: `quality_control.quality_check_view_pivot`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `finished_product_sequence`
- XPath or positional patches: 1

### `quality_check_view_search_inherit_mrp_workorder`
- Name: quality.check.view.search.inherit.mrp.workorder
- Model: `quality.check`
- Type: inferred from arch
- Inherits: `quality_control.quality_check_view_search`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `quality_point_view_search_inherit_mrp_workorder`
- Name: quality.point.view.search.inherit.mrp.workorder
- Model: `quality.point`
- Type: inferred from arch
- Inherits: `quality_control.quality_point_view_search`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `quality_check_view_tree_inherit_mrp_workorder`
- Name: quality.check.view.list.inherit.mrp.workorder
- Model: `quality.check`
- Type: inferred from arch
- Inherits: `quality_control.quality_check_view_tree`
- Root tag: `field`
- Field references: 3
- Sample fields: `finished_lot_ids`, `lot_name`, `operation_id`
- XPath or positional patches: 1

### `quality_check_view_form_inherit_mrp_workorder`
- Name: quality.check.view.form.inherit.mrp.workorder
- Model: `quality.check`
- Type: inferred from arch
- Inherits: `quality_control.quality_check_view_form`
- Root tag: `field`
- Field references: 5
- Sample fields: `finished_lot_ids`, `lot_ids`, `operation_id`, `production_id`, `workorder_id`
- XPath or positional patches: 2

### `quality_check_view_search_inherit_quality_mrp_workorder`
- Name: quality.check.view.search.inherit.quality.mrp.workorder
- Model: `quality.check`
- Type: inferred from arch
- Inherits: `quality_control.quality_check_view_search`
- Root tag: `field`
- Field references: 2
- Sample fields: `finished_lot_ids`, `lot_ids`
- XPath or positional patches: 1

### `quality_alert_view_search_inherit_quality_mrp_workorder`
- Name: quality.alert.view.search.inherit.mrp
- Model: `quality.alert`
- Type: inferred from arch
- Inherits: `quality.quality_alert_view_search`
- Root tag: `field`
- Field references: 2
- Sample fields: `product_id`, `workorder_id`
- XPath or positional patches: 0

### `quality_alert_view_form_inherit_mrp`
- Name: quality.alert.view.form.inherit.mrp
- Model: `quality.alert`
- Type: inferred from arch
- Inherits: `quality_control.quality_alert_view_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `lot_ids`, `workcenter_id`
- XPath or positional patches: 1

## Actions

- `quality_control.quality_check_action_main`: `act_window`
- `quality_control.quality_point_action`: `act_window`
- `quality_check_action_wo`: `act_window` Quality Checks

## Navigation

- **Parent:** [[docs/Enterprise Addons/quality_mrp_workorder/Views]]

