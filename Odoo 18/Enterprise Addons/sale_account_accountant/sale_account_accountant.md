<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Sale Accounting

- Version: v18
- Category: enterprise
- Source: enterprise18/sale_account_accountant
- Dependencies: [[Odoo 18/Community Addons/sale/sale|sale]], [[Odoo 18/Enterprise Addons/account_accountant/account_accountant|account_accountant]]

## Summary

Bridge between Sale and Accounting

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountReconcileModel`
- `BankRecWidget`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sale Accounting - Models and Relations
class AccountReconcileModel
class BankRecWidget
class "sale.order" as sale_order
BankRecWidget .. sale_order : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
