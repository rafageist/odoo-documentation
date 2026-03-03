---
tags: [odoo, community, generated, views]
---

# views/website_visitor_views.xml

- Module: [[docs/Community Addons/website/website|website]]
- Scope: Community Addons
- Source file: `views/website_visitor_views.xml`
- Views: 10
- Actions: 4
- Menus: 2
- Rules: 0

## View records

### `website_visitor_track_view_graph`
- Name: website.track.view.graph
- Model: `website.track`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 1
- Sample fields: `url`
- XPath or positional patches: 0

### `website_visitor_track_view_tree`
- Name: website.track.view.list
- Model: `website.track`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `page_id`, `url`, `visit_datetime`, `visitor_id`
- XPath or positional patches: 0

### `website_visitor_view_graph`
- Name: website.visitor.view.graph
- Model: `website.visitor`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 1
- Sample fields: `last_connection_datetime`
- XPath or positional patches: 0

### `website_visitor_view_search`
- Name: website.visitor.view.search
- Model: `website.visitor`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `country_id`, `lang_id`, `name`, `page_ids`, `visit_count`
- XPath or positional patches: 0

### `website_visitor_view_tree`
- Name: website.visitor.view.list
- Model: `website.visitor`
- Type: inferred from arch
- Root tag: `list`
- Field references: 11
- Sample fields: `country_flag`, `country_id`, `create_date`, `display_name`, `email`, `is_connected`, `lang_id`, `last_connection_datetime`, `last_visited_page_id`, `page_ids`, and 1 more
- Buttons: `action_send_mail`
- XPath or positional patches: 0

### `website_visitor_view_form`
- Name: website.visitor.view.form
- Model: `website.visitor`
- Type: inferred from arch
- Root tag: `form`
- Field references: 14
- Sample fields: `country_flag`, `country_id`, `create_date`, `display_name`, `email`, `is_connected`, `lang_id`, `last_connection_datetime`, `mobile`, `page_ids`, and 4 more
- Buttons: `%(website.website_visitor_page_action)d`, `action_send_mail`
- XPath or positional patches: 0

### `website_visitor_view_kanban`
- Name: website.visitor.view.kanban
- Model: `website.visitor`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 11
- Sample fields: `country_flag`, `country_id`, `display_name`, `email`, `is_connected`, `last_visited_page_id`, `page_count`, `partner_id`, `partner_image`, `time_since_last_action`, and 1 more
- Buttons: `action_send_mail`
- XPath or positional patches: 0

### `website_visitor_page_view_search`
- Name: website.track.view.search
- Model: `website.track`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `page_id`, `url`, `visit_datetime`, `visitor_id`
- XPath or positional patches: 0

### `website_visitor_page_view_graph`
- Name: website.track.view.graph
- Model: `website.track`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 1
- Sample fields: `url`
- XPath or positional patches: 0

### `website_visitor_page_view_tree`
- Name: website.track.view.list
- Model: `website.track`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `page_id`, `url`, `visit_datetime`, `visitor_id`
- XPath or positional patches: 0

## Actions

- `website_visitor_view_action`: `act_window` Page Views
- `website_visitors_action`: `act_window` Visitors
- `website.visitor_partner_action`: `act_window` Partners
- `website_visitor_page_action`: `act_window` Page Views History

## Menus

- `menu_visitor_view_menu`: Page Views
- `website_visitor_menu`: Visitors

## Navigation

- **Parent:** [[docs/Community Addons/website/Views]]

