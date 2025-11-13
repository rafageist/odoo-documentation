<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Point of Sale - UrbanPiper Enhancements

- Version: v18
- Category: enterprise
- Source: enterprise18/pos_urban_piper_enhancements
- Dependencies: [[Odoo 18/Enterprise Addons/pos_urban_piper/pos_urban_piper|pos_urban_piper]]
## XML Artifacts (detected)

- Views: 5
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `PosConfig`
- `PosOrder`
- `PosSession`
- `pos.store.timing`
- `PosPreparationDisplayOrder`
- `ProductTemplate`
- `ProductTemplateAttributeValue`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Point of Sale - UrbanPiper Enhancements - Models and Relations
class PosConfig
class PosOrder
class PosSession
class "pos.store.timing" as pos_store_timing
class PosPreparationDisplayOrder
class ProductTemplate
class ProductTemplateAttributeValue
class ResPartner
class "pos.config" as pos_config
pos_store_timing .. pos_config : many2many
ProductTemplateAttributeValue .. pos_config : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
