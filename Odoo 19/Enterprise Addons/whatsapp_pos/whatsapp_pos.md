<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# WhatsApp-POS

- Version: v19
- Category: enterprise
- Source: enterprise19/whatsapp_pos
- Dependencies: [[Odoo 19/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[Odoo 19/Enterprise Addons/whatsapp/whatsapp|whatsapp]]
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
!include ../../../Templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
