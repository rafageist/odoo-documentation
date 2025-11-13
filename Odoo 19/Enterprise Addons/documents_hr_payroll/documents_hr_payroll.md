<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Documents - Payroll

- Version: v19
- Category: enterprise
- Source: enterprise19/documents_hr_payroll
- Dependencies: [[Odoo 19/Enterprise Addons/documents_hr/documents_hr|documents_hr]], [[Odoo 19/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]

## Summary

Store employee payslips in the Document app

## XML Artifacts (detected)

- Views: 3
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HrEmployee`
- `HrPayrollEmployeeDeclaration`
- `hr.payslip`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Documents - Payroll - Models and Relations
class HrEmployee
class HrPayrollEmployeeDeclaration
class "hr.payslip" as hr_payslip
class ResCompany
class "documents.document" as documents_document
HrPayrollEmployeeDeclaration --> documents_document : many2one
class "documents.tag" as documents_tag
ResCompany .. documents_tag : many2many
ResCompany --> documents_document : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
