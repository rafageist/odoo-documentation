<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Extended Addresses

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/base_address_extended
- Dependencies: base (not documented), [[Odoo 19/Community Addons/contacts/contacts|contacts]]

## Summary

Add extra fields on addresses

## XML Artifacts (detected)

- Views: 5
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `res.city`
- `ResCountry`
- `ResPartner`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Extended Addresses - Models and Relations
class "res.city" as res_city
class ResCountry
class ResPartner
class "res.country" as res_country
res_city --> res_country : many2one
class "res.country.state" as res_country_state
res_city --> res_country_state : many2one
ResPartner --> res_city : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


