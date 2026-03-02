<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# United States - Payroll

- Scope: Enterprise Addons
- Source: enterprise/l10n_us_hr_payroll
- Dependencies: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]], [[docs/Community Addons/hr_work_entry_holidays/hr_work_entry_holidays|hr_work_entry_holidays]], [[docs/Enterprise Addons/hr_payroll_holidays/hr_payroll_holidays|hr_payroll_holidays]], [[docs/Community Addons/base_address_extended/base_address_extended|base_address_extended]], [[docs/Community Addons/l10n_us/l10n_us|l10n_us]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



