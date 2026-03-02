
<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Sales Expense Margin

- Scope: Community Addons
- Source: odoo/addons/sale_expense_margin
- Dependencies: [[docs/Community Addons/sale_expense/sale_expense|sale_expense]], [[docs/Community Addons/sale_margin/sale_margin|sale_margin]]

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
!include ../../../templates/DiagramStyles.puml
title Sales Expense Margin - Models and Relations
class AccountMoveLine
class SaleOrderLine
class "hr.expense" as hr_expense
SaleOrderLine --> hr_expense : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



