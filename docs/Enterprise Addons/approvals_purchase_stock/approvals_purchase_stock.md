<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Approvals - Purchase - Stock

- Scope: Enterprise Addons
- Source: enterprise/approvals_purchase_stock
- Dependencies: [[docs/Enterprise Addons/approvals_purchase/approvals_purchase|approvals_purchase]], [[docs/Community Addons/purchase_stock/purchase_stock|purchase_stock]]

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
!include ../../../templates/DiagramStyles.puml
title Approvals - Purchase - Stock - Models and Relations
class ApprovalProductLine
class ApprovalRequest
class "stock.warehouse" as stock_warehouse
ApprovalProductLine --> stock_warehouse : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



