<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Czech - Accounting

- Version: v19
- Scope: Community Addons
- Source: odoo19/addons/l10n_cz
- Dependencies: [[Odoo 19/Community Addons/account/account|account]], [[Odoo 19/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]], [[Odoo 19/Community Addons/base_iban/base_iban|base_iban]], [[Odoo 19/Community Addons/base_vat/base_vat|base_vat]]

## XML Artifacts (detected)

- Views: 5
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountMove`
- `l10n_cz.tax_office`
- `ResCompany`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Czech - Accounting - Models and Relations
class AccountMove
class "l10n_cz.tax_office" as l10n_cz_tax_office
class ResCompany
ResCompany --> l10n_cz_tax_office : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


