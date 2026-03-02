<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# CodaBox

- Scope: Enterprise Addons
- Source: enterprise/l10n_be_codabox
- Dependencies: [[docs/Enterprise Addons/l10n_be_coda/l10n_be_coda|l10n_be_coda]], [[docs/Enterprise Addons/l10n_be_soda/l10n_be_soda|l10n_be_soda]], [[docs/Enterprise Addons/l10n_be_reports/l10n_be_reports|l10n_be_reports]]

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
!include ../../../templates/DiagramStyles.puml
title CodaBox - Models and Relations
class AccountJournal
class ResCompany
class "account.journal" as account_journal
ResCompany --> account_journal : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



