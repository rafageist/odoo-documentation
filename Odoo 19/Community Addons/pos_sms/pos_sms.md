<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# POS - SMS

- Version: v19
- Category: community
- Source: odoo19/addons/pos_sms
- Dependencies: [[Odoo 19/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[Odoo 19/Community Addons/sms/sms|sms]]
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
