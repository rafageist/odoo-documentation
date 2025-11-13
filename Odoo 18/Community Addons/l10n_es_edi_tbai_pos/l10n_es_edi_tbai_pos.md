<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Spain - Point of Sale + TicketBAI

- Version: v18
- Category: community
- Source: odoo/addons/l10n_es_edi_tbai_pos
- Dependencies: [[Odoo 18/Community Addons/l10n_es_edi_tbai/l10n_es_edi_tbai|l10n_es_edi_tbai]], [[Odoo 18/Community Addons/point_of_sale/point_of_sale|point_of_sale]]
## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `PosOrder`
- `PosSession`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Spain - Point of Sale + TicketBAI - Models and Relations
class PosOrder
class PosSession
class ResCompany
class "l10n_es_edi_tbai.document" as l10n_es_edi_tbai_document
PosOrder --> l10n_es_edi_tbai_document : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
