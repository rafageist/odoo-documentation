<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Spain - Veri*Factu

- Scope: Community Addons
- Source: odoo/addons/l10n_es_edi_verifactu
- Dependencies: [[docs/Community Addons/l10n_es/l10n_es|l10n_es]]

## Summary

Module for sending Spanish Veri*Factu XML to the AEAT

## XML Artifacts (detected)

- Views: 12
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountMove`
- `AccountTax`
- `Certificate`
- `ResCompany`
- `ResPartner`
- `l10n_es_edi_verifactu.document`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Spain - Veri*Factu - Models and Relations
class AccountMove
class AccountTax
class Certificate
class ResCompany
class ResPartner
class "l10n_es_edi_verifactu.document" as l10n_es_edi_verifactu_document
AccountMove --|> l10n_es_edi_verifactu_document : one2many
class "account.move" as account_move
AccountMove --> account_move : many2one
AccountMove --|> account_move : one2many
class "certificate.certificate" as certificate_certificate
ResCompany --|> certificate_certificate : one2many
class "ir.sequence" as ir_sequence
ResCompany --> ir_sequence : many2one
class "res.company" as res_company
l10n_es_edi_verifactu_document --> res_company : many2one
l10n_es_edi_verifactu_document --> account_move : many2one
class "ir.attachment" as ir_attachment
l10n_es_edi_verifactu_document --> ir_attachment : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





