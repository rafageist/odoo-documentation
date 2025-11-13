<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Partner Autocomplete

- Version: v18
- Category: community
- Source: odoo/addons/partner_autocomplete
- Dependencies: [[Odoo 18/Community Addons/iap_mail/iap_mail|iap_mail]]

## Summary

Auto-complete partner companies' data

## XML Artifacts (detected)

- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `res.company`
- `res.partner`
- `res.partner.autocomplete.sync`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Partner Autocomplete - Models and Relations
class "res.company" as res_company
class "res.partner" as res_partner
class "res.partner.autocomplete.sync" as res_partner_autocomplete_sync
res_partner_autocomplete_sync --> res_partner : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
