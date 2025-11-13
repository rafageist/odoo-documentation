<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# United States Postal Service (USPS) Shipping

- Version: v18
- Category: enterprise
- Source: enterprise18/delivery_usps_rest
- Dependencies: [[Odoo 18/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[Odoo 18/Community Addons/mail/mail|mail]]
## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ProviderUSPS`
- `PackageType`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title United States Postal Service (USPS) Shipping - Models and Relations
class ProviderUSPS
class PackageType
class "stock.package.type" as stock_package_type
ProviderUSPS --> stock_package_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
