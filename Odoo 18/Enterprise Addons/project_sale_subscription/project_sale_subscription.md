<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Project Sales Subscription

- Version: v18
- Category: enterprise
- Source: enterprise18/project_sale_subscription
- Dependencies: [[Odoo 18/Community Addons/sale_project/sale_project|sale_project]], [[Odoo 18/Enterprise Addons/sale_subscription/sale_subscription|sale_subscription]]

## Summary

Project sales subscriptions

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountAnalyticAccount`
- `Project`
- `SaleOrder`
- `SaleOrderLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Project Sales Subscription - Models and Relations
class AccountAnalyticAccount
class Project
class SaleOrder
class SaleOrderLine
class "sale.order" as sale_order
AccountAnalyticAccount --|> sale_order : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
