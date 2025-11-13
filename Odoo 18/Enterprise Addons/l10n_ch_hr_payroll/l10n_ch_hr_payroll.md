<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Switzerland - Payroll

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_ch_hr_payroll
- Dependencies: [[Odoo 18/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]], [[Odoo 18/Enterprise Addons/hr_contract_reports/hr_contract_reports|hr_contract_reports]], [[Odoo 18/Community Addons/hr_work_entry_holidays/hr_work_entry_holidays|hr_work_entry_holidays]], [[Odoo 18/Enterprise Addons/hr_payroll_holidays/hr_payroll_holidays|hr_payroll_holidays]]
## XML Artifacts (detected)

- Views: 39
- Actions: 22
- Menus: 17
- Rules (ir.rule): 5
- Access CSV entries: 32

## Detected Models

- `HrContract`
- `HrEmployee`
- `hr.employee.is.line`
- `HrPayslip`
- `HrPayslipRun`
- `HrSalaryRuleParameter`
- `HrSalaryRule`
- `l10n.ch.accident.insurance`
- `l10n.ch.accident.insurance.line`
- `l10n.ch.accident.insurance.line.rate`
- `l10n.ch.additional.accident.insurance`
- `l10n.ch.additional.accident.insurance.line`
- `l10n.ch.additional.accident.insurance.line.rate`
- `l10n.ch.compensation.fund`
- `l10n.ch.compensation.fund.line`
- `l10n.ch.hr.employee.children`
- `l10n.ch.individual.account`
- `ch.yearly.report`
- `ch.yearly.report.line`
- `hr.payslip.is.log.line`
- `l10n.ch.location.unit`
- `l10n.ch.lpp.insurance`
- `l10n.ch.monthly.summary`
- `l10n.ch.salary.certificate`
- `l10n.ch.sickness.insurance`
- `l10n.ch.sickness.insurance.line`
- `l10n.ch.sickness.insurance.line.rate`
- `l10n.ch.social.insurance`
- `l10n.ch.social.insurance.avs.line`
- `l10n.ch.social.insurance.ac.line`
- `l10n.ch.social.insurance.avs.retirement.rente`
- `l10n.ch.social.insurance.avs.ac.threshold`
- `l10n.ch.social.insurance.avs.acc.threshold`
- `l10n.ch.is.report`
- `l10n.ch.is.report.line`
- `ResCompany`
- `User`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Switzerland - Payroll - Models and Relations
class HrContract
class HrEmployee
class "hr.employee.is.line" as hr_employee_is_line
class HrPayslip
class HrPayslipRun
class HrSalaryRuleParameter
class HrSalaryRule
class "l10n.ch.accident.insurance" as l10n_ch_accident_insurance
class "l10n.ch.accident.insurance.line" as l10n_ch_accident_insurance_line
class "l10n.ch.accident.insurance.line.rate" as l10n_ch_accident_insurance_line_rate
class "l10n.ch.additional.accident.insurance" as l10n_ch_additional_accident_insurance
class "l10n.ch.additional.accident.insurance.line" as l10n_ch_additional_accident_insurance_line
class "l10n.ch.additional.accident.insurance.line.rate" as l10n_ch_additional_accident_insurance_line_rate
class "l10n.ch.compensation.fund" as l10n_ch_compensation_fund
class "l10n.ch.compensation.fund.line" as l10n_ch_compensation_fund_line
class "l10n.ch.hr.employee.children" as l10n_ch_hr_employee_children
class "l10n.ch.individual.account" as l10n_ch_individual_account
class "ch.yearly.report" as ch_yearly_report
class "ch.yearly.report.line" as ch_yearly_report_line
class "hr.payslip.is.log.line" as hr_payslip_is_log_line
class "l10n.ch.location.unit" as l10n_ch_location_unit
class "l10n.ch.lpp.insurance" as l10n_ch_lpp_insurance
class "l10n.ch.monthly.summary" as l10n_ch_monthly_summary
class "l10n.ch.salary.certificate" as l10n_ch_salary_certificate
class "l10n.ch.sickness.insurance" as l10n_ch_sickness_insurance
class "l10n.ch.sickness.insurance.line" as l10n_ch_sickness_insurance_line
class "l10n.ch.sickness.insurance.line.rate" as l10n_ch_sickness_insurance_line_rate
class "l10n.ch.social.insurance" as l10n_ch_social_insurance
class "l10n.ch.social.insurance.avs.line" as l10n_ch_social_insurance_avs_line
class "l10n.ch.social.insurance.ac.line" as l10n_ch_social_insurance_ac_line
class "l10n.ch.social.insurance.avs.retirement.rente" as l10n_ch_social_insurance_avs_retirement_rente
class "l10n.ch.social.insurance.avs.ac.threshold" as l10n_ch_social_insurance_avs_ac_threshold
class "l10n.ch.social.insurance.avs.acc.threshold" as l10n_ch_social_insurance_avs_acc_threshold
class "l10n.ch.is.report" as l10n_ch_is_report
class "l10n.ch.is.report.line" as l10n_ch_is_report_line
class ResCompany
class User
HrContract --> l10n_ch_social_insurance : many2one
HrContract --> l10n_ch_lpp_insurance : many2one
HrContract --> l10n_ch_accident_insurance_line : many2one
HrContract .. l10n_ch_additional_accident_insurance_line : many2many
HrContract .. l10n_ch_sickness_insurance_line : many2many
HrContract --> l10n_ch_compensation_fund : many2one
HrContract --> l10n_ch_location_unit : many2one
HrEmployee --|> l10n_ch_hr_employee_children : one2many
class "hr.employee" as hr_employee
hr_employee_is_line --> hr_employee : many2one
class "hr.payslip" as hr_payslip
hr_employee_is_line .. hr_payslip : many2many
HrPayslip --> l10n_ch_social_insurance : many2one
HrPayslip --> l10n_ch_lpp_insurance : many2one
HrPayslip --> l10n_ch_accident_insurance_line : many2one
HrPayslip .. l10n_ch_additional_accident_insurance_line : many2many
HrPayslip .. l10n_ch_sickness_insurance_line : many2many
HrPayslip --> l10n_ch_compensation_fund : many2one
HrPayslip --|> hr_payslip_is_log_line : one2many
class "res.partner" as res_partner
l10n_ch_accident_insurance --> res_partner : many2one
l10n_ch_accident_insurance --|> l10n_ch_accident_insurance_line : one2many
l10n_ch_accident_insurance_line --> l10n_ch_accident_insurance : many2one
l10n_ch_accident_insurance_line --|> l10n_ch_accident_insurance_line_rate : one2many
l10n_ch_accident_insurance_line_rate --> l10n_ch_accident_insurance_line : many2one
l10n_ch_additional_accident_insurance --> res_partner : many2one
l10n_ch_additional_accident_insurance --|> l10n_ch_additional_accident_insurance_line : one2many
l10n_ch_additional_accident_insurance_line --> l10n_ch_additional_accident_insurance : many2one
l10n_ch_additional_accident_insurance_line --|> l10n_ch_additional_accident_insurance_line_rate : one2many
l10n_ch_additional_accident_insurance_line_rate --> l10n_ch_additional_accident_insurance_line : many2one
l10n_ch_compensation_fund --|> l10n_ch_compensation_fund_line : one2many
l10n_ch_compensation_fund_line --> l10n_ch_compensation_fund : many2one
l10n_ch_hr_employee_children --> hr_employee : many2one
ch_yearly_report .. l10n_ch_social_insurance : many2many
ch_yearly_report .. l10n_ch_accident_insurance : many2many
ch_yearly_report .. l10n_ch_additional_accident_insurance : many2many
ch_yearly_report .. l10n_ch_sickness_insurance : many2many
ch_yearly_report .. l10n_ch_compensation_fund : many2many
class "res.company" as res_company
ch_yearly_report --> res_company : many2one
class "res.currency" as res_currency
ch_yearly_report --> res_currency : many2one
ch_yearly_report --|> ch_yearly_report_line : one2many
ch_yearly_report_line --> ch_yearly_report : many2one
hr_payslip_is_log_line --> hr_payslip : many2one
hr_payslip_is_log_line --> hr_payslip : many2one
l10n_ch_location_unit --> res_company : many2one
l10n_ch_location_unit --> res_partner : many2one
l10n_ch_lpp_insurance --> res_partner : many2one
l10n_ch_monthly_summary .. res_company : many2many
l10n_ch_monthly_summary --> res_currency : many2one
l10n_ch_salary_certificate --> res_company : many2one
l10n_ch_salary_certificate --> res_currency : many2one
l10n_ch_sickness_insurance --> res_partner : many2one
l10n_ch_sickness_insurance --|> l10n_ch_sickness_insurance_line : one2many
l10n_ch_sickness_insurance_line --> l10n_ch_sickness_insurance : many2one
l10n_ch_sickness_insurance_line --|> l10n_ch_sickness_insurance_line_rate : one2many
l10n_ch_sickness_insurance_line_rate --> l10n_ch_sickness_insurance_line : many2one
l10n_ch_social_insurance --|> l10n_ch_social_insurance_avs_line : one2many
l10n_ch_social_insurance --|> l10n_ch_social_insurance_ac_line : one2many
l10n_ch_social_insurance --|> l10n_ch_social_insurance_avs_retirement_rente : one2many
l10n_ch_social_insurance --|> l10n_ch_social_insurance_avs_ac_threshold : one2many
l10n_ch_social_insurance --|> l10n_ch_social_insurance_avs_acc_threshold : one2many
l10n_ch_social_insurance --> l10n_ch_accident_insurance : many2one
l10n_ch_social_insurance --> l10n_ch_lpp_insurance : many2one
l10n_ch_social_insurance_avs_line --> l10n_ch_social_insurance : many2one
l10n_ch_social_insurance_ac_line --> l10n_ch_social_insurance : many2one
l10n_ch_social_insurance_avs_retirement_rente --> l10n_ch_social_insurance : many2one
l10n_ch_social_insurance_avs_ac_threshold --> l10n_ch_social_insurance : many2one
l10n_ch_social_insurance_avs_acc_threshold --> l10n_ch_social_insurance : many2one
l10n_ch_is_report --> res_company : many2one
l10n_ch_is_report --> res_currency : many2one
l10n_ch_is_report .. l10n_ch_location_unit : many2many
l10n_ch_is_report --|> l10n_ch_is_report_line : one2many
l10n_ch_is_report_line --> l10n_ch_is_report : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
