<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Units of measure

- Version: v18
- Category: community
- Source: odoo/addons/uom
- Dependencies: base (not documented)
## XML Artifacts (detected)

- Views: 6
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `uom.category`
- `uom.uom`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Units of measure - Models and Relations
class "uom.category" as uom_category
class "uom.uom" as uom_uom
uom_category --|> uom_uom : one2many
uom_category --> uom_uom : many2one
uom_uom --> uom_category : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
