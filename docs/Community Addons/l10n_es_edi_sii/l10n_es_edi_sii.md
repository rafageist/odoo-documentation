<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Spain - SII EDI Suministro de Libros

- Scope: Community Addons
- Source: odoo/addons/l10n_es_edi_sii
- Dependencies: [[docs/Community Addons/certificate/certificate|certificate]], [[docs/Community Addons/l10n_es/l10n_es|l10n_es]], [[docs/Community Addons/account_edi/account_edi|account_edi]]

## XML Artifacts (detected)

- Views: 4
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountEdiFormat`
- `AccountMove`
- `CertificateCertificate`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Spain - SII EDI Suministro de Libros - Models and Relations
class AccountEdiFormat
class AccountMove
class CertificateCertificate
class ResCompany
class "certificate.certificate" as certificate_certificate
ResCompany --> certificate_certificate : many2one
ResCompany --|> certificate_certificate : one2many
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





