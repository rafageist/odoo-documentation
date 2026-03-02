<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Check Printing Base

- Scope: Community Addons
- Source: odoo/addons/account_check_printing
- Dependencies: [[docs/Community Addons/account/account|account]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





