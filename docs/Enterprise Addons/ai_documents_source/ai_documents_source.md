<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# AI Documents Source

- Scope: Enterprise Addons
- Source: enterprise/ai_documents_source
- Dependencies: [[docs/Enterprise Addons/ai/ai|ai]], [[docs/Enterprise Addons/documents/documents|documents]]

## Summary

Add documents to AI agents as sources.

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ai.agent.source`
- `DocumentsDocument`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title AI Documents Source - Models and Relations
class "ai.agent.source" as ai_agent_source
class DocumentsDocument
class "documents.document" as documents_document
ai_agent_source --> documents_document : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



