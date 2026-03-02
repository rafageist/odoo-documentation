<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Web

- Scope: Community Addons
- Source: odoo/addons/web
- Dependencies: base (not documented)

## Generated coverage

- Models: 15
- XML files with UI/data artifacts: 5
- Views: 2
- Actions: 5
- Menus: 0
- Rules (ir.rule): 2
- Access CSV entries: 2
- Controller units: 19
- Frontend asset files: 790

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
title Web - Generated Coverage
component "Module Overview" as overview
component "Models\n15" as models
component "Views / XML\n2 views\n5 files" as views
component "Controllers\n68 routes" as controllers
component "Frontend\n790 files" as frontend
component "Security / Data\n2 rules\n2 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/web/Models|Models]] (15)
- Views and XML: [[docs/Community Addons/web/Views|Views]] (5 files)
- Controllers: [[docs/Community Addons/web/Controllers|Controllers]] (19)
- Frontend: [[docs/Community Addons/web/Frontend|Frontend]] (790 files)

## Key models

- `base`
- `base.document.layout`
- `ir.http`
- `ir.model`
- `ir.qweb.field.image`
- `ir.qweb.field.image_url`
- `ir.ui.menu`
- `ir.ui.view`
- `properties.base.definition`
- `res.company`
- `res.config.settings`
- `res.partner`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




