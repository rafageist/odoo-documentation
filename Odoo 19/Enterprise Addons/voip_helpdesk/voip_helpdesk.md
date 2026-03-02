<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Phone - Helpdesk

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/voip_helpdesk
- Dependencies: [[Odoo 19/Enterprise Addons/voip/voip|voip]], [[Odoo 19/Enterprise Addons/helpdesk/helpdesk|helpdesk]]

## Summary

Phone integration with Helpdesk module.

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ResPartner`
- `VoipCall`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Phone - Helpdesk - Models and Relations
class ResPartner
class VoipCall
class "helpdesk.ticket" as helpdesk_ticket
ResPartner --|> helpdesk_ticket : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

