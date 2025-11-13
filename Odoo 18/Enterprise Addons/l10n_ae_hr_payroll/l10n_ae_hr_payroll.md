<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# United Arab Emirates - Payroll

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_ae_hr_payroll
- Dependencies: [[Odoo 18/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]], [[Odoo 18/Community Addons/hr_work_entry_holidays/hr_work_entry_holidays|hr_work_entry_holidays]]
## XML Artifacts (detected)

- Views: 6
- Actions: 2
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `HRContract`
- `HrEmployee`
- `HrLeaveType`
- `report.l10n_ae_hr_payroll.master`
- `HrPayslip`
- `HrPayslipRun`
- `IrUiMenu`
- `ResBank`
- `Company`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title United Arab Emirates - Payroll - Models and Relations
class HRContract
class HrEmployee
class HrLeaveType
class "report.l10n_ae_hr_payroll.master" as report_l10n_ae_hr_payroll_master
class HrPayslip
class HrPayslipRun
class IrUiMenu
class ResBank
class Company
class "res.partner.bank" as res_partner_bank
Company --> res_partner_bank : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
