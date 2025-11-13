<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Brazilian Accounting EDI for POS

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_br_edi_pos
- Dependencies: [[Odoo 19/Enterprise Addons/l10n_br_edi/l10n_br_edi|l10n_br_edi]], [[Odoo 19/Community Addons/point_of_sale/point_of_sale|point_of_sale]]
## XML Artifacts (detected)

- Views: 5
- Actions: 2
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `AccountTax`
- `l10n_latam.identification.type`
- `PosConfig`
- `pos.order`
- `POSPaymentMethod`
- `PosSession`
- `ProductTemplate`
- `ResCompany`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Brazilian Accounting EDI for POS - Models and Relations
class AccountMove
class AccountTax
class "l10n_latam.identification.type" as l10n_latam_identification_type
class PosConfig
class "pos.order" as pos_order
class POSPaymentMethod
class PosSession
class ProductTemplate
class ResCompany
class ResPartner
class "res.users" as res_users
pos_order --> res_users : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
