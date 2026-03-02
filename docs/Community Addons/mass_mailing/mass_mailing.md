<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Email Marketing

- Scope: Community Addons
- Source: odoo/addons/mass_mailing
- Dependencies: [[docs/Community Addons/contacts/contacts|contacts]], [[docs/Community Addons/mail/mail|mail]], [[docs/Community Addons/html_builder/html_builder|html_builder]], [[docs/Community Addons/utm/utm|utm]], [[docs/Community Addons/link_tracker/link_tracker|link_tracker]], [[docs/Community Addons/social_media/social_media|social_media]], [[docs/Community Addons/web_tour/web_tour|web_tour]], [[docs/Community Addons/digest/digest|digest]]

## Summary

Design, send and track emails

## Generated coverage

- Models: 30
- XML files with UI/data artifacts: 20
- Views: 57
- Actions: 22
- Menus: 19
- Rules (ir.rule): 1
- Access CSV entries: 25
- Controller units: 2
- Frontend asset files: 52

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
title Email Marketing - Generated Coverage
component "Module Overview" as overview
component "Models\n30" as models
component "Views / XML\n57 views\n20 files" as views
component "Controllers\n17 routes" as controllers
component "Frontend\n52 files" as frontend
component "Security / Data\n1 rules\n25 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/mass_mailing/Models|Models]] (30)
- Views and XML: [[docs/Community Addons/mass_mailing/Views|Views]] (20 files)
- Controllers: [[docs/Community Addons/mass_mailing/Controllers|Controllers]] (2)
- Frontend: [[docs/Community Addons/mass_mailing/Frontend|Frontend]] (52 files)

## Key models

- `ir.http`
- `ir.mail_server`
- `ir.model`
- `link.tracker`
- `link.tracker.click`
- `mail.blacklist`
- `mail.compose.message`
- `mail.mail`
- `mail.render.mixin`
- `mail.thread`
- `mailing.contact`
- `mailing.contact.import`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->






