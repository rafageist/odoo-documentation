<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/forum_forum_views.xml

- Module: [[docs/Community Addons/website_forum/website_forum|website_forum]]
- Scope: Community Addons
- Source file: `views/forum_forum_views.xml`
- Views: 4
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `forum_forum_view_search`
- Name: forum.forum.view.search
- Model: `forum.forum`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `forum_forum_view_form_add`
- Name: forum.forum.view.form.add
- Model: `forum.forum`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `authorized_group_id`, `mode`, `name`, `privacy`
- XPath or positional patches: 0

### `forum_forum_view_form`
- Name: forum.forum.view.form
- Model: `forum.forum`
- Type: inferred from arch
- Root tag: `form`
- Field references: 47
- Sample fields: `active`, `authorized_group_id`, `default_order`, `description`, `image_1920`, `karma_answer`, `karma_answer_accept_all`, `karma_answer_accept_own`, `karma_ask`, `karma_close_all`, and 37 more
- Buttons: `%(forum_post_action_favorites)d`, `%(forum_post_action_forum_main)d`, `go_to_website`
- XPath or positional patches: 0

### `forum_forum_view_tree`
- Name: forum.forum.view.list
- Model: `forum.forum`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `active`, `name`, `sequence`, `total_answers`, `total_favorites`, `total_posts`, `total_views`, `website_id`
- XPath or positional patches: 0

## Actions

- `forum_forum_action_add`: `act_window` New Forum
- `forum_forum_action`: `act_window` Forums

## Navigation

- **Parent:** [[docs/Community Addons/website_forum/Views]]

<!-- GENERATED:VIEWFILE -->
