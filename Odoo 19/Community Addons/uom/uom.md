<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Units of measure

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/uom
- Dependencies: base (not documented)

## XML Artifacts (detected)

- Views: 3
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `uom.uom`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Units of measure - Models and Relations
class "uom.uom" as uom_uom
uom_uom --> uom_uom : many2one
uom_uom --|> uom_uom : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

