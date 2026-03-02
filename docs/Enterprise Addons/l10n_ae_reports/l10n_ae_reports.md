<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# United Arab Emirates - Accounting Reports

- Scope: Enterprise Addons
- Source: enterprise/l10n_ae_reports
- Dependencies: [[docs/Community Addons/l10n_ae/l10n_ae|l10n_ae]], [[docs/Enterprise Addons/account_reports/account_reports|account_reports]], [[docs/Enterprise Addons/account_fiscal_categories/account_fiscal_categories|account_fiscal_categories]]

## XML Artifacts (detected)

- Views: 1
- Actions: 1
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 0

## Detected Models

- `AccountReport`
- `AccountReturn`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title United Arab Emirates - Accounting Reports - Models and Relations
class AccountReport
class AccountReturn
class ResCompany
class "account.account" as account_account
ResCompany --> account_account : many2one
ResCompany --> account_account : many2one
ResCompany --> account_account : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



