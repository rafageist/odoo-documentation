<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Brazilian Accounting EDI for stock

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_br_edi_stock
- Dependencies: [[Odoo 19/Enterprise Addons/l10n_br_edi/l10n_br_edi|l10n_br_edi]], [[Odoo 19/Community Addons/sale_stock/sale_stock|sale_stock]]
## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `SaleOrder`
- `StockPackage`
- `StockPackageType`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Brazilian Accounting EDI for stock - Models and Relations
class AccountMove
class SaleOrder
class StockPackage
class StockPackageType
class "stock.package" as stock_package
AccountMove .. stock_package : many2many
AccountMove --|> stock_package : one2many
class "account.move" as account_move
StockPackage --> account_move : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
