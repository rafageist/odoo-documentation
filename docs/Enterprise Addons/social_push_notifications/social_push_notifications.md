<!-- GENERATED:MODULE -->
---
tags: [odoo, enterprise, module]
---

# Social Push Notifications

- Scope: Enterprise Addons
- Source: enterprise/social_push_notifications
- Dependencies: [[docs/Enterprise Addons/social/social|social]], [[docs/Community Addons/website/website|website]]

## Summary

Send live notifications to your web visitors

## Generated coverage

- Models: 11
- XML files with UI/data artifacts: 5
- Views: 9
- Actions: 1
- Menus: 1
- Rules (ir.rule): 0
- Access CSV entries: 3
- Controller units: 1
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
title Social Push Notifications - Generated Coverage
component "Module Overview" as overview
component "Models\n11" as models
component "Views / XML\n9 views\n5 files" as views
component "Controllers\n4 routes" as controllers
component "Frontend\n4 files" as frontend
component "Security / Data\n0 rules\n3 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Enterprise Addons/social_push_notifications/Models|Models]] (11)
- Views and XML: [[docs/Enterprise Addons/social_push_notifications/Views|Views]] (5 files)
- Controllers: [[docs/Enterprise Addons/social_push_notifications/Controllers|Controllers]] (1)
- Frontend: [[docs/Enterprise Addons/social_push_notifications/Frontend|Frontend]] (4 files)

## Key models

- `ir.http`
- `res.config.settings`
- `social.account`
- `social.live.post`
- `social.media`
- `social.post`
- `social.post.template`
- `utm.campaign`
- `website`
- `website.visitor`
- `website.visitor.push.subscription`

## Navigation

- [[../Enterprise Addons/Enterprise Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




