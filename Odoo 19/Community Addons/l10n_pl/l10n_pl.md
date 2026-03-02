<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Poland - Accounting

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/l10n_pl
- Dependencies: [[Odoo 19/Community Addons/base_iban/base_iban|base_iban]], [[Odoo 19/Community Addons/base_vat/base_vat|base_vat]], [[Odoo 19/Community Addons/account/account|account]], [[Odoo 19/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]]

## XML Artifacts (detected)

- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountMove`
- `l10n_pl.l10n_pl_tax_office`
- `ProductTemplate`
- `ResCompany`
- `ResPartner`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Poland - Accounting - Models and Relations
class AccountMove
class "l10n_pl.l10n_pl_tax_office" as l10n_pl_l10n_pl_tax_office
class ProductTemplate
class ResCompany
class ResPartner
ResCompany --> l10n_pl_l10n_pl_tax_office : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


