<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Ecuadorian Point of Sale

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_ec_edi_pos
- Dependencies: [[Odoo 18/Enterprise Addons/l10n_ec_edi/l10n_ec_edi|l10n_ec_edi]], [[Odoo 18/Community Addons/point_of_sale/point_of_sale|point_of_sale]]
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
- `PoSPaymentMethod`
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
class PoSPaymentMethod
class PosSession
class ResPartner
class "l10n_ec.sri.payment" as l10n_ec_sri_payment
PoSPaymentMethod --> l10n_ec_sri_payment : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
