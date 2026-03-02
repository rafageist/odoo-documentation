<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/knowledge_article_views.xml

- Module: [[docs/Enterprise Addons/knowledge/knowledge|knowledge]]
- Scope: Enterprise Addons
- Source file: `views/knowledge_article_views.xml`
- Views: 15
- Actions: 16
- Menus: 0
- Rules: 0

## View records

### `knowledge_article_template_view_form`
- Name: knowledge.article.template.view.form
- Model: `knowledge.article`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `article_properties`, `icon`, `is_article_item`, `parent_id`, `template_body`, `template_category_id`, `template_child_default_create`, `template_description`, `template_name`
- XPath or positional patches: 0

### `knowledge_article_template_view_tree`
- Name: knowledge.article.template.view.list
- Model: `knowledge.article`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `display_name`, `parent_id`, `template_category_id`
- XPath or positional patches: 0

### `knowledge_article_template_view_search`
- Name: knowledge.article.template.view.search
- Model: `knowledge.article`
- Type: inferred from arch
- Root tag: `search`
- Field references: 0
- XPath or positional patches: 0

### `knowledge_article_view_search_items`
- Name: knowledge.article.view.search.embedded
- Model: `knowledge.article`
- Type: inferred from arch
- Root tag: `search`
- Field references: 6
- Sample fields: `article_properties`, `body`, `last_edition_uid`, `name`, `root_article_id`, `stage_id`
- XPath or positional patches: 0

### `knowledge_article_view_search`
- Name: knowledge.article.view.search
- Model: `knowledge.article`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `article_properties`, `body`, `last_edition_uid`, `name`, `root_article_id`
- XPath or positional patches: 0

### `knowledge_article_view_calendar_items`
- Name: knowledge.article.view.calendar.embedded
- Model: `knowledge.article`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 3
- Sample fields: `article_properties`, `parent_id`, `user_can_write`
- XPath or positional patches: 0

### `knowledge_article_view_kanban_items_stages`
- Name: knowledge.article.view.kanban.embedded.stages
- Model: `knowledge.article`
- Type: inferred from arch
- Inherits: `knowledge.knowledge_article_view_kanban_items`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `knowledge_article_view_kanban_items`
- Name: knowledge.article.view.kanban.embedded
- Model: `knowledge.article`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 13
- Sample fields: `activity_ids`, `article_properties`, `cover_image_url`, `create_uid`, `icon`, `is_locked`, `is_template`, `is_user_favorite`, `name`, `parent_id`, and 3 more
- XPath or positional patches: 0

### `knowledge_article_view_kanban`
- Name: knowledge.article.view.kanban
- Model: `knowledge.article`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `activity_ids`, `display_name`, `is_user_favorite`, `parent_id`
- XPath or positional patches: 0

### `knowledge_article_view_tree_items`
- Name: knowledge.article.view.list.embedded
- Model: `knowledge.article`
- Type: inferred from arch
- Root tag: `list`
- Field references: 12
- Sample fields: `article_properties`, `category`, `create_date`, `create_uid`, `display_name`, `favorite_count`, `is_user_favorite`, `last_edition_date`, `last_edition_uid`, `parent_id`, and 2 more
- Buttons: `action_send_to_trash`, `action_toggle_favorite`
- XPath or positional patches: 0

### `knowledge_article_view_form_item_quick_create`
- Name: knowledge.article.view.form.item.quick_create
- Model: `knowledge.article`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `article_properties`, `icon`, `name`, `parent_id`
- XPath or positional patches: 0

### `knowledge_article_view_tree_trash`
- Name: knowledge.article.view.list.trash
- Model: `knowledge.article`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `category`, `deletion_date`, `display_name`, `favorite_count`, `is_user_favorite`, `last_edition_date`, `last_edition_uid`, `parent_id`, `root_article_id`
- Buttons: `action_toggle_favorite`, `action_unarchive`
- XPath or positional patches: 0

### `knowledge_article_view_tree`
- Name: knowledge.article.view.list
- Model: `knowledge.article`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `category`, `create_date`, `create_uid`, `display_name`, `favorite_count`, `is_user_favorite`, `last_edition_date`, `last_edition_uid`, `parent_id`, `root_article_id`
- Buttons: `action_send_to_trash`, `action_toggle_favorite`
- XPath or positional patches: 0

### `knowledge_article_view_hierarchy`
- Name: knowledge.article.view.hierarchy
- Model: `knowledge.article`
- Type: inferred from arch
- Root tag: `hierarchy`
- Field references: 9
- Sample fields: `article_properties`, `category`, `display_name`, `icon`, `id`, `is_user_favorite`, `name`, `parent_id`, `sequence`
- Buttons: `action_toggle_favorite`
- XPath or positional patches: 0

### `knowledge_article_view_form`
- Name: knowledge.article.view.form
- Model: `knowledge.article`
- Type: inferred from arch
- Root tag: `form`
- Field references: 28
- Sample fields: `active`, `article_properties`, `body`, `category`, `cover_image_id`, `cover_image_position`, `cover_image_url`, `create_date`, `create_uid`, `deletion_date`, and 18 more
- XPath or positional patches: 0

## Actions

- `knowledge_article_template_action_view_form`: `view`
- `knowledge_article_template_action_view_tree`: `view`
- `knowledge_article_template_action`: `act_window` Article Templates
- `knowledge_article_action_trashed_tree`: `view`
- `knowledge_article_view_items_tree_stages`: `view`
- `knowledge_article_view_items_kanban_stages`: `view`
- `knowledge_article_item_action_stages`: `act_window` Article Items
- `knowledge_article_view_item_calendar`: `view`
- `knowledge_article_action_item_calendar`: `act_window` Article Items
- `knowledge_article_view_items_tree`: `view`
- `knowledge_article_view_items_kanban`: `view`
- `knowledge_article_item_action`: `act_window` Article Items
- `knowledge_article_action_form_show_resolved`: `act_window` Articles
- `knowledge_article_action_form`: `act_window` Articles
- `knowledge_article_action`: `act_window` Articles
- `knowledge_article_action_trashed`: `act_window` Trash

## Navigation

- **Parent:** [[docs/Enterprise Addons/knowledge/Views]]

<!-- GENERATED:VIEWFILE -->
