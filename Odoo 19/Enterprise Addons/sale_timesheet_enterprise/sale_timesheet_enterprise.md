<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Sales Timesheet: Invoicing

- Version: v19
- Category: enterprise
- Source: enterprise19/sale_timesheet_enterprise
- Dependencies: [[Odoo 19/Community Addons/sale_timesheet/sale_timesheet|sale_timesheet]], [[Odoo 19/Enterprise Addons/timesheet_grid/timesheet_grid|timesheet_grid]]

## Summary

Configure timesheet invoicing

## XML Artifacts (detected)

- Views: 20
- Actions: 5
- Menus: 5
- Rules (ir.rule): 2
- Access CSV entries: 3

## Detected Models

- `AccountAnalyticLine`
- `AccountMoveLine`
- `HrEmployee`
- `HREmployeePublic`
- `hr.timesheet.tip`
- `IrUiMenu`
- `ProjectProject`
- `ProjectTask`
- `ResCompany`
- `sale.order.line`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sales Timesheet: Invoicing - Models and Relations
class AccountAnalyticLine
class AccountMoveLine
class HrEmployee
class HREmployeePublic
class "hr.timesheet.tip" as hr_timesheet_tip
class IrUiMenu
class ProjectProject
class ProjectTask
class ResCompany
class "sale.order.line" as sale_order_line
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
