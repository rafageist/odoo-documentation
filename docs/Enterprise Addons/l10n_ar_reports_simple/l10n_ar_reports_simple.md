<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Argentinean Accounting IVA Simple Export

- Scope: Enterprise Addons
- Source: enterprise/l10n_ar_reports_simple
- Dependencies: [[docs/Enterprise Addons/l10n_ar_reports/l10n_ar_reports|l10n_ar_reports]]

## Summary

IVA Simple Reporting for Argentinean Localization

## XML Artifacts (detected)

- Views: 5
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `AccountAccount`
- `l10n_ar.arca.activity`
- `ResCompany`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title Argentinean Accounting IVA Simple Export - Models and Relations
class AccountAccount
class "l10n_ar.arca.activity" as l10n_ar_arca_activity
class ResCompany
AccountAccount --> l10n_ar_arca_activity : many2one
ResCompany --> l10n_ar_arca_activity : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



