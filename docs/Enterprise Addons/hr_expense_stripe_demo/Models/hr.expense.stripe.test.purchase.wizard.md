<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.expense.stripe.test.purchase.wizard

- Module: [[docs/Enterprise Addons/hr_expense_stripe_demo/hr_expense_stripe_demo|hr_expense_stripe_demo]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/hr_expense_stripe_test_purchase_wizard.py`
- Python classes: `HrExpenseStripeTestPurchaseWizard`
- Description: Test Purchase Wizard for Stripe

## Field footprint

- Detected fields: 15
- Field types: `Boolean` x 3, `Char` x 1, `Many2one` x 6, `Monetary` x 4, `Selection` x 1
- Relation fields: 6

## Sample fields

- `amount_currency`: `Monetary`
- `atm_fee`: `Monetary`
- `authorization_method`: `Selection`
- `capture`: `Boolean`
- `capture_surcharge`: `Monetary`
- `card_currency_id`: `Many2one` (related `card_id.currency_id`)
- `card_id`: `Many2one` (comodel `hr.expense.stripe.card`)
- `cashback_amount`: `Monetary`
- `company_id`: `Many2one` (comodel `res.company`)
- `currency_id`: `Many2one` (comodel `res.currency`)
- `force_capture`: `Boolean`
- `mcc_id`: `Many2one` (comodel `product.mcc.stripe.tag`)
- `merchant_country_id`: `Many2one` (comodel `res.country`)
- `merchant_name`: `Char`
- `split_capture`: `Boolean`

## Method hints

- Detected methods: 1
- Action methods: `action_test_purchase`
- Compute methods: none
- Onchange methods: none

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
title hr.expense.stripe.test.purchase.wizard - Direct Relations
class "hr.expense.stripe.test.purchase.wizard" as hr_expense_stripe_test_purchase_wizard
class "hr.expense.stripe.card" as hr_expense_stripe_card
class "product.mcc.stripe.tag" as product_mcc_stripe_tag
class "res.company" as res_company
class "res.country" as res_country
class "res.currency" as res_currency
hr_expense_stripe_test_purchase_wizard --> res_company : company_id
hr_expense_stripe_test_purchase_wizard --> hr_expense_stripe_card : card_id
hr_expense_stripe_test_purchase_wizard --> res_currency : currency_id
hr_expense_stripe_test_purchase_wizard --> res_country : merchant_country_id
hr_expense_stripe_test_purchase_wizard --> product_mcc_stripe_tag : mcc_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_expense_stripe_demo/Models]]

<!-- GENERATED:MODEL -->
