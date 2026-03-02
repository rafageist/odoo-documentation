<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Sales Timesheet: Invoicing

- Scope: Enterprise Addons
- Source: enterprise/sale_timesheet_enterprise
- Dependencies: [[docs/Community Addons/sale_timesheet/sale_timesheet|sale_timesheet]], [[docs/Enterprise Addons/timesheet_grid/timesheet_grid|timesheet_grid]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




