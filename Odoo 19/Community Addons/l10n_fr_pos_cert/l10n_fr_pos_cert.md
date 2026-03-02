<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# France - VAT Anti-Fraud Certification for Point of Sale (CGI 286 I-3 bis)

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/l10n_fr_pos_cert
- Dependencies: [[Odoo 19/Community Addons/l10n_fr_account/l10n_fr_account|l10n_fr_account]], [[Odoo 19/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

## XML Artifacts (detected)

- Views: 4
- Actions: 3
- Menus: 4
- Rules (ir.rule): 1
- Access CSV entries: 1

## Detected Models

- `account.sale.closing`
- `AccountFiscalPosition`
- `PosConfig`
- `PosSession`
- `PosOrder`
- `PosOrderLine`
- `ResCompany`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title France - VAT Anti-Fraud Certification for Point of Sale (CGI 286 I-3 bis) - Models and Relations
class "account.sale.closing" as account_sale_closing
class AccountFiscalPosition
class PosConfig
class PosSession
class PosOrder
class PosOrderLine
class ResCompany
class "res.company" as res_company
account_sale_closing --> res_company : many2one
class "pos.order" as pos_order
account_sale_closing --> pos_order : many2one
class "res.currency" as res_currency
account_sale_closing --> res_currency : many2one
PosOrder --> pos_order : many2one
class "ir.sequence" as ir_sequence
ResCompany --> ir_sequence : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


