<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Romania - E-invoicing

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/l10n_ro_edi
- Dependencies: [[Odoo 19/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]], [[Odoo 19/Community Addons/l10n_ro/l10n_ro|l10n_ro]]

## Summary

E-Invoice implementation for Romania

## XML Artifacts (detected)

- Views: 6
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountMove`
- `l10n_ro_edi.document`
- `ResCompany`
- `ResPartner`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Romania - E-invoicing - Models and Relations
class AccountMove
class "l10n_ro_edi.document" as l10n_ro_edi_document
class ResCompany
class ResPartner
AccountMove --|> l10n_ro_edi_document : one2many
class "account.move" as account_move
l10n_ro_edi_document --> account_move : many2one
class "account.journal" as account_journal
ResCompany --> account_journal : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


