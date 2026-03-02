<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Budget Management

- Scope: Enterprise Addons
- Source: enterprise/account_budget_purchase
- Dependencies: [[docs/Enterprise Addons/account_budget/account_budget|account_budget]], [[docs/Community Addons/purchase/purchase|purchase]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




