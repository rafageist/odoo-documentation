<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Indian Payroll

- Scope: Enterprise Addons
- Source: enterprise/l10n_in_hr_payroll
- Dependencies: [[docs/Enterprise Addons/hr_payroll_holidays/hr_payroll_holidays|hr_payroll_holidays]], [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]

## XML Artifacts (detected)

- Views: 15
- Actions: 12
- Menus: 7
- Rules (ir.rule): 0
- Access CSV entries: 8

## Detected Models

- `HrEmployee`
- `HrPayrollStructureType`
- `HrPayslip`
- `HrPayslipRun`
- `HrVersion`
- `l10n_in_hr_payroll.salary.statement`
- `ResCompany`
- `ResUsers`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Indian Payroll - Models and Relations
class HrEmployee
class HrPayrollStructureType
class HrPayslip
class HrPayslipRun
class HrVersion
class "l10n_in_hr_payroll.salary.statement" as l10n_in_hr_payroll_salary_statement
class ResCompany
class ResUsers
class "hr.rule.parameter" as hr_rule_parameter
HrVersion --> hr_rule_parameter : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



