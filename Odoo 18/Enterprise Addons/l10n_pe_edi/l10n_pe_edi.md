<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# EDI for Peru

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_pe_edi
- Dependencies: [[Odoo 18/Community Addons/iap/iap|iap]], [[Odoo 18/Community Addons/l10n_pe/l10n_pe|l10n_pe]], [[Odoo 18/Enterprise Addons/product_unspsc/product_unspsc|product_unspsc]], [[Odoo 18/Community Addons/account_edi/account_edi|account_edi]], [[Odoo 18/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]], [[Odoo 18/Community Addons/certificate/certificate|certificate]]

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
- `ProductUoM`


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
class ProductUoM
class "certificate.certificate" as certificate_certificate
ResCompany --> certificate_certificate : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
