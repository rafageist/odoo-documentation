<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# Spain - Real Estates

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_es_real_estates
- Dependencies: [[Odoo 19/Enterprise Addons/l10n_es_reports/l10n_es_reports|l10n_es_reports]]

## XML Artifacts (detected)

- Views: 4
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `AccountMove`
- `AccountMoveLine`
- `l10n_es_reports.real.estate`

```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Spain - Real Estates - Models and Relations
class AccountMove
class AccountMoveLine
class "l10n_es_reports.real.estate" as l10n_es_reports_real_estate
AccountMove --> l10n_es_reports_real_estate : many2one
class "account.move" as account_move
l10n_es_reports_real_estate --|> account_move : one2many
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->


