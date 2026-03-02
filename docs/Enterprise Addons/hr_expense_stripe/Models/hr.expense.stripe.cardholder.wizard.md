<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.expense.stripe.cardholder.wizard

- Module: [[docs/Enterprise Addons/hr_expense_stripe/hr_expense_stripe|hr_expense_stripe]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/hr_expense_stripe_cardholder_wizard.py`
- Python classes: `HrExpenseStripeCardholderWizard`
- Description: Wizard to configure the cardholder
- Inherits: `mail.thread`

## Field footprint

- Detected fields: 16
- Field types: `Char` x 8, `Date` x 1, `Json` x 1, `Many2one` x 6
- Relation fields: 6

## Sample fields

- `billing_city`: `Char`
- `billing_country_id`: `Many2one` (comodel `res.country`)
- `billing_state_id`: `Many2one` (comodel `res.country.state`)
- `billing_street`: `Char`
- `billing_street2`: `Char`
- `billing_zip`: `Char`
- `birthday`: `Date`
- `card_id`: `Many2one` (comodel `hr.expense.stripe.card`)
- `company_country_id`: `Many2one` (related `company_id.country_id`)
- `company_id`: `Many2one` (comodel `res.company`)
- `email`: `Char`
- `employee_id`: `Many2one` (comodel `hr.employee`)
- `firstname`: `Char`
- `lastname`: `Char`
- `phone_number`: `Char`
- `stripe_values`: `Json`

## Method hints

- Detected methods: 5
- Action methods: `action_save_cardholder`
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
title hr.expense.stripe.cardholder.wizard - Direct Relations
class "hr.expense.stripe.cardholder.wizard" as hr_expense_stripe_cardholder_wizard
class "hr.employee" as hr_employee
class "hr.expense.stripe.card" as hr_expense_stripe_card
class "res.company" as res_company
class "res.country" as res_country
class "res.country.state" as res_country_state
hr_expense_stripe_cardholder_wizard --> hr_expense_stripe_card : card_id
hr_expense_stripe_cardholder_wizard --> res_company : company_id
hr_expense_stripe_cardholder_wizard --> hr_employee : employee_id
hr_expense_stripe_cardholder_wizard --> res_country : billing_country_id
hr_expense_stripe_cardholder_wizard --> res_country_state : billing_state_id
@enduml
```

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_expense_stripe/Models]]

<!-- GENERATED:MODEL -->
