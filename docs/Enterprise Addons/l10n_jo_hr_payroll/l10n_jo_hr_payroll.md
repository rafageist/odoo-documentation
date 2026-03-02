<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Jordan - Payroll

- Scope: Enterprise Addons
- Source: enterprise/l10n_jo_hr_payroll
- Dependencies: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]], [[docs/Enterprise Addons/hr_payroll_holidays/hr_payroll_holidays|hr_payroll_holidays]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




