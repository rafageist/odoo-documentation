<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# ESG

- Scope: Enterprise Addons
- Source: enterprise/esg
- Dependencies: [[docs/Enterprise Addons/account_reports/account_reports|account_reports]], [[docs/Community Addons/web_hierarchy/web_hierarchy|web_hierarchy]]

## Summary

Calculate and report your company's Environmental, Social, and Governance impact.

## XML Artifacts (detected)

- Views: 23
- Actions: 11
- Menus: 17
- Rules (ir.rule): 3
- Access CSV entries: 11

## Detected Models

- `AccountAccount`
- `AccountMove`
- `AccountMoveLine`
- `esg.activity.type`
- `esg.assignation.line`
- `esg.database`
- `esg.emission.factor`
- `esg.emission.factor.line`
- `esg.emission.source`
- `esg.gas`
- `esg.other.emission`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title ESG - Models and Relations
class AccountAccount
class AccountMove
class AccountMoveLine
class "esg.activity.type" as esg_activity_type
class "esg.assignation.line" as esg_assignation_line
class "esg.database" as esg_database
class "esg.emission.factor" as esg_emission_factor
class "esg.emission.factor.line" as esg_emission_factor_line
class "esg.emission.source" as esg_emission_source
class "esg.gas" as esg_gas
class "esg.other.emission" as esg_other_emission
AccountMoveLine --> esg_emission_factor : many2one
esg_assignation_line --> esg_emission_factor : many2one
class "account.account" as account_account
esg_assignation_line --> account_account : many2one
class "res.partner" as res_partner
esg_assignation_line --> res_partner : many2one
class "product.product" as product_product
esg_assignation_line --> product_product : many2one
esg_emission_factor --> esg_emission_source : many2one
class "res.company" as res_company
esg_emission_factor --> res_company : many2one
esg_emission_factor --> esg_database : many2one
esg_emission_factor --|> esg_emission_factor_line : one2many
esg_emission_factor --|> esg_assignation_line : one2many
class "uom.uom" as uom_uom
esg_emission_factor --> uom_uom : many2one
class "res.currency" as res_currency
esg_emission_factor --> res_currency : many2one
esg_emission_factor .. esg_activity_type : many2many
class "account.move.line" as account_move_line
esg_emission_factor --|> account_move_line : one2many
esg_emission_factor --|> esg_other_emission : one2many
esg_emission_factor_line --> esg_emission_factor : many2one
esg_emission_factor_line --> esg_activity_type : many2one
esg_emission_factor_line --> esg_gas : many2one
esg_emission_source --> esg_emission_source : many2one
esg_emission_source --|> esg_emission_source : one2many
esg_other_emission --> res_company : many2one
esg_other_emission --> esg_emission_factor : many2one
esg_other_emission --> uom_uom : many2one
esg_other_emission --> res_currency : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



