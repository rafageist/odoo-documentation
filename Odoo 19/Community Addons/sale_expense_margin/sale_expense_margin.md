<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Sales Expense Margin

- Version: v19
- Category: community
- Source: odoo19/addons/sale_expense_margin
- Dependencies: [[Odoo 19/Community Addons/sale_expense/sale_expense|sale_expense]], [[Odoo 19/Community Addons/sale_margin/sale_margin|sale_margin]]
## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMoveLine`
- `SaleOrderLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sales Expense Margin - Models and Relations
class AccountMoveLine
class SaleOrderLine
class "hr.expense" as hr_expense
SaleOrderLine --> hr_expense : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
