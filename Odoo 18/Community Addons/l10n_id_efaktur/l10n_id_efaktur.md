<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Indonesia E-faktur

- Version: v18
- Category: community
- Source: odoo/addons/l10n_id_efaktur
- Dependencies: [[Odoo 18/Community Addons/l10n_id/l10n_id|l10n_id]]
## XML Artifacts (detected)

- Views: 9
- Actions: 2
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 2

## Detected Models

- `AccountMove`
- `l10n_id_efaktur.efaktur.range`
- `l10n_id_efaktur.document`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Indonesia E-faktur - Models and Relations
class AccountMove
class "l10n_id_efaktur.efaktur.range" as l10n_id_efaktur_efaktur_range
class "l10n_id_efaktur.document" as l10n_id_efaktur_document
class ResPartner
class "account.move" as account_move
AccountMove --> account_move : many2one
AccountMove --> l10n_id_efaktur_document : many2one
AccountMove --> l10n_id_efaktur_efaktur_range : many2one
class "res.company" as res_company
l10n_id_efaktur_efaktur_range --> res_company : many2one
l10n_id_efaktur_document --> res_company : many2one
l10n_id_efaktur_document --|> account_move : one2many
class "ir.attachment" as ir_attachment
l10n_id_efaktur_document --> ir_attachment : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
