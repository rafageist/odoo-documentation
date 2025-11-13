<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Employees cost registration on production

- Version: v18
- Category: enterprise
- Source: enterprise18/mrp_workorder_hr_account
- Dependencies: [[Odoo 18/Enterprise Addons/mrp_workorder/mrp_workorder|mrp_workorder]], [[Odoo 18/Enterprise Addons/mrp_account_enterprise/mrp_account_enterprise|mrp_account_enterprise]]

## Summary

Analytic cost of employee work in manufacturing

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountAnalyticAccountLine`
- `MrpRouting`
- `MrpWorkcenterProductivity`
- `MrpWorkorder`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Employees cost registration on production - Models and Relations
class AccountAnalyticAccountLine
class MrpRouting
class MrpWorkcenterProductivity
class MrpWorkorder
class "hr.employee" as hr_employee
AccountAnalyticAccountLine --> hr_employee : many2one
class "account.analytic.line" as account_analytic_line
MrpWorkorder .. account_analytic_line : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
