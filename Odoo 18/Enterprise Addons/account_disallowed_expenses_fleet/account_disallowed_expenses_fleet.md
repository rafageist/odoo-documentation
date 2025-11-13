<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Disallowed Expenses on Fleets

- Version: v18
- Category: enterprise
- Source: enterprise18/account_disallowed_expenses_fleet
- Dependencies: [[Odoo 18/Enterprise Addons/account_accountant_fleet/account_accountant_fleet|account_accountant_fleet]], [[Odoo 18/Enterprise Addons/account_disallowed_expenses/account_disallowed_expenses|account_disallowed_expenses]]

## Summary

Manage disallowed expenses with fleets

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `AccountDisallowedExpensesCategory`
- `AccountMoveLine`
- `BankRecWidgetLine`
- `FleetVehicle`
- `fleet.disallowed.expenses.rate`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Disallowed Expenses on Fleets - Models and Relations
class AccountDisallowedExpensesCategory
class AccountMoveLine
class BankRecWidgetLine
class FleetVehicle
class "fleet.disallowed.expenses.rate" as fleet_disallowed_expenses_rate
FleetVehicle --|> fleet_disallowed_expenses_rate : one2many
class "fleet.vehicle" as fleet_vehicle
fleet_disallowed_expenses_rate --> fleet_vehicle : many2one
class "res.company" as res_company
fleet_disallowed_expenses_rate --> res_company : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
