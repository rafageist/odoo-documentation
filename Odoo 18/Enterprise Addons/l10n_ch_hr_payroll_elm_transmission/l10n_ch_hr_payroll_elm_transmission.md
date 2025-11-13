<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Swissdec Certified Payroll (ELM 5.0)

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_ch_hr_payroll_elm_transmission
- Dependencies: [[Odoo 18/Enterprise Addons/l10n_ch_hr_payroll/l10n_ch_hr_payroll|l10n_ch_hr_payroll]], [[Odoo 18/Community Addons/iap/iap|iap]]
## XML Artifacts (detected)

- Views: 65
- Actions: 23
- Menus: 34
- Rules (ir.rule): 13
- Access CSV entries: 26

## Detected Models

- `HrContract`
- `HrEmployee`
- `HrLeave`
- `HRLeaveType`
- `HrPayslip`
- `hr.salary.rule`
- `IrUiMenu`
- `L10nCHPayslipISLogLine`
- `l10nChSocialInsurance`
- `l10nChSocialInsuranceAVSLine`
- `l10n.ch.avs.splits`
- `l10n.ch.avs.split.lines`
- `l10nChCafInsurance`
- `L10nChHrEmployeeChildren`
- `l10n.ch.lpp.basis.report`
- `l10n.ch.lpp.basis.report.line`
- `l10n.ch.ema.declaration`
- `l10n.ch.salary.certificate`
- `l10n.ch.is.report`
- `l10n.ch.statistic.report`
- `ch.yearly.report`
- `l10n.ch.is.mutation`
- `l10n.ch.lpp.mutation`
- `l10n.ch.employee.monthly.values`
- `l10n.ch.employee.yearly.values`
- `l10n.ch.hr.contract.wage`
- `l10nChSicknessInsurance`
- `l10nChSicknessInsuranceLine`
- `L10nChIndividualAccount`
- `L10nCHISMutationLine`
- `hr.employee.is.line.correction`
- `l10nChAccidentInsurance`
- `l10n.ch.accident.group`
- `l10nChAccidentInsuranceLineRate`
- `l10nChAdditionalAccidentInsurance`
- `l10nChAdditionalAccidentInsuranceLine`
- `l10nChLppInsurance`
- `l10n.ch.lpp.insurance.line`
- `l10n.ch.master.data.report`
- `L10nChMonthlySummaryWizard`
- `l10n.ch.salary.certificate.profile`
- `l10n.ch.source.tax.institution`
- `l10n.ch.swissdec.declaration`
- `l10n.ch.dialog.message`
- `l10n.ch.dialog.message.field`
- `l10n.ch.swissdec.job.result`
- `l10n.ch.swiss.wage.component`
- `L10nChWorkLocation`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Swissdec Certified Payroll (ELM 5.0) - Models and Relations
class HrContract
class HrEmployee
class HrLeave
class HRLeaveType
class HrPayslip
class "hr.salary.rule" as hr_salary_rule
class IrUiMenu
class L10nCHPayslipISLogLine
class l10nChSocialInsurance
class l10nChSocialInsuranceAVSLine
class "l10n.ch.avs.splits" as l10n_ch_avs_splits
class "l10n.ch.avs.split.lines" as l10n_ch_avs_split_lines
class l10nChCafInsurance
class L10nChHrEmployeeChildren
class "l10n.ch.lpp.basis.report" as l10n_ch_lpp_basis_report
class "l10n.ch.lpp.basis.report.line" as l10n_ch_lpp_basis_report_line
class "l10n.ch.ema.declaration" as l10n_ch_ema_declaration
class "l10n.ch.salary.certificate" as l10n_ch_salary_certificate
class "l10n.ch.is.report" as l10n_ch_is_report
class "l10n.ch.statistic.report" as l10n_ch_statistic_report
class "ch.yearly.report" as ch_yearly_report
class "l10n.ch.is.mutation" as l10n_ch_is_mutation
class "l10n.ch.lpp.mutation" as l10n_ch_lpp_mutation
class "l10n.ch.employee.monthly.values" as l10n_ch_employee_monthly_values
class "l10n.ch.employee.yearly.values" as l10n_ch_employee_yearly_values
class "l10n.ch.hr.contract.wage" as l10n_ch_hr_contract_wage
class l10nChSicknessInsurance
class l10nChSicknessInsuranceLine
class L10nChIndividualAccount
class L10nCHISMutationLine
class "hr.employee.is.line.correction" as hr_employee_is_line_correction
class l10nChAccidentInsurance
class "l10n.ch.accident.group" as l10n_ch_accident_group
class l10nChAccidentInsuranceLineRate
class l10nChAdditionalAccidentInsurance
class l10nChAdditionalAccidentInsuranceLine
class l10nChLppInsurance
class "l10n.ch.lpp.insurance.line" as l10n_ch_lpp_insurance_line
class "l10n.ch.master.data.report" as l10n_ch_master_data_report
class L10nChMonthlySummaryWizard
class "l10n.ch.salary.certificate.profile" as l10n_ch_salary_certificate_profile
class "l10n.ch.source.tax.institution" as l10n_ch_source_tax_institution
class "l10n.ch.swissdec.declaration" as l10n_ch_swissdec_declaration
class "l10n.ch.dialog.message" as l10n_ch_dialog_message
class "l10n.ch.dialog.message.field" as l10n_ch_dialog_message_field
class "l10n.ch.swissdec.job.result" as l10n_ch_swissdec_job_result
class "l10n.ch.swiss.wage.component" as l10n_ch_swiss_wage_component
class L10nChWorkLocation
class ResCompany
class "hr.contract.type" as hr_contract_type
HrContract --> hr_contract_type : many2one
HrContract --> l10n_ch_accident_group : many2one
HrContract .. l10n_ch_lpp_insurance_line : many2many
HrContract --|> l10n_ch_lpp_mutation : one2many
HrContract --|> l10n_ch_hr_contract_wage : one2many
class "res.country" as res_country
HrEmployee --> res_country : many2one
HrEmployee --|> l10n_ch_is_mutation : one2many
HrEmployee --|> l10n_ch_salary_certificate_profile : one2many
HrPayslip --> l10n_ch_accident_group : many2one
class "l10n.ch.location.unit" as l10n_ch_location_unit
HrPayslip --> l10n_ch_location_unit : many2one
class "hr.employee.is.line" as hr_employee_is_line
HrPayslip --> hr_employee_is_line : many2one
HrPayslip --> l10n_ch_employee_monthly_values : many2one
HrPayslip --|> l10n_ch_swiss_wage_component : one2many
class "hr.payslip" as hr_payslip
L10nCHPayslipISLogLine --> hr_payslip : many2one
L10nCHPayslipISLogLine --> hr_employee_is_line : many2one
L10nCHPayslipISLogLine --> hr_payslip : many2one
class "res.company" as res_company
l10nChSocialInsurance --> res_company : many2one
class "hr.employee" as hr_employee
l10n_ch_avs_splits --> hr_employee : many2one
l10n_ch_avs_splits --|> l10n_ch_avs_split_lines : one2many
l10n_ch_avs_split_lines --> l10n_ch_avs_splits : many2one
l10nChCafInsurance --> res_company : many2one
l10n_ch_lpp_basis_report --|> l10n_ch_lpp_basis_report_line : one2many
l10n_ch_lpp_basis_report_line --> hr_employee : many2one
class "l10n.ch.lpp.insurance" as l10n_ch_lpp_insurance
l10n_ch_lpp_basis_report_line --> l10n_ch_lpp_insurance : many2one
l10n_ch_lpp_basis_report_line --> l10n_ch_lpp_basis_report : many2one
class "l10n.ch.social.insurance" as l10n_ch_social_insurance
l10n_ch_ema_declaration .. l10n_ch_social_insurance : many2many
class "l10n.ch.compensation.fund" as l10n_ch_compensation_fund
l10n_ch_ema_declaration .. l10n_ch_compensation_fund : many2many
l10n_ch_ema_declaration .. l10n_ch_lpp_insurance : many2many
l10n_ch_salary_certificate --> ch_yearly_report : many2one
l10n_ch_salary_certificate .. hr_employee : many2many
l10n_ch_is_report .. l10n_ch_source_tax_institution : many2many
ch_yearly_report .. l10n_ch_source_tax_institution : many2many
l10n_ch_is_mutation --> l10n_ch_employee_monthly_values : many2one
l10n_ch_is_mutation --> hr_employee : many2one
l10n_ch_is_mutation --> hr_employee_is_line : many2one
l10n_ch_lpp_mutation --> l10n_ch_employee_monthly_values : many2one
class "hr.contract" as hr_contract
l10n_ch_lpp_mutation --> hr_contract : many2one
l10n_ch_lpp_mutation --> hr_employee : many2one
l10n_ch_employee_monthly_values --> l10n_ch_employee_yearly_values : many2one
l10n_ch_employee_monthly_values --|> l10n_ch_lpp_mutation : one2many
l10n_ch_employee_monthly_values --|> l10n_ch_is_mutation : one2many
l10n_ch_employee_yearly_values --> hr_employee : many2one
l10n_ch_employee_yearly_values --|> l10n_ch_employee_monthly_values : one2many
l10n_ch_hr_contract_wage --> hr_contract : many2one
class "hr.payslip.input.type" as hr_payslip_input_type
l10n_ch_hr_contract_wage --> hr_payslip_input_type : many2one
l10nChSicknessInsurance --> res_company : many2one
L10nCHISMutationLine .. hr_payslip : many2many
L10nCHISMutationLine --|> l10n_ch_is_mutation : one2many
L10nCHISMutationLine --|> hr_employee_is_line_correction : one2many
class "hr.payslip.is.log.line" as hr_payslip_is_log_line
L10nCHISMutationLine --|> hr_payslip_is_log_line : one2many
hr_employee_is_line_correction --> hr_employee_is_line : many2one
hr_employee_is_line_correction --> hr_payslip : many2one
l10nChAccidentInsurance --> res_company : many2one
l10nChAccidentInsurance --|> l10n_ch_accident_group : one2many
class "l10n.ch.accident.insurance" as l10n_ch_accident_insurance
l10n_ch_accident_group --> l10n_ch_accident_insurance : many2one
class "l10n.ch.accident.insurance.line.rate" as l10n_ch_accident_insurance_line_rate
l10n_ch_accident_group --|> l10n_ch_accident_insurance_line_rate : one2many
l10nChAccidentInsuranceLineRate --> l10n_ch_accident_group : many2one
l10nChAdditionalAccidentInsurance --> res_company : many2one
l10nChLppInsurance --> res_company : many2one
l10nChLppInsurance --|> l10n_ch_lpp_insurance_line : one2many
l10n_ch_lpp_insurance_line --> l10n_ch_lpp_insurance : many2one
l10n_ch_master_data_report --> res_company : many2one
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
class "res.currency" as res_currency
l10n_ch_swiss_wage_component --> res_currency : many2one
ResCompany --|> l10n_ch_social_insurance : one2many
ResCompany --|> l10n_ch_compensation_fund : one2many
ResCompany --|> l10n_ch_accident_insurance : one2many
class "l10n.ch.additional.accident.insurance" as l10n_ch_additional_accident_insurance
ResCompany --|> l10n_ch_additional_accident_insurance : one2many
class "l10n.ch.sickness.insurance" as l10n_ch_sickness_insurance
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

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
