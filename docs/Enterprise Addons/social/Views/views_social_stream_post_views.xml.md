---
tags: [odoo, enterprise, generated, views]
---

# views/social_stream_post_views.xml

- Module: [[docs/Enterprise Addons/social/social|social]]
- Scope: Enterprise Addons
- Source file: `views/social_stream_post_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `social_stream_post_view_search`
- Name: social.stream.post.view.search
- Model: `social.stream.post`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `message`
- XPath or positional patches: 0

### `social_stream_post_view_kanban`
- Name: social.stream.post.view.kanban
- Model: `social.stream.post`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 13
- Sample fields: `author_link`, `author_name`, `formatted_published_date`, `link_description`, `link_image_url`, `link_title`, `link_url`, `message`, `post_link`, `published_date`, and 3 more
- XPath or positional patches: 0

## Actions

- `action_social_stream_post`: `act_window` Feed

## Menus

- `menu_social_stream_post`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/social/Views]]

