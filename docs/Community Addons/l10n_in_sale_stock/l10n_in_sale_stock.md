<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# India Sales and Warehouse Management

- Scope: Community Addons
- Source: odoo/addons/l10n_in_sale_stock
- Dependencies: [[docs/Community Addons/l10n_in_sale/l10n_in_sale|l10n_in_sale]], [[docs/Community Addons/l10n_in_stock/l10n_in_stock|l10n_in_stock]], [[docs/Community Addons/sale_stock/sale_stock|sale_stock]]

## Summary

Get warehouse address if the invoice is created from Sale Order

## Generated coverage

- Models: 3
- XML files with UI/data artifacts: 0
- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
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
title India Sales and Warehouse Management - Generated Coverage
component "Module Overview" as overview
component "Models\n3" as models
component "Views / XML\n0 views\n0 files" as views
component "Controllers\n0 routes" as controllers
component "Frontend\n0 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/l10n_in_sale_stock/Models|Models]] (3)

## Key models

- `account.move`
- `stock.move`
- `stock.picking`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






