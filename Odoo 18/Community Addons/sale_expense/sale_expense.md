<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Sales Expense

- Version: v18
- Category: community
- Source: odoo/addons/sale_expense
- Dependencies: [[Odoo 18/Community Addons/sale_management/sale_management|sale_management]], [[Odoo 18/Community Addons/hr_expense/hr_expense|hr_expense]]

## Summary

Quotation, Sales Orders, Delivery & Invoicing Control

## XML Artifacts (detected)

- Views: 8
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMoveLine`
- `AccountMove`
- `Expense`
- `HrExpenseSheet`
- `ProductTemplate`
- `SaleOrder`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sales Expense - Models and Relations
class AccountMoveLine
class AccountMove
class Expense
class HrExpenseSheet
class ProductTemplate
class SaleOrder
class "sale.order" as sale_order
Expense --> sale_order : many2one
class "hr.expense" as hr_expense
SaleOrder --|> hr_expense : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
