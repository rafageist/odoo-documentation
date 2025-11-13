<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# United States - Payroll

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_us_hr_payroll
- Dependencies: [[Odoo 18/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]], [[Odoo 18/Enterprise Addons/hr_contract_reports/hr_contract_reports|hr_contract_reports]], [[Odoo 18/Community Addons/hr_work_entry_holidays/hr_work_entry_holidays|hr_work_entry_holidays]], [[Odoo 18/Enterprise Addons/hr_payroll_holidays/hr_payroll_holidays|hr_payroll_holidays]], [[Odoo 18/Community Addons/base_address_extended/base_address_extended|base_address_extended]]
## XML Artifacts (detected)

- Views: 8
- Actions: 4
- Menus: 3
- Rules (ir.rule): 1
- Access CSV entries: 2

## Detected Models

- `HrContract`
- `HrEmployee`
- `HolidaysAllocation`
- `HolidaysType`
- `HrPayslipWorkedDays`
- `l10n.us.w2`
- `l10n.us.worker.compensation`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title United States - Payroll - Models and Relations
class HrContract
class HrEmployee
class HolidaysAllocation
class HolidaysType
class HrPayslipWorkedDays
class "l10n.us.w2" as l10n_us_w2
class "l10n.us.worker.compensation" as l10n_us_worker_compensation
class ResCompany
HrContract --> l10n_us_worker_compensation : many2one
class "res.company" as res_company
l10n_us_w2 --> res_company : many2one
class "hr.payslip" as hr_payslip
l10n_us_w2 .. hr_payslip : many2many
l10n_us_w2 .. hr_payslip : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
