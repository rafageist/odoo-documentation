
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Bangladesh - Accounting Reports

- Scope: Enterprise Addons
- Source: enterprise/l10n_bd_reports
- Dependencies: [[docs/Enterprise Addons/account_reports/account_reports|account_reports]], [[docs/Community Addons/l10n_bd/l10n_bd|l10n_bd]]

## XML Artifacts (detected)

- Views: 1
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Bangladesh - Accounting Reports - Models and Relations
class ResCompany
class "account.account" as account_account
ResCompany --> account_account : many2one
ResCompany --> account_account : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

