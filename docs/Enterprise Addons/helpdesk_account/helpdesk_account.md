
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Helpdesk Account

- Scope: Enterprise Addons
- Source: enterprise/helpdesk_account
- Dependencies: [[docs/Enterprise Addons/helpdesk_sale/helpdesk_sale|helpdesk_sale]], [[docs/Community Addons/account/account|account]]

## Summary

Project, Tasks, Account

## XML Artifacts (detected)

- Views: 3
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `HelpdeskTicket`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Helpdesk Account - Models and Relations
class AccountMove
class HelpdeskTicket
class "helpdesk.ticket" as helpdesk_ticket
AccountMove --> helpdesk_ticket : many2one
class "account.move" as account_move
HelpdeskTicket .. account_move : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

