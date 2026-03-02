<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/slide_channel_partner_views.xml

- Module: [[docs/Community Addons/website_slides/website_slides|website_slides]]
- Scope: Community Addons
- Source file: `views/slide_channel_partner_views.xml`
- Views: 5
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `slide_channel_partner_view_pivot`
- Name: slide.channel.partner.view.pivot
- Model: `slide.channel.partner`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 1
- Sample fields: `completion`
- XPath or positional patches: 0

### `slide_channel_partner_view_graph`
- Name: slide.channel.partner.view.graph
- Model: `slide.channel.partner`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 0
- XPath or positional patches: 0

### `slide_channel_partner_view_kanban`
- Name: slide.channel.partner.view.kanban
- Model: `slide.channel.partner`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `channel_id`, `channel_user_id`, `completion`, `partner_id`
- XPath or positional patches: 0

### `slide_channel_partner_view_tree`
- Name: slide.channel.partner.list
- Model: `slide.channel.partner`
- Type: inferred from arch
- Root tag: `list`
- Field references: 15
- Sample fields: `active`, `channel_enroll`, `channel_id`, `channel_type`, `channel_user_id`, `channel_visibility`, `channel_website_id`, `completion`, `create_date`, `last_invitation_date`, and 5 more
- Buttons: `action_archive`, `action_unarchive`
- XPath or positional patches: 0

### `slide_channel_partner_view_search`
- Name: slide.channel.partner.search
- Model: `slide.channel.partner`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `channel_id`, `partner_email`, `partner_id`
- XPath or positional patches: 0

## Actions

- `slide_channel_partner_action_report`: `act_window` Attendees
- `slide_channel_partner_action`: `act_window` Attendees

## Navigation

- **Parent:** [[docs/Community Addons/website_slides/Views]]

<!-- GENERATED:VIEWFILE -->
