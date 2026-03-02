<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Argentinean Electronic Invoicing

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_ar_edi
- Dependencies: [[Odoo 19/Community Addons/l10n_ar/l10n_ar|l10n_ar]], [[Odoo 19/Community Addons/certificate/certificate|certificate]]

## XML Artifacts (detected)

- Views: 11
- Actions: 3
- Menus: 3
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `AccountJournal`
- `AccountMove`
- `CertificateCertificate`
- `l10n_ar.afipws.connection`
- `ProductTemplate`
- `ResCompany`
- `ResCurrency`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Argentinean Electronic Invoicing - Models and Relations
class AccountJournal
class AccountMove
class CertificateCertificate
class "l10n_ar.afipws.connection" as l10n_ar_afipws_connection
class ProductTemplate
class ResCompany
class ResCurrency
class "res.company" as res_company
l10n_ar_afipws_connection --> res_company : many2one
ResCompany --|> l10n_ar_afipws_connection : one2many
class "certificate.key" as certificate_key
ResCompany --> certificate_key : many2one
class "certificate.certificate" as certificate_certificate
ResCompany --> certificate_certificate : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


