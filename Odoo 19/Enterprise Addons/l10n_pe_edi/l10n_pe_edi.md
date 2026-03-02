<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# EDI for Peru

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_pe_edi
- Dependencies: [[Odoo 19/Community Addons/iap/iap|iap]], [[Odoo 19/Community Addons/l10n_pe/l10n_pe|l10n_pe]], [[Odoo 19/Enterprise Addons/product_unspsc/product_unspsc|product_unspsc]], [[Odoo 19/Community Addons/account_edi/account_edi|account_edi]], [[Odoo 19/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]], [[Odoo 19/Community Addons/certificate/certificate|certificate]]

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
!include ../../../Templates/DiagramStyles.puml
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
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

