<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Accounting/Fleet bridge

- Version: v18
- Category: enterprise
- Source: enterprise18/account_accountant_fleet
- Dependencies: [[Odoo 18/Community Addons/account_fleet/account_fleet|account_fleet]], [[Odoo 18/Enterprise Addons/account_accountant/account_accountant|account_accountant]]

## Summary

Manage accounting with fleet features

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountTax`
- `BankRecWidget`
- `BankRecWidgetLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Accounting/Fleet bridge - Models and Relations
class AccountTax
class BankRecWidget
class BankRecWidgetLine
class "fleet.vehicle" as fleet_vehicle
BankRecWidgetLine --> fleet_vehicle : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
