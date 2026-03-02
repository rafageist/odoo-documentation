<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Guatemala - E-Invoicing

- Scope: Enterprise Addons
- Source: enterprise/l10n_gt_edi
- Dependencies: [[docs/Community Addons/account_debit_note/account_debit_note|account_debit_note]], [[docs/Community Addons/account_tax_python/account_tax_python|account_tax_python]], [[docs/Community Addons/l10n_gt/l10n_gt|l10n_gt]], [[docs/Community Addons/l10n_latam_base/l10n_latam_base|l10n_latam_base]]

## XML Artifacts (detected)

- Views: 10
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `AccountMove`
- `AccountTax`
- `l10n_gt_edi.document`
- `l10n_gt_edi.phrase`
- `ResCompany`
- `ResPartner`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Guatemala - E-Invoicing - Models and Relations
class AccountMove
class AccountTax
class "l10n_gt_edi.document" as l10n_gt_edi_document
class "l10n_gt_edi.phrase" as l10n_gt_edi_phrase
class ResCompany
class ResPartner
AccountMove --|> l10n_gt_edi_document : one2many
AccountMove .. l10n_gt_edi_phrase : many2many
class "res.partner" as res_partner
AccountMove --> res_partner : many2one
class "ir.attachment" as ir_attachment
AccountMove --> ir_attachment : many2one
class "account.move" as account_move
l10n_gt_edi_document --> account_move : many2one
l10n_gt_edi_document --> ir_attachment : many2one
ResPartner .. l10n_gt_edi_phrase : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



