<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/website_pages_views.xml

- Module: [[docs/Community Addons/website_blog/website_blog|website_blog]]
- Scope: Community Addons
- Source file: `views/website_pages_views.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `view_blog_post_list`
- Name: Blog Post Pages List
- Model: `blog.post`
- Type: inferred from arch
- Root tag: `list`
- Field references: 11
- Sample fields: `active`, `author_id`, `blog_id`, `create_uid`, `is_published`, `is_seo_optimized`, `name`, `website_id`, `website_url`, `write_date`, and 1 more
- XPath or positional patches: 0

### `view_blog_post_search`
- Name: blog.post.search
- Model: `blog.post`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `blog_id`, `name`, `write_uid`
- XPath or positional patches: 0

### `blog_post_view_kanban`
- Name: blog.post.kanban
- Model: `blog.post`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 6
- Sample fields: `author_id`, `blog_id`, `is_published`, `name`, `post_date`, `website_id`
- XPath or positional patches: 0

### `view_blog_post_form`
- Name: blog.post.form
- Model: `blog.post`
- Type: inferred from arch
- Root tag: `form`
- Field references: 16
- Sample fields: `active`, `author_id`, `blog_id`, `create_date`, `is_published`, `name`, `post_date`, `subtitle`, `tag_ids`, `visits`, and 6 more
- XPath or positional patches: 0

## Actions

- `action_blog_post`: `act_window` Blog Post Pages

## Menus

- `menu_blog_post_pages`: Blog Posts

## Navigation

- **Parent:** [[docs/Community Addons/website_blog/Views]]

<!-- GENERATED:VIEWFILE -->
