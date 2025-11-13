<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# UK - Construction Industry Scheme

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_uk_reports_cis
- Dependencies: [[Odoo 18/Enterprise Addons/l10n_uk_reports/l10n_uk_reports|l10n_uk_reports]], [[Odoo 18/Enterprise Addons/l10n_uk_hmrc/l10n_uk_hmrc|l10n_uk_hmrc]]
## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `AccountMove`
- `HmrcTransaction`
- `ResCompany`
- `ResPartner`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title UK - Construction Industry Scheme - Models and Relations
class AccountMove
class HmrcTransaction
class ResCompany
class ResPartner
class "ir.attachment" as ir_attachment
HmrcTransaction --> ir_attachment : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
