<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Czech Republic - Accounting Reports 2025

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_cz_reports_2025
- Dependencies: [[Odoo 18/Enterprise Addons/l10n_cz_reports/l10n_cz_reports|l10n_cz_reports]]
## XML Artifacts (detected)

- Views: 7
- Actions: 2
- Menus: 3
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `AccountTax`
- `l10n_cz.tax_office`
- `ProductTemplate`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Czech Republic - Accounting Reports 2025 - Models and Relations
class AccountMove
class AccountMoveLine
class AccountTax
class "l10n_cz.tax_office" as l10n_cz_tax_office
class ProductTemplate
class ResCompany
ResCompany --> l10n_cz_tax_office : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
