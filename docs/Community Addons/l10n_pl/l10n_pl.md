<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Poland - Accounting

- Scope: Community Addons
- Source: odoo/addons/l10n_pl
- Dependencies: [[docs/Community Addons/base_iban/base_iban|base_iban]], [[docs/Community Addons/base_vat/base_vat|base_vat]], [[docs/Community Addons/account/account|account]], [[docs/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]]

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
!include ../../../templates/DiagramStyles.puml
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
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





