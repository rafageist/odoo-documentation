<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Austria - Security Regulation for Point of Sale

- Scope: Enterprise Addons
- Source: enterprise/l10n_at_pos
- Dependencies: [[docs/Community Addons/l10n_at/l10n_at|l10n_at]], [[docs/Community Addons/iap/iap|iap]], [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]

## Summary

The Austrian Cash Security Regulation

## Generated coverage

- Models: 6
- XML files with UI/data artifacts: 5
- Views: 4
- Actions: 3
- Menus: 2
- Rules (ir.rule): 0
- Access CSV entries: 1
- Controller units: 0
- Frontend asset files: 9

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
title Austria - Security Regulation for Point of Sale - Generated Coverage
component "Module Overview" as overview
component "Models\n6" as models
component "Views / XML\n4 views\n5 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n9 files" as frontend
component "Security / Data\n0 rules\n1 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/l10n_at_pos/Models|Models]] (6)
- Views and XML: [[docs/Enterprise Addons/l10n_at_pos/Views|Views]] (5 files)
- Frontend: [[docs/Enterprise Addons/l10n_at_pos/Frontend|Frontend]] (9 files)

## Key models

- `pos.config`
- `pos.fiskaly.details.wizard`
- `pos.order`
- `pos.session`
- `report.l10n_at_pos.report_config_audit_template`
- `res.company`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




