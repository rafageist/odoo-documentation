<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# WhatsApp-Sign

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/whatsapp_sign
- Dependencies: [[Odoo 19/Enterprise Addons/sign/sign|sign]], [[Odoo 19/Enterprise Addons/whatsapp/whatsapp|whatsapp]]

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
!include ../../../Templates/DiagramStyles.puml
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
