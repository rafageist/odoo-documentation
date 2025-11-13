<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Documents - HR

- Version: v19
- Category: enterprise
- Source: enterprise19/documents_hr
- Dependencies: [[Odoo 19/Enterprise Addons/documents/documents|documents]], [[Odoo 19/Community Addons/hr/hr|hr]]

## Summary

Access documents from the employee profile

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `DocumentsDocument`
- `DocumentsRedirect`
- `DocumentsTag`
- `hr.employee`
- `HrEmployeePublic`
- `hr.version`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Documents - HR - Models and Relations
class DocumentsDocument
class DocumentsRedirect
class DocumentsTag
class "hr.employee" as hr_employee
class HrEmployeePublic
class "hr.version" as hr_version
class ResCompany
DocumentsRedirect --> hr_employee : many2one
class "documents.document" as documents_document
hr_employee --> documents_document : many2one
hr_employee --> documents_document : many2one
ResCompany --> documents_document : many2one
class "documents.tag" as documents_tag
ResCompany .. documents_tag : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
