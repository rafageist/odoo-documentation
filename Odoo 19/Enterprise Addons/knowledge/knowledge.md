<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Knowledge

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/knowledge
- Dependencies: [[Odoo 19/Community Addons/web/web|web]], [[Odoo 19/Community Addons/digest/digest|digest]], [[Odoo 19/Community Addons/html_editor/html_editor|html_editor]], [[Odoo 19/Community Addons/mail/mail|mail]], [[Odoo 19/Community Addons/portal/portal|portal]], [[Odoo 19/Community Addons/web_unsplash/web_unsplash|web_unsplash]], [[Odoo 19/Community Addons/web_hierarchy/web_hierarchy|web_hierarchy]]

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
- `ResPartner`
- `ResUsers`

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
class ResPartner
class ResUsers
knowledge_article --> knowledge_cover : many2one
knowledge_article --> knowledge_article : many2one
knowledge_article --|> knowledge_article_member : one2many
knowledge_article --> knowledge_article : many2one
knowledge_article --|> knowledge_article : one2many
knowledge_article --> knowledge_article : many2one
knowledge_article --> knowledge_article_stage : many2one
class "res.users" as res_users
knowledge_article --> res_users : many2one
knowledge_article --|> knowledge_article_favorite : one2many
knowledge_article --> knowledge_article_template_category : many2one
knowledge_article --> knowledge_article : many2one
knowledge_article_favorite --> knowledge_article : many2one
knowledge_article_favorite --> res_users : many2one
knowledge_article_member --> knowledge_article : many2one
class "res.partner" as res_partner
knowledge_article_member --> res_partner : many2one
knowledge_article_stage --> knowledge_article : many2one
knowledge_article_thread --> knowledge_article : many2one
class "ir.attachment" as ir_attachment
knowledge_cover --> ir_attachment : many2one
knowledge_cover --|> knowledge_article : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

## Curated analysis

### Functional role
- `knowledge` is the enterprise article system for internal documentation, structured playbooks, and collaborative long-form notes.
- The hierarchy, membership, favorites, stages, and covers are all first-class models, which makes this module closer to a governed content platform than to a simple wiki.

### Operational footprint
- `knowledge_article.py` is the main content model, while the companion files handle membership, favorites, stages, covers, and invite flows.
- Security is central: `security/ir_rule.xml` enforces article visibility and writer/reader rules, and the hooks create private article scaffolding per user.

### Evidence
- Source files: `enterprise19/knowledge/models/knowledge_article.py`, `enterprise19/knowledge/models/knowledge_cover.py`, `enterprise19/knowledge/wizard/knowledge_invite.py`
- UI and data: `enterprise19/knowledge/views/knowledge_article_views.xml`, `enterprise19/knowledge/data/knowledge_article_stage_data.xml`, `enterprise19/knowledge/security/ir_rule.xml`
- Tests: `enterprise19/knowledge/tests/test_knowledge_article_business.py`, `enterprise19/knowledge/tests/test_knowledge_article_constraints.py`, `enterprise19/knowledge/tests/test_knowledge_article_sequence.py`

### Related notes
- `[[Odoo 19/Enterprise Addons/documents/documents|documents]]`
- `[[Odoo 19/Community Addons/mail/mail|mail]]`

### Rollout and migration concerns
- Hierarchical constraints and membership rules need to be validated before importing or restructuring a large article tree, because the model actively protects against invalid parentage.
- Heavy frontend customization and shared editing patterns mean rollout should include user training, permission reviews, and article-template governance.
- Odoo 18 comparison backlog was retired on 2026-03-02; keep this note focused on Odoo 19 behavior.

