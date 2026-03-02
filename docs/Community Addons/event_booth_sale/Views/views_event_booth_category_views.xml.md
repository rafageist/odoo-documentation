<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/event_booth_category_views.xml

- Module: [[docs/Community Addons/event_booth_sale/event_booth_sale|event_booth_sale]]
- Scope: Community Addons
- Source file: `views/event_booth_category_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `event_booth_category_view_tree`
- Name: event.booth.category.view.list.inherit.sale
- Model: `event.booth.category`
- Type: inferred from arch
- Inherits: `event_booth.event_booth_category_view_tree`
- Root tag: `field`
- Field references: 4
- Sample fields: `currency_id`, `name`, `price`, `product_id`
- XPath or positional patches: 0

### `event_booth_category_view_form`
- Name: event.booth.category.view.form.inherit.sale
- Model: `event.booth.category`
- Type: inferred from arch
- Inherits: `event_booth.event_booth_category_view_form`
- Root tag: `group`
- Field references: 3
- Sample fields: `currency_id`, `price`, `product_id`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/event_booth_sale/Views]]

<!-- GENERATED:VIEWFILE -->
