
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Payroll

- Scope: Enterprise Addons
- Source: enterprise/hr_payroll
- Dependencies: [[docs/Enterprise Addons/hr_work_entry_enterprise/hr_work_entry_enterprise|hr_work_entry_enterprise]], [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/html_editor/html_editor|html_editor]]

## Summary

Manage your employee payroll

## XML Artifacts (detected)

- Views: 87
- Actions: 52
- Menus: 28
- Rules (ir.rule): 16
- Access CSV entries: 35

## Detected Models

- `HrEmployee`
- `hr.payroll.dashboard.warning`
- `hr.payroll.employee.declaration`
- `hr.payroll.headcount`
- `hr.payroll.headcount.line`
- `hr.payroll.headcount.working.rate`
- `hr.payroll.structure`
- `HrPayrollStructureType`
- `hr.payslip`
- `hr.payslip.input`
- `hr.payslip.input.type`
- `hr.payslip.line`
- `hr.payslip.run`
- `hr.payslip.worked_days`
- `hr.rule.parameter.value`
- `hr.rule.parameter`
- `hr.salary.attachment`
- `hr.salary.rule`
- `hr.salary.rule.category`
- `hr.salary.rule.section`
- `HrVersion`
- `HrWorkEntry`
- `HrWorkEntryType`
- `hr.payroll.note`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Payroll - Models and Relations
class HrEmployee
class "hr.payroll.dashboard.warning" as hr_payroll_dashboard_warning
class "hr.payroll.employee.declaration" as hr_payroll_employee_declaration
class "hr.payroll.headcount" as hr_payroll_headcount
class "hr.payroll.headcount.line" as hr_payroll_headcount_line
class "hr.payroll.headcount.working.rate" as hr_payroll_headcount_working_rate
class "hr.payroll.structure" as hr_payroll_structure
class HrPayrollStructureType
class "hr.payslip" as hr_payslip
class "hr.payslip.input" as hr_payslip_input
class "hr.payslip.input.type" as hr_payslip_input_type
class "hr.payslip.line" as hr_payslip_line
class "hr.payslip.run" as hr_payslip_run
class "hr.payslip.worked_days" as hr_payslip_worked_days
class "hr.rule.parameter.value" as hr_rule_parameter_value
class "hr.rule.parameter" as hr_rule_parameter
class "hr.salary.attachment" as hr_salary_attachment
class "hr.salary.rule" as hr_salary_rule
class "hr.salary.rule.category" as hr_salary_rule_category
class "hr.salary.rule.section" as hr_salary_rule_section
class HrVersion
class HrWorkEntry
class HrWorkEntryType
class "hr.payroll.note" as hr_payroll_note
class ResCompany
class "res.currency" as res_currency
HrEmployee --> res_currency : many2one
HrEmployee --|> hr_payslip : one2many
HrEmployee .. hr_salary_attachment : many2many
class "res.country" as res_country
hr_payroll_dashboard_warning --> res_country : many2one
class "hr.employee" as hr_employee
hr_payroll_employee_declaration --> hr_employee : many2one
class "res.company" as res_company
hr_payroll_employee_declaration --> res_company : many2one
hr_payroll_headcount --> res_company : many2one
hr_payroll_headcount --|> hr_payroll_headcount_line : one2many
hr_payroll_headcount_line --> hr_payroll_headcount : many2one
hr_payroll_headcount_line .. hr_payroll_headcount_working_rate : many2many
class "hr.version" as hr_version
hr_payroll_headcount_line --> hr_version : many2one
class "hr.payroll.structure.type" as hr_payroll_structure_type
hr_payroll_structure --> hr_payroll_structure_type : many2one
hr_payroll_structure --> res_country : many2one
hr_payroll_structure --|> hr_salary_rule : one2many
class "ir.actions.report" as ir_actions_report
hr_payroll_structure --> ir_actions_report : many2one
class "hr.work.entry.type" as hr_work_entry_type
hr_payroll_structure .. hr_work_entry_type : many2many
hr_payroll_structure .. hr_payslip_input_type : many2many
HrPayrollStructureType --|> hr_payroll_structure : one2many
HrPayrollStructureType --> hr_payroll_structure : many2one
HrPayrollStructureType --> hr_work_entry_type : many2one
hr_payslip --> hr_payroll_structure : many2one
hr_payslip --> hr_payroll_structure_type : many2one
hr_payslip --> hr_employee : many2one
class "hr.department" as hr_department
hr_payslip --> hr_department : many2one
class "hr.job" as hr_job
hr_payslip --> hr_job : many2one
hr_payslip --|> hr_payslip_line : one2many
hr_payslip --> res_company : many2one
hr_payslip --> res_country : many2one
hr_payslip --|> hr_payslip_worked_days : one2many
hr_payslip --|> hr_payslip_input : one2many
hr_payslip --> hr_version : many2one
hr_payslip --> hr_payslip_run : many2one
hr_payslip .. hr_salary_attachment : many2many
hr_payslip --> hr_payslip : many2one
hr_payslip --|> hr_payslip : one2many
hr_payslip_input --> hr_payslip : many2one
hr_payslip_input --> hr_employee : many2one
hr_payslip_input --> hr_payslip_input_type : many2one
hr_payslip_input .. hr_payslip_input_type : many2many
hr_payslip_input_type .. hr_payroll_structure : many2many
hr_payslip_input_type --> res_country : many2one
hr_payslip_line --> hr_payslip : many2one
hr_payslip_line --> hr_salary_rule : many2one
hr_payslip_line --> hr_version : many2one
hr_payslip_line --> hr_employee : many2one
hr_payslip_line --> res_currency : many2one
hr_payslip_run --|> hr_payslip : one2many
hr_payslip_run --> hr_payroll_structure : many2one
hr_payslip_run --> res_company : many2one
hr_payslip_run --> res_country : many2one
hr_payslip_worked_days --> hr_payslip : many2one
hr_payslip_worked_days --> hr_employee : many2one
hr_payslip_worked_days --> hr_work_entry_type : many2one
hr_payslip_worked_days --> res_currency : many2one
hr_rule_parameter_value --> hr_rule_parameter : many2one
hr_rule_parameter --> res_country : many2one
hr_rule_parameter --|> hr_rule_parameter_value : one2many
hr_rule_parameter --|> hr_salary_rule : one2many
hr_salary_attachment .. hr_employee : many2many
hr_salary_attachment --> res_company : many2one
hr_salary_attachment --> res_currency : many2one
hr_salary_attachment --> hr_payslip_input_type : many2one
hr_salary_attachment .. hr_payslip : many2many
hr_salary_rule --> hr_payroll_structure : many2one
hr_salary_rule --> hr_salary_rule_category : many2one
hr_salary_rule --> hr_payslip_input_type : many2one
hr_salary_rule --> hr_payslip_input_type : many2one
class "res.partner" as res_partner
hr_salary_rule --> res_partner : many2one
hr_salary_rule --> hr_salary_rule_section : many2one
hr_salary_rule --> hr_salary_rule : many2one
hr_salary_rule_category --> hr_salary_rule_category : many2one
hr_salary_rule_category --|> hr_salary_rule_category : one2many
hr_salary_rule_category --> res_country : many2one
hr_salary_rule_section .. hr_payroll_structure : many2many
class "resource.calendar" as resource_calendar
HrVersion --> resource_calendar : many2one
HrWorkEntryType .. hr_payroll_structure : many2many
hr_payroll_note --> res_company : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

