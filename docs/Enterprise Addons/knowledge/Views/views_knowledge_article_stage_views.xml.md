<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/knowledge_article_stage_views.xml

- Module: [[docs/Enterprise Addons/knowledge/knowledge|knowledge]]
- Scope: Enterprise Addons
- Source file: `views/knowledge_article_stage_views.xml`
- Views: 4
- Actions: 6
- Menus: 0
- Rules: 0

## View records

### `knowledge_article_template_stage_view_form`
- Name: knowledge.article.template.stage.view.form
- Model: `knowledge.article.stage`
- Type: inferred from arch
- Inherits: `knowledge.knowledge_article_stage_view_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `knowledge_article_stage_view_search`
- Name: knowledge.article.stage.view.search
- Model: `knowledge.article.stage`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `name`, `parent_id`
- XPath or positional patches: 0

### `knowledge_article_stage_view_tree`
- Name: knowledge.article.stage.view.list
- Model: `knowledge.article.stage`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `fold`, `name`, `parent_id`, `sequence`
- XPath or positional patches: 0

### `knowledge_article_stage_view_form`
- Name: knowledge.article.stage.view.form
- Model: `knowledge.article.stage`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `fold`, `name`, `parent_id`, `sequence`
- XPath or positional patches: 0

## Actions

- `knowledge_article_template_stage_action_view_form`: `view`
- `knowledge_article_template_stage_action_view_tree`: `view`
- `knowledge_article_template_stage_action`: `act_window` Template Stages
- `knowledge_article_stage_action_view_form`: `view`
- `knowledge_article_stage_action_view_tree`: `view`
- `knowledge_article_stage_action`: `act_window` Stages

## Navigation

- **Parent:** [[docs/Enterprise Addons/knowledge/Views]]

<!-- GENERATED:VIEWFILE -->
