
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Audit Reports

- Scope: Enterprise Addons
- Source: enterprise/accountant_knowledge
- Dependencies: [[docs/Enterprise Addons/accountant/accountant|accountant]], [[docs/Enterprise Addons/knowledge/knowledge|knowledge]], [[docs/Enterprise Addons/sign/sign|sign]]

## Summary

Create Audit Reports with Knowledge

## XML Artifacts (detected)

- Views: 4
- Actions: 2
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `audit.report`
- `IrActionsReport`
- `knowledge.article`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Audit Reports - Models and Relations
class "audit.report" as audit_report
class IrActionsReport
class "knowledge.article" as knowledge_article
audit_report --> knowledge_article : many2one
class "res.company" as res_company
audit_report --> res_company : many2one
class "res.users" as res_users
audit_report .. res_users : many2many
audit_report --> knowledge_article : many2one
knowledge_article --|> audit_report : one2many
knowledge_article --|> audit_report : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

