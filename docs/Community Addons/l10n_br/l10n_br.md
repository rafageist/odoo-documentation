<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Brazilian - Accounting

- Scope: Community Addons
- Source: odoo/addons/l10n_br
- Dependencies: [[docs/Community Addons/account/account|account]], [[docs/Community Addons/account_qr_code_emv/account_qr_code_emv|account_qr_code_emv]], [[docs/Community Addons/base_address_extended/base_address_extended|base_address_extended]], [[docs/Community Addons/l10n_latam_base/l10n_latam_base|l10n_latam_base]], [[docs/Community Addons/l10n_latam_invoice_document/l10n_latam_invoice_document|l10n_latam_invoice_document]]

## XML Artifacts (detected)

- Views: 7
- Actions: 0
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountTax`
- `AccountFiscalPosition`
- `AccountJournal`
- `AccountMove`
- `l10n_br.zip.range`
- `ResCity`
- `ResCompany`
- `ResPartner`
- `ResPartnerBank`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Brazilian - Accounting - Models and Relations
class AccountTax
class AccountFiscalPosition
class AccountJournal
class AccountMove
class "l10n_br.zip.range" as l10n_br_zip_range
class ResCity
class ResCompany
class ResPartner
class ResPartnerBank
class "res.city" as res_city
l10n_br_zip_range --> res_city : many2one
ResCity --|> l10n_br_zip_range : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





