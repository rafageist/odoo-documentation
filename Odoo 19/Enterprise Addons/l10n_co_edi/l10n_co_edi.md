<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Electronic invoicing for Colombia with Carvajal

- Version: v19
- Category: enterprise
- Source: enterprise19/l10n_co_edi
- Dependencies: [[Odoo 19/Community Addons/account_edi/account_edi|account_edi]], [[Odoo 19/Community Addons/l10n_co/l10n_co|l10n_co]], [[Odoo 19/Enterprise Addons/product_unspsc/product_unspsc|product_unspsc]], [[Odoo 19/Community Addons/base_address_extended/base_address_extended|base_address_extended]]

## Summary

Colombian Localization for EDI documents

## XML Artifacts (detected)

- Views: 13
- Actions: 2
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `AccountEdiFormat`
- `AccountMove`
- `AccountMoveLine`
- `AccountJournal`
- `AccountTax`
- `l10n_co_edi.payment.option`
- `ProductTemplate`
- `UomUom`
- `ResCity`
- `ResCompany`
- `ResCountryState`
- `ResPartner`
- `l10n_co_edi.tax.type`
- `l10n_co_edi.type_code`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Electronic invoicing for Colombia with Carvajal - Models and Relations
class AccountEdiFormat
class AccountMove
class AccountMoveLine
class AccountJournal
class AccountTax
class "l10n_co_edi.payment.option" as l10n_co_edi_payment_option
class ProductTemplate
class UomUom
class ResCity
class ResCompany
class ResCountryState
class ResPartner
class "l10n_co_edi.tax.type" as l10n_co_edi_tax_type
class "l10n_co_edi.type_code" as l10n_co_edi_type_code
AccountMove --> l10n_co_edi_payment_option : many2one
AccountTax --> l10n_co_edi_tax_type : many2one
ResPartner .. l10n_co_edi_type_code : many2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
