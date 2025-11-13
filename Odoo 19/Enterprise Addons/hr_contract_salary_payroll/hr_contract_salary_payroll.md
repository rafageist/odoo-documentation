<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Salary Configurator - Payroll

- Version: v19
- Category: enterprise
- Source: enterprise19/hr_contract_salary_payroll
- Dependencies: [[Odoo 19/Enterprise Addons/hr_contract_salary/hr_contract_salary|hr_contract_salary]], [[Odoo 19/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]

## Summary

Adds a Gross to Net Salary Simulaton

## XML Artifacts (detected)

- Views: 8
- Actions: 2
- Menus: 6
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `HrApplicant`
- `HrContractSalaryBenefit`
- `HrContractSalaryOffer`
- `HrContractSalaryResume`
- `HrEmployee`
- `HrPayrollHeadcountLine`
- `HrPayslipWorkedDays`
- `HrVersion`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Salary Configurator - Payroll - Models and Relations
class HrApplicant
class HrContractSalaryBenefit
class HrContractSalaryOffer
class HrContractSalaryResume
class HrEmployee
class HrPayrollHeadcountLine
class HrPayslipWorkedDays
class HrVersion
class "hr.salary.rule" as hr_salary_rule
HrContractSalaryBenefit --> hr_salary_rule : many2one
class "hr.payroll.structure" as hr_payroll_structure
HrContractSalaryOffer --> hr_payroll_structure : many2one
class "resource.calendar" as resource_calendar
HrContractSalaryOffer --> resource_calendar : many2one
class "hr.employee" as hr_employee
HrContractSalaryOffer --> hr_employee : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
