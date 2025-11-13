<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Payroll Accounting

- Version: v19
- Category: enterprise
- Source: enterprise19/hr_payroll_account
- Dependencies: [[Odoo 19/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]], [[Odoo 19/Enterprise Addons/accountant/accountant|accountant]], [[Odoo 19/Community Addons/base_iban/base_iban|base_iban]]
## XML Artifacts (detected)

- Views: 12
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountJournal`
- `AccountMove`
- `AccountMoveLine`
- `AccountPayment`
- `HrPayrollStructure`
- `HrPayslip`
- `HrPayslipLine`
- `HrPayslipRun`
- `hr.salary.rule`
- `hr.version`
- `ResCompany`
- `ResPartnerBank`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Payroll Accounting - Models and Relations
class AccountJournal
class AccountMove
class AccountMoveLine
class AccountPayment
class HrPayrollStructure
class HrPayslip
class HrPayslipLine
class HrPayslipRun
class "hr.salary.rule" as hr_salary_rule
class "hr.version" as hr_version
class ResCompany
class ResPartnerBank
class "hr.payslip" as hr_payslip
AccountMove --|> hr_payslip : one2many
class "res.partner.bank" as res_partner_bank
AccountMoveLine --> res_partner_bank : many2one
class "account.journal" as account_journal
HrPayrollStructure --> account_journal : many2one
HrPayslip --> account_journal : many2one
class "account.move" as account_move
HrPayslip --> account_move : many2one
class "account.account.tag" as account_account_tag
HrPayslipLine .. account_account_tag : many2many
HrPayslipLine .. account_account_tag : many2many
HrPayslipRun --> account_move : many2one
class "account.account" as account_account
hr_salary_rule --> account_account : many2one
hr_salary_rule --> account_account : many2one
hr_salary_rule .. account_account_tag : many2many
hr_salary_rule .. account_account_tag : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
