<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Partnership / Membership

- Scope: Community Addons
- Source: odoo/addons/partnership
- Dependencies: [[docs/Community Addons/crm/crm|crm]], [[docs/Community Addons/sale/sale|sale]]

## XML Artifacts (detected)

- Views: 9
- Actions: 3
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `ProductPricelist`
- `ProductTemplate`
- `ResCompany`
- `ResPartner`
- `res.partner.grade`
- `SaleOrder`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Partnership / Membership - Models and Relations
class ProductPricelist
class ProductTemplate
class ResCompany
class ResPartner
class "res.partner.grade" as res_partner_grade
class SaleOrder
ProductTemplate --> res_partner_grade : many2one
ResPartner --> res_partner_grade : many2one
class "res.company" as res_company
res_partner_grade --> res_company : many2one
class "product.pricelist" as product_pricelist
res_partner_grade --> product_pricelist : many2one
SaleOrder --> res_partner_grade : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





