<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Knowledge

- Scope: Enterprise Addons
- Source: enterprise/knowledge
- Dependencies: [[docs/Community Addons/web/web|web]], [[docs/Community Addons/digest/digest|digest]], [[docs/Community Addons/html_editor/html_editor|html_editor]], [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/portal/portal|portal]], [[docs/Community Addons/web_unsplash/web_unsplash|web_unsplash]], [[docs/Community Addons/web_hierarchy/web_hierarchy|web_hierarchy]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



## Curated analysis

### Functional role
- `knowledge` is the enterprise article system for internal documentation, structured playbooks, and collaborative long-form notes.
- The hierarchy, membership, favorites, stages, and covers are all first-class models, which makes this module closer to a governed content platform than to a simple wiki.

### Operational footprint
- `knowledge_article.py` is the main content model, while the companion files handle membership, favorites, stages, covers, and invite flows.
- Security is central: `security/ir_rule.xml` enforces article visibility and writer/reader rules, and the hooks create private article scaffolding per user.

### Evidence
- Source files: `enterprise/knowledge/models/knowledge_article.py`, `enterprise/knowledge/models/knowledge_cover.py`, `enterprise/knowledge/wizard/knowledge_invite.py`
- UI and data: `enterprise/knowledge/views/knowledge_article_views.xml`, `enterprise/knowledge/data/knowledge_article_stage_data.xml`, `enterprise/knowledge/security/ir_rule.xml`
- Tests: `enterprise/knowledge/tests/test_knowledge_article_business.py`, `enterprise/knowledge/tests/test_knowledge_article_constraints.py`, `enterprise/knowledge/tests/test_knowledge_article_sequence.py`

### Related notes
- `[[docs/Enterprise Addons/documents/documents|documents]]`
- `[[docs/Community Addons/mail/mail|mail]]`

### Rollout and migration concerns
- Hierarchical constraints and membership rules need to be validated before importing or restructuring a large article tree, because the model actively protects against invalid parentage.
- Heavy frontend customization and shared editing patterns mean rollout should include user training, permission reviews, and article-template governance.
- Legacy comparison backlog was retired on 2026-03-02; keep this note focused on the current codebase.

