<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Unsplash Image Library

- Scope: Community Addons
- Source: odoo/addons/web_unsplash
- Dependencies: [[docs/Community Addons/base_setup/base_setup|base_setup]], [[docs/Community Addons/html_editor/html_editor|html_editor]]

## Summary

Find free high-resolution images from Unsplash

## Generated coverage

- Models: 4
- XML files with UI/data artifacts: 1
- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 0
- Controller units: 1
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
title Unsplash Image Library - Generated Coverage
component "Module Overview" as overview
component "Models\n4" as models
component "Views / XML\n1 views\n1 files" as views
component "Controllers\n4 routes" as controllers
component "Frontend\n9 files" as frontend
component "Security / Data\n0 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/web_unsplash/Models|Models]] (4)
- Views and XML: [[docs/Community Addons/web_unsplash/Views|Views]] (1 files)
- Controllers: [[docs/Community Addons/web_unsplash/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/web_unsplash/Frontend|Frontend]] (9 files)

## Key models

- `ir.attachment`
- `ir.qweb.field.image`
- `res.config.settings`
- `res.users`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





