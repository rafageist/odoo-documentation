<!-- GENERATED:CONTROLLER -->
---
tags: [odoo, enterprise, generated, controller]
---

# KnowledgeController

- Module: [[docs/Enterprise Addons/knowledge/knowledge|knowledge]]
- Scope: Enterprise Addons
- Source file: `controllers/main.py`
- Base classes: `http.Controller`
- Routes: 3

## Routes

### `access_knowledge_home`
- Paths: `/knowledge/home`
- Type: `http`
- Auth: `user`

### `redirect_to_article`
- Paths: `/knowledge/article/<int:article_id>`
- Type: `http`
- Auth: `user`

### `article_invite`
- Paths: `/knowledge/article/invite/<int:member_id>/<string:invitation_hash>`
- Type: `http`
- Auth: `public`

## Navigation

- **Parent:** [[docs/Enterprise Addons/knowledge/Controllers]]

<!-- GENERATED:CONTROLLER -->
