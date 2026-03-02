<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Jordan E-Invoicing

- Scope: Community Addons
- Source: odoo/addons/l10n_jo_edi
- Dependencies: [[docs/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]], [[docs/Community Addons/l10n_jo/l10n_jo|l10n_jo]]

## Summary

Electronic Invoicing for Jordan UBL 2.1

## XML Artifacts (detected)

- Views: 5
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `AccountTax`
- `IrAttachment`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Jordan E-Invoicing - Models and Relations
class AccountMove
class AccountTax
class IrAttachment
class ResCompany
class "ir.attachment" as ir_attachment
AccountMove --> ir_attachment : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





