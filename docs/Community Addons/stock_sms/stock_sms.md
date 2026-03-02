<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Stock - SMS

- Scope: Community Addons
- Source: odoo/addons/stock_sms
- Dependencies: [[docs/Community Addons/stock/stock|stock]], [[docs/Community Addons/sms/sms|sms]]

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
!include ../../../templates/DiagramStyles.puml
title Stock - SMS - Models and Relations
class ResCompany
class StockPicking
class "sms.template" as sms_template
ResCompany --> sms_template : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




