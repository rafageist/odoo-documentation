<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Ecuadorian Accounting

- Version: v18
- Category: community
- Source: odoo/addons/l10n_ec
- Dependencies: base (not documented), [[Odoo 18/Community Addons/base_iban/base_iban|base_iban]], [[Odoo 18/Community Addons/account_debit_note/account_debit_note|account_debit_note]], [[Odoo 18/Community Addons/l10n_latam_invoice_document/l10n_latam_invoice_document|l10n_latam_invoice_document]], [[Odoo 18/Community Addons/l10n_latam_base/l10n_latam_base|l10n_latam_base]], [[Odoo 18/Community Addons/account/account|account]]
## XML Artifacts (detected)

- Views: 7
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `AccountJournal`
- `AccountMove`
- `AccountTax`
- `AccountTaxGroup`
- `l10n_ec.sri.payment`
- `L10nLatamDocumentType`
- `ResCompany`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Ecuadorian Accounting - Models and Relations
class AccountJournal
class AccountMove
class AccountTax
class AccountTaxGroup
class "l10n_ec.sri.payment" as l10n_ec_sri_payment
class L10nLatamDocumentType
class ResCompany
class ResPartner
class "res.partner" as res_partner
AccountJournal --> res_partner : many2one
AccountMove --> l10n_ec_sri_payment : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
