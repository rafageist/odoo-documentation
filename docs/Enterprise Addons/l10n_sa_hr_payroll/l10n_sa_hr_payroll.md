<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Saudi Arabia - Payroll

- Scope: Enterprise Addons
- Source: enterprise/l10n_sa_hr_payroll
- Dependencies: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]], [[docs/Community Addons/hr_work_entry_holidays/hr_work_entry_holidays|hr_work_entry_holidays]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




