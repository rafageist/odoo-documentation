<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Expenses in Payslips

- Scope: Enterprise Addons
- Source: enterprise/hr_payroll_expense
- Dependencies: [[docs/Community Addons/hr_expense/hr_expense|hr_expense]], [[docs/Enterprise Addons/hr_payroll_account/hr_payroll_account|hr_payroll_account]]

## Summary

Submit, validate and reinvoice employee expenses

## XML Artifacts (detected)

- Views: 3
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `HrExpense`
- `HrPayrollStructure`
- `HrPayslip`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Expenses in Payslips - Models and Relations
class AccountMove
class HrExpense
class HrPayrollStructure
class HrPayslip
class "hr.payslip" as hr_payslip
HrExpense --> hr_payslip : many2one
class "hr.expense" as hr_expense
HrPayslip --|> hr_expense : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



