<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# France - VAT Anti-Fraud Certification for Point of Sale (CGI 286 I-3 bis)

- Version: v18
- Category: community
- Source: odoo/addons/l10n_fr_pos_cert
- Dependencies: [[Odoo 18/Community Addons/l10n_fr_account/l10n_fr_account|l10n_fr_account]], [[Odoo 18/Community Addons/point_of_sale/point_of_sale|point_of_sale]]
## XML Artifacts (detected)

- Views: 4
- Actions: 3
- Menus: 4
- Rules (ir.rule): 1
- Access CSV entries: 1

## Detected Models

- `account.sale.closing`
- `AccountFiscalPosition`
- `pos_config`
- `pos_session`
- `pos_order`
- `PosOrderLine`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title France - VAT Anti-Fraud Certification for Point of Sale (CGI 286 I-3 bis) - Models and Relations
class "account.sale.closing" as account_sale_closing
class AccountFiscalPosition
class pos_config
class pos_session
class pos_order
class PosOrderLine
class ResCompany
class "res.company" as res_company
account_sale_closing --> res_company : many2one
class "pos.order" as pos_order
account_sale_closing --> pos_order : many2one
class "res.currency" as res_currency
account_sale_closing --> res_currency : many2one
pos_order --> pos_order : many2one
class "ir.sequence" as ir_sequence
ResCompany --> ir_sequence : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
