<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Extended Addresses

- Scope: Community Addons
- Source: odoo/addons/base_address_extended
- Dependencies: base (not documented), [[docs/Community Addons/contacts/contacts|contacts]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





