<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# LATAM Document

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/l10n_latam_invoice_document
- Dependencies: [[Odoo 19/Community Addons/account/account|account]], [[Odoo 19/Community Addons/account_debit_note/account_debit_note|account_debit_note]]

## Summary

LATAM Document Types

## XML Artifacts (detected)

- Views: 10
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountJournal`
- `AccountMove`
- `AccountMoveLine`
- `l10n_latam.document.type`
- `ResCompany`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title LATAM Document - Models and Relations
class AccountJournal
class AccountMove
class AccountMoveLine
class "l10n_latam.document.type" as l10n_latam_document_type
class ResCompany
AccountMove .. l10n_latam_document_type : many2many
AccountMove --> l10n_latam_document_type : many2one
class "res.country" as res_country
l10n_latam_document_type --> res_country : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


