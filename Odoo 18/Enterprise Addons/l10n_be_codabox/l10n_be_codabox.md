<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# CodaBox

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_be_codabox
- Dependencies: [[Odoo 18/Enterprise Addons/l10n_be_coda/l10n_be_coda|l10n_be_coda]], [[Odoo 18/Enterprise Addons/l10n_be_soda/l10n_be_soda|l10n_be_soda]], [[Odoo 18/Enterprise Addons/l10n_be_reports/l10n_be_reports|l10n_be_reports]]
## XML Artifacts (detected)

- Views: 5
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 3

## Detected Models

- `AccountJournal`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title CodaBox - Models and Relations
class AccountJournal
class ResCompany
class "account.journal" as account_journal
ResCompany --> account_journal : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
