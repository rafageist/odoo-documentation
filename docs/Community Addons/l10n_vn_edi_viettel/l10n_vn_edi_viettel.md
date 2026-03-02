<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Vietnam - E-invoicing

- Scope: Community Addons
- Source: odoo/addons/l10n_vn_edi_viettel
- Dependencies: [[docs/Community Addons/l10n_vn/l10n_vn|l10n_vn]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





