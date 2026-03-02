<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Electronic Exports of Goods for Chile

- Scope: Enterprise Addons
- Source: enterprise/l10n_cl_edi_exports
- Dependencies: [[docs/Enterprise Addons/l10n_cl_edi/l10n_cl_edi|l10n_cl_edi]]

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
!include ../../../templates/DiagramStyles.puml
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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



