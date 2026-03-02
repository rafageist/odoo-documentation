<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Expense cards

- Scope: Enterprise Addons
- Source: enterprise/hr_expense_stripe
- Dependencies: [[docs/Community Addons/hr_expense/hr_expense|hr_expense]], [[docs/Community Addons/certificate/certificate|certificate]]

## Summary

Create and manage company expense cards via Stripe

## XML Artifacts (detected)

- Views: 17
- Actions: 2
- Menus: 2
- Rules (ir.rule): 5
- Access CSV entries: 10

## Detected Models

- `AccountBankStatementLine`
- `AccountJournal`
- `AccountPayment`
- `AccountPaymentMethodLine`
- `hr.employee`
- `HrExpense`
- `hr.expense.stripe.card`
- `product.mcc.stripe.tag`
- `ProductProduct`
- `ResCompany`
- `ResUsers`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Expense cards - Models and Relations
class AccountBankStatementLine
class AccountJournal
class AccountPayment
class AccountPaymentMethodLine
class "hr.employee" as hr_employee
class HrExpense
class "hr.expense.stripe.card" as hr_expense_stripe_card
class "product.mcc.stripe.tag" as product_mcc_stripe_tag
class ProductProduct
class ResCompany
class ResUsers
AccountJournal --|> hr_expense_stripe_card : one2many
AccountPaymentMethodLine --|> hr_expense_stripe_card : one2many
HrExpense --> hr_expense_stripe_card : many2one
HrExpense --> product_mcc_stripe_tag : many2one
class "res.company" as res_company
hr_expense_stripe_card --> res_company : many2one
class "res.partner" as res_partner
hr_expense_stripe_card --> res_partner : many2one
hr_expense_stripe_card --> hr_employee : many2one
class "account.journal" as account_journal
hr_expense_stripe_card --> account_journal : many2one
hr_expense_stripe_card --> res_partner : many2one
class "res.users" as res_users
hr_expense_stripe_card --> res_users : many2one
hr_expense_stripe_card .. product_mcc_stripe_tag : many2many
class "res.country" as res_country
hr_expense_stripe_card .. res_country : many2many
class "hr.expense" as hr_expense
hr_expense_stripe_card --|> hr_expense : one2many
class "account.payment.method.line" as account_payment_method_line
hr_expense_stripe_card --> account_payment_method_line : many2one
class "product.product" as product_product
product_mcc_stripe_tag --> product_product : many2one
ProductProduct --|> product_mcc_stripe_tag : one2many
ResCompany --> account_journal : many2one
class "res.currency" as res_currency
ResCompany --> res_currency : many2one
class "certificate.key" as certificate_key
ResCompany --> certificate_key : many2one
ResCompany --> certificate_key : many2one
ResUsers --|> hr_expense_stripe_card : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



