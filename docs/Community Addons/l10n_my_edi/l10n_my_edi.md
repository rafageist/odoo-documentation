<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Malaysia - E-invoicing

- Scope: Community Addons
- Source: odoo/addons/l10n_my_edi
- Dependencies: [[docs/Community Addons/l10n_my/l10n_my|l10n_my]], [[docs/Community Addons/l10n_my_ubl_pint/l10n_my_ubl_pint|l10n_my_ubl_pint]], [[docs/Community Addons/account_edi_proxy_client/account_edi_proxy_client|account_edi_proxy_client]]

## Summary

E-invoicing using MyInvois

## Generated coverage

- Models: 14
- XML files with UI/data artifacts: 11
- Views: 12
- Actions: 2
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 7
- Controller units: 0
- Frontend asset files: 0

## Module map

```plantuml
@startuml
!define ODOO_COLOR_PRIMARY #714B67
!define ODOO_COLOR_ACCENT #875A7B
!define ODOO_COLOR_BG #FAF7FA

skinparam backgroundColor ODOO_COLOR_BG
skinparam defaultTextAlignment left
skinparam ArrowColor ODOO_COLOR_ACCENT
skinparam ClassBackgroundColor white
skinparam ClassBorderColor ODOO_COLOR_PRIMARY
skinparam ComponentBackgroundColor white
skinparam ComponentBorderColor ODOO_COLOR_PRIMARY
skinparam NoteBackgroundColor #FFF8FF
skinparam NoteBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBorderColor ODOO_COLOR_ACCENT
skinparam SequenceLifeLineBackgroundColor #FFFFFF
skinparam SequenceParticipantBorderColor ODOO_COLOR_PRIMARY
skinparam SequenceParticipantBackgroundColor #FFFFFF
skinparam sequence {
  ArrowColor ODOO_COLOR_ACCENT
  ActorBorderColor ODOO_COLOR_PRIMARY
}
title Malaysia - E-invoicing - Generated Coverage
component "Module Overview" as overview
component "Models\n14" as models
component "Views / XML\n12 views\n11 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n1 rules\n7 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/l10n_my_edi/Models|Models]] (14)
- Views and XML: [[docs/Community Addons/l10n_my_edi/Views|Views]] (11 files)

## Key models

- `account.edi.xml.ubl_myinvois_my`
- `account.move`
- `account.move.line`
- `account.move.send`
- `account.tax`
- `account_edi_proxy_client.user`
- `l10n_my_edi.industry_classification`
- `myinvois.consolidate.invoice.wizard`
- `myinvois.document`
- `myinvois.document.status.update.wizard`
- `product.template`
- `res.company`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






