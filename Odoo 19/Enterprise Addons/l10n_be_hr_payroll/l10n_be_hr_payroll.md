<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Belgium - Payroll

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_be_hr_payroll
- Dependencies: [[Odoo 19/Community Addons/certificate/certificate|certificate]], [[Odoo 19/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]], [[Odoo 19/Community Addons/hr_work_entry_holidays/hr_work_entry_holidays|hr_work_entry_holidays]], [[Odoo 19/Enterprise Addons/hr_payroll_holidays/hr_payroll_holidays|hr_payroll_holidays]]

## XML Artifacts (detected)

- Views: 48
- Actions: 43
- Menus: 19
- Rules (ir.rule): 9
- Access CSV entries: 32

## Detected Models

- `CertificateCertificate`
- `HrDepartureReason`
- `l10n_be.dmfa`
- `l10n_be.dmfa.location.unit`
- `HrEmployee`
- `HrJob`
- `HrLeave`
- `HrLeaveAllocation`
- `HrLeaveType`
- `HrPayrollStructureType`
- `HrPayslip`
- `HrPayslipRun`
- `HrPayslipWorkedDays`
- `HrVersion`
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
- `l10n.be.onss.declaration`
- `l10n.be.onss.file`
- `l10n_be.schedule.change.allocation`
- `ResourceCalendar`
- `ResCompany`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Belgium - Payroll - Models and Relations
class CertificateCertificate
class HrDepartureReason
class "l10n_be.dmfa" as l10n_be_dmfa
class "l10n_be.dmfa.location.unit" as l10n_be_dmfa_location_unit
class HrEmployee
class HrJob
class HrLeave
class HrLeaveAllocation
class HrLeaveType
class HrPayrollStructureType
class HrPayslip
class HrPayslipRun
class HrPayslipWorkedDays
class HrVersion
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
class "l10n.be.onss.declaration" as l10n_be_onss_declaration
class "l10n.be.onss.file" as l10n_be_onss_file
class "l10n_be.schedule.change.allocation" as l10n_be_schedule_change_allocation
class ResourceCalendar
class ResCompany
class "res.company" as res_company
l10n_be_dmfa --> res_company : many2one
l10n_be_dmfa --|> l10n_be_onss_declaration : one2many
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
l10n_be_onss_declaration --> l10n_be_dmfa : many2one
l10n_be_onss_declaration --> res_company : many2one
l10n_be_onss_declaration --|> l10n_be_onss_file : one2many
l10n_be_onss_file --> l10n_be_onss_declaration : many2one
l10n_be_onss_file --> hr_employee : many2one
l10n_be_onss_file --> res_company : many2one
class "hr.version" as hr_version
l10n_be_schedule_change_allocation --> hr_version : many2one
class "hr.leave.allocation" as hr_leave_allocation
l10n_be_schedule_change_allocation --> hr_leave_allocation : many2one
class "resource.calendar" as resource_calendar
l10n_be_schedule_change_allocation --> resource_calendar : many2one
l10n_be_schedule_change_allocation --> resource_calendar : many2one
ResCompany --|> l10n_be_dmfa_location_unit : one2many
class "certificate.certificate" as certificate_certificate
ResCompany --> certificate_certificate : many2one
class "certificate.key" as certificate_key
ResCompany --> certificate_key : many2one
class "hr.leave.type" as hr_leave_type
ResCompany --> hr_leave_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

