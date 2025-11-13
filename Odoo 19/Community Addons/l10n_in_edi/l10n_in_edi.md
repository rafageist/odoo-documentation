<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Indian - E-invoicing

- Version: v19
- Category: community
- Source: odoo19/addons/l10n_in_edi
- Dependencies: [[Odoo 19/Community Addons/account_edi/account_edi|account_edi]], [[Odoo 19/Community Addons/l10n_in/l10n_in|l10n_in]]
## XML Artifacts (detected)

- Views: 6
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `IrAttachment`
- `ResCompany`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Indian - E-invoicing - Models and Relations
class AccountMove
class AccountMoveLine
class IrAttachment
class ResCompany
class ResPartner
class "ir.attachment" as ir_attachment
AccountMove --> ir_attachment : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
