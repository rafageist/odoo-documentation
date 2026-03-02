<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Import/Export electronic invoices with UBL/CII

- Scope: Community Addons
- Source: odoo/addons/account_edi_ubl_cii
- Dependencies: [[docs/Community Addons/account/account|account]]

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `AccountTax`
- `IrActionsReport`
- `ResPartner`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Import/Export electronic invoices with UBL/CII - Models and Relations
class AccountMove
class AccountTax
class IrActionsReport
class ResPartner
class "ir.attachment" as ir_attachment
AccountMove --> ir_attachment : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





