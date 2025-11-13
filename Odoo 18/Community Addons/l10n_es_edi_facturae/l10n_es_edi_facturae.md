<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Spain - Facturae EDI

- Version: v18
- Category: community
- Source: odoo/addons/l10n_es_edi_facturae
- Dependencies: [[Odoo 18/Community Addons/certificate/certificate|certificate]], [[Odoo 18/Community Addons/l10n_es/l10n_es|l10n_es]]
## XML Artifacts (detected)

- Views: 11
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountMove`
- `AccountTax`
- `Certificate`
- `Company`
- `l10n_es_edi_facturae.ac_role_type`
- `Partner`
- `UoM`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Spain - Facturae EDI - Models and Relations
class AccountMove
class AccountTax
class Certificate
class Company
class "l10n_es_edi_facturae.ac_role_type" as l10n_es_edi_facturae_ac_role_type
class Partner
class UoM
class "ir.attachment" as ir_attachment
AccountMove --> ir_attachment : many2one
class "certificate.certificate" as certificate_certificate
Company --|> certificate_certificate : one2many
Partner .. l10n_es_edi_facturae_ac_role_type : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
