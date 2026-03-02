<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# United States - Payroll

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_us_hr_payroll
- Dependencies: [[Odoo 19/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]], [[Odoo 19/Community Addons/hr_work_entry_holidays/hr_work_entry_holidays|hr_work_entry_holidays]], [[Odoo 19/Enterprise Addons/hr_payroll_holidays/hr_payroll_holidays|hr_payroll_holidays]], [[Odoo 19/Community Addons/base_address_extended/base_address_extended|base_address_extended]], [[Odoo 19/Community Addons/l10n_us/l10n_us|l10n_us]]

## XML Artifacts (detected)

- Views: 12
- Actions: 6
- Menus: 5
- Rules (ir.rule): 1
- Access CSV entries: 4

## Detected Models

- `HrEmployee`
- `HrLeaveAllocation`
- `HrLeaveType`
- `HrPayslip`
- `HrVersion`
- `l10n.us.940`
- `l10n.us.941`
- `l10n.us.w2`
- `l10n.us.worker.compensation`
- `ResCompany`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title United States - Payroll - Models and Relations
class HrEmployee
class HrLeaveAllocation
class HrLeaveType
class HrPayslip
class HrVersion
class "l10n.us.940" as l10n_us_940
class "l10n.us.941" as l10n_us_941
class "l10n.us.w2" as l10n_us_w2
class "l10n.us.worker.compensation" as l10n_us_worker_compensation
class ResCompany
HrVersion --> l10n_us_worker_compensation : many2one
class "res.country.state" as res_country_state
l10n_us_940 --> res_country_state : many2one
class "res.company" as res_company
l10n_us_940 --> res_company : many2one
class "hr.payslip" as hr_payslip
l10n_us_940 .. hr_payslip : many2many
l10n_us_940 .. hr_payslip : many2many
l10n_us_941 --> res_company : many2one
l10n_us_941 .. hr_payslip : many2many
l10n_us_941 .. hr_payslip : many2many
l10n_us_w2 --> res_company : many2one
l10n_us_w2 .. hr_payslip : many2many
l10n_us_w2 .. hr_payslip : many2many
class "hr.employee" as hr_employee
ResCompany --> hr_employee : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

