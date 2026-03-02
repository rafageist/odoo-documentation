<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Helpdesk Knowledge

- Scope: Enterprise Addons
- Source: enterprise/website_helpdesk_knowledge
- Dependencies: [[docs/Enterprise Addons/website_helpdesk/website_helpdesk|website_helpdesk]], [[docs/Enterprise Addons/knowledge/knowledge|knowledge]]

## Summary

Helpdesk integration with knowledge

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HelpdeskTeam`
- `KnowledgeArticle`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Helpdesk Knowledge - Models and Relations
class HelpdeskTeam
class KnowledgeArticle
class "knowledge.article" as knowledge_article
HelpdeskTeam --> knowledge_article : many2one
HelpdeskTeam .. knowledge_article : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




