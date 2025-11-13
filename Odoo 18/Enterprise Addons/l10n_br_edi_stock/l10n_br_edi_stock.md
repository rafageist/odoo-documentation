<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Brazilian Accounting EDI for stock

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_br_edi_stock
- Dependencies: [[Odoo 18/Enterprise Addons/l10n_br_edi/l10n_br_edi|l10n_br_edi]], [[Odoo 18/Community Addons/sale_stock/sale_stock|sale_stock]]
## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `SaleOrder`
- `StockPackageType`
- `StockQuantPackage`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Brazilian Accounting EDI for stock - Models and Relations
class AccountMove
class SaleOrder
class StockPackageType
class StockQuantPackage
class "stock.quant.package" as stock_quant_package
AccountMove .. stock_quant_package : many2many
AccountMove --|> stock_quant_package : one2many
class "account.move" as account_move
StockQuantPackage --> account_move : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
