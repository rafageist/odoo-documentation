<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/event_booth_views.xml

- Module: [[docs/Community Addons/event_booth_sale/event_booth_sale|event_booth_sale]]
- Scope: Community Addons
- Source file: `views/event_booth_views.xml`
- Views: 5
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `event_booth_view_pivot`
- Name: event.booth.event.booth.view.pivot.inherit.sale
- Model: `event.booth`
- Type: inferred from arch
- Inherits: `event_booth.event_booth_view_pivot`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `price`
- XPath or positional patches: 1

### `event_booth_view_graph`
- Name: event.booth.event.booth.view.graph.inherit.sale
- Model: `event.booth`
- Type: inferred from arch
- Inherits: `event_booth.event_booth_view_graph`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `price`
- XPath or positional patches: 1

### `event_booth_view_search`
- Name: event.booth.view.search.inherit.sale
- Model: `event.booth`
- Type: inferred from arch
- Inherits: `event_booth.event_booth_view_search`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `sale_order_id`
- XPath or positional patches: 2

### `event_booth_view_tree_from_event`
- Name: event.booth.view.list.from.event.inherit.sale
- Model: `event.booth`
- Type: inferred from arch
- Inherits: `event_booth.event_booth_view_tree_from_event`
- Root tag: `field`
- Field references: 3
- Sample fields: `currency_id`, `partner_id`, `price`
- XPath or positional patches: 0

### `event_booth_view_form_from_event`
- Name: event.booth.view.form.inherit.sale
- Model: `event.booth`
- Type: inferred from arch
- Inherits: `event_booth.event_booth_view_form_from_event`
- Root tag: `div`
- Field references: 8
- Sample fields: `booth_category_id`, `currency_id`, `event_booth_registration_ids`, `is_paid`, `price`, `product_id`, `sale_order_id`, `sale_order_line_id`
- Buttons: `action_view_sale_order`
- XPath or positional patches: 4

## Navigation

- **Parent:** [[docs/Community Addons/event_booth_sale/Views]]

<!-- GENERATED:VIEWFILE -->
