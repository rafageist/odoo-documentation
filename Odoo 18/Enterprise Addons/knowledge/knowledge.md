<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Knowledge

- Version: v18
- Category: enterprise
- Source: enterprise18/knowledge
- Dependencies: [[Odoo 18/Community Addons/web/web|web]], [[Odoo 18/Community Addons/web_editor/web_editor|web_editor]], [[Odoo 18/Community Addons/digest/digest|digest]], [[Odoo 18/Community Addons/html_editor/html_editor|html_editor]], [[Odoo 18/Community Addons/mail/mail|mail]], [[Odoo 18/Community Addons/portal/portal|portal]], [[Odoo 18/Community Addons/web_unsplash/web_unsplash|web_unsplash]], [[Odoo 18/Community Addons/web_hierarchy/web_hierarchy|web_hierarchy]]

## Summary

Centralize, manage, share and grow your knowledge library

## XML Artifacts (detected)

- Views: 28
- Actions: 27
- Menus: 12
- Rules (ir.rule): 14
- Access CSV entries: 29

## Detected Models

- `IrAttachment`
- `knowledge.article`
- `knowledge.article.favorite`
- `knowledge.article.member`
- `knowledge.article.stage`
- `knowledge.article.template.category`
- `knowledge.article.thread`
- `knowledge.cover`
- `res.partner`
- `res.users`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Knowledge - Models and Relations
class IrAttachment
class "knowledge.article" as knowledge_article
class "knowledge.article.favorite" as knowledge_article_favorite
class "knowledge.article.member" as knowledge_article_member
class "knowledge.article.stage" as knowledge_article_stage
class "knowledge.article.template.category" as knowledge_article_template_category
class "knowledge.article.thread" as knowledge_article_thread
class "knowledge.cover" as knowledge_cover
class "res.partner" as res_partner
class "res.users" as res_users
knowledge_article --> knowledge_cover : many2one
knowledge_article --> knowledge_article : many2one
knowledge_article --|> knowledge_article_member : one2many
knowledge_article --> knowledge_article : many2one
knowledge_article --|> knowledge_article : one2many
knowledge_article --> knowledge_article : many2one
knowledge_article --> knowledge_article_stage : many2one
knowledge_article --> res_users : many2one
knowledge_article --|> knowledge_article_favorite : one2many
knowledge_article --> knowledge_article_template_category : many2one
knowledge_article_favorite --> knowledge_article : many2one
knowledge_article_favorite --> res_users : many2one
knowledge_article_member --> knowledge_article : many2one
knowledge_article_member --> res_partner : many2one
knowledge_article_stage --> knowledge_article : many2one
knowledge_article_thread --> knowledge_article : many2one
class "ir.attachment" as ir_attachment
knowledge_cover --> ir_attachment : many2one
knowledge_cover --|> knowledge_article : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
