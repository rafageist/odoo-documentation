<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Helpdesk Account

- Version: v18
- Category: enterprise
- Source: enterprise18/helpdesk_account
- Dependencies: [[Odoo 18/Enterprise Addons/helpdesk_sale/helpdesk_sale|helpdesk_sale]], [[Odoo 18/Community Addons/account/account|account]]

## Summary

Project, Tasks, Account

## XML Artifacts (detected)

- Views: 2
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `HelpdeskTicket`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Helpdesk Account - Models and Relations
class AccountMove
class HelpdeskTicket
class "account.move" as account_move
HelpdeskTicket .. account_move : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
