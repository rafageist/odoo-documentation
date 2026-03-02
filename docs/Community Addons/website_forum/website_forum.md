<!-- GENERATED:MODULE -->
---
tags: [odoo, community, module]
---

# Forum

- Scope: Community Addons
- Source: odoo/addons/website_forum
- Dependencies: [[docs/Community Addons/auth_signup/auth_signup|auth_signup]], [[docs/Community Addons/website_mail/website_mail|website_mail]], [[docs/Community Addons/website_profile/website_profile|website_profile]]

## Summary

Manage a forum with FAQ and Q&A

## Generated coverage

- Models: 10
- XML files with UI/data artifacts: 9
- Views: 14
- Actions: 9
- Menus: 7
- Rules (ir.rule): 12
- Access CSV entries: 15
- Controller units: 2
- Frontend asset files: 24

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
title Forum - Generated Coverage
component "Module Overview" as overview
component "Models\n10" as models
component "Views / XML\n14 views\n9 files" as views
component "Controllers\n40 routes" as controllers
component "Frontend\n24 files" as frontend
component "Security / Data\n12 rules\n15 ACL rows" as security
overview --> models
overview --> views
overview --> controllers
overview --> frontend
overview --> security
@enduml
```

## Detail notes

- Models: [[docs/Community Addons/website_forum/Models|Models]] (10)
- Views and XML: [[docs/Community Addons/website_forum/Views|Views]] (9 files)
- Controllers: [[docs/Community Addons/website_forum/Controllers|Controllers]] (2)
- Frontend: [[docs/Community Addons/website_forum/Frontend|Frontend]] (24 files)

## Key models

- `forum.forum`
- `forum.post`
- `forum.post.reason`
- `forum.post.vote`
- `forum.tag`
- `gamification.challenge`
- `gamification.karma.tracking`
- `ir.attachment`
- `res.users`
- `website`

## Navigation

- [[../Community Addons/Community Addons|Back to scope]]
- [[../../docs/docs|Back to docs]]

<!-- GENERATED:MODULE -->




