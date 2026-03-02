<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Sales Expense

- Scope: Community Addons
- Source: odoo/addons/sale_expense
- Dependencies: [[docs/Community Addons/sale_management/sale_management|sale_management]], [[docs/Community Addons/hr_expense/hr_expense|hr_expense]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




