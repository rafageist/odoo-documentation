<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Field Service - Sale

- Version: v18
- Category: enterprise
- Source: enterprise18/industry_fsm_sale
- Dependencies: [[Odoo 18/Enterprise Addons/industry_fsm/industry_fsm|industry_fsm]], [[Odoo 18/Enterprise Addons/sale_timesheet_enterprise/sale_timesheet_enterprise|sale_timesheet_enterprise]]

## Summary

Schedule and track onsite operations, invoice time and material

## XML Artifacts (detected)

- Views: 15
- Actions: 19
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountAnalyticLine`
- `ProductProduct`
- `ProductTemplate`
- `Project`
- `ProjectProductEmployeeMap`
- `Task`
- `ProjectTaskRecurrence`
- `SaleOrder`
- `SaleOrderLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Field Service - Sale - Models and Relations
class AccountAnalyticLine
class ProductProduct
class ProductTemplate
class Project
class ProjectProductEmployeeMap
class Task
class ProjectTaskRecurrence
class SaleOrder
class SaleOrderLine
class "product.product" as product_product
ProjectProductEmployeeMap --> product_product : many2one
class "res.currency" as res_currency
Task --> res_currency : many2one
class "product.pricelist" as product_pricelist
Task --> product_pricelist : many2one
class "project.task" as project_task
SaleOrder --> project_task : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
