<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Argentina - Payment Withholdings

- Scope: Community Addons
- Source: odoo/addons/l10n_ar_withholding
- Dependencies: [[docs/Community Addons/l10n_ar/l10n_ar|l10n_ar]], [[docs/Community Addons/l10n_latam_check/l10n_latam_check|l10n_latam_check]]

## XML Artifacts (detected)

- Views: 7
- Actions: 1
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 8

## Detected Models

- `AccountMove`
- `AccountPayment`
- `AccountTax`
- `l10n_ar.earnings.scale`
- `l10n_ar.earnings.scale.line`
- `l10n_ar.partner.tax`
- `ResCompany`
- `ResPartner`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Argentina - Payment Withholdings - Models and Relations
class AccountMove
class AccountPayment
class AccountTax
class "l10n_ar.earnings.scale" as l10n_ar_earnings_scale
class "l10n_ar.earnings.scale.line" as l10n_ar_earnings_scale_line
class "l10n_ar.partner.tax" as l10n_ar_partner_tax
class ResCompany
class ResPartner
class "account.move.line" as account_move_line
AccountMove --|> account_move_line : one2many
class "ir.sequence" as ir_sequence
AccountTax --> ir_sequence : many2one
class "res.country.state" as res_country_state
AccountTax --> res_country_state : many2one
AccountTax --> l10n_ar_earnings_scale : many2one
l10n_ar_earnings_scale --|> l10n_ar_earnings_scale_line : one2many
l10n_ar_earnings_scale_line --> l10n_ar_earnings_scale : many2one
class "res.currency" as res_currency
l10n_ar_earnings_scale_line --> res_currency : many2one
class "res.partner" as res_partner
l10n_ar_partner_tax --> res_partner : many2one
class "account.tax" as account_tax
l10n_ar_partner_tax --> account_tax : many2one
class "account.account" as account_account
ResCompany --> account_account : many2one
ResPartner --|> l10n_ar_partner_tax : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





