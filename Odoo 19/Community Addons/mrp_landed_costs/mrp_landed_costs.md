<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Landed Costs On MO

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/mrp_landed_costs
- Dependencies: [[Odoo 19/Community Addons/stock_landed_costs/stock_landed_costs|stock_landed_costs]], [[Odoo 19/Community Addons/mrp/mrp|mrp]]

## Summary

Landed Costs on Manufacturing Order

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `StockLandedCost`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Landed Costs On MO - Models and Relations
class StockLandedCost
class "mrp.production" as mrp_production
StockLandedCost .. mrp_production : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


