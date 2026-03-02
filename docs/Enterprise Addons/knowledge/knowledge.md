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

## Generated coverage

- Models: 11
- XML files with UI/data artifacts: 9
- Views: 28
- Actions: 27
- Menus: 12
- Rules (ir.rule): 14
- Access CSV entries: 29
- Controller units: 5
- Frontend asset files: 182

## Module map

```plantuml
@startuml
!define ODOO_COLOR_PRIMARY #714B67
!define ODOO_COLOR_ACCENT #875A7B
!define ODOO_COLOR_BG #FAF7FA

skinparam backgroundColor ODOO_COLOR_BG
skinparam defaultTextAlignment left
skinparam ArrowColor ODOO_COLOR_ACCENT
skinparam ClassBackgroundColor white
skinparam ClassBorderColor ODOO_COLOR_PRIMARY
skinparam ComponentBackgroundColor white
skinparam ComponentBorderColor ODOO_COLOR_PRIMARY
skinparam NoteBackgroundColor #FFF8FF
skinparam NoteBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBackgroundColor #FFFFFF
skinparam SequenceParticipantBorderColor ODOO_COLOR_PRIMARY
skinparam SequenceParticipantBackgroundColor #FFFFFF
skinparam sequence {
  ArrowColor ODOO_COLOR_ACCENT
  ActorBorderColor ODOO_COLOR_PRIMARY
}
title Knowledge - Generated Coverage
component "Module Overview" as overview
component "Models\n11" as models
component "Views / XML\n28 views\n9 files" as views
component "Controllers\n8 routes" as controllers
component "Frontend\n182 files" as frontend
component "Security / Data\n14 rules\n29 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/knowledge/Models|Models]] (11)
- Views and XML: [[docs/Enterprise Addons/knowledge/Views|Views]] (9 files)
- Controllers: [[docs/Enterprise Addons/knowledge/Controllers|Controllers]] (5)
- Frontend: [[docs/Enterprise Addons/knowledge/Frontend|Frontend]] (182 files)

## Key models

- `ir.attachment`
- `knowledge.article`
- `knowledge.article.favorite`
- `knowledge.article.member`
- `knowledge.article.stage`
- `knowledge.article.template.category`
- `knowledge.article.thread`
- `knowledge.cover`
- `knowledge.invite`
- `res.partner`
- `res.users`

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

