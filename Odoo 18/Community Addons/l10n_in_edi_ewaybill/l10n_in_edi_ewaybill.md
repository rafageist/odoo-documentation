<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Indian - E-waybill

- Version: v18
- Category: community
- Source: odoo/addons/l10n_in_edi_ewaybill
- Dependencies: [[Odoo 18/Community Addons/l10n_in_edi/l10n_in_edi|l10n_in_edi]]
## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountEdiFormat`
- `AccountMove`
- `l10n.in.ewaybill.type`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Indian - E-waybill - Models and Relations
class AccountEdiFormat
class AccountMove
class "l10n.in.ewaybill.type" as l10n_in_ewaybill_type
class ResCompany
AccountMove --> l10n_in_ewaybill_type : many2one
class "res.partner" as res_partner
AccountMove --> res_partner : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
