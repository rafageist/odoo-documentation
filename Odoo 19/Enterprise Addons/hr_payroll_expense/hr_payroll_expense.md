<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Expenses in Payslips

- Version: v19
- Category: enterprise
- Source: enterprise19/hr_payroll_expense
- Dependencies: [[Odoo 19/Community Addons/hr_expense/hr_expense|hr_expense]], [[Odoo 19/Enterprise Addons/hr_payroll_account/hr_payroll_account|hr_payroll_account]]

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
!include ../../../Templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
