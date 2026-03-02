<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Taiwan - E-invoicing

- Scope: Community Addons
- Source: odoo/addons/l10n_tw_edi_ecpay
- Dependencies: [[docs/Community Addons/l10n_tw/l10n_tw|l10n_tw]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





