<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, enterprise, module]
---

# CodaBox

- Version: v19
- Scope: Enterprise Addons
- Source: enterprise19/l10n_be_codabox
- Dependencies: [[Odoo 19/Enterprise Addons/l10n_be_coda/l10n_be_coda|l10n_be_coda]], [[Odoo 19/Enterprise Addons/l10n_be_soda/l10n_be_soda|l10n_be_soda]], [[Odoo 19/Enterprise Addons/l10n_be_reports/l10n_be_reports|l10n_be_reports]]

## XML Artifacts (detected)

- Views: 6
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 4

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

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->

