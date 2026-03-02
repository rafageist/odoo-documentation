<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Türkiye - Nilvera

- Scope: Community Addons
- Source: odoo/addons/l10n_tr_nilvera
- Dependencies: [[docs/Community Addons/l10n_tr/l10n_tr|l10n_tr]]

## XML Artifacts (detected)

- Views: 2
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `AccountJournal`
- `l10n_tr.nilvera.alias`
- `ResCompany`
- `res.partner`
- `Uom`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Türkiye - Nilvera - Models and Relations
class AccountJournal
class "l10n_tr.nilvera.alias" as l10n_tr_nilvera_alias
class ResCompany
class "res.partner" as res_partner
class Uom
l10n_tr_nilvera_alias --> res_partner : many2one
class "account.journal" as account_journal
ResCompany --> account_journal : many2one
res_partner --> l10n_tr_nilvera_alias : many2one
res_partner --|> l10n_tr_nilvera_alias : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





