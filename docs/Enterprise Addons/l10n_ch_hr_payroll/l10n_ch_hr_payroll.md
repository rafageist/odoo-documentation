<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Switzerland - Swissdec Certified ELM 5.0 - Payroll

- Scope: Enterprise Addons
- Source: enterprise/l10n_ch_hr_payroll
- Dependencies: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]], [[docs/Community Addons/hr_work_entry_holidays/hr_work_entry_holidays|hr_work_entry_holidays]], [[docs/Enterprise Addons/hr_payroll_holidays/hr_payroll_holidays|hr_payroll_holidays]], [[docs/Community Addons/iap/iap|iap]]

## XML Artifacts (detected)

- Views: 78
- Actions: 33
- Menus: 34
- Rules (ir.rule): 18
- Access CSV entries: 54

## Detected Models

- `HrEmployee`
- `hr.employee.is.line`
- `hr.employee.is.line.correction`
- `HrLeave`
- `HRLeaveType`
- `HrPayslip`
- `HrPayslipRun`
- `HrRuleParameter`
- `HrSalaryRule`
- `HrVersion`
- `IrUiMenu`
- `l10n.ch.social.insurance`
- `l10n.ch.social.insurance.avs.line`
- `l10n.ch.social.insurance.ac.line`
- `l10n.ch.social.insurance.avs.retirement.rente`
- `l10n.ch.social.insurance.avs.ac.threshold`
- `l10n.ch.social.insurance.avs.acc.threshold`
- `l10n.ch.avs.splits`
- `l10n.ch.avs.split.lines`
- `l10n.ch.compensation.fund`
- `l10n.ch.compensation.fund.line`
- `l10n.ch.lpp.basis.report`
- `l10n.ch.lpp.basis.report.line`
- `l10n.ch.ema.declaration`
- `l10n.ch.salary.certificate`
- `l10n.ch.is.report`
- `l10n.ch.statistic.report`
- `l10n.ch.is.mutation`
- `l10n.ch.lpp.mutation`
- `l10n.ch.employee.monthly.values`
- `l10n.ch.employee.yearly.values`
- `l10n.ch.hr.contract.wage`
- `l10n.ch.hr.employee.children`
- `l10n.ch.sickness.insurance`
- `l10n.ch.sickness.insurance.line`
- `l10n.ch.sickness.insurance.line.rate`
- `l10n.ch.individual.account`
- `ch.yearly.report`
- `hr.payslip.is.log.line`
- `l10n.ch.accident.insurance`
- `l10n.ch.accident.group`
- `l10n.ch.accident.insurance.line`
- `l10n.ch.accident.insurance.line.rate`
- `l10n.ch.additional.accident.insurance`
- `l10n.ch.additional.accident.insurance.line`
- `l10n.ch.additional.accident.insurance.line.rate`
- `l10n.ch.location.unit`
- `l10n.ch.lpp.insurance`
- `l10n.ch.lpp.insurance.line`
- `l10n.ch.master.data.report`
- `l10n.ch.monthly.summary`
- `l10n.ch.occupation`
- `l10n.ch.salary.certificate.profile`
- `l10n.ch.source.tax.institution`
- `l10n.ch.swissdec.declaration`
- `l10n.ch.dialog.message`
- `l10n.ch.dialog.message.field`
- `l10n.ch.swissdec.job.result`
- `l10n.ch.swiss.wage.component`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Switzerland - Swissdec Certified ELM 5.0 - Payroll - Models and Relations
class HrEmployee
class "hr.employee.is.line" as hr_employee_is_line
class "hr.employee.is.line.correction" as hr_employee_is_line_correction
class HrLeave
class HRLeaveType
class HrPayslip
class HrPayslipRun
class HrRuleParameter
class HrSalaryRule
class HrVersion
class IrUiMenu
class "l10n.ch.social.insurance" as l10n_ch_social_insurance
class "l10n.ch.social.insurance.avs.line" as l10n_ch_social_insurance_avs_line
class "l10n.ch.social.insurance.ac.line" as l10n_ch_social_insurance_ac_line
class "l10n.ch.social.insurance.avs.retirement.rente" as l10n_ch_social_insurance_avs_retirement_rente
class "l10n.ch.social.insurance.avs.ac.threshold" as l10n_ch_social_insurance_avs_ac_threshold
class "l10n.ch.social.insurance.avs.acc.threshold" as l10n_ch_social_insurance_avs_acc_threshold
class "l10n.ch.avs.splits" as l10n_ch_avs_splits
class "l10n.ch.avs.split.lines" as l10n_ch_avs_split_lines
class "l10n.ch.compensation.fund" as l10n_ch_compensation_fund
class "l10n.ch.compensation.fund.line" as l10n_ch_compensation_fund_line
class "l10n.ch.lpp.basis.report" as l10n_ch_lpp_basis_report
class "l10n.ch.lpp.basis.report.line" as l10n_ch_lpp_basis_report_line
class "l10n.ch.ema.declaration" as l10n_ch_ema_declaration
class "l10n.ch.salary.certificate" as l10n_ch_salary_certificate
class "l10n.ch.is.report" as l10n_ch_is_report
class "l10n.ch.statistic.report" as l10n_ch_statistic_report
class "l10n.ch.is.mutation" as l10n_ch_is_mutation
class "l10n.ch.lpp.mutation" as l10n_ch_lpp_mutation
class "l10n.ch.employee.monthly.values" as l10n_ch_employee_monthly_values
class "l10n.ch.employee.yearly.values" as l10n_ch_employee_yearly_values
class "l10n.ch.hr.contract.wage" as l10n_ch_hr_contract_wage
class "l10n.ch.hr.employee.children" as l10n_ch_hr_employee_children
class "l10n.ch.sickness.insurance" as l10n_ch_sickness_insurance
class "l10n.ch.sickness.insurance.line" as l10n_ch_sickness_insurance_line
class "l10n.ch.sickness.insurance.line.rate" as l10n_ch_sickness_insurance_line_rate
class "l10n.ch.individual.account" as l10n_ch_individual_account
class "ch.yearly.report" as ch_yearly_report
class "hr.payslip.is.log.line" as hr_payslip_is_log_line
class "l10n.ch.accident.insurance" as l10n_ch_accident_insurance
class "l10n.ch.accident.group" as l10n_ch_accident_group
class "l10n.ch.accident.insurance.line" as l10n_ch_accident_insurance_line
class "l10n.ch.accident.insurance.line.rate" as l10n_ch_accident_insurance_line_rate
class "l10n.ch.additional.accident.insurance" as l10n_ch_additional_accident_insurance
class "l10n.ch.additional.accident.insurance.line" as l10n_ch_additional_accident_insurance_line
class "l10n.ch.additional.accident.insurance.line.rate" as l10n_ch_additional_accident_insurance_line_rate
class "l10n.ch.location.unit" as l10n_ch_location_unit
class "l10n.ch.lpp.insurance" as l10n_ch_lpp_insurance
class "l10n.ch.lpp.insurance.line" as l10n_ch_lpp_insurance_line
class "l10n.ch.master.data.report" as l10n_ch_master_data_report
class "l10n.ch.monthly.summary" as l10n_ch_monthly_summary
class "l10n.ch.occupation" as l10n_ch_occupation
class "l10n.ch.salary.certificate.profile" as l10n_ch_salary_certificate_profile
class "l10n.ch.source.tax.institution" as l10n_ch_source_tax_institution
class "l10n.ch.swissdec.declaration" as l10n_ch_swissdec_declaration
class "l10n.ch.dialog.message" as l10n_ch_dialog_message
class "l10n.ch.dialog.message.field" as l10n_ch_dialog_message_field
class "l10n.ch.swissdec.job.result" as l10n_ch_swissdec_job_result
class "l10n.ch.swiss.wage.component" as l10n_ch_swiss_wage_component
class ResCompany
HrEmployee --|> l10n_ch_hr_employee_children : one2many
HrEmployee --|> l10n_ch_is_mutation : one2many
HrEmployee --|> l10n_ch_salary_certificate_profile : one2many
class "hr.employee" as hr_employee
hr_employee_is_line --> hr_employee : many2one
class "hr.payslip" as hr_payslip
hr_employee_is_line .. hr_payslip : many2many
hr_employee_is_line --|> l10n_ch_is_mutation : one2many
hr_employee_is_line --|> hr_employee_is_line_correction : one2many
hr_employee_is_line --|> hr_payslip_is_log_line : one2many
hr_employee_is_line_correction --> hr_employee_is_line : many2one
hr_employee_is_line_correction --> hr_payslip : many2one
HrPayslip --> l10n_ch_social_insurance : many2one
HrPayslip --> l10n_ch_lpp_insurance : many2one
HrPayslip --> l10n_ch_accident_insurance_line : many2one
HrPayslip .. l10n_ch_additional_accident_insurance_line : many2many
HrPayslip .. l10n_ch_sickness_insurance_line : many2many
HrPayslip --> l10n_ch_compensation_fund : many2one
HrPayslip --|> hr_payslip_is_log_line : one2many
HrPayslip --> l10n_ch_accident_group : many2one
HrPayslip --> l10n_ch_location_unit : many2one
HrPayslip --> hr_employee_is_line : many2one
HrPayslip --> l10n_ch_employee_monthly_values : many2one
HrPayslip --|> l10n_ch_swiss_wage_component : one2many
class "res.country" as res_country
HrVersion --> res_country : many2one
class "hr.contract.type" as hr_contract_type
HrVersion --> hr_contract_type : many2one
HrVersion --> l10n_ch_accident_group : many2one
HrVersion .. l10n_ch_lpp_insurance_line : many2many
HrVersion --|> l10n_ch_lpp_mutation : one2many
HrVersion --> l10n_ch_social_insurance : many2one
HrVersion --> l10n_ch_lpp_insurance : many2one
HrVersion --> l10n_ch_accident_insurance_line : many2one
HrVersion .. l10n_ch_additional_accident_insurance_line : many2many
HrVersion .. l10n_ch_sickness_insurance_line : many2many
HrVersion --> l10n_ch_compensation_fund : many2one
HrVersion --> l10n_ch_location_unit : many2one
HrVersion --|> l10n_ch_hr_contract_wage : one2many
l10n_ch_social_insurance --|> l10n_ch_social_insurance_avs_line : one2many
l10n_ch_social_insurance --|> l10n_ch_social_insurance_ac_line : one2many
l10n_ch_social_insurance --|> l10n_ch_social_insurance_avs_retirement_rente : one2many
l10n_ch_social_insurance --|> l10n_ch_social_insurance_avs_ac_threshold : one2many
l10n_ch_social_insurance --|> l10n_ch_social_insurance_avs_acc_threshold : one2many
l10n_ch_social_insurance --> l10n_ch_accident_insurance : many2one
l10n_ch_social_insurance --> l10n_ch_lpp_insurance : many2one
class "res.company" as res_company
l10n_ch_social_insurance --> res_company : many2one
l10n_ch_social_insurance_avs_line --> l10n_ch_social_insurance : many2one
l10n_ch_social_insurance_ac_line --> l10n_ch_social_insurance : many2one
l10n_ch_social_insurance_avs_retirement_rente --> l10n_ch_social_insurance : many2one
l10n_ch_social_insurance_avs_ac_threshold --> l10n_ch_social_insurance : many2one
l10n_ch_social_insurance_avs_acc_threshold --> l10n_ch_social_insurance : many2one
l10n_ch_avs_splits --> hr_employee : many2one
l10n_ch_avs_splits --|> l10n_ch_avs_split_lines : one2many
l10n_ch_avs_split_lines --> l10n_ch_avs_splits : many2one
l10n_ch_compensation_fund --|> l10n_ch_compensation_fund_line : one2many
l10n_ch_compensation_fund --> res_company : many2one
l10n_ch_compensation_fund_line --> l10n_ch_compensation_fund : many2one
l10n_ch_lpp_basis_report --|> l10n_ch_lpp_basis_report_line : one2many
l10n_ch_lpp_basis_report_line --> hr_employee : many2one
l10n_ch_lpp_basis_report_line --> l10n_ch_lpp_insurance : many2one
l10n_ch_lpp_basis_report_line --> l10n_ch_lpp_basis_report : many2one
l10n_ch_ema_declaration .. l10n_ch_social_insurance : many2many
l10n_ch_ema_declaration .. l10n_ch_compensation_fund : many2many
l10n_ch_ema_declaration .. l10n_ch_lpp_insurance : many2many
l10n_ch_salary_certificate --> ch_yearly_report : many2one
l10n_ch_salary_certificate .. hr_employee : many2many
l10n_ch_is_report .. l10n_ch_source_tax_institution : many2many
l10n_ch_is_mutation --> l10n_ch_employee_monthly_values : many2one
l10n_ch_is_mutation --> hr_employee : many2one
l10n_ch_is_mutation --> hr_employee_is_line : many2one
l10n_ch_lpp_mutation --> l10n_ch_employee_monthly_values : many2one
class "hr.version" as hr_version
l10n_ch_lpp_mutation --> hr_version : many2one
l10n_ch_lpp_mutation --> hr_employee : many2one
l10n_ch_employee_monthly_values --> l10n_ch_employee_yearly_values : many2one
l10n_ch_employee_monthly_values --|> l10n_ch_lpp_mutation : one2many
l10n_ch_employee_monthly_values --|> l10n_ch_is_mutation : one2many
l10n_ch_employee_yearly_values --> hr_employee : many2one
l10n_ch_employee_yearly_values --|> l10n_ch_employee_monthly_values : one2many
l10n_ch_hr_contract_wage --> hr_version : many2one
class "hr.payslip.input.type" as hr_payslip_input_type
l10n_ch_hr_contract_wage --> hr_payslip_input_type : many2one
l10n_ch_hr_employee_children --> hr_employee : many2one
l10n_ch_sickness_insurance --|> l10n_ch_sickness_insurance_line : one2many
l10n_ch_sickness_insurance --> res_company : many2one
l10n_ch_sickness_insurance_line --> l10n_ch_sickness_insurance : many2one
l10n_ch_sickness_insurance_line --|> l10n_ch_sickness_insurance_line_rate : one2many
l10n_ch_sickness_insurance_line_rate --> l10n_ch_sickness_insurance_line : many2one
ch_yearly_report .. l10n_ch_source_tax_institution : many2many
ch_yearly_report .. l10n_ch_social_insurance : many2many
ch_yearly_report .. l10n_ch_accident_insurance : many2many
ch_yearly_report .. l10n_ch_additional_accident_insurance : many2many
ch_yearly_report .. l10n_ch_sickness_insurance : many2many
ch_yearly_report .. l10n_ch_compensation_fund : many2many
hr_payslip_is_log_line --> hr_payslip : many2one
hr_payslip_is_log_line --> hr_employee_is_line : many2one
hr_payslip_is_log_line --> hr_payslip : many2one
l10n_ch_accident_insurance --> res_company : many2one
l10n_ch_accident_insurance --|> l10n_ch_accident_insurance_line : one2many
l10n_ch_accident_insurance --|> l10n_ch_accident_group : one2many
l10n_ch_accident_group --> l10n_ch_accident_insurance : many2one
l10n_ch_accident_group --|> l10n_ch_accident_insurance_line_rate : one2many
l10n_ch_accident_insurance_line --> l10n_ch_accident_insurance : many2one
l10n_ch_accident_insurance_line --|> l10n_ch_accident_insurance_line_rate : one2many
l10n_ch_accident_insurance_line_rate --> l10n_ch_accident_group : many2one
l10n_ch_accident_insurance_line_rate --> l10n_ch_accident_insurance_line : many2one
l10n_ch_additional_accident_insurance --|> l10n_ch_additional_accident_insurance_line : one2many
l10n_ch_additional_accident_insurance --> res_company : many2one
l10n_ch_additional_accident_insurance_line --> l10n_ch_additional_accident_insurance : many2one
l10n_ch_additional_accident_insurance_line --|> l10n_ch_additional_accident_insurance_line_rate : one2many
l10n_ch_additional_accident_insurance_line_rate --> l10n_ch_additional_accident_insurance_line : many2one
l10n_ch_location_unit --> res_company : many2one
class "res.partner" as res_partner
l10n_ch_location_unit --> res_partner : many2one
l10n_ch_lpp_insurance --> res_company : many2one
l10n_ch_lpp_insurance --|> l10n_ch_lpp_insurance_line : one2many
l10n_ch_lpp_insurance_line --> l10n_ch_lpp_insurance : many2one
l10n_ch_master_data_report --> res_company : many2one
l10n_ch_monthly_summary .. res_company : many2many
class "res.currency" as res_currency
l10n_ch_monthly_summary --> res_currency : many2one
l10n_ch_occupation --> hr_employee : many2one
l10n_ch_salary_certificate_profile --> hr_employee : many2one
l10n_ch_salary_certificate_profile --> l10n_ch_salary_certificate_profile : many2one
l10n_ch_salary_certificate_profile --> res_company : many2one
l10n_ch_salary_certificate_profile --> res_country : many2one
l10n_ch_source_tax_institution --> res_company : many2one
l10n_ch_swissdec_declaration --|> l10n_ch_swissdec_job_result : one2many
l10n_ch_dialog_message --> l10n_ch_swissdec_job_result : many2one
l10n_ch_dialog_message --|> l10n_ch_dialog_message_field : one2many
l10n_ch_dialog_message_field --> l10n_ch_dialog_message : many2one
l10n_ch_swissdec_job_result --> l10n_ch_swissdec_declaration : many2one
l10n_ch_swissdec_job_result --|> l10n_ch_dialog_message : one2many
class "ir.attachment" as ir_attachment
l10n_ch_swissdec_job_result --|> ir_attachment : one2many
l10n_ch_swiss_wage_component --> hr_payslip : many2one
class "hr.work.entry.type" as hr_work_entry_type
l10n_ch_swiss_wage_component --> hr_work_entry_type : many2one
l10n_ch_swiss_wage_component --> res_currency : many2one
ResCompany --|> l10n_ch_social_insurance : one2many
ResCompany --|> l10n_ch_compensation_fund : one2many
ResCompany --|> l10n_ch_accident_insurance : one2many
ResCompany --|> l10n_ch_additional_accident_insurance : one2many
ResCompany --|> l10n_ch_sickness_insurance : one2many
ResCompany --|> l10n_ch_lpp_insurance : one2many
ResCompany --|> l10n_ch_location_unit : one2many
ResCompany --|> l10n_ch_source_tax_institution : one2many
ResCompany --|> l10n_ch_salary_certificate_profile : one2many
class "res.country.state" as res_country_state
ResCompany --> res_country_state : many2one
ResCompany --> res_country : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



