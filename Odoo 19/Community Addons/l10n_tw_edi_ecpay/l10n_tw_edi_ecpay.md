<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Taiwan - E-invoicing

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/l10n_tw_edi_ecpay
- Dependencies: [[Odoo 19/Community Addons/l10n_tw/l10n_tw|l10n_tw]]

## Summary

E-invoicing using ECpay

## XML Artifacts (detected)

- Views: 6
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 6

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `AccountTax`
- `ResCompany`
- `ResPartner`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Taiwan - E-invoicing - Models and Relations
class AccountMove
class AccountMoveLine
class AccountTax
class ResCompany
class ResPartner
class "ir.attachment" as ir_attachment
AccountMove --> ir_attachment : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


