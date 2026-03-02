<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Customer Portal

- Scope: Community Addons
- Source: odoo/addons/portal
- Dependencies: [[docs/Community Addons/web/web|web]], [[docs/Community Addons/html_editor/html_editor|html_editor]], [[docs/Community Addons/http_routing/http_routing|http_routing]], [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/auth_signup/auth_signup|auth_signup]]

## Summary

Customer Portal

## Generated coverage

- Models: 12
- XML files with UI/data artifacts: 3
- Views: 3
- Actions: 3
- Menus: 0
- Rules (ir.rule): 0
- Access CSV entries: 3
- Controller units: 4
- Frontend asset files: 33

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
title Customer Portal - Generated Coverage
component "Module Overview" as overview
component "Models\n12" as models
component "Views / XML\n3 views\n3 files" as views
component "Controllers\n18 routes" as controllers
component "Frontend\n33 files" as frontend
component "Security / Data\n0 rules\n3 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/portal/Models|Models]] (12)
- Views and XML: [[docs/Community Addons/portal/Views|Views]] (3 files)
- Controllers: [[docs/Community Addons/portal/Controllers|Controllers]] (4)
- Frontend: [[docs/Community Addons/portal/Frontend|Frontend]] (33 files)

## Key models

- `ir.http`
- `ir.qweb`
- `ir.ui.view`
- `mail.message`
- `mail.thread`
- `portal.mixin`
- `portal.share`
- `portal.wizard`
- `portal.wizard.user`
- `res.config.settings`
- `res.partner`
- `res.users.apikeys.description`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






