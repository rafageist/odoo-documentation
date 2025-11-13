<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Sales - Project

- Version: v19
- Category: community
- Source: odoo19/addons/sale_project
- Dependencies: [[Odoo 19/Community Addons/sale_management/sale_management|sale_management]], [[Odoo 19/Community Addons/sale_service/sale_service|sale_service]], [[Odoo 19/Community Addons/project_account/project_account|project_account]]

## Summary

Task Generation from Sales Orders

## XML Artifacts (detected)

- Views: 28
- Actions: 10
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 4

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `ProductProduct`
- `ProductTemplate`
- `ProjectMilestone`
- `ProjectProject`
- `ProjectTask`
- `ProjectTaskRecurrence`
- `ProjectTaskType`
- `ProjectUpdate`
- `SaleOrder`
- `SaleOrderLine`
- `SaleOrderTemplateLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sales - Project - Models and Relations
class AccountMove
class AccountMoveLine
class ProductProduct
class ProductTemplate
class ProjectMilestone
class ProjectProject
class ProjectTask
class ProjectTaskRecurrence
class ProjectTaskType
class ProjectUpdate
class SaleOrder
class SaleOrderLine
class SaleOrderTemplateLine
class "project.project" as project_project
ProductTemplate --> project_project : many2one
ProductTemplate --> project_project : many2one
class "project.task" as project_task
ProductTemplate --> project_task : many2one
class "sale.order.line" as sale_order_line
ProjectMilestone --> sale_order_line : many2one
ProjectProject --> sale_order_line : many2one
class "sale.order" as sale_order
ProjectProject --> sale_order : many2one
ProjectTask --> sale_order : many2one
ProjectTask --> sale_order_line : many2one
ProjectTask --> sale_order : many2one
SaleOrder .. project_task : many2many
SaleOrder .. project_project : many2many
SaleOrder --> project_project : many2one
class "account.analytic.account" as account_analytic_account
SaleOrder --> account_analytic_account : many2one
SaleOrderLine --> project_project : many2one
SaleOrderLine --> project_task : many2one
class "project.milestone" as project_milestone
SaleOrderLine --|> project_milestone : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
