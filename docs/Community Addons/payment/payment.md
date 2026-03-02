<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Payment Engine

- Scope: Community Addons
- Source: odoo/addons/payment
- Dependencies: [[docs/Community Addons/onboarding/onboarding|onboarding]], [[docs/Community Addons/portal/portal|portal]]

## Summary

The payment engine used by payment provider modules.

## XML Artifacts (detected)

- Views: 20
- Actions: 5
- Menus: 0
- Rules (ir.rule): 5
- Access CSV entries: 12

## Detected Models

- `payment.method`
- `payment.provider`
- `payment.token`
- `payment.transaction`
- `ResCompany`
- `ResCountry`
- `ResPartner`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Payment Engine - Models and Relations
class "payment.method" as payment_method
class "payment.provider" as payment_provider
class "payment.token" as payment_token
class "payment.transaction" as payment_transaction
class ResCompany
class ResCountry
class ResPartner
payment_method --> payment_method : many2one
payment_method --|> payment_method : one2many
payment_method .. payment_provider : many2many
class "res.country" as res_country
payment_method .. res_country : many2many
class "res.currency" as res_currency
payment_method .. res_currency : many2many
class "res.company" as res_company
payment_provider --> res_company : many2one
payment_provider .. payment_method : many2many
class "ir.ui.view" as ir_ui_view
payment_provider --> ir_ui_view : many2one
payment_provider --> ir_ui_view : many2one
payment_provider --> ir_ui_view : many2one
payment_provider --> ir_ui_view : many2one
payment_provider .. res_country : many2many
payment_provider .. res_currency : many2many
class "ir.module.module" as ir_module_module
payment_provider --> ir_module_module : many2one
payment_token --> payment_provider : many2one
payment_token --> payment_method : many2one
class "res.partner" as res_partner
payment_token --> res_partner : many2one
payment_token --|> payment_transaction : one2many
payment_transaction --> payment_provider : many2one
payment_transaction --> payment_method : many2one
payment_transaction --> payment_method : many2one
payment_transaction --> res_currency : many2one
payment_transaction --> payment_token : many2one
payment_transaction --> payment_transaction : many2one
payment_transaction --|> payment_transaction : one2many
payment_transaction --> res_partner : many2one
class "res.country.state" as res_country_state
payment_transaction --> res_country_state : many2one
payment_transaction --> res_country : many2one
ResPartner --|> payment_token : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





