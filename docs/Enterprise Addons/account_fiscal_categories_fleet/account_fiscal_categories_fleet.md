<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Fiscal Categories on Fleets

- Scope: Enterprise Addons
- Source: enterprise/account_fiscal_categories_fleet
- Dependencies: [[docs/Enterprise Addons/account_accountant_fleet/account_accountant_fleet|account_accountant_fleet]], [[docs/Enterprise Addons/account_fiscal_categories/account_fiscal_categories|account_fiscal_categories]]

## Summary

Manage fiscal categories with fleets

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `AccountFiscalCategory`
- `AccountMoveLine`
- `FleetVehicle`
- `fleet.disallowed.expenses.rate`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Fiscal Categories on Fleets - Models and Relations
class AccountFiscalCategory
class AccountMoveLine
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



