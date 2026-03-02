
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# United Arab Emirates - Payroll

- Scope: Enterprise Addons
- Source: enterprise/l10n_ae_hr_payroll
- Dependencies: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]], [[docs/Community Addons/hr_work_entry_holidays/hr_work_entry_holidays|hr_work_entry_holidays]]

## XML Artifacts (detected)

- Views: 6
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HrEmployee`
- `HrLeaveType`
- `HrPayrollStructureType`
- `HrPayslip`
- `HrPayslipRun`
- `HrVersion`
- `ResBank`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title United Arab Emirates - Payroll - Models and Relations
class HrEmployee
class HrLeaveType
class HrPayrollStructureType
class HrPayslip
class HrPayslipRun
class HrVersion
class ResBank
class ResCompany
class "res.partner.bank" as res_partner_bank
ResCompany --> res_partner_bank : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

