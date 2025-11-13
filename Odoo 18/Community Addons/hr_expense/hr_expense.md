<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Expenses

- Version: v18
- Category: community
- Source: odoo/addons/hr_expense
- Dependencies: [[Odoo 18/Community Addons/account/account|account]], [[Odoo 18/Community Addons/web_tour/web_tour|web_tour]], [[Odoo 18/Community Addons/hr/hr|hr]]

## Summary

Submit, validate and reinvoice employee expenses

## XML Artifacts (detected)

- Views: 40
- Actions: 25
- Menus: 12
- Rules (ir.rule): 12
- Access CSV entries: 19

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `AccountPayment`
- `AccountTax`
- `AccountAnalyticApplicability`
- `AccountAnalyticAccount`
- `HrDepartment`
- `Employee`
- `EmployeePublic`
- `User`
- `hr.expense`
- `hr.expense.sheet`
- `IrActionsReport`
- `IrAttachment`
- `ProductProduct`
- `ProductTemplate`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Expenses - Models and Relations
class AccountMove
class AccountMoveLine
class AccountPayment
class AccountTax
class AccountAnalyticApplicability
class AccountAnalyticAccount
class HrDepartment
class Employee
class EmployeePublic
class User
class "hr.expense" as hr_expense
class "hr.expense.sheet" as hr_expense_sheet
class IrActionsReport
class IrAttachment
class ProductProduct
class ProductTemplate
class ResCompany
AccountMove --> hr_expense_sheet : many2one
AccountMoveLine --> hr_expense : many2one
class "res.users" as res_users
Employee --> res_users : many2one
EmployeePublic --> res_users : many2one
class "hr.employee" as hr_employee
hr_expense --> hr_employee : many2one
class "res.company" as res_company
hr_expense --> res_company : many2one
class "product.product" as product_product
hr_expense --> product_product : many2one
class "uom.uom" as uom_uom
hr_expense --> uom_uom : many2one
class "uom.category" as uom_category
hr_expense --> uom_category : many2one
class "ir.attachment" as ir_attachment
hr_expense --|> ir_attachment : one2many
hr_expense --> hr_expense_sheet : many2one
hr_expense --> res_users : many2one
hr_expense .. hr_expense : many2many
hr_expense .. hr_expense : many2many
class "res.currency" as res_currency
hr_expense --> res_currency : many2one
hr_expense --> res_currency : many2one
class "res.partner" as res_partner
hr_expense --> res_partner : many2one
class "account.account" as account_account
hr_expense --> account_account : many2one
class "account.tax" as account_tax
hr_expense .. account_tax : many2many
hr_expense_sheet --|> hr_expense : one2many
hr_expense_sheet --> res_company : many2one
hr_expense_sheet --> hr_employee : many2one
class "hr.department" as hr_department
hr_expense_sheet --> hr_department : many2one
hr_expense_sheet --> res_users : many2one
hr_expense_sheet .. product_product : many2many
hr_expense_sheet --> res_currency : many2one
hr_expense_sheet --> res_currency : many2one
class "account.journal" as account_journal
hr_expense_sheet --> account_journal : many2one
class "account.payment.method.line" as account_payment_method_line
hr_expense_sheet .. account_payment_method_line : many2many
hr_expense_sheet --> account_payment_method_line : many2one
hr_expense_sheet --|> ir_attachment : one2many
class "account.move" as account_move
hr_expense_sheet --|> account_move : one2many
hr_expense_sheet --> account_journal : many2one
ResCompany --> account_journal : many2one
ResCompany --> account_account : many2one
ResCompany .. account_payment_method_line : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
