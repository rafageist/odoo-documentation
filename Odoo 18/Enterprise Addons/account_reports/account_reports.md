<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Accounting Reports

- Version: v18
- Category: enterprise
- Source: enterprise18/account_reports
- Dependencies: [[Odoo 18/Enterprise Addons/accountant/accountant|accountant]]

## Summary

View and create reports

## XML Artifacts (detected)

- Views: 32
- Actions: 24
- Menus: 20
- Rules (ir.rule): 0
- Access CSV entries: 18

## Detected Models

- `AccountAccount`
- `AccountMoveLine`
- `AccountFiscalPosition`
- `AccountJournal`
- `AccountMove`
- `account.move.line`
- `account.report.annotation`
- `AccountReport`
- `AccountReportLine`
- `AccountReportExpression`
- `AccountReportExternalValue`
- `account.report.horizontal.group`
- `account.report.horizontal.group.rule`
- `account.tax.unit`
- `account.report.budget`
- `account.report.budget.item`
- `ExecutiveSummaryReport`
- `AccountTaxReportActivity`
- `AccountTaxReportActivityType`
- `ResCompany`
- `res.partner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Accounting Reports - Models and Relations
class AccountAccount
class AccountMoveLine
class AccountFiscalPosition
class AccountJournal
class AccountMove
class "account.move.line" as account_move_line
class "account.report.annotation" as account_report_annotation
class AccountReport
class AccountReportLine
class AccountReportExpression
class AccountReportExternalValue
class "account.report.horizontal.group" as account_report_horizontal_group
class "account.report.horizontal.group.rule" as account_report_horizontal_group_rule
class "account.tax.unit" as account_tax_unit
class "account.report.budget" as account_report_budget
class "account.report.budget.item" as account_report_budget_item
class ExecutiveSummaryReport
class AccountTaxReportActivity
class AccountTaxReportActivityType
class ResCompany
class "res.partner" as res_partner
class "res.currency" as res_currency
AccountAccount .. res_currency : many2many
AccountAccount --|> account_report_budget_item : one2many
class "account.report" as account_report
AccountMove --> account_report : many2one
account_report_annotation --> account_report : many2one
class "account.fiscal.position" as account_fiscal_position
account_report_annotation --> account_fiscal_position : many2one
AccountReport .. account_report_horizontal_group : many2many
AccountReport --|> account_report_annotation : one2many
class "ir.model" as ir_model
AccountReport --> ir_model : many2one
account_report_horizontal_group --|> account_report_horizontal_group_rule : one2many
account_report_horizontal_group .. account_report : many2many
account_report_horizontal_group_rule --> account_report_horizontal_group : many2one
class "res.country" as res_country
account_tax_unit --> res_country : many2one
class "res.company" as res_company
account_tax_unit .. res_company : many2many
account_tax_unit --> res_company : many2one
account_report_budget --|> account_report_budget_item : one2many
account_report_budget --> res_company : many2one
account_report_budget_item --> account_report_budget : many2one
class "account.account" as account_account
account_report_budget_item --> account_account : many2one
class "account.journal" as account_journal
ResCompany --> account_journal : many2one
ResCompany --> account_journal : many2one
ResCompany --> account_account : many2one
ResCompany --> account_account : many2one
ResCompany .. account_tax_unit : many2many
ResCompany --> res_partner : many2one
res_partner --|> res_company : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
