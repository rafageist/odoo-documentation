<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Electronic invoicing for Colombia with Carvajal

- Scope: Enterprise Addons
- Source: enterprise/l10n_co_edi
- Dependencies: [[docs/Community Addons/account_edi/account_edi|account_edi]], [[docs/Community Addons/l10n_co/l10n_co|l10n_co]], [[docs/Enterprise Addons/product_unspsc/product_unspsc|product_unspsc]], [[docs/Community Addons/base_address_extended/base_address_extended|base_address_extended]]

## Summary

Colombian Localization for EDI documents

## Generated coverage

- Models: 18
- XML files with UI/data artifacts: 12
- Views: 13
- Actions: 2
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 4
- Controller units: 1
- Frontend asset files: 1

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
title Electronic invoicing for Colombia with Carvajal - Generated Coverage
component "Module Overview" as overview
component "Models\n18" as models
component "Views / XML\n13 views\n12 files" as views
component "Controllers\n1 routes" as controllers
component "Frontend\n1 files" as frontend
component "Security / Data\n0 rules\n4 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/l10n_co_edi/Models|Models]] (18)
- Views and XML: [[docs/Enterprise Addons/l10n_co_edi/Views|Views]] (12 files)
- Controllers: [[docs/Enterprise Addons/l10n_co_edi/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/l10n_co_edi/Frontend|Frontend]] (1 files)

## Key models

- `account.chart.template`
- `account.debit.note`
- `account.edi.format`
- `account.journal`
- `account.move`
- `account.move.line`
- `account.move.reversal`
- `account.tax`
- `l10n_co_edi.payment.option`
- `l10n_co_edi.tax.type`
- `l10n_co_edi.type_code`
- `product.template`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




