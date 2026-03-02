<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# WhatsApp-Sign

- Scope: Enterprise Addons
- Source: enterprise/whatsapp_sign
- Dependencies: [[docs/Enterprise Addons/sign/sign|sign]], [[docs/Enterprise Addons/whatsapp/whatsapp|whatsapp]]

## Summary

This module enables users to send signature requests via WhatsApp in Odoo Sign

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `SignRequest`
- `SignRequestItem`
- `WhatsappTemplateVariable`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title WhatsApp-Sign - Models and Relations
class SignRequest
class SignRequestItem
class WhatsappTemplateVariable
class "res.partner" as res_partner
SignRequest --> res_partner : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->


