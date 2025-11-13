<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Payroll Accounting

- Version: v18
- Category: enterprise
- Source: enterprise18/hr_payroll_account
- Dependencies: [[Odoo 18/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]], [[Odoo 18/Enterprise Addons/account_accountant/account_accountant|account_accountant]], [[Odoo 18/Community Addons/base_iban/base_iban|base_iban]]
## XML Artifacts (detected)

- Views: 11
- Actions: 2
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountJournal`
- `AccountMove`
- `AccountPayment`
- `HrContract`
- `HrPayrollStructure`
- `HrPayslip`
- `HrPayslipRun`
- `HrSalaryRule`
- `ResCompany`
- `ResPartnerBank`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Payroll Accounting - Models and Relations
class AccountJournal
class AccountMove
class AccountPayment
class HrContract
class HrPayrollStructure
class HrPayslip
class HrPayslipRun
class HrSalaryRule
class ResCompany
class ResPartnerBank
class "hr.payslip" as hr_payslip
AccountMove --|> hr_payslip : one2many
class "account.analytic.account" as account_analytic_account
HrContract --> account_analytic_account : many2one
class "account.journal" as account_journal
HrPayrollStructure --> account_journal : many2one
HrPayslip --> account_journal : many2one
class "account.move" as account_move
HrPayslip --> account_move : many2one
HrPayslipRun --> account_move : many2one
HrSalaryRule --> account_analytic_account : many2one
class "account.account" as account_account
HrSalaryRule --> account_account : many2one
HrSalaryRule --> account_account : many2one
class "account.account.tag" as account_account_tag
HrSalaryRule .. account_account_tag : many2many
HrSalaryRule .. account_account_tag : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
