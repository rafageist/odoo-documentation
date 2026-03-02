
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Avatax

- Scope: Enterprise Addons
- Source: enterprise/account_avatax
- Dependencies: [[docs/Community Addons/payment/payment|payment]], [[docs/Enterprise Addons/account_external_tax/account_external_tax|account_external_tax]]

## XML Artifacts (detected)

- Views: 13
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 5

## Detected Models

- `AccountFiscalPosition`
- `account.move`
- `avatax.exemption`
- `product.avatax.category`
- `ProductCategory`
- `ProductTemplate`
- `ProductProduct`
- `ResCompany`
- `res.partner`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Avatax - Models and Relations
class AccountFiscalPosition
class "account.move" as account_move
class "avatax.exemption" as avatax_exemption
class "product.avatax.category" as product_avatax_category
class ProductCategory
class ProductTemplate
class ProductProduct
class ResCompany
class "res.partner" as res_partner
class "account.account" as account_account
AccountFiscalPosition --> account_account : many2one
AccountFiscalPosition --> account_account : many2one
class "res.country" as res_country
avatax_exemption .. res_country : many2many
class "res.company" as res_company
avatax_exemption --> res_company : many2one
ProductCategory --> product_avatax_category : many2one
ProductTemplate --> product_avatax_category : many2one
ProductProduct --> product_avatax_category : many2one
res_partner --> avatax_exemption : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

