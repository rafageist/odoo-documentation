<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Employees cost registration on production

- Scope: Enterprise Addons
- Source: enterprise/mrp_workorder_hr_account
- Dependencies: [[docs/Enterprise Addons/mrp_workorder/mrp_workorder|mrp_workorder]], [[docs/Enterprise Addons/mrp_account_enterprise/mrp_account_enterprise|mrp_account_enterprise]]

## Summary

Analytic cost of employee work in manufacturing

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountAnalyticLine`
- `MrpWorkcenterProductivity`
- `MrpWorkorder`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Employees cost registration on production - Models and Relations
class AccountAnalyticLine
class MrpWorkcenterProductivity
class MrpWorkorder
class "hr.employee" as hr_employee
AccountAnalyticLine --> hr_employee : many2one
class "account.analytic.line" as account_analytic_line
MrpWorkorder .. account_analytic_line : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



