<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Spain - Veri*Factu for Point of Sale

- Scope: Community Addons
- Source: odoo/addons/l10n_es_edi_verifactu_pos
- Dependencies: [[docs/Community Addons/l10n_es_edi_verifactu/l10n_es_edi_verifactu|l10n_es_edi_verifactu]], [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

## Summary

Add Veri*Factu support to Point of Sale

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountMove`
- `PosConfig`
- `PosOrder`
- `ResCompany`
- `L10nEsEdiVerifactuDocument`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Spain - Veri*Factu for Point of Sale - Models and Relations
class AccountMove
class PosConfig
class PosOrder
class ResCompany
class L10nEsEdiVerifactuDocument
class "l10n_es_edi_verifactu.document" as l10n_es_edi_verifactu_document
PosOrder --|> l10n_es_edi_verifactu_document : one2many
class "pos.order" as pos_order
L10nEsEdiVerifactuDocument --> pos_order : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





