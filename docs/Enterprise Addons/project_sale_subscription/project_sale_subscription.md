<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Project Sales Subscription

- Scope: Enterprise Addons
- Source: enterprise/project_sale_subscription
- Dependencies: [[docs/Community Addons/sale_project/sale_project|sale_project]], [[docs/Enterprise Addons/sale_subscription/sale_subscription|sale_subscription]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



