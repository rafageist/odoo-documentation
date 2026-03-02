<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Product Lifecycle Management (PLM)

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/mrp_plm
- Dependencies: [[Odoo 19/Community Addons/mrp/mrp|mrp]]

## Summary

Manage engineering change orders on products, bills of material

## XML Artifacts (detected)

- Views: 25
- Actions: 13
- Menus: 14
- Rules (ir.rule): 1
- Access CSV entries: 13

## Detected Models

- `MrpBom`
- `MrpBomLine`
- `MrpBomByproduct`
- `mrp.eco.type`
- `mrp.eco.approval.template`
- `mrp.eco.approval`
- `mrp.eco.stage`
- `mrp.eco`
- `mrp.eco.bom.change`
- `mrp.eco.routing.change`
- `mrp.eco.tag`
- `MrpProduction`
- `MrpRoutingWorkcenter`
- `ProductTemplate`
- `ProductProduct`
- `ProductDocument`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Product Lifecycle Management (PLM) - Models and Relations
class MrpBom
class MrpBomLine
class MrpBomByproduct
class "mrp.eco.type" as mrp_eco_type
class "mrp.eco.approval.template" as mrp_eco_approval_template
class "mrp.eco.approval" as mrp_eco_approval
class "mrp.eco.stage" as mrp_eco_stage
class "mrp.eco" as mrp_eco
class "mrp.eco.bom.change" as mrp_eco_bom_change
class "mrp.eco.routing.change" as mrp_eco_routing_change
class "mrp.eco.tag" as mrp_eco_tag
class MrpProduction
class MrpRoutingWorkcenter
class ProductTemplate
class ProductProduct
class ProductDocument
class "mrp.bom" as mrp_bom
MrpBom --> mrp_bom : many2one
MrpBom --|> mrp_eco : one2many
mrp_eco_type .. mrp_eco_stage : many2many
class "res.users" as res_users
mrp_eco_approval_template .. res_users : many2many
mrp_eco_approval_template --> mrp_eco_stage : many2one
mrp_eco_approval --> mrp_eco : many2one
mrp_eco_approval --> mrp_eco_approval_template : many2one
mrp_eco_approval --> res_users : many2one
mrp_eco_approval .. res_users : many2many
mrp_eco_approval --> mrp_eco_stage : many2one
mrp_eco_approval --> mrp_eco_stage : many2one
mrp_eco_stage .. mrp_eco_type : many2many
mrp_eco_stage --|> mrp_eco_approval_template : one2many
mrp_eco --> res_users : many2one
mrp_eco --> mrp_eco_type : many2one
mrp_eco --> mrp_eco_stage : many2one
class "res.company" as res_company
mrp_eco --> res_company : many2one
mrp_eco .. mrp_eco_tag : many2many
mrp_eco --|> mrp_eco_approval : one2many
class "product.template" as product_template
mrp_eco --> product_template : many2one
class "mrp.production" as mrp_production
mrp_eco --> mrp_production : many2one
mrp_eco --> mrp_bom : many2one
mrp_eco --> mrp_bom : many2one
mrp_eco --|> mrp_eco_bom_change : one2many
mrp_eco --|> mrp_eco_bom_change : one2many
mrp_eco --|> mrp_eco_bom_change : one2many
mrp_eco --|> mrp_eco_bom_change : one2many
mrp_eco --|> mrp_eco_routing_change : one2many
class "product.document" as product_document
mrp_eco --|> product_document : one2many
mrp_eco --> product_document : many2one
class "ir.attachment" as ir_attachment
mrp_eco --> ir_attachment : many2one
mrp_eco --> mrp_bom : many2one
mrp_eco --|> mrp_eco_bom_change : one2many
mrp_eco_bom_change --> mrp_eco : many2one
mrp_eco_bom_change --> mrp_eco : many2one
mrp_eco_bom_change --> mrp_eco : many2one
class "product.product" as product_product
mrp_eco_bom_change --> product_product : many2one
class "uom.uom" as uom_uom
mrp_eco_bom_change --> uom_uom : many2one
mrp_eco_bom_change --> uom_uom : many2one
class "mrp.routing.workcenter" as mrp_routing_workcenter
mrp_eco_bom_change --> mrp_routing_workcenter : many2one
mrp_eco_bom_change --> mrp_routing_workcenter : many2one
class "mrp.bom.line" as mrp_bom_line
mrp_eco_bom_change --> mrp_bom_line : many2one
class "mrp.bom.byproduct" as mrp_bom_byproduct
mrp_eco_bom_change --> mrp_bom_byproduct : many2one
mrp_eco_routing_change --> mrp_eco : many2one
class "mrp.workcenter" as mrp_workcenter
mrp_eco_routing_change --> mrp_workcenter : many2one
mrp_eco_routing_change --> mrp_routing_workcenter : many2one
MrpProduction --|> mrp_eco : one2many
MrpProduction --> mrp_bom : many2one
ProductTemplate --|> mrp_eco : one2many
ProductDocument --> ir_attachment : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

