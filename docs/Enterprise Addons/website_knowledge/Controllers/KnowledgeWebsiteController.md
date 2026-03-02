<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, enterprise, generated, controller]
---

# KnowledgeWebsiteController

- Module: [[docs/Enterprise Addons/website_knowledge/website_knowledge|website_knowledge]]
- Scope: Enterprise Addons
- Source file: `controllers/main.py`
- Base classes: `KnowledgeController`
- Routes: 6

## Routes

### `access_knowledge_home`
- Paths: `/knowledge/home`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `redirect_to_article`
- Paths: `/knowledge/article/<int:article_id>`
- Type: `http`
- Auth: `public`
- Website route: `True`

### `get_public_article_children`
- Paths: `/knowledge/public/children`
- Type: `jsonrpc`
- Auth: `public`

### `get_public_article_content`
- Paths: `/knowledge/public/article`
- Type: `jsonrpc`
- Auth: `public`

### `get_public_sidebar_articles`
- Paths: `/knowledge/public/sidebar`
- Type: `jsonrpc`
- Auth: `public`

### `search_public_article`
- Paths: `/knowledge/public/search`
- Type: `jsonrpc`
- Auth: `public`

## Navigation

- **Parent:** [[docs/Enterprise Addons/website_knowledge/Controllers]]

<!-- GENERATED:CONTROLLER -->
