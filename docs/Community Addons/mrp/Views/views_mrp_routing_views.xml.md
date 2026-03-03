---
tags: [odoo, community, generated, views]
---

# views/mrp_routing_views.xml

- Module: [[docs/Community Addons/mrp/mrp|mrp]]
- Scope: Community Addons
- Source file: `views/mrp_routing_views.xml`
- Views: 6
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `mrp_routing_workcenter_filter`
- Name: mrp.routing.workcenter.filter
- Model: `mrp.routing.workcenter`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `bom_id`, `name`, `workcenter_id`
- XPath or positional patches: 0

### `mrp_routing_workcenter_kanban_view`
- Name: mrp.routing.workcenter.kanban
- Model: `mrp.routing.workcenter`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 2
- Sample fields: `name`, `workcenter_id`
- XPath or positional patches: 0

### `mrp_routing_workcenter_form_view`
- Name: mrp.routing.workcenter.form
- Model: `mrp.routing.workcenter`
- Type: inferred from arch
- Root tag: `form`
- Field references: 17
- Sample fields: `active`, `allow_operation_dependencies`, `blocked_by_operation_ids`, `bom_id`, `bom_product_template_attribute_value_ids`, `company_id`, `cost_mode`, `cycle_number`, `name`, `possible_bom_product_template_attribute_value_ids`, and 7 more
- XPath or positional patches: 0

### `mrp_routing_workcenter_copy_to_bom_tree_view`
- Name: mrp.routing.workcenter.copy_to_bom.list
- Model: `mrp.routing.workcenter`
- Type: inferred from arch
- Inherits: `mrp_routing_workcenter_tree_view`
- Root tag: `xpath`
- Field references: 0
- Buttons: `copy_to_bom`
- XPath or positional patches: 2

### `mrp_routing_workcenter_bom_tree_view`
- Name: mrp.routing.workcenter.bom.list
- Model: `mrp.routing.workcenter`
- Type: inferred from arch
- Inherits: `mrp_routing_workcenter_tree_view`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `blocked_by_operation_ids`, `bom_id`, `sequence`
- Buttons: `action_open_operation_form`, `copy_existing_operations`
- XPath or positional patches: 7

### `mrp_routing_workcenter_tree_view`
- Name: mrp.routing.workcenter.list
- Model: `mrp.routing.workcenter`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `active`, `blocked_by_operation_ids`, `bom_id`, `bom_product_template_attribute_value_ids`, `company_id`, `name`, `possible_bom_product_template_attribute_value_ids`, `time_cycle`, `time_total`, `workcenter_id`
- XPath or positional patches: 0

## Actions

- `mrp_routing_action`: `act_window` Operations

## Menus

- `menu_mrp_routing_action`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/mrp/Views]]

