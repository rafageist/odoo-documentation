<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/slide_channel_tag_views.xml

- Module: [[docs/Community Addons/website_slides/website_slides|website_slides]]
- Scope: Community Addons
- Source file: `views/slide_channel_tag_views.xml`
- Views: 6
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `slide_channel_tag_group_view_tree`
- Name: slide.channel.tag.group.view.list
- Model: `slide.channel.tag.group`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `is_published`, `name`, `sequence`, `tag_ids`
- XPath or positional patches: 0

### `slide_channel_tag_group_view_form`
- Name: slide.channel.tag.group.view.form
- Model: `slide.channel.tag.group`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `color`, `group_sequence`, `is_published`, `name`, `sequence`, `tag_ids`
- XPath or positional patches: 0

### `slide_channel_tag_group_view_search`
- Name: slide.channel.tag.group.view.search
- Model: `slide.channel.tag.group`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `slide_channel_tag_view_tree`
- Name: slide.channel.tag.view.list
- Model: `slide.channel.tag`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `group_id`, `group_sequence`, `name`, `sequence`
- XPath or positional patches: 0

### `slide_channel_tag_view_form`
- Name: slide.channel.tag.view.form
- Model: `slide.channel.tag`
- Type: inferred from arch
- Root tag: `form`
- Field references: 2
- Sample fields: `group_id`, `name`
- XPath or positional patches: 0

### `slide_channel_tag_view_search`
- Name: slide.channel.tag.view.search
- Model: `slide.channel.tag`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `group_id`, `name`
- XPath or positional patches: 0

## Actions

- `slide_channel_tag_group_action`: `act_window` Course Groups
- `slide_channel_tag_action`: `act_window` Course Tags

## Navigation

- **Parent:** [[docs/Community Addons/website_slides/Views]]

<!-- GENERATED:VIEWFILE -->
