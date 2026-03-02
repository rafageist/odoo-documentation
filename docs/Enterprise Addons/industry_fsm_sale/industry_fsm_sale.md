<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Field Service - Sale

- Scope: Enterprise Addons
- Source: enterprise/industry_fsm_sale
- Dependencies: [[docs/Enterprise Addons/industry_fsm/industry_fsm|industry_fsm]], [[docs/Enterprise Addons/sale_timesheet_enterprise/sale_timesheet_enterprise|sale_timesheet_enterprise]]

## Summary

Schedule and track onsite operations, invoice time and material

## XML Artifacts (detected)

- Views: 15
- Actions: 21
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountAnalyticLine`
- `ProductProduct`
- `ProductTemplate`
- `ProjectProject`
- `ProjectSaleLineEmployeeMap`
- `ProjectTask`
- `SaleOrder`
- `SaleOrderLine`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Field Service - Sale - Models and Relations
class AccountAnalyticLine
class ProductProduct
class ProductTemplate
class ProjectProject
class ProjectSaleLineEmployeeMap
class ProjectTask
class SaleOrder
class SaleOrderLine
class "product.product" as product_product
ProjectSaleLineEmployeeMap --> product_product : many2one
class "res.currency" as res_currency
ProjectTask --> res_currency : many2one
class "product.pricelist" as product_pricelist
ProjectTask --> product_pricelist : many2one
class "project.task" as project_task
SaleOrder --> project_task : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



