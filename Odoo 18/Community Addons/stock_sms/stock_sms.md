<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Stock - SMS

- Version: v18
- Category: community
- Source: odoo/addons/stock_sms
- Dependencies: [[Odoo 18/Community Addons/stock/stock|stock]], [[Odoo 18/Community Addons/sms/sms|sms]]

## Summary

Send text messages when final stock move

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 2

## Detected Models

- `Company`
- `Picking`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Stock - SMS - Models and Relations
class Company
class Picking
class "sms.template" as sms_template
Company --> sms_template : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
