<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Check Printing Base

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/account_check_printing
- Dependencies: [[Odoo 19/Community Addons/account/account|account]]

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
- `ResCompany`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Check Printing Base - Models and Relations
class AccountJournal
class AccountPayment
class AccountPaymentMethod
class ResCompany
class "ir.sequence" as ir_sequence
AccountJournal --> ir_sequence : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


