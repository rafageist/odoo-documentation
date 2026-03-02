<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Helpdesk Knowledge

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/website_helpdesk_knowledge
- Dependencies: [[Odoo 19/Enterprise Addons/website_helpdesk/website_helpdesk|website_helpdesk]], [[Odoo 19/Enterprise Addons/knowledge/knowledge|knowledge]]

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
!include ../../../Templates/DiagramStyles.puml
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

