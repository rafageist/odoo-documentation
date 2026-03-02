<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/tour_views.xml

- Module: [[docs/Community Addons/web_tour/web_tour|web_tour]]
- Scope: Community Addons
- Source file: `views/tour_views.xml`
- Views: 3
- Actions: 2
- Menus: 1
- Rules: 0

## View records

### `tour_search`
- Name: tour.search
- Model: `web_tour.tour`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `tour_list`
- Name: unnamed
- Model: `web_tour.tour`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `custom`, `name`, `rainbow_man_message`, `sequence`, `url`
- XPath or positional patches: 0

### `tour_form`
- Name: unnamed
- Model: `web_tour.tour`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `content`, `custom`, `name`, `rainbow_man_message`, `run`, `sequence`, `sharing_url`, `step_ids`, `tooltip_position`, `trigger`, and 1 more
- XPath or positional patches: 0

## Actions

- `tour_export_js_action`: `server` Export JS
- `tour_action`: `act_window` Tours

## Menus

- `menu_tour_action`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/web_tour/Views]]

<!-- GENERATED:VIEWFILE -->
