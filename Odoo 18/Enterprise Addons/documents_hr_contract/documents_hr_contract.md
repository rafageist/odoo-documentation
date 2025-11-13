<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Documents - Contracts

- Version: v18
- Category: enterprise
- Source: enterprise18/documents_hr_contract
- Dependencies: [[Odoo 18/Enterprise Addons/documents_hr/documents_hr|documents_hr]], [[Odoo 18/Community Addons/hr_contract/hr_contract|hr_contract]]

## Summary

Store employee contracts in the Document app

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `Tags`
- `hr.contract`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Documents - Contracts - Models and Relations
class Tags
class "hr.contract" as hr_contract
class ResCompany
class "documents.tag" as documents_tag
ResCompany .. documents_tag : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
