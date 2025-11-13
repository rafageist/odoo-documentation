<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Sale Planning

- Version: v18
- Category: enterprise
- Source: enterprise18/sale_planning
- Dependencies: [[Odoo 18/Community Addons/sale_management/sale_management|sale_management]], [[Odoo 18/Community Addons/sale_service/sale_service|sale_service]], [[Odoo 18/Enterprise Addons/planning/planning|planning]]
## XML Artifacts (detected)

- Views: 16
- Actions: 10
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 2

## Detected Models

- `PlanningRole`
- `PlanningSlot`
- `ProductTemplate`
- `SaleOrder`
- `SaleOrderLine`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sale Planning - Models and Relations
class PlanningRole
class PlanningSlot
class ProductTemplate
class SaleOrder
class SaleOrderLine
class "product.template" as product_template
PlanningRole --|> product_template : one2many
class "sale.order.line" as sale_order_line
PlanningSlot --> sale_order_line : many2one
class "sale.order" as sale_order
PlanningSlot --> sale_order : many2one
class "res.partner" as res_partner
PlanningSlot --> res_partner : many2one
PlanningSlot --|> product_template : one2many
class "planning.role" as planning_role
ProductTemplate --> planning_role : many2one
SaleOrder --> sale_order_line : many2one
class "planning.slot" as planning_slot
SaleOrderLine --|> planning_slot : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
