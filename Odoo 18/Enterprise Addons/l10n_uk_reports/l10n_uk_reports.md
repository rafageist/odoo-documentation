<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# UK - Accounting Reports

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_uk_reports
- Dependencies: [[Odoo 18/Community Addons/l10n_uk/l10n_uk|l10n_uk]], [[Odoo 18/Enterprise Addons/account_reports/account_reports|account_reports]]
## XML Artifacts (detected)

- Views: 4
- Actions: 1
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 2

## Detected Models

- `l10n_uk.vat.obligation`
- `User`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title UK - Accounting Reports - Models and Relations
class "l10n_uk.vat.obligation" as l10n_uk_vat_obligation
class User
class "res.company" as res_company
l10n_uk_vat_obligation --> res_company : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
