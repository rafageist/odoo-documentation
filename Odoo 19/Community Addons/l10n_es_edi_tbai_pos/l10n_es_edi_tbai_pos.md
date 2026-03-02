<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Spain - Point of Sale + TicketBAI

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/l10n_es_edi_tbai_pos
- Dependencies: [[Odoo 19/Community Addons/l10n_es_edi_tbai/l10n_es_edi_tbai|l10n_es_edi_tbai]], [[Odoo 19/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `PosConfig`
- `PosOrder`
- `ResCompany`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Spain - Point of Sale + TicketBAI - Models and Relations
class PosConfig
class PosOrder
class ResCompany
class "l10n_es_edi_tbai.document" as l10n_es_edi_tbai_document
PosOrder --> l10n_es_edi_tbai_document : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


