<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Indian - Accounting

- Version: v19
- Category: community
- Source: odoo19/addons/l10n_in
- Dependencies: [[Odoo 19/Community Addons/account_tax_python/account_tax_python|account_tax_python]], [[Odoo 19/Community Addons/base_vat/base_vat|base_vat]], [[Odoo 19/Community Addons/account_debit_note/account_debit_note|account_debit_note]], [[Odoo 19/Community Addons/account/account|account]], [[Odoo 19/Community Addons/iap/iap|iap]]
## XML Artifacts (detected)

- Views: 27
- Actions: 3
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 6

## Detected Models

- `AccountAccount`
- `AccountMove`
- `AccountMoveLine`
- `AccountPayment`
- `AccountTax`
- `ResCompany`
- `IapAccount`
- `l10n_in.pan.entity`
- `AccountReport`
- `l10n_in.section.alert`
- `l10n_in.port.code`
- `ProductTemplate`
- `ResCountryState`
- `ResPartner`
- `UomUom`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Indian - Accounting - Models and Relations
class AccountAccount
class AccountMove
class AccountMoveLine
class AccountPayment
class AccountTax
class ResCompany
class IapAccount
class "l10n_in.pan.entity" as l10n_in_pan_entity
class AccountReport
class "l10n_in.section.alert" as l10n_in_section_alert
class "l10n_in.port.code" as l10n_in_port_code
class ProductTemplate
class ResCountryState
class ResPartner
class UomUom
AccountAccount --> l10n_in_section_alert : many2one
class "res.country.state" as res_country_state
AccountMove --> res_country_state : many2one
AccountMove --> l10n_in_port_code : many2one
class "res.partner" as res_partner
AccountMove --> res_partner : many2one
class "account.move" as account_move
AccountMove --> account_move : many2one
class "account.payment" as account_payment
AccountMove --> account_payment : many2one
AccountMove --|> account_move : one2many
class "account.move.line" as account_move_line
AccountMove --|> account_move_line : one2many
AccountPayment --|> account_move : one2many
AccountTax --> l10n_in_section_alert : many2one
class "account.account" as account_account
ResCompany --> account_account : many2one
class "account.journal" as account_journal
ResCompany --> account_journal : many2one
l10n_in_pan_entity --|> res_partner : one2many
class "account.tax" as account_tax
l10n_in_section_alert --|> account_tax : one2many
class "account.report.line" as account_report_line
l10n_in_section_alert --> account_report_line : many2one
l10n_in_port_code --> res_country_state : many2one
ResPartner --> l10n_in_pan_entity : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
