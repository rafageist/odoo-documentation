<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Romania - E-invoicing

- Scope: Community Addons
- Source: odoo/addons/l10n_ro_edi
- Dependencies: [[docs/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]], [[docs/Community Addons/l10n_ro/l10n_ro|l10n_ro]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





