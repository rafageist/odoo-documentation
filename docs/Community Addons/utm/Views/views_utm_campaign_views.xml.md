---
tags: [odoo, community, generated, views]
---

# views/utm_campaign_views.xml

- Module: [[docs/Community Addons/utm/utm|utm]]
- Scope: Community Addons
- Source file: `views/utm_campaign_views.xml`
- Views: 5
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `utm_campaign_view_kanban`
- Name: utm.campaign.view.kanban
- Model: `utm.campaign`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 6
- Sample fields: `active`, `color`, `stage_id`, `tag_ids`, `title`, `user_id`
- XPath or positional patches: 0

### `utm_campaign_view_form_quick_create`
- Name: utm.campaign.view.form.quick.create
- Model: `utm.campaign`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `name`, `tag_ids`, `title`, `user_id`
- XPath or positional patches: 0

### `utm_campaign_view_tree`
- Name: utm.campaign.view.list
- Model: `utm.campaign`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `name`, `stage_id`, `tag_ids`, `title`, `user_id`
- XPath or positional patches: 0

### `utm_campaign_view_form`
- Name: utm.campaign.view.form
- Model: `utm.campaign`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `active`, `name`, `stage_id`, `tag_ids`, `title`, `user_id`
- XPath or positional patches: 0

### `view_utm_campaign_view_search`
- Name: utm.campaign.view.search
- Model: `utm.campaign`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `is_auto_campaign`, `tag_ids`, `title`, `user_id`
- XPath or positional patches: 0

## Actions

- `utm_campaign_action`: `act_window` Campaigns

## Navigation

- **Parent:** [[docs/Community Addons/utm/Views]]

