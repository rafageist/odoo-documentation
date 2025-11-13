<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Indonesian - Accounting

- Version: v18
- Category: community
- Source: odoo/addons/l10n_id
- Dependencies: [[Odoo 18/Community Addons/account/account|account]], [[Odoo 18/Community Addons/base_iban/base_iban|base_iban]], [[Odoo 18/Community Addons/base_vat/base_vat|base_vat]]
## XML Artifacts (detected)

- Views: 1
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountMove`
- `l10n_id.qris.transaction`
- `ResBank`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Indonesian - Accounting - Models and Relations
class AccountMove
class "l10n_id.qris.transaction" as l10n_id_qris_transaction
class ResBank
AccountMove .. l10n_id_qris_transaction : many2many
class "res.partner.bank" as res_partner_bank
l10n_id_qris_transaction --> res_partner_bank : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
