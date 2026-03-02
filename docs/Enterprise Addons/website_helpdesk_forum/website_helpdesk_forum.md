<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Helpdesk: Help Center

- Scope: Enterprise Addons
- Source: enterprise/website_helpdesk_forum
- Dependencies: [[docs/Community Addons/website_forum/website_forum|website_forum]], [[docs/Enterprise Addons/website_helpdesk/website_helpdesk|website_helpdesk]]

## Summary

Help Center for helpdesk based on Odoo Forum

## Generated coverage

- Models: 5
- XML files with UI/data artifacts: 3
- Views: 4
- Actions: 1
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 1
- Controller units: 1
- Frontend asset files: 3

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
title Helpdesk: Help Center - Generated Coverage
component "Module Overview" as overview
component "Models\n5" as models
component "Views / XML\n4 views\n3 files" as views
component "Controllers\n2 routes" as controllers
component "Frontend\n3 files" as frontend
component "Security / Data\n0 rules\n1 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/website_helpdesk_forum/Models|Models]] (5)
- Views and XML: [[docs/Enterprise Addons/website_helpdesk_forum/Views|Views]] (3 files)
- Controllers: [[docs/Enterprise Addons/website_helpdesk_forum/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/website_helpdesk_forum/Frontend|Frontend]] (3 files)

## Key models

- `forum.forum`
- `forum.post`
- `helpdesk.team`
- `helpdesk.ticket`
- `helpdesk.ticket.select.forum.wizard`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




