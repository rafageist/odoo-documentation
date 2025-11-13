<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Documents - Payroll

- Version: v18
- Category: enterprise
- Source: enterprise18/documents_hr_payroll
- Dependencies: [[Odoo 18/Enterprise Addons/documents_hr/documents_hr|documents_hr]], [[Odoo 18/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]

## Summary

Store employee payslips in the Document app

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HrContract`
- `HrPayrollEmployeeDeclaration`
- `hr.payslip`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Documents - Payroll - Models and Relations
class HrContract
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
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
