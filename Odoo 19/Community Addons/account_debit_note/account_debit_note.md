<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Debit Notes

- Version: v19
- Category: community
- Source: odoo19/addons/account_debit_note
- Dependencies: [[Odoo 19/Community Addons/account/account|account]]

## Summary

Debit Notes

## XML Artifacts (detected)

- Views: 6
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountJournal`
- `AccountMove`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Debit Notes - Models and Relations
class AccountJournal
class AccountMove
class "account.move" as account_move
AccountMove --> account_move : many2one
AccountMove --|> account_move : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
