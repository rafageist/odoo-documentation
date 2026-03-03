---
tags: [odoo, community, generated, views]
---

# views/website_sale_visitor_views.xml

- Module: [[docs/Community Addons/website_sale/website_sale|website_sale]]
- Scope: Community Addons
- Source file: `views/website_sale_visitor_views.xml`
- Views: 8
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `website_sale_visitor_track_view_graph`
- Name: website.track.view.graph
- Model: `website.track`
- Type: inferred from arch
- Inherits: `website.website_visitor_track_view_graph`
- Root tag: `field`
- Field references: 2
- Sample fields: `product_id`, `url`
- XPath or positional patches: 0

### `website_sale_visitor_track_view_tree`
- Name: website.track.view.list
- Model: `website.track`
- Type: inferred from arch
- Inherits: `website.website_visitor_track_view_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `product_id`, `url`
- XPath or positional patches: 0

### `website_sale_visitor_view_kanban`
- Name: website.visitor.view.kanban
- Model: `website.visitor`
- Type: inferred from arch
- Inherits: `website.website_visitor_view_kanban`
- Root tag: `field`
- Field references: 2
- Sample fields: `country_id`, `product_ids`
- XPath or positional patches: 0

### `website_sale_visitor_view_tree`
- Name: website.visitor.view.list
- Model: `website.visitor`
- Type: inferred from arch
- Inherits: `website.website_visitor_view_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `page_ids`, `product_ids`
- XPath or positional patches: 0

### `website_sale_visitor_view_form`
- Name: website.visitor.view.form
- Model: `website.visitor`
- Type: inferred from arch
- Inherits: `website.website_visitor_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `product_ids`, `visitor_product_count`
- Buttons: `%(website_sale.website_sale_visitor_product_action)d`
- XPath or positional patches: 2

### `website_sale_visitor_page_view_search`
- Name: website.track.view.search
- Model: `website.track`
- Type: inferred from arch
- Inherits: `website.website_visitor_page_view_search`
- Root tag: `field`
- Field references: 2
- Sample fields: `product_id`, `url`
- XPath or positional patches: 2

### `website_sale_visitor_page_view_graph`
- Name: website.track.view.graph
- Model: `website.track`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 1
- Sample fields: `product_id`
- XPath or positional patches: 0

### `website_sale_visitor_page_view_tree`
- Name: website.track.view.list
- Model: `website.track`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `product_id`, `visit_datetime`, `visitor_id`
- XPath or positional patches: 0

## Actions

- `website_sale_visitor_product_action`: `act_window` Product Views History

## Navigation

- **Parent:** [[docs/Community Addons/website_sale/Views]]

