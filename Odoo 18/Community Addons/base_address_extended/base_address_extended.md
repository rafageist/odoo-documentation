<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Extended Addresses

- Version: v18
- Category: community
- Source: odoo/addons/base_address_extended
- Dependencies: base (not documented), [[Odoo 18/Community Addons/contacts/contacts|contacts]]

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
- `Country`
- `Partner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Extended Addresses - Models and Relations
class "res.city" as res_city
class Country
class Partner
class "res.country" as res_country
res_city --> res_country : many2one
class "res.country.state" as res_country_state
res_city --> res_country_state : many2one
Partner --> res_city : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
