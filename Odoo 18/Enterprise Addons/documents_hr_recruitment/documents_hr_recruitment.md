<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Documents - Recruitment

- Version: v18
- Category: enterprise
- Source: enterprise18/documents_hr_recruitment
- Dependencies: [[Odoo 18/Enterprise Addons/documents_hr/documents_hr|documents_hr]], [[Odoo 18/Community Addons/hr_recruitment/hr_recruitment|hr_recruitment]]

## Summary

Recruitment resumés and letters from documents

## XML Artifacts (detected)

- Views: 1
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `DocumentsDocument`
- `hr.applicant`
- `hr.job`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Documents - Recruitment - Models and Relations
class DocumentsDocument
class "hr.applicant" as hr_applicant
class "hr.job" as hr_job
class ResCompany
class "documents.document" as documents_document
ResCompany --> documents_document : many2one
class "documents.tag" as documents_tag
ResCompany .. documents_tag : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
