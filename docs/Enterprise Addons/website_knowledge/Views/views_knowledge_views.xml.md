<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/knowledge_views.xml

- Module: [[docs/Enterprise Addons/website_knowledge/website_knowledge|website_knowledge]]
- Scope: Enterprise Addons
- Source file: `views/knowledge_views.xml`
- Views: 3
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `knowledge_article_view_search`
- Name: knowledge.article.view.search.inherit.website
- Model: `knowledge.article`
- Type: inferred from arch
- Inherits: `knowledge.knowledge_article_view_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `knowledge_article_view_tree`
- Name: knowledge.article.view.list.inherit.website
- Model: `knowledge.article`
- Type: inferred from arch
- Inherits: `knowledge.knowledge_article_view_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `last_edition_date`, `website_published`
- XPath or positional patches: 0

### `knowledge_article_view_form`
- Name: knowledge.article.view.form.inherit.website
- Model: `knowledge.article`
- Type: inferred from arch
- Inherits: `knowledge.knowledge_article_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `article_url`, `website_published`
- XPath or positional patches: 1

## Actions

- `knowledge_action_unpublish_articles`: `server` Unpublish Articles
- `knowledge_action_publish_articles`: `server` Publish Articles

## Navigation

- **Parent:** [[docs/Enterprise Addons/website_knowledge/Views]]

<!-- GENERATED:VIEWFILE -->
