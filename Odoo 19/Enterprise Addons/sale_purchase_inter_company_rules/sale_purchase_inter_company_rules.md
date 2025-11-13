<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Inter Company Module for Sale/Purchase Orders and Invoices

- Version: v19
- Category: enterprise
- Source: enterprise19/sale_purchase_inter_company_rules
- Dependencies: [[Odoo 19/Community Addons/sale_management/sale_management|sale_management]], [[Odoo 19/Community Addons/purchase/purchase|purchase]], [[Odoo 19/Enterprise Addons/account_inter_company_rules/account_inter_company_rules|account_inter_company_rules]]

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
!include ../../../Templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
