<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Indian - E-invoicing

- Scope: Community Addons
- Source: odoo/addons/l10n_in_edi
- Dependencies: [[docs/Community Addons/account_edi/account_edi|account_edi]], [[docs/Community Addons/l10n_in/l10n_in|l10n_in]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





