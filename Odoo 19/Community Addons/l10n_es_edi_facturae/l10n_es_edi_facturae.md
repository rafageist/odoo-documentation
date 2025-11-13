<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Spain - Facturae EDI

- Version: v19
- Category: community
- Source: odoo19/addons/l10n_es_edi_facturae
- Dependencies: [[Odoo 19/Community Addons/certificate/certificate|certificate]], [[Odoo 19/Community Addons/l10n_es/l10n_es|l10n_es]]
## XML Artifacts (detected)

- Views: 10
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountMove`
- `AccountTax`
- `CertificateCertificate`
- `ResCompany`
- `l10n_es_edi_facturae.ac_role_type`
- `ResPartner`
- `UomUom`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Spain - Facturae EDI - Models and Relations
class AccountMove
class AccountTax
class CertificateCertificate
class ResCompany
class "l10n_es_edi_facturae.ac_role_type" as l10n_es_edi_facturae_ac_role_type
class ResPartner
class UomUom
class "ir.attachment" as ir_attachment
AccountMove --> ir_attachment : many2one
class "certificate.certificate" as certificate_certificate
ResCompany --|> certificate_certificate : one2many
ResPartner .. l10n_es_edi_facturae_ac_role_type : many2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
