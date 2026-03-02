<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Sweden Registered Cash Register

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_se_pos
- Dependencies: [[Odoo 19/Community Addons/pos_restaurant/pos_restaurant|pos_restaurant]], [[Odoo 19/Enterprise Addons/pos_iot/pos_iot|pos_iot]], [[Odoo 19/Community Addons/l10n_se/l10n_se|l10n_se]]

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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


