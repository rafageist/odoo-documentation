<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Sweden Registered Cash Register

- Scope: Enterprise Addons
- Source: enterprise/l10n_se_pos
- Dependencies: [[docs/Community Addons/pos_restaurant/pos_restaurant|pos_restaurant]], [[docs/Enterprise Addons/pos_iot/pos_iot|pos_iot]], [[docs/Community Addons/l10n_se/l10n_se|l10n_se]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




