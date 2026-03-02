<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# POS - SMS

- Scope: Community Addons
- Source: odoo/addons/pos_sms
- Dependencies: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]], [[docs/Community Addons/sms/sms|sms]]

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
!include ../../../templates/DiagramStyles.puml
title POS - SMS - Models and Relations
class PosConfig
class PosOrder
class "sms.template" as sms_template
PosConfig --> sms_template : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





