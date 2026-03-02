<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# WhatsApp-POS

- Scope: Enterprise Addons
- Source: enterprise/whatsapp_pos
- Dependencies: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[docs/Enterprise Addons/whatsapp/whatsapp|whatsapp]]

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `PosConfig`
- `PosOrder`
- `WhatsappTemplate`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title WhatsApp-POS - Models and Relations
class PosConfig
class PosOrder
class WhatsappTemplate
class "whatsapp.template" as whatsapp_template
PosConfig --> whatsapp_template : many2one
PosConfig --> whatsapp_template : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



