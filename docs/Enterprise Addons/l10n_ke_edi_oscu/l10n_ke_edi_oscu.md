
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Kenya eTIMS EDI Integration

- Scope: Enterprise Addons
- Source: enterprise/l10n_ke_edi_oscu
- Dependencies: [[docs/Community Addons/l10n_ke/l10n_ke|l10n_ke]], [[docs/Enterprise Addons/product_unspsc/product_unspsc|product_unspsc]]

## Summary


            Kenya eTIMS Device EDI Integration
        

## XML Artifacts (detected)

- Views: 17
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
- `ProductUnspscCode`
- `ResCompany`
- `ResPartner`
- `ResUsers`
- `UomUom`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Kenya eTIMS EDI Integration - Models and Relations
class AccountMove
class AccountMoveLine
class AccountTax
class "l10n_ke_edi_oscu.code" as l10n_ke_edi_oscu_code
class "l10n_ke_edi_oscu.notice" as l10n_ke_edi_oscu_notice
class ProductTemplate
class ProductProduct
class ProductUnspscCode
class ResCompany
class ResPartner
class ResUsers
class UomUom
AccountMove --> l10n_ke_edi_oscu_code : many2one
AccountMove --> l10n_ke_edi_oscu_code : many2one
AccountTax --> l10n_ke_edi_oscu_code : many2one
ProductTemplate --> l10n_ke_edi_oscu_code : many2one
class "res.country" as res_country
ProductTemplate --> res_country : many2one
ProductProduct --> l10n_ke_edi_oscu_code : many2one
ProductProduct --> res_country : many2one
ProductUnspscCode --> l10n_ke_edi_oscu_code : many2one
class "res.company" as res_company
ResUsers --|> res_company : one2many
UomUom --> l10n_ke_edi_oscu_code : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

