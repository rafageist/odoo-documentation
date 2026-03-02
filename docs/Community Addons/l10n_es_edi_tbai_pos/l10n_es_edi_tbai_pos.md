<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Spain - Point of Sale + TicketBAI

- Scope: Community Addons
- Source: odoo/addons/l10n_es_edi_tbai_pos
- Dependencies: [[docs/Community Addons/l10n_es_edi_tbai/l10n_es_edi_tbai|l10n_es_edi_tbai]], [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





