<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Spain - TicketBAI

- Scope: Community Addons
- Source: odoo/addons/l10n_es_edi_tbai
- Dependencies: [[docs/Community Addons/l10n_es/l10n_es|l10n_es]], [[docs/Community Addons/certificate/certificate|certificate]]

## XML Artifacts (detected)

- Views: 6
- Actions: 1
- Menus: 3
- Rules (ir.rule): 1
- Access CSV entries: 1

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `CertificateCertificate`
- `l10n_es_edi_tbai.document`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Spain - TicketBAI - Models and Relations
class AccountMove
class AccountMoveLine
class CertificateCertificate
class "l10n_es_edi_tbai.document" as l10n_es_edi_tbai_document
class ResCompany
AccountMove --> l10n_es_edi_tbai_document : many2one
AccountMove --> l10n_es_edi_tbai_document : many2one
class "account.move" as account_move
AccountMove .. account_move : many2many
class "ir.attachment" as ir_attachment
l10n_es_edi_tbai_document --> ir_attachment : many2one
class "res.company" as res_company
l10n_es_edi_tbai_document --> res_company : many2one
class "certificate.certificate" as certificate_certificate
ResCompany --> certificate_certificate : many2one
ResCompany --|> certificate_certificate : one2many
class "ir.sequence" as ir_sequence
ResCompany --> ir_sequence : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





