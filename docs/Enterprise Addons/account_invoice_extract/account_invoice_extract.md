<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Account Invoice Extract

- Scope: Enterprise Addons
- Source: enterprise/account_invoice_extract
- Dependencies: [[docs/Enterprise Addons/account_extract/account_extract|account_extract]]

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
!include ../../../templates/DiagramStyles.puml
title Account Invoice Extract - Models and Relations
class "account.move" as account_move
class IrAttachment
class ResCompany
class ResPartner
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



