<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Debit Notes

- Scope: Community Addons
- Source: odoo/addons/account_debit_note
- Dependencies: [[docs/Community Addons/account/account|account]]

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
!include ../../../templates/DiagramStyles.puml
title Debit Notes - Models and Relations
class AccountJournal
class AccountMove
class "account.move" as account_move
AccountMove --> account_move : many2one
AccountMove --|> account_move : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





