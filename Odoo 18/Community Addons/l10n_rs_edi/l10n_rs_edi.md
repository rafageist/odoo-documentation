<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Serbia - eFaktura E-invoicing

- Version: v18
- Category: community
- Source: odoo/addons/l10n_rs_edi
- Dependencies: [[Odoo 18/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]], [[Odoo 18/Community Addons/l10n_rs/l10n_rs|l10n_rs]]

## Summary

E-Invoice implementation for Serbia

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `ResCompany`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Serbia - eFaktura E-invoicing - Models and Relations
class AccountMove
class ResCompany
class ResPartner
class "ir.attachment" as ir_attachment
AccountMove --> ir_attachment : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
