<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Project Sales Subscription

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/project_sale_subscription
- Dependencies: [[Odoo 19/Community Addons/sale_project/sale_project|sale_project]], [[Odoo 19/Enterprise Addons/sale_subscription/sale_subscription|sale_subscription]]

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
- `ProjectProject`
- `SaleOrder`
- `SaleOrderLine`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Project Sales Subscription - Models and Relations
class AccountAnalyticAccount
class ProjectProject
class SaleOrder
class SaleOrderLine
class "sale.order" as sale_order
AccountAnalyticAccount --|> sale_order : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

