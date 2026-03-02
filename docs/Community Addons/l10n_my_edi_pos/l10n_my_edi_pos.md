<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Malaysia - E-invoicing (POS)

- Scope: Community Addons
- Source: odoo/addons/l10n_my_edi_pos
- Dependencies: [[docs/Community Addons/l10n_my_edi/l10n_my_edi|l10n_my_edi]], [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





