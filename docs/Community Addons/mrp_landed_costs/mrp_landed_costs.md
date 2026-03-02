<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Landed Costs On MO

- Scope: Community Addons
- Source: odoo/addons/mrp_landed_costs
- Dependencies: [[docs/Community Addons/stock_landed_costs/stock_landed_costs|stock_landed_costs]], [[docs/Community Addons/mrp/mrp|mrp]]

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
!include ../../../templates/DiagramStyles.puml
title Landed Costs On MO - Models and Relations
class StockLandedCost
class "mrp.production" as mrp_production
StockLandedCost .. mrp_production : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





