<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Vietnam - E-invoicing

- Version: v19
- Category: community
- Source: odoo19/addons/l10n_vn_edi_viettel
- Dependencies: [[Odoo 19/Community Addons/l10n_vn/l10n_vn|l10n_vn]]

## Summary

E-invoicing using SInvoice by Viettel

## XML Artifacts (detected)

- Views: 7
- Actions: 3
- Menus: 3
- Rules (ir.rule): 0
- Access CSV entries: 5

## Detected Models

- `AccountMove`
- `ResCompany`
- `ResPartner`
- `l10n_vn_edi_viettel.sinvoice.template`
- `l10n_vn_edi_viettel.sinvoice.symbol`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Vietnam - E-invoicing - Models and Relations
class AccountMove
class ResCompany
class ResPartner
class "l10n_vn_edi_viettel.sinvoice.template" as l10n_vn_edi_viettel_sinvoice_template
class "l10n_vn_edi_viettel.sinvoice.symbol" as l10n_vn_edi_viettel_sinvoice_symbol
AccountMove --> l10n_vn_edi_viettel_sinvoice_symbol : many2one
class "ir.attachment" as ir_attachment
AccountMove --> ir_attachment : many2one
AccountMove --> ir_attachment : many2one
AccountMove --> ir_attachment : many2one
class "account.move" as account_move
AccountMove --> account_move : many2one
ResPartner --> l10n_vn_edi_viettel_sinvoice_symbol : many2one
l10n_vn_edi_viettel_sinvoice_template --|> l10n_vn_edi_viettel_sinvoice_symbol : one2many
l10n_vn_edi_viettel_sinvoice_symbol --> l10n_vn_edi_viettel_sinvoice_template : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
