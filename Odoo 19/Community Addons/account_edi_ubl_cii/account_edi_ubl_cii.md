<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Import/Export electronic invoices with UBL/CII

- Version: v19
- Category: community
- Source: odoo19/addons/account_edi_ubl_cii
- Dependencies: [[Odoo 19/Community Addons/account/account|account]]
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
!include ../../../Templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
