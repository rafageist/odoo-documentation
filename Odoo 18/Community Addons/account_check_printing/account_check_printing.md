<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Check Printing Base

- Version: v18
- Category: community
- Source: odoo/addons/account_check_printing
- Dependencies: [[Odoo 18/Community Addons/account/account|account]]

## Summary

Check printing basic features

## XML Artifacts (detected)

- Views: 6
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountJournal`
- `AccountPayment`
- `AccountPaymentMethod`
- `res_company`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Check Printing Base - Models and Relations
class AccountJournal
class AccountPayment
class AccountPaymentMethod
class res_company
class "ir.sequence" as ir_sequence
AccountJournal --> ir_sequence : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
