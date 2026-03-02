<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Brazilian - Accounting

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/l10n_br
- Dependencies: [[Odoo 19/Community Addons/account/account|account]], [[Odoo 19/Community Addons/account_qr_code_emv/account_qr_code_emv|account_qr_code_emv]], [[Odoo 19/Community Addons/base_address_extended/base_address_extended|base_address_extended]], [[Odoo 19/Community Addons/l10n_latam_base/l10n_latam_base|l10n_latam_base]], [[Odoo 19/Community Addons/l10n_latam_invoice_document/l10n_latam_invoice_document|l10n_latam_invoice_document]]

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
!include ../../../Templates/DiagramStyles.puml
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


