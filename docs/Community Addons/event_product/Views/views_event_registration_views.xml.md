<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/event_registration_views.xml

- Module: [[docs/Community Addons/event_product/event_product|event_product]]
- Scope: Community Addons
- Source file: `views/event_registration_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `event_registration_ticket_view_form`
- Name: event.registration.form.inherit
- Model: `event.registration`
- Type: inferred from arch
- Inherits: `event.view_event_registration_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `event_registration_view_graph`
- Name: event.registration.graph.inherit.event.sale
- Model: `event.registration`
- Type: inferred from arch
- Inherits: `event.view_event_registration_graph`
- Root tag: `field`
- Field references: 2
- Sample fields: `event_id`, `sale_status`
- XPath or positional patches: 0

### `view_event_registration_ticket_tree`
- Name: event.registration.list.inherit
- Model: `event.registration`
- Type: inferred from arch
- Inherits: `event.view_event_registration_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `sale_status`, `state`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/event_product/Views]]

<!-- GENERATED:VIEWFILE -->
