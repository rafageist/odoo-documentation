<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Malaysia - E-invoicing (POS)

- Version: v19
- Category: community
- Source: odoo19/addons/l10n_my_edi_pos
- Dependencies: [[Odoo 19/Community Addons/l10n_my_edi/l10n_my_edi|l10n_my_edi]], [[Odoo 19/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

## Summary

Consolidated E-invoicing using MyInvois

## XML Artifacts (detected)

- Views: 4
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `MyInvoisDocumentPoS`
- `PosOrder`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Malaysia - E-invoicing (POS) - Models and Relations
class MyInvoisDocumentPoS
class PosOrder
class "pos.order" as pos_order
MyInvoisDocumentPoS .. pos_order : many2many
class "pos.config" as pos_config
MyInvoisDocumentPoS --> pos_config : many2one
class "myinvois.document" as myinvois_document
PosOrder .. myinvois_document : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
