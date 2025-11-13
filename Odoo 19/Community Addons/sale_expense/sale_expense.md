<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Sales Expense

- Version: v19
- Category: community
- Source: odoo19/addons/sale_expense
- Dependencies: [[Odoo 19/Community Addons/sale_management/sale_management|sale_management]], [[Odoo 19/Community Addons/hr_expense/hr_expense|hr_expense]]

## Summary

Quotation, Sales Orders, Delivery & Invoicing Control

## XML Artifacts (detected)

- Views: 6
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `HrExpense`
- `ProductTemplate`
- `SaleOrder`
- `SaleOrderLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sales Expense - Models and Relations
class AccountMove
class AccountMoveLine
class HrExpense
class ProductTemplate
class SaleOrder
class SaleOrderLine
class "sale.order" as sale_order
HrExpense --> sale_order : many2one
class "sale.order.line" as sale_order_line
HrExpense --> sale_order_line : many2one
class "hr.expense" as hr_expense
SaleOrder --|> hr_expense : one2many
SaleOrderLine --|> hr_expense : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
