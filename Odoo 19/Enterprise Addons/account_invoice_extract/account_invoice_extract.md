<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Account Invoice Extract

- Version: v19
- Category: enterprise
- Source: enterprise19/account_invoice_extract
- Dependencies: [[Odoo 19/Enterprise Addons/account_extract/account_extract|account_extract]]

## Summary

Extract data from invoice scans to fill them automatically

## XML Artifacts (detected)

- Views: 2
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `account.move`
- `IrAttachment`
- `ResCompany`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Account Invoice Extract - Models and Relations
class "account.move" as account_move
class IrAttachment
class ResCompany
class ResPartner
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
