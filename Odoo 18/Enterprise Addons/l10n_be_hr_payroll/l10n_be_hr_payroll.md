<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Belgium - Payroll

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_be_hr_payroll
- Dependencies: [[Odoo 18/Community Addons/certificate/certificate|certificate]], [[Odoo 18/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]], [[Odoo 18/Enterprise Addons/hr_contract_reports/hr_contract_reports|hr_contract_reports]], [[Odoo 18/Community Addons/hr_work_entry_holidays/hr_work_entry_holidays|hr_work_entry_holidays]], [[Odoo 18/Enterprise Addons/hr_payroll_holidays/hr_payroll_holidays|hr_payroll_holidays]]
## XML Artifacts (detected)

- Views: 45
- Actions: 36
- Menus: 17
- Rules (ir.rule): 7
- Access CSV entries: 30

## Detected Models

- `Certificate`
- `HrContract`
- `DepartureReason`
- `l10n_be.dmfa`
- `l10n_be.dmfa.location.unit`
- `HrEmployee`
- `HrJob`
- `hr.leave`
- `hr.leave.allocation`
- `Payslip`
- `HrPayslipRun`
- `HrPayslipWorkedDays`
- `HrWorkEntry`
- `HrWorkEntryType`
- `IrUiMenu`
- `l10n_be.273s`
- `l10n_be.274_xx`
- `l10n_be.274_xx.line`
- `l10n_be.281_10`
- `l10n_be.281_45`
- `l10n.be.double.pay.recovery.line`
- `l10n_be.individual.account`
- `l10n_be.schedule.change.allocation`
- `ResCompany`
- `User`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Belgium - Payroll - Models and Relations
class Certificate
class HrContract
class DepartureReason
class "l10n_be.dmfa" as l10n_be_dmfa
class "l10n_be.dmfa.location.unit" as l10n_be_dmfa_location_unit
class HrEmployee
class HrJob
class "hr.leave" as hr_leave
class "hr.leave.allocation" as hr_leave_allocation
class Payslip
class HrPayslipRun
class HrPayslipWorkedDays
class HrWorkEntry
class HrWorkEntryType
class IrUiMenu
class "l10n_be.273s" as l10n_be_273s
class "l10n_be.274_xx" as l10n_be_274_xx
class "l10n_be.274_xx.line" as l10n_be_274_xx_line
class "l10n_be.281_10" as l10n_be_281_10
class "l10n_be.281_45" as l10n_be_281_45
class "l10n.be.double.pay.recovery.line" as l10n_be_double_pay_recovery_line
class "l10n_be.individual.account" as l10n_be_individual_account
class "l10n_be.schedule.change.allocation" as l10n_be_schedule_change_allocation
class ResCompany
class User
class "res.company" as res_company
l10n_be_dmfa --> res_company : many2one
l10n_be_dmfa_location_unit --> res_company : many2one
class "res.partner" as res_partner
l10n_be_dmfa_location_unit --> res_partner : many2one
HrEmployee .. l10n_be_double_pay_recovery_line : many2many
HrEmployee .. l10n_be_double_pay_recovery_line : many2many
HrEmployee --|> l10n_be_double_pay_recovery_line : one2many
l10n_be_273s --> res_company : many2one
class "res.currency" as res_currency
l10n_be_273s --> res_currency : many2one
l10n_be_274_xx --|> l10n_be_274_xx_line : one2many
l10n_be_274_xx --> res_company : many2one
l10n_be_274_xx --> res_currency : many2one
l10n_be_274_xx_line --> l10n_be_274_xx : many2one
class "hr.employee" as hr_employee
l10n_be_274_xx_line --> hr_employee : many2one
l10n_be_274_xx_line --> res_company : many2one
l10n_be_274_xx_line --> res_currency : many2one
l10n_be_double_pay_recovery_line --> hr_employee : many2one
l10n_be_double_pay_recovery_line --> res_company : many2one
class "hr.contract" as hr_contract
l10n_be_schedule_change_allocation --> hr_contract : many2one
l10n_be_schedule_change_allocation --> hr_leave_allocation : many2one
class "resource.calendar" as resource_calendar
l10n_be_schedule_change_allocation --> resource_calendar : many2one
l10n_be_schedule_change_allocation --> resource_calendar : many2one
ResCompany --|> l10n_be_dmfa_location_unit : one2many
class "certificate.certificate" as certificate_certificate
ResCompany --> certificate_certificate : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
