<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Sweden Registered Cash Register

- Version: v18
- Category: enterprise
- Source: enterprise18/pos_l10n_se
- Dependencies: [[Odoo 18/Community Addons/pos_restaurant/pos_restaurant|pos_restaurant]], [[Odoo 18/Enterprise Addons/pos_iot/pos_iot|pos_iot]], [[Odoo 18/Community Addons/l10n_se/l10n_se|l10n_se]]

## Summary

Implements the registered cash system

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `PosConfig`
- `PosOrder`
- `ProductProduct`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Sweden Registered Cash Register - Models and Relations
class PosConfig
class PosOrder
class ProductProduct
class "iot.device" as iot_device
PosConfig --> iot_device : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
