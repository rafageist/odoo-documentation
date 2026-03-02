
<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Website Helpdesk

- Scope: Enterprise Addons
- Source: enterprise/website_helpdesk
- Dependencies: [[docs/Enterprise Addons/helpdesk/helpdesk|helpdesk]], [[docs/Community Addons/website/website|website]]

## Summary

Bridge module for helpdesk modules using the website.

## Generated coverage

- Models: 5
- XML files with UI/data artifacts: 2
- Views: 1
- Actions: 0
- Menus: 0
- Rules (ir.rule): 1
- Access CSV entries: 0
- Controller units: 2
- Frontend asset files: 4

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
title Website Helpdesk - Generated Coverage
component "Module Overview" as overview
component "Models\n5" as models
component "Views / XML\n1 views\n2 files" as views
component "Controllers\n4 routes" as controllers
component "Frontend\n4 files" as frontend
component "Security / Data\n1 rules\n0 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/website_helpdesk/Models|Models]] (5)
- Views and XML: [[docs/Enterprise Addons/website_helpdesk/Views|Views]] (2 files)
- Controllers: [[docs/Enterprise Addons/website_helpdesk/Controllers|Controllers]] (2)
- Frontend: [[docs/Enterprise Addons/website_helpdesk/Frontend|Frontend]] (4 files)

## Key models

- `helpdesk.team`
- `helpdesk.ticket`
- `website`
- `website.menu`
- `website.page`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->



