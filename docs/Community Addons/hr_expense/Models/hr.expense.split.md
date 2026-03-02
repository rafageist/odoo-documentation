<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# hr.expense.split

- Module: [[docs/Community Addons/hr_expense/hr_expense|hr_expense]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `wizard/hr_expense_split.py`
- Python classes: `HrExpenseSplit`
- Description: Expense Split
- Inherits: `analytic.mixin`

## Field footprint

- Detected fields: 15
- Field types: `Boolean` x 2, `Char` x 1, `Datetime` x 1, `Many2many` x 1, `Many2one` x 7, `Monetary` x 2, `Selection` x 1
- Relation fields: 8

## Sample fields

- `approval_date`: `Datetime`
- `approval_state`: `Selection`
- `company_id`: `Many2one` (comodel `res.company`)
- `currency_id`: `Many2one` (comodel `res.currency`)
- `employee_id`: `Many2one` (comodel `hr.employee`)
- `expense_id`: `Many2one` (comodel `hr.expense`)
- `manager_id`: `Many2one` (comodel `res.users`)
- `name`: `Char`
- `product_has_cost`: `Boolean` (compute `_compute_from_product_id`, store `True`)
- `product_has_tax`: `Boolean` (compute `_compute_product_has_tax`)
- `product_id`: `Many2one` (comodel `product.product`)
- `tax_amount_currency`: `Monetary` (compute `_compute_tax_amount_currency`)
- `tax_ids`: `Many2many` (comodel `account.tax`)
- `total_amount_currency`: `Monetary` (compute `_compute_from_product_id`, store `True`)
- `wizard_id`: `Many2one` (comodel `hr.expense.split.wizard`)

## Method hints

- Detected methods: 6
- Action methods: none
- Compute methods: `_compute_from_product_id`, `_compute_product_has_tax`, `_compute_tax_amount_currency`
- Onchange methods: `_onchange_product_id`

## Direct relation diagram

```plantuml
@startuml
!define ODOO_COLOR_PRIMARY #714B67
!define ODOO_COLOR_ACCENT #875A7B
!define ODOO_COLOR_BG #FAF7FA

skinparam backgroundColor ODOO_COLOR_BG
skinparam defaultTextAlignment left
skinparam ArrowColor ODOO_COLOR_ACCENT
skinparam ClassBackgroundColor white
skinparam ClassBorderColor ODOO_COLOR_PRIMARY
skinparam ComponentBackgroundColor white
skinparam ComponentBorderColor ODOO_COLOR_PRIMARY
skinparam NoteBackgroundColor #FFF8FF
skinparam NoteBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBackgroundColor #FFFFFF
skinparam SequenceParticipantBorderColor ODOO_COLOR_PRIMARY
skinparam SequenceParticipantBackgroundColor #FFFFFF
skinparam sequence {
  ArrowColor ODOO_COLOR_ACCENT
  ActorBorderColor ODOO_COLOR_PRIMARY
}
title hr.expense.split - Direct Relations
class "hr.expense.split" as hr_expense_split
class "account.tax" as account_tax
class "hr.employee" as hr_employee
class "hr.expense" as hr_expense
class "hr.expense.split.wizard" as hr_expense_split_wizard
class "product.product" as product_product
class "res.company" as res_company
class "res.currency" as res_currency
class "res.users" as res_users
hr_expense_split --> hr_expense_split_wizard : wizard_id
hr_expense_split --> hr_expense : expense_id
hr_expense_split --> product_product : product_id
hr_expense_split .. account_tax : tax_ids
hr_expense_split --> hr_employee : employee_id
hr_expense_split --> res_company : company_id
hr_expense_split --> res_currency : currency_id
hr_expense_split --> res_users : manager_id
@enduml
```

## Navigation

- **Parent:** [[docs/Community Addons/hr_expense/Models]]

<!-- GENERATED:MODEL -->
