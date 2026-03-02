
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Stock - WhatsApp

- Scope: Enterprise Addons
- Source: enterprise/whatsapp_stock
- Dependencies: [[docs/Enterprise Addons/stock_enterprise/stock_enterprise|stock_enterprise]], [[docs/Enterprise Addons/whatsapp/whatsapp|whatsapp]]

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
!include ../../../templates/DiagramStyles.puml
title Stock - WhatsApp - Models and Relations
class ResCompany
class StockPicking
class "whatsapp.template" as whatsapp_template
ResCompany --> whatsapp_template : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

