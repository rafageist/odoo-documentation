<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Indian - E-waybill

- Scope: Community Addons
- Source: odoo/addons/l10n_in_ewaybill
- Dependencies: [[docs/Community Addons/l10n_in/l10n_in|l10n_in]]

## XML Artifacts (detected)

- Views: 5
- Actions: 2
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 4

## Detected Models

- `AccountMove`
- `l10n.in.ewaybill.type`
- `IrAttachment`
- `l10n.in.ewaybill`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Indian - E-waybill - Models and Relations
class AccountMove
class "l10n.in.ewaybill.type" as l10n_in_ewaybill_type
class IrAttachment
class "l10n.in.ewaybill" as l10n_in_ewaybill
class ResCompany
AccountMove --|> l10n_in_ewaybill : one2many
class "account.move" as account_move
l10n_in_ewaybill --> account_move : many2one
class "res.company" as res_company
l10n_in_ewaybill --> res_company : many2one
class "res.partner" as res_partner
l10n_in_ewaybill --> res_partner : many2one
l10n_in_ewaybill --> res_partner : many2one
l10n_in_ewaybill --> res_partner : many2one
l10n_in_ewaybill --> res_partner : many2one
l10n_in_ewaybill --> l10n_in_ewaybill_type : many2one
l10n_in_ewaybill --> res_partner : many2one
class "ir.attachment" as ir_attachment
l10n_in_ewaybill --> ir_attachment : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





