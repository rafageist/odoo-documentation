<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Saudi Arabia - Payroll

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_sa_hr_payroll
- Dependencies: [[Odoo 19/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]], [[Odoo 19/Community Addons/hr_work_entry_holidays/hr_work_entry_holidays|hr_work_entry_holidays]]

## XML Artifacts (detected)

- Views: 9
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HrDepartureReason`
- `HrEmployee`
- `HrPayrollStructureType`
- `HrPayslip`
- `HrPayslipRun`
- `HrSalaryAttachment`
- `HrVersion`
- `ResBank`
- `ResCompany`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Saudi Arabia - Payroll - Models and Relations
class HrDepartureReason
class HrEmployee
class HrPayrollStructureType
class HrPayslip
class HrPayslipRun
class HrSalaryAttachment
class HrVersion
class ResBank
class ResCompany
class "res.partner.bank" as res_partner_bank
ResCompany --> res_partner_bank : many2one
class "hr.leave.type" as hr_leave_type
ResCompany --> hr_leave_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

