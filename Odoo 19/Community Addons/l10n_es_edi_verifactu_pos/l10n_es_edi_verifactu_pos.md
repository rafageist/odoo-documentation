<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Spain - Veri*Factu for Point of Sale

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/l10n_es_edi_verifactu_pos
- Dependencies: [[Odoo 19/Community Addons/l10n_es_edi_verifactu/l10n_es_edi_verifactu|l10n_es_edi_verifactu]], [[Odoo 19/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

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
!include ../../../Templates/DiagramStyles.puml
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


