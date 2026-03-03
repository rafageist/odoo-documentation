---
tags: [odoo, community, generated, views]
---

# views/forum_post_views.xml

- Module: [[docs/Community Addons/website_forum/website_forum|website_forum]]
- Scope: Community Addons
- Source file: `views/forum_post_views.xml`
- Views: 5
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `forum_post_view_kanban`
- Name: Forum Post Pages Kanban
- Model: `forum.post`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 7
- Sample fields: `child_count`, `create_uid`, `forum_id`, `name`, `parent_id`, `views`, `website_id`
- XPath or positional patches: 0

### `forum_post_view_tree`
- Name: forum.post.view.list
- Model: `forum.post`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `active`, `child_count`, `forum_id`, `is_seo_optimized`, `name`, `state`, `views`, `website_id`, `website_url`
- XPath or positional patches: 0

### `forum_post_view_graph`
- Name: forum.post.view.graph
- Model: `forum.post`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `forum_id`, `write_date`
- XPath or positional patches: 0

### `forum_post_view_search`
- Name: forum.post.view.search
- Model: `forum.post`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `create_uid`, `forum_id`, `name`, `tag_ids`
- XPath or positional patches: 0

### `forum_post_view_form`
- Name: forum.post.view.form
- Model: `forum.post`
- Type: inferred from arch
- Root tag: `form`
- Field references: 21
- Sample fields: `active`, `child_count`, `child_ids`, `closed_date`, `closed_reason_id`, `closed_uid`, `create_date`, `create_uid`, `favourite_count`, `forum_id`, and 11 more
- Buttons: `go_to_website`
- XPath or positional patches: 0

## Actions

- `forum_post_action_forum_main`: `act_window` Posts
- `forum_post_action_favorites`: `act_window` Users favorite posts
- `forum_post_action`: `act_window` Forum Post Pages

## Navigation

- **Parent:** [[docs/Community Addons/website_forum/Views]]

