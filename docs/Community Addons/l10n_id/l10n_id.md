<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Indonesian - Accounting

- Scope: Community Addons
- Source: odoo/addons/l10n_id
- Dependencies: [[docs/Community Addons/account/account|account]], [[docs/Community Addons/base_iban/base_iban|base_iban]], [[docs/Community Addons/base_vat/base_vat|base_vat]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





