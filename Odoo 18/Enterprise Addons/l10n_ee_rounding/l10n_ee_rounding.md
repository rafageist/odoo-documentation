<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Estonia - Rounding

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_ee_rounding
- Dependencies: [[Odoo 18/Enterprise Addons/l10n_ee_reports/l10n_ee_reports|l10n_ee_reports]]
## XML Artifacts (detected)

- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Estonia - Rounding - Models and Relations
class ResCompany
class "account.account" as account_account
ResCompany --> account_account : many2one
ResCompany --> account_account : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
