<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# HTML Editor

- Scope: Community Addons
- Source: odoo/addons/html_editor
- Dependencies: base (not documented), [[docs/Community Addons/bus/bus|bus]], [[docs/Community Addons/web/web|web]]

## Summary


        A Html Editor component and plugin system
    

## Generated coverage

- Models: 24
- XML files with UI/data artifacts: 0
- Views: 0
- Actions: 0
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 2
- Controller units: 1
- Frontend asset files: 229

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
title HTML Editor - Generated Coverage
component "Module Overview" as overview
component "Models\n24" as models
component "Views / XML\n0 views\n0 files" as views
component "Controllers\n15 routes" as controllers
component "Frontend\n229 files" as frontend
component "Security / Data\n0 rules\n2 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/html_editor/Models|Models]] (24)
- Controllers: [[docs/Community Addons/html_editor/Controllers|Controllers]] (1)
- Frontend: [[docs/Community Addons/html_editor/Frontend|Frontend]] (229 files)

## Key models

- `base`
- `html.field.history.mixin`
- `html_editor.converter.test`
- `html_editor.converter.test.sub`
- `ir.attachment`
- `ir.http`
- `ir.qweb`
- `ir.qweb.field`
- `ir.qweb.field.contact`
- `ir.qweb.field.date`
- `ir.qweb.field.datetime`
- `ir.qweb.field.duration`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






