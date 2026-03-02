<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/forum_forum_views.xml

- Module: [[docs/Community Addons/website_slides_forum/website_slides_forum|website_slides_forum]]
- Scope: Community Addons
- Source file: `views/forum_forum_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `forum_forum_view_tree_slides`
- Name: forum.forum.view.list.slides
- Model: `forum.forum`
- Type: inferred from arch
- Inherits: `website_forum.forum_forum_view_tree`
- Root tag: `field`
- Field references: 3
- Sample fields: `slide_channel_id`, `visibility`, `website_id`
- XPath or positional patches: 0

### `forum_forum_view_form`
- Name: forum.forum.view.form.inherit.slides
- Model: `forum.forum`
- Type: inferred from arch
- Inherits: `website_forum.forum_forum_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `slide_channel_id`, `visibility`
- XPath or positional patches: 4

## Actions

- `forum_forum_action_channel`: `act_window` Forums

## Navigation

- **Parent:** [[docs/Community Addons/website_slides_forum/Views]]

<!-- GENERATED:VIEWFILE -->
