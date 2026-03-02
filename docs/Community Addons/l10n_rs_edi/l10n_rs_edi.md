<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Serbia - eFaktura E-invoicing

- Scope: Community Addons
- Source: odoo/addons/l10n_rs_edi
- Dependencies: [[docs/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]], [[docs/Community Addons/l10n_rs/l10n_rs|l10n_rs]]

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
!include ../../../templates/DiagramStyles.puml
title Serbia - eFaktura E-invoicing - Models and Relations
class AccountMove
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





