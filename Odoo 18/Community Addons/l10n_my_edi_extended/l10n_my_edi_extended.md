<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Malaysia - E-invoicing Extended Features

- Version: v18
- Category: community
- Source: odoo/addons/l10n_my_edi_extended
- Dependencies: [[Odoo 18/Community Addons/l10n_my_edi/l10n_my_edi|l10n_my_edi]]

## Summary

Extended features for the E-invoicing using MyInvois

## XML Artifacts (detected)

- Views: 2
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Malaysia - E-invoicing Extended Features - Models and Relations
class AccountMove
class AccountMoveLine
class ResPartner
class "l10n_my_edi.industry_classification" as l10n_my_edi_industry_classification
ResPartner --> l10n_my_edi_industry_classification : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
