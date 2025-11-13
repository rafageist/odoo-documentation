<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Documents - HR

- Version: v18
- Category: enterprise
- Source: enterprise18/documents_hr
- Dependencies: [[Odoo 18/Enterprise Addons/documents/documents|documents]], [[Odoo 18/Community Addons/hr/hr|hr]]

## Summary

Access documents from the employee profile

## XML Artifacts (detected)

- Views: 4
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `DocumentRedirect`
- `hr.employee`
- `ResCompany`
- `res.users`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Documents - HR - Models and Relations
class DocumentRedirect
class "hr.employee" as hr_employee
class ResCompany
class "res.users" as res_users
DocumentRedirect --> hr_employee : many2one
class "documents.document" as documents_document
ResCompany --> documents_document : many2one
res_users --|> documents_document : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
