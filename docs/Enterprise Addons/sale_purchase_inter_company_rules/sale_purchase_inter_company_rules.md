<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Inter Company Module for Sale/Purchase Orders and Invoices

- Scope: Enterprise Addons
- Source: enterprise/sale_purchase_inter_company_rules
- Dependencies: [[docs/Community Addons/sale_management/sale_management|sale_management]], [[docs/Community Addons/purchase/purchase|purchase]], [[docs/Enterprise Addons/account_inter_company_rules/account_inter_company_rules|account_inter_company_rules]]

## Summary

Intercompany SO/PO/INV rules

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `PurchaseOrder`
- `ResCompany`
- `SaleOrder`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Inter Company Module for Sale/Purchase Orders and Invoices - Models and Relations
class PurchaseOrder
class ResCompany
class SaleOrder
class "sale.order" as sale_order
PurchaseOrder --> sale_order : many2one
class "purchase.order" as purchase_order
SaleOrder --> purchase_order : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




