<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Jordan E-Invoicing

- Version: v19
- Category: community
- Source: odoo19/addons/l10n_jo_edi
- Dependencies: [[Odoo 19/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]], [[Odoo 19/Community Addons/l10n_jo/l10n_jo|l10n_jo]]

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
!include ../../../Templates/DiagramStyles.puml
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

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
