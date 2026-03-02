<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/event_ticket_views.xml

- Module: [[docs/Community Addons/event_product/event_product|event_product]]
- Scope: Community Addons
- Source file: `views/event_ticket_views.xml`
- Views: 6
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `event_event_ticket_form_view`
- Name: event.event.ticket.view.form.inherit.event.product
- Model: `event.event.ticket`
- Type: inferred from arch
- Inherits: `event.event_event_ticket_form_view`
- Root tag: `field`
- Field references: 5
- Sample fields: `end_sale_datetime`, `price`, `price_reduce`, `product_id`, `seats_used`
- XPath or positional patches: 0

### `event_event_ticket_view_kanban_from_event`
- Name: event.event.ticket.view.kanban.from.event.product
- Model: `event.event.ticket`
- Type: inferred from arch
- Inherits: `event.event_event_ticket_view_kanban_from_event`
- Root tag: `field`
- Field references: 3
- Sample fields: `name`, `price`, `product_id`
- XPath or positional patches: 1

### `event_event_ticket_view_form_from_event`
- Name: event.event.ticket.view.form.from.event.inherit.event.product
- Model: `event.event.ticket`
- Type: inferred from arch
- Inherits: `event.event_event_ticket_view_form_from_event`
- Root tag: `field`
- Field references: 4
- Sample fields: `description`, `name`, `price`, `product_id`
- XPath or positional patches: 0

### `event_event_ticket_view_tree_from_event`
- Name: event.event.ticket.view.list.from.event.inherit.event.product
- Model: `event.event.ticket`
- Type: inferred from arch
- Inherits: `event.event_event_ticket_view_tree_from_event`
- Root tag: `field`
- Field references: 6
- Sample fields: `description`, `end_sale_datetime`, `name`, `price`, `product_id`, `start_sale_datetime`
- XPath or positional patches: 0

### `event_type_ticket_view_form_from_type`
- Name: event.type.ticket.view.form.inherit.event.product
- Model: `event.type.ticket`
- Type: inferred from arch
- Inherits: `event.event_type_ticket_view_form_from_type`
- Root tag: `field`
- Field references: 4
- Sample fields: `description`, `name`, `price`, `product_id`
- XPath or positional patches: 0

### `event_type_ticket_view_tree_from_type`
- Name: event.type.ticket.view.list.inherit.event.product
- Model: `event.type.ticket`
- Type: inferred from arch
- Inherits: `event.event_type_ticket_view_tree_from_type`
- Root tag: `field`
- Field references: 4
- Sample fields: `description`, `name`, `price`, `product_id`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/event_product/Views]]

<!-- GENERATED:VIEWFILE -->
