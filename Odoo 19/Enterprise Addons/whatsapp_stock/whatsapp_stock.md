<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Stock - WhatsApp

- Version: v19
- Category: enterprise
- Source: enterprise19/whatsapp_stock
- Dependencies: [[Odoo 19/Enterprise Addons/stock_enterprise/stock_enterprise|stock_enterprise]], [[Odoo 19/Enterprise Addons/whatsapp/whatsapp|whatsapp]]

## Summary

Send whatsapp messages when final stock move

## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ResCompany`
- `StockPicking`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Stock - WhatsApp - Models and Relations
class ResCompany
class StockPicking
class "whatsapp.template" as whatsapp_template
ResCompany --> whatsapp_template : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
