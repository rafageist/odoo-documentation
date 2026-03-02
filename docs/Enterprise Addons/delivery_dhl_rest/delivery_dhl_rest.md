
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# DHL Express Shipping

- Scope: Enterprise Addons
- Source: enterprise/delivery_dhl_rest
- Dependencies: [[docs/Community Addons/stock_delivery/stock_delivery|stock_delivery]], [[docs/Community Addons/mail/mail|mail]]

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ProviderDHL`
- `PackageType`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title DHL Express Shipping - Models and Relations
class ProviderDHL
class PackageType
class "stock.package.type" as stock_package_type
ProviderDHL --> stock_package_type : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

