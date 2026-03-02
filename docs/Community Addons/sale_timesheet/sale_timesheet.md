<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Sales Timesheet

- Scope: Community Addons
- Source: odoo/addons/sale_timesheet
- Dependencies: [[docs/Community Addons/sale_project/sale_project|sale_project]], [[docs/Community Addons/hr_timesheet/hr_timesheet|hr_timesheet]]

## Summary

Sell based on timesheets

## XML Artifacts (detected)

- Views: 37
- Actions: 24
- Menus: 1
- Rules (ir.rule): 2
- Access CSV entries: 2

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `HrEmployee`
- `AccountAnalyticLine`
- `ProductProduct`
- `ProductTemplate`
- `ProjectProject`
- `project.sale.line.employee.map`
- `ProjectTask`
- `SaleOrder`
- `SaleOrderLine`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Sales Timesheet - Models and Relations
class AccountMove
class AccountMoveLine
class HrEmployee
class AccountAnalyticLine
class ProductProduct
class ProductTemplate
class ProjectProject
class "project.sale.line.employee.map" as project_sale_line_employee_map
class ProjectTask
class SaleOrder
class SaleOrderLine
class "account.analytic.line" as account_analytic_line
AccountMove --|> account_analytic_line : one2many
class "uom.uom" as uom_uom
AccountMove --> uom_uom : many2one
class "res.partner" as res_partner
AccountAnalyticLine --> res_partner : many2one
class "account.move" as account_move
AccountAnalyticLine --> account_move : many2one
ProjectProject --|> project_sale_line_employee_map : one2many
class "product.product" as product_product
ProjectProject --> product_product : many2one
class "project.project" as project_project
project_sale_line_employee_map --> project_project : many2one
class "hr.employee" as hr_employee
project_sale_line_employee_map --> hr_employee : many2one
project_sale_line_employee_map .. hr_employee : many2many
class "sale.order.line" as sale_order_line
project_sale_line_employee_map --> sale_order_line : many2one
class "res.company" as res_company
project_sale_line_employee_map --> res_company : many2one
class "res.currency" as res_currency
project_sale_line_employee_map --> res_currency : many2one
project_sale_line_employee_map --> res_currency : many2one
ProjectTask --> sale_order_line : many2one
SaleOrder --> uom_uom : many2one
SaleOrderLine --|> account_analytic_line : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




