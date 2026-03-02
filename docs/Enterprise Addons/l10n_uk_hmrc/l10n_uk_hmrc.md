<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# UK - HMRC API

- Scope: Enterprise Addons
- Source: enterprise/l10n_uk_hmrc
- Dependencies: [[docs/Community Addons/l10n_uk/l10n_uk|l10n_uk]]

## XML Artifacts (detected)

- Views: 2
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2

## Detected Models

- `l10n_uk.hmrc.transaction`
- `ResCompany`
- `ResPartner`

```plantuml
@startuml
!include ../../../templates/DiagramStyles.puml
title UK - HMRC API - Models and Relations
class "l10n_uk.hmrc.transaction" as l10n_uk_hmrc_transaction
class ResCompany
class ResPartner
class "res.users" as res_users
l10n_uk_hmrc_transaction --> res_users : many2one
class "res.company" as res_company
l10n_uk_hmrc_transaction --> res_company : many2one
@enduml
```

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



