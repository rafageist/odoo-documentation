
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# EDI for Peru

- Scope: Enterprise Addons
- Source: enterprise/l10n_pe_edi
- Dependencies: [[docs/Community Addons/iap/iap|iap]], [[docs/Community Addons/l10n_pe/l10n_pe|l10n_pe]], [[docs/Enterprise Addons/product_unspsc/product_unspsc|product_unspsc]], [[docs/Community Addons/account_edi/account_edi|account_edi]], [[docs/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]], [[docs/Community Addons/certificate/certificate|certificate]]

## Summary

Electronic Invoicing for Peru (OSE method) and UBL 2.1

## XML Artifacts (detected)

- Views: 10
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountEdiDocument`
- `AccountEdiFormat`
- `AccountJournal`
- `AccountMove`
- `AccountMoveLine`
- `AccountTax`
- `AccountTaxGroup`
- `ProductTemplate`
- `ResCompany`
- `UomUom`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title EDI for Peru - Models and Relations
class AccountEdiDocument
class AccountEdiFormat
class AccountJournal
class AccountMove
class AccountMoveLine
class AccountTax
class AccountTaxGroup
class ProductTemplate
class ResCompany
class UomUom
class "certificate.certificate" as certificate_certificate
ResCompany --> certificate_certificate : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->


