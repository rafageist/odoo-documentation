<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# PLM for workorder

- Version: v18
- Category: enterprise
- Source: enterprise18/mrp_workorder_plm
- Dependencies: [[Odoo 18/Enterprise Addons/mrp_workorder/mrp_workorder|mrp_workorder]], [[Odoo 18/Enterprise Addons/mrp_plm/mrp_plm|mrp_plm]]

## Summary

PLM for workorder

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `MrpEco`
- `MrpEcoRoutingChange`
- `MrpProduction`
- `QualityCheck`
- `QualityPoint`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title PLM for workorder - Models and Relations
class MrpEco
class MrpEcoRoutingChange
class MrpProduction
class QualityCheck
class QualityPoint
class "mrp.eco.routing.change" as mrp_eco_routing_change
MrpEco --|> mrp_eco_routing_change : one2many
MrpEco --|> mrp_eco_routing_change : one2many
class "quality.point" as quality_point
MrpEcoRoutingChange --> quality_point : many2one
class "quality.point.test_type" as quality_point_test_type
MrpEcoRoutingChange --> quality_point_test_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
