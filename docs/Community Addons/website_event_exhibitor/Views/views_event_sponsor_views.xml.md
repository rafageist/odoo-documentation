---
tags: [odoo, community, generated, views]
---

# views/event_sponsor_views.xml

- Module: [[docs/Community Addons/website_event_exhibitor/website_event_exhibitor|website_event_exhibitor]]
- Scope: Community Addons
- Source file: `views/event_sponsor_views.xml`
- Views: 6
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `event_sponsor_view_kanban`
- Name: event.sponsor.view.kanban
- Model: `event.sponsor`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 6
- Sample fields: `exhibitor_type`, `image_128`, `name`, `partner_email`, `sponsor_type_id`, `url`
- XPath or positional patches: 0

### `event_sponsor_view_tree`
- Name: event.sponsor.view.list
- Model: `event.sponsor`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `email`, `exhibitor_type`, `is_published`, `name`, `partner_id`, `phone`, `sequence`, `show_on_ticket`, `sponsor_type_id`, `url`
- XPath or positional patches: 0

### `event_sponsor_view_form`
- Name: event.sponsor.view.form
- Model: `event.sponsor`
- Type: inferred from arch
- Root tag: `form`
- Field references: 19
- Sample fields: `active`, `email`, `event_date_tz`, `event_id`, `exhibitor_type`, `hour_from`, `hour_to`, `image_512`, `is_published`, `name`, and 9 more
- XPath or positional patches: 0

### `event_sponsor_view_search`
- Name: event.sponsor.search
- Model: `event.sponsor`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `email`, `event_id`, `name`, `partner_id`, `phone`
- XPath or positional patches: 0

### `event_sponsor_type_view_tree`
- Name: Sponsor Levels
- Model: `event.sponsor.type`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `display_ribbon_style`, `name`, `sequence`
- XPath or positional patches: 0

### `event_sponsor_type_view_form`
- Name: Sponsor Levels
- Model: `event.sponsor.type`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `display_ribbon_style`, `name`, `sequence`
- XPath or positional patches: 0

## Actions

- `event_sponsor_action_from_event`: `act_window` Event Sponsors
- `event_sponsor_action`: `act_window` Event Sponsors
- `event_sponsor_type_action`: `act_window` Sponsor Levels

## Navigation

- **Parent:** [[docs/Community Addons/website_event_exhibitor/Views]]

