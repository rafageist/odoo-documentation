<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Fedex Shipping

- Scope: Enterprise Addons
- Source: enterprise/delivery_fedex_rest
- Dependencies: [[docs/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[docs/Community Addons/mail/mail|mail]]

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ProviderFedex`
- `PackageType`
- `UoM`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Fedex Shipping - Models and Relations
class ProviderFedex
class PackageType
class UoM
class "stock.package.type" as stock_package_type
ProviderFedex --> stock_package_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



