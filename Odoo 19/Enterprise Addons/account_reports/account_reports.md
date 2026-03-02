<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Accounting Reports

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/account_reports
- Dependencies: [[Odoo 19/Enterprise Addons/account_accountant/account_accountant|account_accountant]]

## Summary

View and create reports

## XML Artifacts (detected)

- Views: 49
- Actions: 36
- Menus: 27
- Rules (ir.rule): 3
- Access CSV entries: 36

## Detected Models

- `AccountAccount`
- `AccountMoveLine`
- `account.audit.account.status`
- `AccountFiscalPosition`
- `AccountJournal`
- `AccountMove`
- `account.report.annotation`
- `AccountReport`
- `AccountReportLine`
- `AccountReportExpression`
- `AccountReportExternalValue`
- `account.report.horizontal.group`
- `account.report.horizontal.group.rule`
- `account.return.type`
- `account.return`
- `account.return.check`
- `account.return.check.template`
- `account.tax.unit`
- `account.report.budget`
- `account.report.budget.item`
- `IrUiMenu`
- `MailActivity`
- `MailMessage`
- `MailScheduledMessage`
- `MailTrackingValue`
- `ResCompany`
- `ResPartner`
- `ResUsers`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Accounting Reports - Models and Relations
class AccountAccount
class AccountMoveLine
class "account.audit.account.status" as account_audit_account_status
class AccountFiscalPosition
class AccountJournal
class AccountMove
class "account.report.annotation" as account_report_annotation
class AccountReport
class AccountReportLine
class AccountReportExpression
class AccountReportExternalValue
class "account.report.horizontal.group" as account_report_horizontal_group
class "account.report.horizontal.group.rule" as account_report_horizontal_group_rule
class "account.return.type" as account_return_type
class "account.return" as account_return
class "account.return.check" as account_return_check
class "account.return.check.template" as account_return_check_template
class "account.tax.unit" as account_tax_unit
class "account.report.budget" as account_report_budget
class "account.report.budget.item" as account_report_budget_item
class IrUiMenu
class MailActivity
class MailMessage
class MailScheduledMessage
class MailTrackingValue
class ResCompany
class ResPartner
class ResUsers
class "res.currency" as res_currency
AccountAccount .. res_currency : many2many
AccountAccount --|> account_report_budget_item : one2many
AccountAccount --|> account_audit_account_status : one2many
account_audit_account_status --> account_return : many2one
class "account.account" as account_account
account_audit_account_status --> account_account : many2one
AccountMove --> account_return : many2one
class "mail.message" as mail_message
account_report_annotation --> mail_message : many2one
AccountReport .. account_report_horizontal_group : many2many
AccountReport --|> account_return_type : one2many
class "ir.model" as ir_model
AccountReport --> ir_model : many2one
account_report_horizontal_group --|> account_report_horizontal_group_rule : one2many
class "account.report" as account_report
account_report_horizontal_group .. account_report : many2many
account_report_horizontal_group_rule --> account_report_horizontal_group : many2one
account_return_type --> account_report : many2one
class "res.country" as res_country
account_return_type --> res_country : many2one
class "res.partner.bank" as res_partner_bank
account_return_type --> res_partner_bank : many2one
class "res.partner" as res_partner
account_return_type --> res_partner : many2one
account_return --> account_return_type : many2one
class "res.company" as res_company
account_return --> res_company : many2one
account_return --> account_tax_unit : many2one
account_return .. res_company : many2many
class "account.move" as account_move
account_return --|> account_move : one2many
class "ir.attachment" as ir_attachment
account_return .. ir_attachment : many2many
account_return --|> account_return_check : one2many
account_return --> res_currency : many2one
account_return --|> account_audit_account_status : one2many
account_return_check --> account_return_check_template : many2one
account_return_check --> ir_model : many2one
account_return_check .. ir_attachment : many2many
account_return_check --> account_return : many2one
class "res.users" as res_users
account_return_check .. res_users : many2many
account_return_check --> res_users : many2one
account_return_check .. res_users : many2many
account_return_check_template --> account_return_type : many2one
account_return_check_template .. res_country : many2many
class "ir.actions.actions" as ir_actions_actions
account_return_check_template --> ir_actions_actions : many2one
class "mail.activity.type" as mail_activity_type
account_return_check_template --> mail_activity_type : many2one
account_tax_unit --> res_country : many2one
account_tax_unit .. res_company : many2many
account_tax_unit --> res_company : many2one
account_report_budget --|> account_report_budget_item : one2many
account_report_budget --> res_company : many2one
account_report_budget_item --> account_report_budget : many2one
account_report_budget_item --> account_account : many2one
class "account.journal" as account_journal
ResCompany --> account_journal : many2one
ResCompany --> account_journal : many2one
ResCompany --> account_account : many2one
ResCompany --> account_account : many2one
ResCompany .. account_tax_unit : many2many
ResCompany --> res_partner : many2one
ResPartner --|> res_company : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

