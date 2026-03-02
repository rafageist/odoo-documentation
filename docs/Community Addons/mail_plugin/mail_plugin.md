<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Mail Plugin

- Scope: Community Addons
- Source: odoo/addons/mail_plugin
- Dependencies: [[docs/Community Addons/web/web|web]], [[docs/Community Addons/contacts/contacts|contacts]], [[docs/Community Addons/iap/iap|iap]]

## Summary

Allows integration with mail plugins.

## Generated coverage

- Models: 3
- XML files with UI/data artifacts: 1
- Views: 2
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 1
- Controller units: 2
- Frontend asset files: 2

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
title Mail Plugin - Generated Coverage
component "Module Overview" as overview
component "Models\n3" as models
component "Views / XML\n2 views\n1 files" as views
component "Controllers\n11 routes" as controllers
component "Frontend\n2 files" as frontend
component "Security / Data\n0 rules\n1 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/mail_plugin/Models|Models]] (3)
- Views and XML: [[docs/Community Addons/mail_plugin/Views|Views]] (1 files)
- Controllers: [[docs/Community Addons/mail_plugin/Controllers|Controllers]] (2)
- Frontend: [[docs/Community Addons/mail_plugin/Frontend|Frontend]] (2 files)

## Key models

- `ir.http`
- `res.partner`
- `res.partner.iap`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






