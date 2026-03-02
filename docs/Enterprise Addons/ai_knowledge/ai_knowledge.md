<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# AI Text Draft - Knowledge

- Scope: Enterprise Addons
- Source: enterprise/ai_knowledge
- Dependencies: [[docs/Enterprise Addons/ai/ai|ai]], [[docs/Enterprise Addons/knowledge/knowledge|knowledge]]

## Summary

AI text draft integration with knowledge

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ai.agent.source`
- `ai.composer`
- `KnowledgeArticle`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title AI Text Draft - Knowledge - Models and Relations
class "ai.agent.source" as ai_agent_source
class "ai.composer" as ai_composer
class KnowledgeArticle
class "knowledge.article" as knowledge_article
ai_agent_source --> knowledge_article : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



