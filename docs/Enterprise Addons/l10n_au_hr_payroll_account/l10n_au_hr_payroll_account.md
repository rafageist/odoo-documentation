<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Australia - Payroll with Accounting

- Scope: Enterprise Addons
- Source: enterprise/l10n_au_hr_payroll_account
- Dependencies: [[docs/Enterprise Addons/l10n_au_hr_payroll/l10n_au_hr_payroll|l10n_au_hr_payroll]], [[docs/Enterprise Addons/hr_payroll_account/hr_payroll_account|hr_payroll_account]], [[docs/Community Addons/l10n_au/l10n_au|l10n_au]], [[docs/Enterprise Addons/l10n_au_aba/l10n_au_aba|l10n_au_aba]]

## XML Artifacts (detected)

- Views: 27
- Actions: 7
- Menus: 4
- Rules (ir.rule): 4
- Access CSV entries: 13

## Detected Models

- `AccountBatchPayment`
- `AccountJournal`
- `AccountPayment`
- `AccountPaymentMethod`
- `L10NAUAccountReturn`
- `HrEmployee`
- `HrPayslip`
- `HrPayslipLine`
- `HrPayslipRun`
- `HrVersion`
- `l10n_au.payslip.ytd`
- `l10n_au.payslip.ytd.input`
- `l10n_au.stp`
- `l10n_au.stp.emp`
- `L10n_AuSuperFund`
- `l10n_au.super.stream`
- `l10n_au.super.stream.line`
- `ResCompany`
- `ResPartner`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Australia - Payroll with Accounting - Models and Relations
class AccountBatchPayment
class AccountJournal
class AccountPayment
class AccountPaymentMethod
class L10NAUAccountReturn
class HrEmployee
class HrPayslip
class HrPayslipLine
class HrPayslipRun
class HrVersion
class "l10n_au.payslip.ytd" as l10n_au_payslip_ytd
class "l10n_au.payslip.ytd.input" as l10n_au_payslip_ytd_input
class "l10n_au.stp" as l10n_au_stp
class "l10n_au.stp.emp" as l10n_au_stp_emp
class L10n_AuSuperFund
class "l10n_au.super.stream" as l10n_au_super_stream
class "l10n_au.super.stream.line" as l10n_au_super_stream_line
class ResCompany
class ResPartner
HrEmployee --|> l10n_au_payslip_ytd : one2many
class "account.batch.payment" as account_batch_payment
HrPayslipRun --> account_batch_payment : many2one
class "hr.employee" as hr_employee
l10n_au_payslip_ytd --> hr_employee : many2one
class "hr.payroll.structure" as hr_payroll_structure
l10n_au_payslip_ytd --> hr_payroll_structure : many2one
class "hr.salary.rule" as hr_salary_rule
l10n_au_payslip_ytd --> hr_salary_rule : many2one
l10n_au_payslip_ytd --|> l10n_au_payslip_ytd_input : one2many
l10n_au_payslip_ytd_input --> l10n_au_payslip_ytd : many2one
class "hr.payslip.run" as hr_payslip_run
l10n_au_stp --> hr_payslip_run : many2one
class "hr.payslip" as hr_payslip
l10n_au_stp .. hr_payslip : many2many
class "res.company" as res_company
l10n_au_stp --> res_company : many2one
class "res.currency" as res_currency
l10n_au_stp --> res_currency : many2one
l10n_au_stp --> l10n_au_stp : many2one
l10n_au_stp --|> l10n_au_stp_emp : one2many
l10n_au_stp_emp --> hr_employee : many2one
l10n_au_stp_emp .. hr_payslip : many2many
l10n_au_stp_emp .. l10n_au_payslip_ytd : many2many
l10n_au_stp_emp --> res_currency : many2one
l10n_au_stp_emp --> l10n_au_stp : many2one
class "res.partner.bank" as res_partner_bank
L10n_AuSuperFund --> res_partner_bank : many2one
l10n_au_super_stream --> res_company : many2one
l10n_au_super_stream --> res_currency : many2one
l10n_au_super_stream --|> l10n_au_super_stream_line : one2many
class "ir.attachment" as ir_attachment
l10n_au_super_stream --> ir_attachment : many2one
class "account.journal" as account_journal
l10n_au_super_stream --> account_journal : many2one
class "account.payment" as account_payment
l10n_au_super_stream --> account_payment : many2one
l10n_au_super_stream_line --> l10n_au_super_stream : many2one
l10n_au_super_stream_line --> res_company : many2one
l10n_au_super_stream_line --> res_company : many2one
l10n_au_super_stream_line --> hr_employee : many2one
l10n_au_super_stream_line --> hr_employee : many2one
class "l10n_au.super.fund" as l10n_au_super_fund
l10n_au_super_stream_line --> l10n_au_super_fund : many2one
l10n_au_super_stream_line --> hr_payslip : many2one
class "l10n_au.super.account" as l10n_au_super_account
l10n_au_super_stream_line --> l10n_au_super_account : many2one
l10n_au_super_stream_line .. l10n_au_super_account : many2many
ResCompany --> hr_employee : many2one
ResCompany --> hr_employee : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



