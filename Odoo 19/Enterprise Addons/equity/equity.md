<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Equity

- Version: v19
- Category: enterprise
- Source: enterprise19/equity
- Dependencies: [[Odoo 19/Community Addons/portal/portal|portal]]

## Summary

Manage securities, transactions, and cap tables.

## XML Artifacts (detected)

- Views: 16
- Actions: 11
- Menus: 12
- Rules (ir.rule): 2
- Access CSV entries: 14

## Detected Models

- `equity.cap.table`
- `equity.security.class`
- `equity.transaction`
- `equity.ubo`
- `equity.valuation`
- `res.partner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Equity - Models and Relations
class "equity.cap.table" as equity_cap_table
class "equity.security.class" as equity_security_class
class "equity.transaction" as equity_transaction
class "equity.ubo" as equity_ubo
class "equity.valuation" as equity_valuation
class "res.partner" as res_partner
equity_cap_table --> res_partner : many2one
equity_cap_table --> res_partner : many2one
equity_cap_table --> equity_security_class : many2one
equity_transaction --> res_partner : many2one
class "res.currency" as res_currency
equity_transaction --> res_currency : many2one
equity_transaction --> equity_security_class : many2one
equity_transaction --> equity_security_class : many2one
equity_transaction --> res_partner : many2one
equity_transaction --> res_partner : many2one
class "ir.attachment" as ir_attachment
equity_transaction --|> ir_attachment : one2many
equity_ubo --> res_partner : many2one
equity_ubo --> res_partner : many2one
equity_ubo --|> ir_attachment : one2many
equity_valuation --> res_partner : many2one
equity_valuation --> res_currency : many2one
equity_valuation --|> ir_attachment : one2many
res_partner --|> equity_transaction : one2many
res_partner --> res_currency : many2one
res_partner --|> equity_ubo : one2many
res_partner --|> equity_ubo : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
