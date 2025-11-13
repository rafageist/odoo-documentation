<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Inter Company Module for Sale/Purchase Orders and Invoices

- Version: v18
- Category: enterprise
- Source: enterprise18/sale_purchase_inter_company_rules
- Dependencies: [[Odoo 18/Community Addons/sale_management/sale_management|sale_management]], [[Odoo 18/Community Addons/purchase/purchase|purchase]], [[Odoo 18/Enterprise Addons/account_inter_company_rules/account_inter_company_rules|account_inter_company_rules]]

## Summary

Intercompany SO/PO/INV rules

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `purchase_order`
- `res_company`
- `sale_order`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Inter Company Module for Sale/Purchase Orders and Invoices - Models and Relations
class purchase_order
class res_company
class sale_order
class "sale.order" as sale_order
purchase_order --> sale_order : many2one
class "purchase.order" as purchase_order
sale_order --> purchase_order : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
