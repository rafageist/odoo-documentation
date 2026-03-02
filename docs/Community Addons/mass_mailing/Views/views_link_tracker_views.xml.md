<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/link_tracker_views.xml

- Module: [[docs/Community Addons/mass_mailing/mass_mailing|mass_mailing]]
- Scope: Community Addons
- Source file: `views/link_tracker_views.xml`
- Views: 7
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `link_tracker_click_view_graph`
- Name: link.tracker.click.view.graph.inherit.mass_mailing
- Model: `link.tracker.click`
- Type: inferred from arch
- Inherits: `link_tracker.link_tracker_click_view_graph`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `campaign_id`, `mass_mailing_id`
- XPath or positional patches: 1

### `link_tracker_click_view_tree`
- Name: link.tracker.click.view.list.inherit.mass_mailing
- Model: `link.tracker.click`
- Type: inferred from arch
- Inherits: `link_tracker.link_tracker_click_view_tree`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `campaign_id`, `mass_mailing_id`
- XPath or positional patches: 1

### `link_tracker_click_view_form`
- Name: link.tracker.click.view.form.inherit.mass_mailing
- Model: `link.tracker.click`
- Type: inferred from arch
- Inherits: `link_tracker.link_tracker_click_view_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `campaign_id`, `mailing_trace_id`, `mass_mailing_id`
- XPath or positional patches: 1

### `link_tracker_click_view_search`
- Name: link.tracker.click.view.search.inherit.mass_mailing
- Model: `link.tracker.click`
- Type: inferred from arch
- Inherits: `link_tracker.link_tracker_click_view_search`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `campaign_id`, `mass_mailing_id`
- XPath or positional patches: 2

### `link_tracker_view_tree`
- Name: link.tracker.view.list.inherit.mass.mail
- Model: `link.tracker`
- Type: inferred from arch
- Inherits: `link_tracker.link_tracker_view_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `mass_mailing_id`
- XPath or positional patches: 1

### `link_tracker_view_form`
- Name: link.tracker.view.form.inherit.mass.mail
- Model: `link.tracker`
- Type: inferred from arch
- Inherits: `link_tracker.link_tracker_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `mass_mailing_id`
- XPath or positional patches: 1

### `link_tracker_view_search`
- Name: link.tracker.view.search.inherit.mass.mail
- Model: `link.tracker`
- Type: inferred from arch
- Inherits: `link_tracker.link_tracker_view_search`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `mass_mailing_id`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Community Addons/mass_mailing/Views]]

<!-- GENERATED:VIEWFILE -->
