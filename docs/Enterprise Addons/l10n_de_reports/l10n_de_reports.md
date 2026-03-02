<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Germany - Accounting Reports

- Scope: Enterprise Addons
- Source: enterprise/l10n_de_reports
- Dependencies: [[docs/Community Addons/l10n_de/l10n_de|l10n_de]], [[docs/Enterprise Addons/account_reports/account_reports|account_reports]]

## XML Artifacts (detected)

- Views: 3
- Actions: 0
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountMove`
- `ResCompany`
- `ResPartner`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Germany - Accounting Reports - Models and Relations
class AccountMove
class ResCompany
class ResPartner
class "account.account" as account_account
AccountMove --> account_account : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




