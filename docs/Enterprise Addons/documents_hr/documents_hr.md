
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Documents - HR

- Scope: Enterprise Addons
- Source: enterprise/documents_hr
- Dependencies: [[docs/Enterprise Addons/documents/documents|documents]], [[docs/Community Addons/hr/hr|hr]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

