<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Netherlands - SBR Status information service

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_nl_reports_sbr_status_info
- Dependencies: [[Odoo 18/Enterprise Addons/l10n_nl_reports_sbr/l10n_nl_reports_sbr|l10n_nl_reports_sbr]]

## Summary

Adds the use of a service checking the status of the submitted documents to Digipoort

## XML Artifacts (detected)

- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1

## Detected Models

- `l10n_nl_reports_sbr.status.service`
- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Netherlands - SBR Status information service - Models and Relations
class "l10n_nl_reports_sbr.status.service" as l10n_nl_reports_sbr_status_service
class ResCompany
class "res.company" as res_company
l10n_nl_reports_sbr_status_service --> res_company : many2one
class "account.move" as account_move
l10n_nl_reports_sbr_status_service --> account_move : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
