<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Phone - Helpdesk

- Scope: Enterprise Addons
- Source: enterprise/voip_helpdesk
- Dependencies: [[docs/Enterprise Addons/voip/voip|voip]], [[docs/Enterprise Addons/helpdesk/helpdesk|helpdesk]]

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
!include ../../../templates/DiagramStyles.puml
title Phone - Helpdesk - Models and Relations
class ResPartner
class VoipCall
class "helpdesk.ticket" as helpdesk_ticket
ResPartner --|> helpdesk_ticket : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




