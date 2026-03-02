<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# LATAM Localization Base

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/l10n_latam_base
- Dependencies: [[Odoo 19/Community Addons/contacts/contacts|contacts]], [[Odoo 19/Community Addons/base_vat/base_vat|base_vat]]

## Summary

LATAM Identification Types

## XML Artifacts (detected)

- Views: 3
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `l10n_latam.identification.type`
- `ResCompany`
- `ResPartner`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title LATAM Localization Base - Models and Relations
class "l10n_latam.identification.type" as l10n_latam_identification_type
class ResCompany
class ResPartner
class "res.country" as res_country
l10n_latam_identification_type --> res_country : many2one
ResPartner --> l10n_latam_identification_type : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


