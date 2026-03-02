<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Ecuadorian Point of Sale

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_ec_edi_pos
- Dependencies: [[Odoo 19/Enterprise Addons/l10n_ec_edi/l10n_ec_edi|l10n_ec_edi]], [[Odoo 19/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountEdiFormat`
- `account.move`
- `l10n_latam.identification.type`
- `PosConfig`
- `PosOrder`
- `PosPaymentMethod`
- `PosSession`
- `ResPartner`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Ecuadorian Point of Sale - Models and Relations
class AccountEdiFormat
class "account.move" as account_move
class "l10n_latam.identification.type" as l10n_latam_identification_type
class PosConfig
class PosOrder
class PosPaymentMethod
class PosSession
class ResPartner
class "l10n_ec.sri.payment" as l10n_ec_sri_payment
PosPaymentMethod --> l10n_ec_sri_payment : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

