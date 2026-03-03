---
tags: [odoo, community, generated, views]
---

# views/link_tracker_views.xml

- Module: [[docs/Community Addons/link_tracker/link_tracker|link_tracker]]
- Scope: Community Addons
- Source file: `views/link_tracker_views.xml`
- Views: 8
- Actions: 3
- Menus: 1
- Rules: 0

## View records

### `link_tracker_click_view_graph`
- Name: link.tracker.click.view.graph
- Model: `link.tracker.click`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `country_id`, `ip`, `link_id`
- XPath or positional patches: 0

### `link_tracker_click_view_tree`
- Name: link.tracker.click.view.list
- Model: `link.tracker.click`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `country_id`, `ip`, `link_id`
- XPath or positional patches: 0

### `link_tracker_click_view_form`
- Name: link.tracker.click.view.form
- Model: `link.tracker.click`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `country_id`, `ip`, `link_id`
- XPath or positional patches: 0

### `link_tracker_click_view_search`
- Name: link.tracker.click.view.search
- Model: `link.tracker.click`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `country_id`, `link_id`
- XPath or positional patches: 0

### `link_tracker_view_graph`
- Name: link.tracker.view.graph
- Model: `link.tracker`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `count`, `url`
- XPath or positional patches: 0

### `link_tracker_view_tree`
- Name: link.tracker.view.list
- Model: `link.tracker`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `campaign_id`, `count`, `create_date`, `label`, `medium_id`, `short_url`, `source_id`, `title`, `url`
- XPath or positional patches: 0

### `link_tracker_view_form`
- Name: link.tracker.view.form
- Model: `link.tracker`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `campaign_id`, `code`, `count`, `label`, `medium_id`, `short_url_host`, `source_id`, `title`, `url`
- Buttons: `action_view_statistics`, `action_visit_page`
- XPath or positional patches: 0

### `link_tracker_view_search`
- Name: link.tracker.view.search
- Model: `link.tracker`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `campaign_id`, `label`, `medium_id`, `source_id`, `url`
- XPath or positional patches: 0

## Actions

- `link_tracker_action_campaign`: `act_window` Statistics of Clicks
- `link_tracker_click_action_statistics`: `act_window` Click Statistics
- `link_tracker_action`: `act_window` Link Tracker

## Menus

- `link_tracker_menu_main`: Link Tracker

## Navigation

- **Parent:** [[docs/Community Addons/link_tracker/Views]]

