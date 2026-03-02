<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Audit Reports

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/accountant_knowledge
- Dependencies: [[Odoo 19/Enterprise Addons/accountant/accountant|accountant]], [[Odoo 19/Enterprise Addons/knowledge/knowledge|knowledge]], [[Odoo 19/Enterprise Addons/sign/sign|sign]]

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
!include ../../../Templates/DiagramStyles.puml
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

