---
tags: [odoo, enterprise, generated, views]
---

# views/frontdesk_visitor_views.xml

- Module: [[docs/Enterprise Addons/frontdesk/frontdesk|frontdesk]]
- Scope: Enterprise Addons
- Source file: `views/frontdesk_visitor_views.xml`
- Views: 8
- Actions: 7
- Menus: 0
- Rules: 0

## View records

### `frontdesk_visitor_view_search`
- Name: frontdesk.visitor.view.search
- Model: `frontdesk.visitor`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `host_ids`, `name`, `station_id`
- XPath or positional patches: 0

### `frontdesk_visitor_view_gantt`
- Name: frontdesk.visitor.view.gantt
- Model: `frontdesk.visitor`
- Type: inferred from arch
- Root tag: `gantt`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `frontdesk_visitor_view_calendar`
- Name: frontdesk.visitor.view.calendar
- Model: `frontdesk.visitor`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `frontdesk_visitor_view_pivot`
- Name: frontdesk.visitor.view.pivot
- Model: `frontdesk.visitor`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `drink_ids`, `station_id`
- XPath or positional patches: 0

### `frontdesk_visitor_view_graph`
- Name: frontdesk.visitor.view.graph
- Model: `frontdesk.visitor`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `duration`, `station_id`
- XPath or positional patches: 0

### `frontdesk_visitor_view_kanban`
- Name: frontdesk.visitor.view.kanban
- Model: `frontdesk.visitor`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `check_in`, `host_ids`, `name`, `state`, `station_id`
- XPath or positional patches: 0

### `frontdesk_visitor_view_form`
- Name: frontdesk.visitor.view.form
- Model: `frontdesk.visitor`
- Type: inferred from arch
- Root tag: `form`
- Field references: 15
- Sample fields: `active`, `check_in`, `company`, `company_id`, `drink_ids`, `duration`, `email`, `host_ids`, `message`, `name`, and 5 more
- Buttons: `action_canceled`, `action_check_in`, `action_check_out`, `action_planned`
- XPath or positional patches: 0

### `frontdesk_visitor_view_tree`
- Name: frontdesk.visitor.view.list
- Model: `frontdesk.visitor`
- Type: inferred from arch
- Root tag: `list`
- Field references: 14
- Sample fields: `check_in`, `check_out`, `company`, `company_id`, `drink_ids`, `duration`, `email`, `host_ids`, `name`, `phone`, and 4 more
- Buttons: `%(frontdesk_visitor_print_badge)d`, `action_check_in`, `action_check_out`, `action_served`
- XPath or positional patches: 0

## Actions

- `frontdesk_visitor_action_configure_properties_field`: `client` Add Properties
- `action_open_drink_to_serve_visitor`: `act_window` Drinks to Serve
- `action_open_planned_visitor`: `act_window` Planned
- `action_open_guest_on_site_visitor`: `act_window` Guest On Site
- `action_open_station_visitor`: `act_window` Station Visitors
- `action_frontdesk_visitor`: `act_window` Visitors
- `frontdesk_visitor_print_badge`: `report` Print Visitor Badge

## Navigation

- **Parent:** [[docs/Enterprise Addons/frontdesk/Views]]

