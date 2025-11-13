<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Jordan - Payroll

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_jo_hr_payroll
- Dependencies: [[Odoo 19/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]], [[Odoo 19/Enterprise Addons/hr_payroll_holidays/hr_payroll_holidays|hr_payroll_holidays]]
## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HrEmployee`
- `HrPayrollStructureType`
- `HrPayslip`
- `HrVersion`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Jordan - Payroll - Models and Relations
class HrEmployee
class HrPayrollStructureType
class HrPayslip
class HrVersion
class ResCompany
class "hr.leave.type" as hr_leave_type
ResCompany --> hr_leave_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
