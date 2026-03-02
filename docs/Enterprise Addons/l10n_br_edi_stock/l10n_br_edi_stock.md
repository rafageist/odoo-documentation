
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Brazilian Accounting EDI for stock

- Scope: Enterprise Addons
- Source: enterprise/l10n_br_edi_stock
- Dependencies: [[docs/Enterprise Addons/l10n_br_edi/l10n_br_edi|l10n_br_edi]], [[docs/Community Addons/sale_stock/sale_stock|sale_stock]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

