<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Invoicing

- Version: v18
- Category: community
- Source: odoo/addons/account
- Dependencies: [[Odoo 18/Community Addons/base_setup/base_setup|base_setup]], [[Odoo 18/Community Addons/onboarding/onboarding|onboarding]], [[Odoo 18/Community Addons/product/product|product]], [[Odoo 18/Community Addons/analytic/analytic|analytic]], [[Odoo 18/Community Addons/portal/portal|portal]], [[Odoo 18/Community Addons/digest/digest|digest]]

## Summary

Invoices, Payments, Follow-ups & Bank Synchronization

## XML Artifacts (detected)

- Views: 144
- Actions: 80
- Menus: 53
- Rules (ir.rule): 31
- Access CSV entries: 152

## Detected Models

- `account.account`
- `account.group`
- `account.account.tag`
- `AccountAnalyticAccount`
- `AccountAnalyticDistributionModel`
- `AccountAnalyticLine`
- `AccountAnalyticApplicability`
- `account.bank.statement`
- `account.bank.statement.line`
- `account.move`
- `account.cash.rounding`
- `account.code.mapping`
- `account.full.reconcile`
- `account.incoterms`
- `account.journal.group`
- `account.journal`
- `account_journal`
- `account.lock_exception`
- `account.move.line`
- `AccountMoveLine`
- `account.partial.reconcile`
- `account.payment`
- `account.payment.method`
- `account.payment.method.line`
- `account.payment.term`
- `account.payment.term.line`
- `account.reconcile.model.partner.mapping`
- `account.reconcile.model.line`
- `account.reconcile.model`
- `account.report`
- `account.report.line`
- `account.report.expression`
- `account.report.column`
- `account.report.external.value`
- `account.root`
- `account.tax.group`
- `account.tax`
- `account.tax.repartition.line`
- `res.company`
- `DecimalPrecision`
- `Digest`
- `IrActionsReport`
- `IrAttachment`
- `IrModule`
- `IrUiMenu`
- `Message`
- `MailTemplate`
- `MailTrackingValues`
- `Onboarding`
- `OnboardingStep`
- `account.fiscal.position`
- `account.fiscal.position.tax`
- `account.fiscal.position.account`
- `res.partner`
- `ProductCategory`
- `ProductTemplate`
- `ProductProduct`
- `ResCurrency`
- `res.partner.bank`
- `GroupsView`
- `UoM`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Invoicing - Models and Relations
class "account.account" as account_account
class "account.group" as account_group
class "account.account.tag" as account_account_tag
class AccountAnalyticAccount
class AccountAnalyticDistributionModel
class AccountAnalyticLine
class AccountAnalyticApplicability
class "account.bank.statement" as account_bank_statement
class "account.bank.statement.line" as account_bank_statement_line
class "account.move" as account_move
class "account.cash.rounding" as account_cash_rounding
class "account.code.mapping" as account_code_mapping
class "account.full.reconcile" as account_full_reconcile
class "account.incoterms" as account_incoterms
class "account.journal.group" as account_journal_group
class "account.journal" as account_journal
class account_journal
class "account.lock_exception" as account_lock_exception
class "account.move.line" as account_move_line
class AccountMoveLine
class "account.partial.reconcile" as account_partial_reconcile
class "account.payment" as account_payment
class "account.payment.method" as account_payment_method
class "account.payment.method.line" as account_payment_method_line
class "account.payment.term" as account_payment_term
class "account.payment.term.line" as account_payment_term_line
class "account.reconcile.model.partner.mapping" as account_reconcile_model_partner_mapping
class "account.reconcile.model.line" as account_reconcile_model_line
class "account.reconcile.model" as account_reconcile_model
class "account.report" as account_report
class "account.report.line" as account_report_line
class "account.report.expression" as account_report_expression
class "account.report.column" as account_report_column
class "account.report.external.value" as account_report_external_value
class "account.root" as account_root
class "account.tax.group" as account_tax_group
class "account.tax" as account_tax
class "account.tax.repartition.line" as account_tax_repartition_line
class "res.company" as res_company
class DecimalPrecision
class Digest
class IrActionsReport
class IrAttachment
class IrModule
class IrUiMenu
class Message
class MailTemplate
class MailTrackingValues
class Onboarding
class OnboardingStep
class "account.fiscal.position" as account_fiscal_position
class "account.fiscal.position.tax" as account_fiscal_position_tax
class "account.fiscal.position.account" as account_fiscal_position_account
class "res.partner" as res_partner
class ProductCategory
class ProductTemplate
class ProductProduct
class ResCurrency
class "res.partner.bank" as res_partner_bank
class GroupsView
class UoM
class "res.currency" as res_currency
account_account --> res_currency : many2one
account_account --> res_currency : many2one
account_account .. account_tax : many2many
account_account .. res_company : many2many
account_account --|> account_code_mapping : one2many
account_account .. account_account_tag : many2many
account_account --> account_group : many2one
account_account --> account_root : many2one
account_account .. account_journal : many2many
account_group --> account_group : many2one
account_group --> res_company : many2one
class "res.country" as res_country
account_account_tag --> res_country : many2one
class "product.product" as product_product
AccountAnalyticDistributionModel --> product_product : many2one
class "product.category" as product_category
AccountAnalyticDistributionModel --> product_category : many2one
AccountAnalyticLine --> product_product : many2one
AccountAnalyticLine --> account_account : many2one
AccountAnalyticLine --> account_journal : many2one
AccountAnalyticLine --> account_move_line : many2one
AccountAnalyticApplicability --> product_category : many2one
account_bank_statement --> res_company : many2one
account_bank_statement --> res_currency : many2one
account_bank_statement --> account_journal : many2one
account_bank_statement --|> account_bank_statement_line : one2many
class "ir.attachment" as ir_attachment
account_bank_statement .. ir_attachment : many2many
account_bank_statement_line --> account_move : many2one
account_bank_statement_line --> account_journal : many2one
account_bank_statement_line --> res_company : many2one
account_bank_statement_line --> account_bank_statement : many2one
account_bank_statement_line .. account_payment : many2many
account_bank_statement_line --> res_partner : many2one
account_bank_statement_line --> res_currency : many2one
account_bank_statement_line --> res_currency : many2one
account_move --|> account_bank_statement_line : one2many
account_cash_rounding --> account_account : many2one
account_cash_rounding --> account_account : many2one
account_code_mapping --> account_account : many2one
account_code_mapping --> res_company : many2one
account_full_reconcile --|> account_partial_reconcile : one2many
account_full_reconcile --|> account_move_line : one2many
account_full_reconcile --> account_move : many2one
account_journal_group --> res_company : many2one
account_journal_group .. account_journal : many2many
account_journal .. account_account : many2many
account_journal --> account_account : many2one
account_journal --> account_account : many2one
account_journal --> res_currency : many2one
account_journal --> res_company : many2one
account_journal --|> account_payment_method_line : one2many
account_journal --|> account_payment_method_line : one2many
account_journal --> account_account : many2one
account_journal --> account_account : many2one
account_journal --> res_partner : many2one
account_journal --> res_partner_bank : many2one
class "res.bank" as res_bank
account_journal --> res_bank : many2one
account_journal .. account_journal_group : many2many
account_journal .. account_payment_method : many2many
account_journal --> account_bank_statement : many2one
account_lock_exception --> res_company : many2one
class "res.users" as res_users
account_lock_exception --> res_users : many2one
account_move_line --> account_move : many2one
account_move_line --> account_journal_group : many2one
account_move_line --> account_account : many2one
account_move_line --> res_currency : many2one
account_move_line --> res_partner : many2one
account_move_line --> account_reconcile_model : many2one
account_move_line --> account_payment : many2one
account_move_line --> account_bank_statement_line : many2one
account_move_line .. account_tax : many2many
account_move_line --> account_tax : many2one
account_move_line --> account_tax : many2one
account_move_line --> account_tax_repartition_line : many2one
account_move_line .. account_account_tag : many2many
account_move_line --> account_full_reconcile : many2one
account_move_line --|> account_partial_reconcile : one2many
account_move_line --|> account_partial_reconcile : one2many
account_move_line --> product_product : many2one
class "uom.uom" as uom_uom
account_move_line --> uom_uom : many2one
class "uom.category" as uom_category
account_move_line --> uom_category : many2one
class "account.analytic.line" as account_analytic_line
account_move_line --|> account_analytic_line : one2many
account_partial_reconcile --> account_move_line : many2one
account_partial_reconcile --> account_move_line : many2one
account_partial_reconcile --> account_full_reconcile : many2one
account_partial_reconcile --> account_move : many2one
account_partial_reconcile --> res_currency : many2one
account_partial_reconcile --> res_currency : many2one
account_partial_reconcile --> res_currency : many2one
account_partial_reconcile --> res_company : many2one
account_payment --> account_move : many2one
account_payment --> account_journal : many2one
account_payment --> res_company : many2one
account_payment .. res_partner_bank : many2many
account_payment --> res_partner_bank : many2one
account_payment --> account_payment : many2one
account_payment --> account_payment_method_line : many2one
account_payment .. account_payment_method_line : many2many
account_payment .. account_journal : many2many
account_payment --> res_currency : many2one
account_payment --> res_partner : many2one
account_payment --> account_account : many2one
account_payment --> account_account : many2one
account_payment .. account_move : many2many
account_payment .. account_move : many2many
account_payment .. account_move : many2many
account_payment .. account_bank_statement_line : many2many
account_payment .. account_payment : many2many
account_payment --|> ir_attachment : one2many
account_payment_method_line --> account_payment_method : many2one
account_payment_method_line --> account_account : many2one
account_payment_method_line --> account_journal : many2one
account_payment_term --|> account_payment_term_line : one2many
account_payment_term --> res_company : many2one
account_payment_term --> res_currency : many2one
account_payment_term_line --> account_payment_term : many2one
account_reconcile_model_partner_mapping --> account_reconcile_model : many2one
account_reconcile_model_partner_mapping --> res_partner : many2one
account_reconcile_model_line --> account_reconcile_model : many2one
account_reconcile_model_line --> account_account : many2one
account_reconcile_model_line --> account_journal : many2one
account_reconcile_model_line .. account_tax : many2many
account_reconcile_model --> res_company : many2one
account_reconcile_model .. account_journal : many2many
account_reconcile_model .. res_partner : many2many
class "res.partner.category" as res_partner_category
account_reconcile_model .. res_partner_category : many2many
account_reconcile_model --|> account_reconcile_model_line : one2many
account_reconcile_model --|> account_reconcile_model_partner_mapping : one2many
account_report --|> account_report_line : one2many
account_report --|> account_report_column : one2many
account_report --> account_report : many2one
account_report --|> account_report : one2many
account_report .. account_report : many2many
account_report .. account_report : many2many
account_report --> res_country : many2one
account_report_line --|> account_report_expression : one2many
account_report_line --> account_report : many2one
account_report_line --> account_report_line : many2one
account_report_line --|> account_report_line : one2many
class "ir.actions.actions" as ir_actions_actions
account_report_line --> ir_actions_actions : many2one
account_report_expression --> account_report_line : many2one
account_report_column --> account_report : many2one
class "ir.actions.act_window" as ir_actions_act_window
account_report_column --> ir_actions_act_window : many2one
account_report_external_value --> account_report_expression : many2one
account_report_external_value --> res_company : many2one
account_report_external_value --> account_fiscal_position : many2one
account_report_external_value --> account_report_line : many2one
account_root --> account_root : many2one
account_tax_group --> res_company : many2one
account_tax_group --> account_account : many2one
account_tax_group --> account_account : many2one
account_tax_group --> account_account : many2one
account_tax_group --> res_country : many2one
account_tax --> res_company : many2one
account_tax .. account_tax : many2many
account_tax --> account_tax_group : many2one
account_tax --> account_account : many2one
account_tax --|> account_tax_repartition_line : one2many
account_tax --|> account_tax_repartition_line : one2many
account_tax --|> account_tax_repartition_line : one2many
account_tax --> res_country : many2one
account_tax_repartition_line --> account_account : many2one
account_tax_repartition_line .. account_account_tag : many2many
account_tax_repartition_line --> account_tax : many2one
account_tax_repartition_line --> res_company : many2one
res_company --> account_account : many2one
res_company --> account_account : many2one
res_company --> account_account : many2one
res_company --> account_account : many2one
res_company --> account_account : many2one
res_company --> account_account : many2one
res_company --> account_tax : many2one
res_company --> account_tax : many2one
res_company --> account_journal : many2one
res_company --> account_account : many2one
res_company --> account_account : many2one
res_company --|> account_journal : one2many
res_company --> account_incoterms : many2one
class "ir.sequence" as ir_sequence
res_company --> ir_sequence : many2one
res_company --> account_move : many2one
res_company --> account_journal : many2one
res_company --> account_account : many2one
res_company --> account_account : many2one
res_company --> account_account : many2one
res_company --> account_journal : many2one
res_company --> res_country : many2one
res_company .. res_country : many2many
res_company --> account_journal : many2one
res_company --> account_account : many2one
res_company --|> account_fiscal_position : one2many
res_company .. res_country : many2many
res_company --> account_account : many2one
res_company --> account_account : many2one
Message --> account_move : many2one
Message --> res_partner : many2one
Message --> account_account : many2one
Message --> account_tax : many2one
Message --> res_company : many2one
account_fiscal_position --> res_company : many2one
account_fiscal_position --|> account_fiscal_position_account : one2many
account_fiscal_position --|> account_fiscal_position_tax : one2many
account_fiscal_position --> res_country : many2one
class "res.country.group" as res_country_group
account_fiscal_position --> res_country_group : many2one
class "res.country.state" as res_country_state
account_fiscal_position .. res_country_state : many2many
account_fiscal_position_tax --> account_fiscal_position : many2one
account_fiscal_position_tax --> res_company : many2one
account_fiscal_position_tax --> account_tax : many2one
account_fiscal_position_tax --> account_tax : many2one
account_fiscal_position_account --> account_fiscal_position : many2one
account_fiscal_position_account --> res_company : many2one
account_fiscal_position_account --> account_account : many2one
account_fiscal_position_account --> account_account : many2one
res_partner --> res_currency : many2one
res_partner --> account_account : many2one
res_partner --> account_account : many2one
res_partner --> account_fiscal_position : many2one
res_partner --> account_payment_term : many2one
res_partner --> account_payment_term : many2one
res_partner --|> res_company : one2many
res_partner --|> account_move : one2many
class "account.analytic.account" as account_analytic_account
res_partner --|> account_analytic_account : one2many
class "ir.actions.report" as ir_actions_report
res_partner --> ir_actions_report : many2one
res_partner --> account_payment_method_line : many2one
res_partner --> account_payment_method_line : many2one
ProductCategory --> account_account : many2one
ProductCategory --> account_account : many2one
ProductTemplate .. account_tax : many2many
ProductTemplate .. account_tax : many2many
ProductTemplate --> account_account : many2one
ProductTemplate --> account_account : many2one
ProductTemplate .. account_account_tag : many2many
res_partner_bank --|> account_journal : one2many
res_partner_bank --|> account_move : one2many
res_partner_bank .. res_partner : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
