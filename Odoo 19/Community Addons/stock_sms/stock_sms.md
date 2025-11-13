<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Stock - SMS

- Version: v19
- Category: community
- Source: odoo19/addons/stock_sms
- Dependencies: [[Odoo 19/Community Addons/stock/stock|stock]], [[Odoo 19/Community Addons/sms/sms|sms]]

## Summary

Send text messages when final stock move

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 2

## Detected Models

- `ResCompany`
- `StockPicking`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Stock - SMS - Models and Relations
class ResCompany
class StockPicking
class "sms.template" as sms_template
ResCompany --> sms_template : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
