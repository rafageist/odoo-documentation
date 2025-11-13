<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# POS - SMS

- Version: v18
- Category: community
- Source: odoo/addons/pos_sms
- Dependencies: [[Odoo 18/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[Odoo 18/Community Addons/sms/sms|sms]]
## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `PosConfig`
- `PosOrder`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title POS - SMS - Models and Relations
class PosConfig
class PosOrder
class "sms.template" as sms_template
PosConfig --> sms_template : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
