<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Point of Sale - UrbanPiper Enhancements

- Scope: Enterprise Addons
- Source: enterprise/pos_urban_piper_enhancements
- Dependencies: [[docs/Enterprise Addons/pos_urban_piper/pos_urban_piper|pos_urban_piper]]

## XML Artifacts (detected)

- Views: 5
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `PosConfig`
- `PosOrder`
- `PosPrepOrder`
- `PosSession`
- `pos.store.timing`
- `ProductTemplate`
- `ProductTemplateAttributeValue`
- `ResPartner`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Point of Sale - UrbanPiper Enhancements - Models and Relations
class PosConfig
class PosOrder
class PosPrepOrder
class PosSession
class "pos.store.timing" as pos_store_timing
class ProductTemplate
class ProductTemplateAttributeValue
class ResPartner
class "pos.config" as pos_config
pos_store_timing .. pos_config : many2many
ProductTemplateAttributeValue .. pos_config : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




