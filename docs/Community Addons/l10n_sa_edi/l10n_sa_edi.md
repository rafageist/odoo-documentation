<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Saudi Arabia - E-invoicing

- Scope: Community Addons
- Source: odoo/addons/l10n_sa_edi
- Dependencies: [[docs/Community Addons/account_edi/account_edi|account_edi]], [[docs/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]], [[docs/Community Addons/l10n_sa/l10n_sa|l10n_sa]], [[docs/Community Addons/base_vat/base_vat|base_vat]], [[docs/Community Addons/certificate/certificate|certificate]]

## Summary


        E-Invoicing, Universal Business Language
    

## XML Artifacts (detected)

- Views: 8
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountEdiDocument`
- `AccountEdiFormat`
- `AccountJournal`
- `AccountMove`
- `AccountMoveLine`
- `AccountTax`
- `CertificateCertificate`
- `IrAttachment`
- `ResCompany`
- `ResPartner`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Saudi Arabia - E-invoicing - Models and Relations
class AccountEdiDocument
class AccountEdiFormat
class AccountJournal
class AccountMove
class AccountMoveLine
class AccountTax
class CertificateCertificate
class IrAttachment
class ResCompany
class ResPartner
class "certificate.certificate" as certificate_certificate
AccountJournal --> certificate_certificate : many2one
AccountJournal --> certificate_certificate : many2one
class "ir.sequence" as ir_sequence
AccountJournal --> ir_sequence : many2one
class "account.move" as account_move
AccountMove --> account_move : many2one
class "certificate.key" as certificate_key
ResCompany --> certificate_key : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





