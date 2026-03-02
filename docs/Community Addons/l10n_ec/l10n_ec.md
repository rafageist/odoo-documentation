<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Ecuadorian Accounting

- Scope: Community Addons
- Source: odoo/addons/l10n_ec
- Dependencies: base (not documented), [[docs/Community Addons/base_iban/base_iban|base_iban]], [[docs/Community Addons/account_debit_note/account_debit_note|account_debit_note]], [[docs/Community Addons/l10n_latam_invoice_document/l10n_latam_invoice_document|l10n_latam_invoice_document]], [[docs/Community Addons/l10n_latam_base/l10n_latam_base|l10n_latam_base]], [[docs/Community Addons/account/account|account]]

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
- `L10n_LatamDocumentType`
- `ResCompany`
- `ResPartner`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Ecuadorian Accounting - Models and Relations
class AccountJournal
class AccountMove
class AccountTax
class AccountTaxGroup
class "l10n_ec.sri.payment" as l10n_ec_sri_payment
class L10n_LatamDocumentType
class ResCompany
class ResPartner
class "res.partner" as res_partner
AccountJournal --> res_partner : many2one
AccountMove --> l10n_ec_sri_payment : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





