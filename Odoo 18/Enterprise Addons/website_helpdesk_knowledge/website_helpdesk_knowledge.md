<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Helpdesk Knowledge

- Version: v18
- Category: enterprise
- Source: enterprise18/website_helpdesk_knowledge
- Dependencies: [[Odoo 18/Enterprise Addons/website_helpdesk/website_helpdesk|website_helpdesk]], [[Odoo 18/Enterprise Addons/knowledge/knowledge|knowledge]]

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
- `Article`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Helpdesk Knowledge - Models and Relations
class HelpdeskTeam
class Article
class "knowledge.article" as knowledge_article
HelpdeskTeam --> knowledge_article : many2one
HelpdeskTeam .. knowledge_article : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
