<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Units of measure

- Scope: Community Addons
- Source: odoo/addons/uom
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
!include ../../../templates/DiagramStyles.puml
title Units of measure - Models and Relations
class "uom.uom" as uom_uom
uom_uom --> uom_uom : many2one
uom_uom --|> uom_uom : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



