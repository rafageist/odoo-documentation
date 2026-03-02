<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/event_registration_views.xml

- Module: [[docs/Community Addons/event_sale/event_sale|event_sale]]
- Scope: Community Addons
- Source file: `views/event_registration_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `event_registration_ticket_view_form`
- Name: event.registration.form.inherit
- Model: `event.registration`
- Type: inferred from arch
- Inherits: `event_product.event_registration_ticket_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `sale_order_id`, `sale_order_line_id`
- Buttons: `action_view_sale_order`
- XPath or positional patches: 2

### `view_event_registration_ticket_tree`
- Name: event.registration.list.inherit
- Model: `event.registration`
- Type: inferred from arch
- Inherits: `event.view_event_registration_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `event_id`, `sale_order_id`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/event_sale/Views]]

<!-- GENERATED:VIEWFILE -->
