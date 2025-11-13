<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# POS - HR

- Version: v19
- Category: community
- Source: odoo19/addons/pos_hr
- Dependencies: [[Odoo 19/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[Odoo 19/Community Addons/hr/hr|hr]]

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
!include ../../../Templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
