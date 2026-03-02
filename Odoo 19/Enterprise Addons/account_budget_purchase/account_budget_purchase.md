<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Budget Management

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/account_budget_purchase
- Dependencies: [[Odoo 19/Enterprise Addons/account_budget/account_budget|account_budget]], [[Odoo 19/Community Addons/purchase/purchase|purchase]]

## XML Artifacts (detected)

- Views: 8
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `BudgetLine`
- `PurchaseOrder`
- `PurchaseOrderLine`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Budget Management - Models and Relations
class BudgetLine
class PurchaseOrder
class PurchaseOrderLine
class "budget.line" as budget_line
PurchaseOrderLine --|> budget_line : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

