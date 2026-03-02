<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# POS - HR

- Scope: Community Addons
- Source: odoo/addons/pos_hr
- Dependencies: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[docs/Community Addons/hr/hr|hr]]

## Summary

Link module between Point of Sale and HR

## XML Artifacts (detected)

- Views: 9
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountBankStatementLine`
- `hr.employee`
- `PosConfig`
- `PosOrder`
- `PosPayment`
- `PosSession`
- `ProductProduct`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title POS - HR - Models and Relations
class AccountBankStatementLine
class "hr.employee" as hr_employee
class PosConfig
class PosOrder
class PosPayment
class PosSession
class ProductProduct
AccountBankStatementLine --> hr_employee : many2one
PosConfig .. hr_employee : many2many
PosConfig .. hr_employee : many2many
PosConfig .. hr_employee : many2many
PosOrder --> hr_employee : many2one
PosPayment --> hr_employee : many2one
PosSession --> hr_employee : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





