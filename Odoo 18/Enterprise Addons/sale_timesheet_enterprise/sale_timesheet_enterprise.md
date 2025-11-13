<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Sales Timesheet: Invoicing

- Version: v18
- Category: enterprise
- Source: enterprise18/sale_timesheet_enterprise
- Dependencies: [[Odoo 18/Community Addons/sale_timesheet/sale_timesheet|sale_timesheet]], [[Odoo 18/Enterprise Addons/timesheet_grid/timesheet_grid|timesheet_grid]]

## Summary

Configure timesheet invoicing

## XML Artifacts (detected)

- Views: 15
- Actions: 3
- Menus: 3
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountInvoice`
- `AnalyticLine`
- `HrEmployee`
- `hr.timesheet.tip`
- `Project`
- `ProjectTask`
- `ResCompany`
- `sale.order.line`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sales Timesheet: Invoicing - Models and Relations
class AccountInvoice
class AnalyticLine
class HrEmployee
class "hr.timesheet.tip" as hr_timesheet_tip
class Project
class ProjectTask
class ResCompany
class "sale.order.line" as sale_order_line
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
