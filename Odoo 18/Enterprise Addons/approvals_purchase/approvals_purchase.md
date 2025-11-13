<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Approvals - Purchase

- Version: v18
- Category: enterprise
- Source: enterprise18/approvals_purchase
- Dependencies: [[Odoo 18/Enterprise Addons/approvals/approvals|approvals]], [[Odoo 18/Community Addons/purchase/purchase|purchase]]
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
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Approvals - Purchase - Models and Relations
class ApprovalCategory
class ApprovalProductLine
class ApprovalRequest
class ResPartner
class "purchase.order.line" as purchase_order_line
ApprovalProductLine --> purchase_order_line : many2one
class "product.supplierinfo" as product_supplierinfo
ApprovalProductLine --> product_supplierinfo : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
