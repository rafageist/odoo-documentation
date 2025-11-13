<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Electronic Exports of Goods for Chile

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_cl_edi_exports
- Dependencies: [[Odoo 19/Enterprise Addons/l10n_cl_edi/l10n_cl_edi|l10n_cl_edi]]
## XML Artifacts (detected)

- Views: 3
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountMove`
- `l10n_cl.customs_port`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Electronic Exports of Goods for Chile - Models and Relations
class AccountMove
class "l10n_cl.customs_port" as l10n_cl_customs_port
AccountMove --> l10n_cl_customs_port : many2one
AccountMove --> l10n_cl_customs_port : many2one
class "res.country" as res_country
AccountMove --> res_country : many2one
l10n_cl_customs_port --> res_country : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
