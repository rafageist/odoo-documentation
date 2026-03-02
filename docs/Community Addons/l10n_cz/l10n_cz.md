<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Czech - Accounting

- Scope: Community Addons
- Source: odoo/addons/l10n_cz
- Dependencies: [[docs/Community Addons/account/account|account]], [[docs/Community Addons/account_edi_ubl_cii/account_edi_ubl_cii|account_edi_ubl_cii]], [[docs/Community Addons/base_iban/base_iban|base_iban]], [[docs/Community Addons/base_vat/base_vat|base_vat]]

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
!include ../../../templates/DiagramStyles.puml
title Czech - Accounting - Models and Relations
class AccountMove
class "l10n_cz.tax_office" as l10n_cz_tax_office
class ResCompany
ResCompany --> l10n_cz_tax_office : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





