<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Indonesian - Accounting

- Version: v19
- Category: community
- Source: odoo19/addons/l10n_id
- Dependencies: [[Odoo 19/Community Addons/account/account|account]], [[Odoo 19/Community Addons/base_iban/base_iban|base_iban]], [[Odoo 19/Community Addons/base_vat/base_vat|base_vat]]
## XML Artifacts (detected)

- Views: 1
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountMove`
- `l10n_id.qris.transaction`
- `ResPartnerBank`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Indonesian - Accounting - Models and Relations
class AccountMove
class "l10n_id.qris.transaction" as l10n_id_qris_transaction
class ResPartnerBank
AccountMove .. l10n_id_qris_transaction : many2many
class "res.partner.bank" as res_partner_bank
l10n_id_qris_transaction --> res_partner_bank : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
