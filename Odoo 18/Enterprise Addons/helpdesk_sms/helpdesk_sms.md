<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Helpdesk - SMS

- Version: v18
- Category: enterprise
- Source: enterprise18/helpdesk_sms
- Dependencies: [[Odoo 18/Enterprise Addons/helpdesk/helpdesk|helpdesk]], [[Odoo 18/Community Addons/sms/sms|sms]]

## Summary

Send text messages when ticket stage move

## XML Artifacts (detected)

- Views: 3
- Actions: 1
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 1

## Detected Models

- `HelpdeskStage`
- `HelpdeskTicket`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Helpdesk - SMS - Models and Relations
class HelpdeskStage
class HelpdeskTicket
class "sms.template" as sms_template
HelpdeskStage --> sms_template : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
