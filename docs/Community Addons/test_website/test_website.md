<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Website Test

- Scope: Community Addons
- Source: odoo/addons/test_website
- Dependencies: [[docs/Community Addons/web_unsplash/web_unsplash|web_unsplash]], [[docs/Community Addons/website/website|website]], [[docs/Community Addons/theme_default/theme_default|theme_default]]

## Summary

Website Test, mainly for module install/uninstall tests

## Generated coverage

- Models: 6
- XML files with UI/data artifacts: 3
- Views: 10
- Actions: 4
- Menus: 1
- Rules (ir.rule): 1
- Access CSV entries: 19
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
title Website Test - Generated Coverage
component "Module Overview" as overview
component "Models\n6" as models
component "Views / XML\n10 views\n3 files" as views
component "Controllers\n37 routes" as controllers
component "Frontend\n1 files" as frontend
component "Security / Data\n1 rules\n19 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/test_website/Models|Models]] (6)
- Views and XML: [[docs/Community Addons/test_website/Views|Views]] (3 files)
- Controllers: [[docs/Community Addons/test_website/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/test_website/Frontend|Frontend]] (1 files)

## Key models

- `test.model`
- `test.model.exposed`
- `test.model.multi.website`
- `test.submodel`
- `test.tag`
- `website`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





