<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Australia - Payroll

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_au_hr_payroll
- Dependencies: [[Odoo 18/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]], [[Odoo 18/Enterprise Addons/hr_contract_reports/hr_contract_reports|hr_contract_reports]], [[Odoo 18/Community Addons/hr_work_entry_holidays/hr_work_entry_holidays|hr_work_entry_holidays]], [[Odoo 18/Enterprise Addons/hr_payroll_holidays/hr_payroll_holidays|hr_payroll_holidays]]
## XML Artifacts (detected)

- Views: 16
- Actions: 4
- Menus: 5
- Rules (ir.rule): 1
- Access CSV entries: 3

## Detected Models

- `HrContract`
- `HrEmployee`
- `HolidaysType`
- `HrPayrollStructure`
- `HrPayrollStructureType`
- `HrPayslip`
- `HrPayslipInput`
- `HrPayslipWorkedDays`
- `HrWorkEntryType`
- `l10n_au.super.account`
- `l10n_au.super.fund`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Australia - Payroll - Models and Relations
class HrContract
class HrEmployee
class HolidaysType
class HrPayrollStructure
class HrPayrollStructureType
class HrPayslip
class HrPayslipInput
class HrPayslipWorkedDays
class HrWorkEntryType
class "l10n_au.super.account" as l10n_au_super_account
class "l10n_au.super.fund" as l10n_au_super_fund
class ResCompany
class "hr.leave.type" as hr_leave_type
HrContract .. hr_leave_type : many2many
HrEmployee --|> l10n_au_super_account : one2many
class "res.country" as res_country
HrEmployee --> res_country : many2one
class "hr.payslip.input.type" as hr_payslip_input_type
HrPayrollStructureType .. hr_payslip_input_type : many2many
class "hr.employee" as hr_employee
l10n_au_super_account --> hr_employee : many2one
l10n_au_super_account --> l10n_au_super_fund : many2one
class "res.partner" as res_partner
l10n_au_super_account --> res_partner : many2one
class "res.company" as res_company
l10n_au_super_account --> res_company : many2one
l10n_au_super_fund --> res_partner : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
