<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Spain - SII EDI Suministro de Libros

- Version: v18
- Category: community
- Source: odoo/addons/l10n_es_edi_sii
- Dependencies: [[Odoo 18/Community Addons/certificate/certificate|certificate]], [[Odoo 18/Community Addons/l10n_es/l10n_es|l10n_es]], [[Odoo 18/Community Addons/account_edi/account_edi|account_edi]]
## XML Artifacts (detected)

- Views: 4
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountEdiFormat`
- `AccountMove`
- `Certificate`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Spain - SII EDI Suministro de Libros - Models and Relations
class AccountEdiFormat
class AccountMove
class Certificate
class ResCompany
class "certificate.certificate" as certificate_certificate
ResCompany --> certificate_certificate : many2one
ResCompany --|> certificate_certificate : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
