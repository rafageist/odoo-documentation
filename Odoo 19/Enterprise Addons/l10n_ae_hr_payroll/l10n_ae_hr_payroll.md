<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# United Arab Emirates - Payroll

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_ae_hr_payroll
- Dependencies: [[Odoo 19/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]], [[Odoo 19/Community Addons/hr_work_entry_holidays/hr_work_entry_holidays|hr_work_entry_holidays]]
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
!include ../../../Templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
