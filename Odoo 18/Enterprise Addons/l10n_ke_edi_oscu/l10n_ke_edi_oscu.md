<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Kenya eTIMS EDI Integration

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_ke_edi_oscu
- Dependencies: [[Odoo 18/Community Addons/l10n_ke/l10n_ke|l10n_ke]], [[Odoo 18/Enterprise Addons/product_unspsc/product_unspsc|product_unspsc]]

## Summary


            Kenya eTIMS Device EDI Integration
        

## XML Artifacts (detected)

- Views: 19
- Actions: 2
- Menus: 3
- Rules (ir.rule): 0
- Access CSV entries: 4

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `AccountTax`
- `l10n_ke_edi_oscu.code`
- `l10n_ke_edi_oscu.notice`
- `ProductTemplate`
- `ProductProduct`
- `ProductCode`
- `ResCompany`
- `ResPartner`
- `Users`
- `Uom`
- `UoMCategory`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Kenya eTIMS EDI Integration - Models and Relations
class AccountMove
class AccountMoveLine
class AccountTax
class "l10n_ke_edi_oscu.code" as l10n_ke_edi_oscu_code
class "l10n_ke_edi_oscu.notice" as l10n_ke_edi_oscu_notice
class ProductTemplate
class ProductProduct
class ProductCode
class ResCompany
class ResPartner
class Users
class Uom
class UoMCategory
AccountMove --> l10n_ke_edi_oscu_code : many2one
AccountMove --> l10n_ke_edi_oscu_code : many2one
class "ir.attachment" as ir_attachment
AccountMove --> ir_attachment : many2one
AccountTax --> l10n_ke_edi_oscu_code : many2one
ProductTemplate --> l10n_ke_edi_oscu_code : many2one
class "res.country" as res_country
ProductTemplate --> res_country : many2one
ProductProduct --> l10n_ke_edi_oscu_code : many2one
ProductProduct --> res_country : many2one
ProductCode --> l10n_ke_edi_oscu_code : many2one
class "res.company" as res_company
Users --|> res_company : one2many
Uom --> l10n_ke_edi_oscu_code : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
