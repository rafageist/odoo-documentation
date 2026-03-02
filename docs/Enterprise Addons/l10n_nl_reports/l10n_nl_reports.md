
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Netherlands - Accounting Reports

- Scope: Enterprise Addons
- Source: enterprise/l10n_nl_reports
- Dependencies: [[docs/Community Addons/l10n_nl/l10n_nl|l10n_nl]], [[docs/Enterprise Addons/account_reports/account_reports|account_reports]], [[docs/Community Addons/certificate/certificate|certificate]]

## XML Artifacts (detected)

- Views: 6
- Actions: 2
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 5

## Detected Models

- `AccountReturn`
- `l10n_nl_reports.sbr.status.service`
- `ResCompany`
- `ResUsers`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Netherlands - Accounting Reports - Models and Relations
class AccountReturn
class "l10n_nl_reports.sbr.status.service" as l10n_nl_reports_sbr_status_service
class ResCompany
class ResUsers
class "res.company" as res_company
l10n_nl_reports_sbr_status_service --> res_company : many2one
class "account.move" as account_move
l10n_nl_reports_sbr_status_service --> account_move : many2one
class "certificate.certificate" as certificate_certificate
ResCompany --> certificate_certificate : many2one
ResCompany --> certificate_certificate : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->

