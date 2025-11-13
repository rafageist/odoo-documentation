<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, enterprise, module]
---

# Netherlands - SBR

- Version: v18
- Category: enterprise
- Source: enterprise18/l10n_nl_reports_sbr
- Dependencies: [[Odoo 18/Enterprise Addons/l10n_nl_reports/l10n_nl_reports|l10n_nl_reports]], [[Odoo 18/Community Addons/certificate/certificate|certificate]]

## Summary

Dutch Localization for SBR documents

## XML Artifacts (detected)

- Views: 2
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `ResCompany`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Netherlands - SBR - Models and Relations
class ResCompany
class "certificate.certificate" as certificate_certificate
ResCompany --> certificate_certificate : many2one
ResCompany --> certificate_certificate : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to category]]
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
