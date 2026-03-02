<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# UK - Accounting Reports

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_uk_reports
- Dependencies: [[Odoo 19/Community Addons/l10n_uk/l10n_uk|l10n_uk]], [[Odoo 19/Enterprise Addons/account_reports/account_reports|account_reports]]

## XML Artifacts (detected)

- Views: 4
- Actions: 1
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 2

## Detected Models

- `AccountReturnType`
- `AccountReturn`
- `l10n_uk.vat.obligation`
- `ResCompany`
- `ResUsers`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title UK - Accounting Reports - Models and Relations
class AccountReturnType
class AccountReturn
class "l10n_uk.vat.obligation" as l10n_uk_vat_obligation
class ResCompany
class ResUsers
class "res.company" as res_company
l10n_uk_vat_obligation --> res_company : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

