<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Uruguay - Electronic Invoice

- Scope: Enterprise Addons
- Source: enterprise/l10n_uy_edi
- Dependencies: [[docs/Community Addons/l10n_uy/l10n_uy|l10n_uy]]

## XML Artifacts (detected)

- Views: 11
- Actions: 1
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 2

## Detected Models

- `AccountJournal`
- `AccountMove`
- `AccountMoveLine`
- `L10nLatamDocumentType`
- `l10n_uy_edi.addenda`
- `l10n_uy_edi.document`
- `ResCompany`
- `ResPartner`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Uruguay - Electronic Invoice - Models and Relations
class AccountJournal
class AccountMove
class AccountMoveLine
class L10nLatamDocumentType
class "l10n_uy_edi.addenda" as l10n_uy_edi_addenda
class "l10n_uy_edi.document" as l10n_uy_edi_document
class ResCompany
class ResPartner
AccountMove --> l10n_uy_edi_document : many2one
AccountMove .. l10n_uy_edi_addenda : many2many
class "ir.attachment" as ir_attachment
AccountMove --> ir_attachment : many2one
AccountMoveLine .. l10n_uy_edi_addenda : many2many
class "res.company" as res_company
l10n_uy_edi_addenda --> res_company : many2one
class "account.move" as account_move
l10n_uy_edi_document --> account_move : many2one
l10n_uy_edi_document --> ir_attachment : many2one
class "l10n_latam.document.type" as l10n_latam_document_type
l10n_uy_edi_document --> l10n_latam_document_type : many2one
l10n_uy_edi_document --> res_company : many2one
class "res.partner" as res_partner
l10n_uy_edi_document --> res_partner : many2one
ResCompany --|> l10n_uy_edi_addenda : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



