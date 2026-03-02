<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Approvals - Purchase

- Scope: Enterprise Addons
- Source: enterprise/approvals_purchase
- Dependencies: [[docs/Enterprise Addons/approvals/approvals|approvals]], [[docs/Community Addons/purchase/purchase|purchase]]

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ApprovalCategory`
- `ApprovalProductLine`
- `ApprovalRequest`
- `PurchaseOrder`
- `ResPartner`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Approvals - Purchase - Models and Relations
class ApprovalCategory
class ApprovalProductLine
class ApprovalRequest
class PurchaseOrder
class ResPartner
class "purchase.order.line" as purchase_order_line
ApprovalProductLine --> purchase_order_line : many2one
class "product.supplierinfo" as product_supplierinfo
ApprovalProductLine --> product_supplierinfo : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




