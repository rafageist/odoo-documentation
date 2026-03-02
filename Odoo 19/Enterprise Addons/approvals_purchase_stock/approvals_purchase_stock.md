<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Approvals - Purchase - Stock

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/approvals_purchase_stock
- Dependencies: [[Odoo 19/Enterprise Addons/approvals_purchase/approvals_purchase|approvals_purchase]], [[Odoo 19/Community Addons/purchase_stock/purchase_stock|purchase_stock]]

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ApprovalProductLine`
- `ApprovalRequest`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Approvals - Purchase - Stock - Models and Relations
class ApprovalProductLine
class ApprovalRequest
class "stock.warehouse" as stock_warehouse
ApprovalProductLine --> stock_warehouse : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

