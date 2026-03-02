
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Helpdesk - SMS

- Scope: Enterprise Addons
- Source: enterprise/helpdesk_sms
- Dependencies: [[docs/Enterprise Addons/helpdesk/helpdesk|helpdesk]], [[docs/Community Addons/sms/sms|sms]]

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
!include ../../../templates/DiagramStyles.puml
title Helpdesk - SMS - Models and Relations
class HelpdeskStage
class HelpdeskTicket
class "sms.template" as sms_template
HelpdeskStage --> sms_template : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

