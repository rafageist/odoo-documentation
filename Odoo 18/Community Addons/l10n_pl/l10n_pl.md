<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Poland - Accounting

- Version: v18
- Category: community
- Source: odoo/addons/l10n_pl
- Dependencies: [[Odoo 18/Community Addons/base_iban/base_iban|base_iban]], [[Odoo 18/Community Addons/base_vat/base_vat|base_vat]], [[Odoo 18/Community Addons/account/account|account]]
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
- `Company`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Poland - Accounting - Models and Relations
class AccountMove
class "l10n_pl.l10n_pl_tax_office" as l10n_pl_l10n_pl_tax_office
class ProductTemplate
class Company
class ResPartner
Company --> l10n_pl_l10n_pl_tax_office : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
