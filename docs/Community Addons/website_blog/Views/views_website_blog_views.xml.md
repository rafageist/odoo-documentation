<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/website_blog_views.xml

- Module: [[docs/Community Addons/website_blog/website_blog|website_blog]]
- Scope: Community Addons
- Source file: `views/website_blog_views.xml`
- Views: 7
- Actions: 3
- Menus: 4
- Rules: 0

## View records

### `blog_tag_category_tree`
- Name: blog_tag_category.list
- Model: `blog.tag.category`
- Type: inferred from arch
- Root tag: `list`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `blog_tag_category_form`
- Name: blog_tag_category_form
- Model: `blog.tag.category`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `blog_tag_form`
- Name: blog_tag_form
- Model: `blog.tag`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `category_id`, `color`, `name`, `post_ids`
- XPath or positional patches: 0

### `blog_tag_tree`
- Name: blog_tag.list
- Model: `blog.tag`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `category_id`, `color`, `name`, `post_ids`
- XPath or positional patches: 0

### `blog_blog_view_search`
- Name: blog.blog.search
- Model: `blog.blog`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `view_blog_blog_form`
- Name: blog.blog.form
- Model: `blog.blog`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `active`, `name`, `subtitle`, `website_id`
- XPath or positional patches: 0

### `view_blog_blog_list`
- Name: blog.blog.list
- Model: `blog.blog`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `active`, `blog_post_count`, `name`, `sequence`, `website_id`
- XPath or positional patches: 0

## Actions

- `action_tag_category`: `act_window` Tag Category
- `action_tags`: `act_window` Blog Tags
- `action_blog_blog`: `act_window` Blogs

## Menus

- `menu_website_blog_tag_category_global`: Tag Categories
- `menu_blog_tag_global`: Tags
- `menu_blog_global`: Blogs
- `menu_website_blog_root_global`: Blog

## Navigation

- **Parent:** [[docs/Community Addons/website_blog/Views]]

<!-- GENERATED:VIEWFILE -->
