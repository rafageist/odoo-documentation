<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Egypt E-Invoicing

- Scope: Community Addons
- Source: odoo/addons/l10n_eg_edi_eta
- Dependencies: [[docs/Community Addons/account_edi/account_edi|account_edi]], [[docs/Community Addons/l10n_eg/l10n_eg|l10n_eg]]

## Summary


            Egypt Tax Authority Invoice Integration
        

## Generated coverage

- Models: 13
- XML files with UI/data artifacts: 8
- Views: 8
- Actions: 2
- Menus: 2
- Rules (ir.rule): 1
- Access CSV entries: 3
- Controller units: 0
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
title Egypt E-Invoicing - Generated Coverage
component "Module Overview" as overview
component "Models\n13" as models
component "Views / XML\n8 views\n8 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n1 files" as frontend
component "Security / Data\n1 rules\n3 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/l10n_eg_edi_eta/Models|Models]] (13)
- Views and XML: [[docs/Community Addons/l10n_eg_edi_eta/Views|Views]] (8 files)
- Frontend: [[docs/Community Addons/l10n_eg_edi_eta/Frontend|Frontend]] (1 files)

## Key models

- `account.edi.format`
- `account.journal`
- `account.move`
- `l10n_eg_edi.activity.type`
- `l10n_eg_edi.thumb.drive`
- `l10n_eg_edi.uom.code`
- `product.product`
- `product.template`
- `res.company`
- `res.config.settings`
- `res.currency.rate`
- `res.partner`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






