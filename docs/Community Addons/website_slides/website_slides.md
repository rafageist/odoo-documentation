<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# eLearning

- Scope: Community Addons
- Source: odoo/addons/website_slides
- Dependencies: [[docs/Community Addons/portal_rating/portal_rating|portal_rating]], [[docs/Community Addons/website/website|website]], [[docs/Community Addons/website_mail/website_mail|website_mail]], [[docs/Community Addons/website_profile/website_profile|website_profile]]

## Summary

Manage and publish an eLearning platform

## Generated coverage

- Models: 20
- XML files with UI/data artifacts: 17
- Views: 50
- Actions: 29
- Menus: 15
- Rules (ir.rule): 21
- Access CSV entries: 41
- Controller units: 2
- Frontend asset files: 74

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
title eLearning - Generated Coverage
component "Module Overview" as overview
component "Models\n20" as models
component "Views / XML\n50 views\n17 files" as views
component "Controllers\n39 routes" as controllers
component "Frontend\n74 files" as frontend
component "Security / Data\n21 rules\n41 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/website_slides/Models|Models]] (20)
- Views and XML: [[docs/Community Addons/website_slides/Views|Views]] (17 files)
- Controllers: [[docs/Community Addons/website_slides/Controllers|Controllers]] (2)
- Frontend: [[docs/Community Addons/website_slides/Frontend|Frontend]] (74 files)

## Key models

- `gamification.challenge`
- `gamification.karma.tracking`
- `mail.activity`
- `res.config.settings`
- `res.groups`
- `res.partner`
- `res.users`
- `slide.answer`
- `slide.channel`
- `slide.channel.invite`
- `slide.channel.partner`
- `slide.channel.tag`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->





