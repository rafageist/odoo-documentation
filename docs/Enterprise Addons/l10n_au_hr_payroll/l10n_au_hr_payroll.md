<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Australia - Payroll

- Scope: Enterprise Addons
- Source: enterprise/l10n_au_hr_payroll
- Dependencies: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]], [[docs/Community Addons/hr_work_entry_holidays/hr_work_entry_holidays|hr_work_entry_holidays]], [[docs/Enterprise Addons/hr_payroll_holidays/hr_payroll_holidays|hr_payroll_holidays]], [[docs/Community Addons/base_address_extended/base_address_extended|base_address_extended]]

## XML Artifacts (detected)

- Views: 17
- Actions: 4
- Menus: 5
- Rules (ir.rule): 1
- Access CSV entries: 4

## Detected Models

- `HrEmployee`
- `HrLeaveType`
- `HrPayrollStructure`
- `HrPayrollStructureType`
- `HrPayslip`
- `HrPayslipInput`
- `HrPayslipInputType`
- `HrPayslipWorkedDays`
- `HrVersion`
- `HrWorkEntryType`
- `l10n_au.hr.input.details`
- `l10n_au.super.account`
- `l10n_au.super.fund`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Australia - Payroll - Models and Relations
class HrEmployee
class HrLeaveType
class HrPayrollStructure
class HrPayrollStructureType
class HrPayslip
class HrPayslipInput
class HrPayslipInputType
class HrPayslipWorkedDays
class HrVersion
class HrWorkEntryType
class "l10n_au.hr.input.details" as l10n_au_hr_input_details
class "l10n_au.super.account" as l10n_au_super_account
class "l10n_au.super.fund" as l10n_au_super_fund
class ResCompany
HrEmployee --|> l10n_au_super_account : one2many
class "hr.payslip.input.type" as hr_payslip_input_type
HrPayrollStructureType .. hr_payslip_input_type : many2many
HrPayslip --|> l10n_au_hr_input_details : one2many
HrPayslipInput --> l10n_au_hr_input_details : many2one
class "res.currency" as res_currency
HrPayslipInputType --> res_currency : many2one
class "res.country" as res_country
HrVersion --> res_country : many2one
class "hr.leave.type" as hr_leave_type
HrVersion .. hr_leave_type : many2many
class "hr.payslip.input" as hr_payslip_input
l10n_au_hr_input_details --> hr_payslip_input : many2one
class "res.city" as res_city
l10n_au_hr_input_details --> res_city : many2one
l10n_au_hr_input_details --> res_country : many2one
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




