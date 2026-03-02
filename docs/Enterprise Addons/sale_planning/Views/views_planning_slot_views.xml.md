<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/planning_slot_views.xml

- Module: [[docs/Enterprise Addons/sale_planning/sale_planning|sale_planning]]
- Scope: Enterprise Addons
- Source file: `views/planning_slot_views.xml`
- Views: 10
- Actions: 10
- Menus: 1
- Rules: 0

## View records

### `planning_action_schedule_by_sale_order_item_view_graph_inherit`
- Name: planning.action.schedule.by.sale.order.graph.inherit
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_action_schedule_by_resource_view_graph_inherit`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `sale_line_id`
- XPath or positional patches: 1

### `planning_action_schedule_by_sale_order_item_view_pivot_inherit`
- Name: planning.action.schedule.by.sale.order.pivot.inherit
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_pivot`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `resource_id`, `sale_line_id`
- XPath or positional patches: 1

### `planning_view_form_in_gantt_inherit_sale_planning`
- Name: planning.slot.form.gantt
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_form_in_gantt`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `sale_line_plannable`
- Buttons: `action_unschedule`
- XPath or positional patches: 1

### `planning_slot_view_kanban_inherit_sale_planning`
- Name: planning.slot.kanban.inherit.sale.planning
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_kanban`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `allocated_hours`, `allocated_percentage`, `sale_line_id`
- XPath or positional patches: 3

### `planning_slot_view_tree_inherit_sale_planning`
- Name: planning.slot.list.inherit.sale.planning
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_tree`
- Root tag: `field`
- Field references: 6
- Sample fields: `allocated_hours`, `company_id`, `resource_id`, `sale_line_id`, `sale_line_plannable`, `start_datetime`
- XPath or positional patches: 0

### `planning_slot_view_calendar_inherit_sale_planning`
- Name: planning.slot.calendar.inherit.sale.planning
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_calendar`
- Root tag: `field`
- Field references: 2
- Sample fields: `role_id`, `sale_line_id`
- XPath or positional patches: 0

### `planning_view_gantt_group_by_sale_order_item`
- Name: planning.slot.gantt
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning_slot_view_gantt_inherit_sale_planning`
- Root tag: `gantt`
- Field references: 0
- XPath or positional patches: 1

### `planning_slot_view_gantt_inherit_sale_planning`
- Name: planning.slot.gantt.inherit.sale.planning
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_gantt`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `sale_line_plannable`
- XPath or positional patches: 2

### `planning_slot_view_form_inherit_sale_planning`
- Name: planning.slot.form.inherit.sale.planning
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_form`
- Root tag: `field`
- Field references: 7
- Sample fields: `end_datetime`, `role_id`, `sale_line_id`, `sale_line_plannable`, `sale_order_id`, `sale_order_state`, `start_datetime`
- Buttons: `action_view_sale_order`
- XPath or positional patches: 1

### `planning_slot_view_search_inherit_sale_planning`
- Name: planning.slot.search.inherit.sale.planning
- Model: `planning.slot`
- Type: inferred from arch
- Inherits: `planning.planning_view_search_base`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `sale_order_id`
- XPath or positional patches: 4

## Actions

- `planning_action_schedule_by_sale_order_item_view_graph`: `view`
- `planning_action_schedule_by_sale_order_item_view_pivot`: `view`
- `planning_action_schedule_by_sale_order_item_view_kanban`: `view`
- `planning_action_schedule_by_sale_order_item_view_tree`: `view`
- `planning_action_schedule_by_sale_order_item_view_calendar`: `view`
- `planning_action_schedule_by_sale_order_item_view_gantt`: `view`
- `sale_planning_action_schedule_by_sale_order`: `act_window` Schedule by Sales Order
- `planning.planning_action_schedule_by_role`: `act_window`
- `planning.planning_action_schedule_by_resource`: `act_window`
- `planning.planning_action_my_calendar`: `act_window`

## Menus

- `sale_planning_menu_schedule_by_sale_order`: By Sales Order

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_planning/Views]]

<!-- GENERATED:VIEWFILE -->
