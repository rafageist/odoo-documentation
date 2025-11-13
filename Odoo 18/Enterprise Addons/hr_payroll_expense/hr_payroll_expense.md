<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Expenses in Payslips

- Version: v18
- Category: enterprise
- Source: enterprise18/hr_payroll_expense
- Dependencies: [[Odoo 18/Community Addons/hr_expense/hr_expense|hr_expense]], [[Odoo 18/Enterprise Addons/hr_payroll_account/hr_payroll_account|hr_payroll_account]]

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
- `HrExpenseSheet`
- `HrPayrollStructure`
- `HrPayslip`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Expenses in Payslips - Models and Relations
class AccountMove
class HrExpenseSheet
class HrPayrollStructure
class HrPayslip
class "hr.payslip" as hr_payslip
HrExpenseSheet --> hr_payslip : many2one
class "hr.expense.sheet" as hr_expense_sheet
HrPayslip --|> hr_expense_sheet : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
